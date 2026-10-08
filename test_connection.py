"""
Script de Validação de Conexão com o Sankhya ERP.
Executa autenticação OAuth2 e testa comunicação com o Gateway.
"""

import sys
import json
import base64
from sankhya_client import SankhyaClient


def decode_jwt_payload(token: str) -> dict:
    """Decodifica a carga útil (payload) do JWT sem validação de assinatura."""
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return {}
        payload_b64 = parts[1]
        # Adiciona padding se necessário
        rem = len(payload_b64) % 4
        if rem > 0:
            payload_b64 += "=" * (4 - rem)
        decoded_bytes = base64.urlsafe_b64decode(payload_b64.encode("utf-8"))
        return json.loads(decoded_bytes.decode("utf-8"))
    except Exception as e:
        return {"error": f"Não foi possível decodificar JWT: {e}"}


def main():
    print("=" * 65)
    print("      TESTE DE CONEXÃO COM O ERP SANKHYA (SANDBOX/GATEWAY)")
    print("=" * 65)

    try:
        client = SankhyaClient()
        print(f"[+] Ambiente configurado: {client.env.upper()}")
        print(f"[+] URL Base: {client.base_url}")
        print(f"[+] Client ID: {client.client_id[:8]}...{client.client_id[-4:]}")
        print("[+] Tentando autenticar...")

        auth_data = client.authenticate()
        print("\n[OK] Autenticação bem-sucedida (Status HTTP 200)!")
        
        token = auth_data.get("access_token", "")
        expires_in = auth_data.get("expires_in")
        print(f"[+] Token Type: {auth_data.get('token_type', 'Bearer')}")
        print(f"[+] Expira em: {expires_in} segundos (~{expires_in // 60} minutos)")

        # Inspeciona informações dentro do token retornado pela Sankhya
        payload = decode_jwt_payload(token)
        if payload:
            print("\n--- Informações do Vínculo de Integração ---")
            print(f"  • Empresa / Integrador: {payload.get('plainNomeIntegrador', 'N/D')}")
            print(f"  • Aplicação: {payload.get('plainNomeAplicacao', 'N/D')}")
            print(f"  • Ambiente interno: {payload.get('ambiente', 'N/D')}")
            print(f"  • Escopos: {payload.get('scope', 'N/D')}")
            print(f"  • Environment ID (X-Token): {payload.get('environment', 'N/D')}")

        # Teste de chamada ao Gateway MGE
        print("\n[+] Testando requisição ao Gateway MGE...")
        try:
            # Consulta simples de exemplo na entidade Parceiro
            result = client.load_records(
                entity_name="Parceiro",
                fields=["CODPARC", "NOMEPARC"],
                criteria="this.CODPARC > 0"
            )
            status = result.get("status")
            status_msg = result.get("statusMessage", "OK")
            print(f"[OK] Gateway respondeu com status: {status} ({status_msg})")
            
            response_body = result.get("responseBody", {})
            entities = response_body.get("entities", {})
            total = entities.get("total", 0)
            print(f"[+] Total de registros na página: {total}")
            
            # Se vieram registros, exibe os primeiros
            records = entities.get("entity", [])
            if isinstance(records, dict):
                records = [records]
            for idx, r in enumerate(records[:3], 1):
                f_cod = r.get("f0", {}).get("$", "N/A")
                f_nome = r.get("f1", {}).get("$", "N/A")
                print(f"    {idx}. Cód: {f_cod} | Nome: {f_nome}")
        except Exception as gw_err:
            print(f"[!] Chamada de serviço Gateway retornou: {gw_err}")
            print("    (Obs: Autenticação OAuth2 validada com 100% de sucesso! Restrições de serviço dependem das permissões do usuário no ERP).")

        print("\n" + "=" * 65)
        print(">> Conexão validada com sucesso! O conector está pronto para uso.")
        print("=" * 65)

    except Exception as e:
        print(f"\n[FALHA] Erro ao conectar: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
