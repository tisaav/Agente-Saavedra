"""
Cliente de Conexão com o ERP Sankhya (Python)
Suporta autenticação OAuth2 (Client Credentials) e chamadas aos serviços Gateway MGE.
"""

import os
import time
import json
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional, Dict, Any


def load_dotenv(dotenv_path: str = ".env") -> None:
    """Carrega variáveis do arquivo .env manualmente caso python-dotenv não esteja instalado."""
    if not os.path.exists(dotenv_path):
        return
    with open(dotenv_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key not in os.environ:
                os.environ[key] = val


class SankhyaClient:
    """Cliente para integração com a API Sankhya Om / Gateway."""

    ENV_URLS = {
        "sandbox": "https://api.sandbox.sankhya.com.br",
        "production": "https://api.sankhya.com.br",
        "hml": "https://api.sandbox.sankhya.com.br",
        "prod": "https://api.sankhya.com.br",
    }

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        x_token: Optional[str] = None,
        env: Optional[str] = None,
    ):
        load_dotenv()
        self.client_id = client_id or os.getenv("SANKHYA_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("SANKHYA_CLIENT_SECRET")
        self.x_token = x_token or os.getenv("SANKHYA_X_TOKEN")
        self.env = (env or os.getenv("SANKHYA_ENV") or "sandbox").lower()

        if not self.client_id or not self.client_secret or not self.x_token:
            raise ValueError(
                "Credenciais incompletas! Verifique se SANKHYA_CLIENT_ID, "
                "SANKHYA_CLIENT_SECRET e SANKHYA_X_TOKEN estão configurados."
            )

        self.base_url = self.ENV_URLS.get(self.env, self.ENV_URLS["sandbox"])
        self.access_token: Optional[str] = None
        self.token_expiry: float = 0
        self.token_payload: Dict[str, Any] = {}

    def is_token_valid(self) -> bool:
        """Verifica se o token atual ainda é válido com margem de segurança de 30s."""
        return bool(self.access_token and time.time() < (self.token_expiry - 30))

    def authenticate(self, force: bool = False) -> Dict[str, Any]:
        """
        Realiza a autenticação OAuth2 (Client Credentials) junto à Sankhya.
        Retorna as informações do token gerado.
        """
        if not force and self.is_token_valid():
            return {
                "access_token": self.access_token,
                "expires_in": int(self.token_expiry - time.time()),
                "token_type": "Bearer",
                "cached": True,
            }

        auth_url = f"{self.base_url}/authenticate"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Token": self.x_token,
            "User-Agent": "SankhyaPythonConnector/1.0",
        }
        data = urllib.parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }).encode("utf-8")

        req = urllib.request.Request(auth_url, data=data, headers=headers, method="POST")

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                status_code = resp.status
                response_body = resp.read().decode("utf-8")
                token_data = json.loads(response_body)

                self.access_token = token_data.get("access_token")
                expires_in = token_data.get("expires_in", 300)
                self.token_expiry = time.time() + expires_in
                self.token_payload = token_data

                return token_data
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8") if e.fp else ""
            raise RuntimeError(
                f"Erro na autenticação Sankhya (HTTP {e.code}): {error_body}"
            ) from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"Falha de conexão com a API Sankhya: {e.reason}") from e

    def call_service(
        self,
        service_name: str,
        request_body: Optional[Dict[str, Any]] = None,
        module: str = "mge",
    ) -> Dict[str, Any]:
        """
        Executa uma chamada a um serviço do Gateway Sankhya (ex: CRUDServiceProvider.loadRecords).
        """
        # Garante token válido
        if not self.is_token_valid():
            self.authenticate()

        url = f"{self.base_url}/gateway/v1/{module}/service.sbr?serviceName={service_name}&outputType=json"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "User-Agent": "SankhyaPythonConnector/1.0",
        }
        payload = {
            "serviceName": service_name,
            "requestBody": request_body or {},
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")

        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                resp_text = resp.read().decode("utf-8")
                return json.loads(resp_text)
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8") if e.fp else ""
            # Se deu 401, tenta renovar o token 1 vez
            if e.code == 401:
                self.authenticate(force=True)
                headers["Authorization"] = f"Bearer {self.access_token}"
                req = urllib.request.Request(url, data=data, headers=headers, method="POST")
                with urllib.request.urlopen(req, timeout=45) as resp2:
                    return json.loads(resp2.read().decode("utf-8"))

            raise RuntimeError(
                f"Erro ao executar serviço '{service_name}' (HTTP {e.code}): {error_body}"
            ) from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"Falha de rede ao conectar com Gateway: {e.reason}") from e

    def execute_query(self, sql: str) -> Dict[str, Any]:
        """
        Executa uma consulta SQL no Sankhya utilizando o serviço DbExplorerSP.executeQuery.
        Nota: Requer permissão de acesso ao serviço no ERP.
        """
        body = {
            "sql": sql
        }
        return self.call_service("DbExplorerSP.executeQuery", request_body=body)

    def load_records(
        self,
        entity_name: str,
        fields: Optional[list] = None,
        criteria: Optional[str] = None,
        offset_page: int = 0,
    ) -> Dict[str, Any]:
        """
        Consulta registros de uma entidade usando CRUDServiceProvider.loadRecords.
        Exemplo: entity_name="Parceiro", fields=["CODPARC", "NOMEPARC", "CGC_CPF"]
        """
        data_set = {
            "rootEntity": entity_name,
            "includePresentationFields": "N",
            "offsetPage": str(offset_page),
        }

        if fields:
            data_set["entity"] = {
                "fieldset": {
                    "list": ", ".join(fields)
                }
            }

        if criteria:
            data_set["criteria"] = {
                "expression": {
                    "$": criteria
                }
            }

        return self.call_service("CRUDServiceProvider.loadRecords", request_body={"dataSet": data_set})
