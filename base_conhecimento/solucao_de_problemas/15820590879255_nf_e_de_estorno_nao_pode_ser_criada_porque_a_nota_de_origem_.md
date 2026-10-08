# NF-e de estorno não pode ser criada porque a nota de origem (Nro. Único: XXXX) não está aprovada

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15820590879255-NF-e-de-estorno-n%C3%A3o-pode-ser-criada-porque-a-nota-de-origem-Nro-%C3%9Anico-XXXX-n%C3%A3o-est%C3%A1-aprovada](https://ajuda.sankhya.com.br/hc/pt-br/articles/15820590879255-NF-e-de-estorno-n%C3%A3o-pode-ser-criada-porque-a-nota-de-origem-Nro-%C3%9Anico-XXXX-n%C3%A3o-est%C3%A1-aprovada)  
> **ID:** `15820590879255` | **Última Atualização:** 2026-07-22T14:56:08Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15820575685655)

 MENSAGEM:**

[CORE_E04662] NF-e de estorno não pode ser criada porque a nota de origem (Nro. Único: XXXX) não está aprovada.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15820606830359)

 CAUSA:**

Ocorre ao utilizar uma TOP incorreta para o lançamento de uma devolução.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15820622496023)

 SOLUÇÃO:**

Quando a marcação** "NF-e de estorno"** for efetuada, identifica que o Tipo de Operação será utilizado para Estorno de Nota Fiscal Eletrônica, situação que ocorre quando é necessário o cancelamento em prazo superior ao estabelecido pela SEFAZ do estado. Quando for acionado o botão **"Cancelar"** sobre uma NF-e que já tenha sido aprovada e o prazo de cancelamento seja maior que o permitido, o sistema abrirá uma janela para informar-se o código da TOP de Estorno (que deve estar com esta opção marcada), a Série e a justificativa para o estorno.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15820648843671)

 

Vale salientar que este campo estará habilitado apenas se as seguintes particularidades forem simultaneamente respeitadas:

- Tipo de movimento: **"Devolução de Venda"** ou **"Devolução de Compra"**;

- Campo** "Tipo de Emissão"** definido como **"Normal"**;

- Campo **"NF-e" **definido como **"Devolução"** ou** "Normal"**.

Para configurações de nota de Estorno é importante verificar o help [NF-e de Estorno.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601354-NF-e-de-Estorno?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg1MTQ3MjYzOTMsInRpY2tldF9pZCI6Mjg0MTU0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY4NzA4ODU0MH0.lRcoqMHdPIV0CGKZLdxlx29FxtKEP3m-V3eWpztRf3Y)

**

![4](https://ajuda.sankhya.com.br/hc/article_attachments/15820559490839)

 OBSERVAÇÃO: **

Caso não seja um estorno, e sim devolução, é necessário verificar a configuração da TOP de devolução utilizada no lançamento.


---

### 🔗 Links e Referências Internas:

- [NF-e de Estorno.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601354-NF-e-de-Estorno?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg1MTQ3MjYzOTMsInRpY2tldF9pZCI6Mjg0MTU0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY4NzA4ODU0MH0.lRcoqMHdPIV0CGKZLdxlx29FxtKEP3m-V3eWpztRf3Y)