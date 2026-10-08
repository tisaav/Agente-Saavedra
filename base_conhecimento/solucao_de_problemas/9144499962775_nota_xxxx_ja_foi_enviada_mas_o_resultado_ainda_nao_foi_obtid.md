# Nota XXXX já foi enviada mas o resultado ainda não foi obtido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9144499962775-Nota-XXXX-j%C3%A1-foi-enviada-mas-o-resultado-ainda-n%C3%A3o-foi-obtido](https://ajuda.sankhya.com.br/hc/pt-br/articles/9144499962775-Nota-XXXX-j%C3%A1-foi-enviada-mas-o-resultado-ainda-n%C3%A3o-foi-obtido)  
> **ID:** `9144499962775` | **Última Atualização:** 2026-07-22T15:10:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276632494103)

 MENSAGEM:**

[CORE_E00547] Nota XXXX já foi enviada mas o resultado ainda não foi obtido. Favor utilizar a opção Buscar autorização.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276632496279)

 SITUAÇÃO:**

Ao tentar emitir uma NFS-e a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276632497175)

 CAUSA:**

Ocorre ao emitir nota RPS.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276592897431)

 SOLUÇÃO:**

- Verifique se o serviço está devidamente configurado para reter ISS.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9143899036055)

 

Em casos de emissão como RPS, verifique alguns pontos:

1. A nota será negada por limite de tentativa, não sairá da API, e será emitida em ambiente de Homologação com o sequencial zero:

1. A série informada no cadastro da empresa está incorreta, enviando **NF-e** deve ser **1;**

1. **Para emissões no ambiente de produção, libere o RPS na prefeitura. **