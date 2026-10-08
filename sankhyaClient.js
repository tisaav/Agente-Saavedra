/**
 * Cliente de Conexão com o ERP Sankhya (Node.js)
 * Compatível com Node.js 18+ (usa fetch nativo).
 */

const fs = require('fs');
const path = require('path');

// Carregador simples de variáveis do .env caso dotenv não esteja instalado
function loadEnv(filePath = '.env') {
  const fullPath = path.resolve(process.cwd(), filePath);
  if (!fs.existsSync(fullPath)) return;
  const content = fs.readFileSync(fullPath, 'utf-8');
  for (const line of content.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) continue;
    const [key, ...values] = trimmed.split('=');
    const val = values.join('=').trim().replace(/^["']|["']$/g, '');
    if (!process.env[key.trim()]) {
      process.env[key.trim()] = val;
    }
  }
}

class SankhyaClient {
  static ENV_URLS = {
    sandbox: 'https://api.sandbox.sankhya.com.br',
    production: 'https://api.sankhya.com.br',
    hml: 'https://api.sandbox.sankhya.com.br',
    prod: 'https://api.sankhya.com.br',
  };

  constructor(options = {}) {
    loadEnv();
    this.clientId = options.clientId || process.env.SANKHYA_CLIENT_ID;
    this.clientSecret = options.clientSecret || process.env.SANKHYA_CLIENT_SECRET;
    this.xToken = options.xToken || process.env.SANKHYA_X_TOKEN;
    this.env = (options.env || process.env.SANKHYA_ENV || 'sandbox').toLowerCase();

    if (!this.clientId || !this.clientSecret || !this.xToken) {
      throw new Error(
        'Credenciais incompletas! Verifique SANKHYA_CLIENT_ID, SANKHYA_CLIENT_SECRET e SANKHYA_X_TOKEN.'
      );
    }

    this.baseUrl = SankhyaClient.ENV_URLS[this.env] || SankhyaClient.ENV_URLS.sandbox;
    this.accessToken = null;
    this.tokenExpiry = 0;
  }

  isTokenValid() {
    return Boolean(this.accessToken && Date.now() < this.tokenExpiry - 30000);
  }

  async authenticate(force = false) {
    if (!force && this.isTokenValid()) {
      return {
        access_token: this.accessToken,
        expires_in: Math.floor((this.tokenExpiry - Date.now()) / 1000),
        token_type: 'Bearer',
        cached: true,
      };
    }

    const authUrl = `${this.baseUrl}/authenticate`;
    const body = new URLSearchParams({
      grant_type: 'client_credentials',
      client_id: this.clientId,
      client_secret: this.clientSecret,
    });

    const response = await fetch(authUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Token': this.xToken,
        'User-Agent': 'SankhyaNodeConnector/1.0',
      },
      body: body.toString(),
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Erro na autenticação Sankhya (HTTP ${response.status}): ${errText}`);
    }

    const data = await response.json();
    this.accessToken = data.access_token;
    this.tokenExpiry = Date.now() + (data.expires_in || 300) * 1000;
    return data;
  }

  async callService(serviceName, requestBody = {}, module = 'mge') {
    if (!this.isTokenValid()) {
      await this.authenticate();
    }

    const url = `${this.baseUrl}/gateway/v1/${module}/service.sbr?serviceName=${serviceName}&outputType=json`;
    const payload = {
      serviceName,
      requestBody,
    };

    let response = await fetch(url, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
        'User-Agent': 'SankhyaNodeConnector/1.0',
      },
      body: JSON.stringify(payload),
    });

    if (response.status === 401) {
      // Tenta reautenticar
      await this.authenticate(true);
      response = await fetch(url, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json',
          'User-Agent': 'SankhyaNodeConnector/1.0',
        },
        body: JSON.stringify(payload),
      });
    }

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Erro ao executar serviço ${serviceName} (HTTP ${response.status}): ${errText}`);
    }

    return await response.json();
  }

  async loadRecords(entityName, fields = [], criteria = '', offsetPage = 0) {
    const dataSet = {
      rootEntity: entityName,
      includePresentationFields: 'N',
      offsetPage: String(offsetPage),
    };

    if (fields.length > 0) {
      dataSet.entity = {
        fieldset: {
          list: fields.join(', '),
        },
      };
    }

    if (criteria) {
      dataSet.criteria = {
        expression: {
          $: criteria,
        },
      };
    }

    return await this.callService('CRUDServiceProvider.loadRecords', { dataSet });
  }

  async executeQuery(sql) {
    return await this.callService('DbExplorerSP.executeQuery', { sql });
  }
}

module.exports = SankhyaClient;
