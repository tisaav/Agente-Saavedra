# Dígito Verificador da Chave de Acesso da NF-e Referenciada inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043196533-D%C3%ADgito-Verificador-da-Chave-de-Acesso-da-NF-e-Referenciada-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043196533-D%C3%ADgito-Verificador-da-Chave-de-Acesso-da-NF-e-Referenciada-inv%C3%A1lido)  
> **ID:** `360043196533` | **Última Atualização:** 2026-07-22T16:06:47Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512793321751)

 MENSAGEM:**

[547 - Rejeição]: Dígito Verificador da Chave de Acesso da NF-e Referenciada inválido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512800614551)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

Para conseguir aprovar a NF-e de Devolução, informe a chave correta na nota de origem ou no campo: **"Chave NF-e Referenciada"**.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512793328663)

 Selecione a NF-e de Venda(Origem) e confira a chave - Caso a chave esta correta.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512800624535)

 Acesse a NF-e de Devolução e busque pelo campo **"Chave NF-e Referenciada"** - Identifique se a chave esta correta.

- Se a nota de devolução está sendo feita de forma Manual, informe a chave da nota referenciada corretamente.

- Se a nota de devolução foi feita a partir da Nota de Origem(Venda), a chave referenciada será populada automaticamente e deverá estar correta também.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512800626839)

 Após os ajustes, gere o lote da NF-e de devolução novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512793336215)

 CAUSA:**

Ocorre quando foi emitido uma Nota Fiscal Eletrônica onde referenciou um ou mais documento(s) de origem, seja manualmente ou de forma automática. Onde o documento referenciado possui a chave de acesso com o dígito verificador inválido.