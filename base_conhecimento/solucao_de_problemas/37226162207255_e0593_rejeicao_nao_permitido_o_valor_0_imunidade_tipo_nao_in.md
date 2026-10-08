# E0593 Rejeição: Não permitido o valor "0 - Imunidade (tipo não informado na nota de origem)" na DPS quando utilizado os Emissores Públicos Nacionais para emissão de NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226162207255-E0593-Rejei%C3%A7%C3%A3o-N%C3%A3o-permitido-o-valor-0-Imunidade-tipo-n%C3%A3o-informado-na-nota-de-origem-na-DPS-quando-utilizado-os-Emissores-P%C3%BAblicos-Nacionais-para-emiss%C3%A3o-de-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226162207255-E0593-Rejei%C3%A7%C3%A3o-N%C3%A3o-permitido-o-valor-0-Imunidade-tipo-n%C3%A3o-informado-na-nota-de-origem-na-DPS-quando-utilizado-os-Emissores-P%C3%BAblicos-Nacionais-para-emiss%C3%A3o-de-NFS-e)  
> **ID:** `37226162207255` | **Última Atualização:** 2026-07-22T14:15:15Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226162189079)

 **MENSAGEM**

E0593 Rejeição: Não permitido o valor "0 - Imunidade (tipo não informado na nota de origem)" na DPS quando utilizado os Emissores Públicos Nacionais para emissão de NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226162190999)

 **SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** utilizando os **Emissores Públicos Nacionais**, o sistema rejeitou o documento com a mensagem E0593.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226177969175)

 **SOLUÇÃO**

Para resolver esta rejeição, ajuste a **natureza de operação do ISS** configurada no sistema:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226162196631)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Configurações » Cadastros » Tipos de Operação).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226162198039)

 Localize e selecione o **Tipo de Operação** utilizado na emissão da NFS-e rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226177974807)

 Acesse a aba **"NFS-e"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226177978135)

 No campo **"Cód. Natureza Oper. ISS (NFS-e)"**, selecione uma das opções válidas permitidas pela prefeitura:

- 

**''Exigível''**

- 

**''Não incidência''**

- 

**''Isenção''**

- 

**''Exportação''**

- 

**''Imunidade''**

- 

**''Exigibilidade suspensa por decisão judicial''**

- 

**''Exigibilidade suspensa por procedimento administrativo''**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226162201367)

 Salve as alterações realizadas.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226177984791)

 Emita novamente a **NFS-e** utilizando o Tipo de Operação ajustado. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226162204183)

 **CAUSA**

A rejeição ocorreu porque o código **"0 - Imunidade (tipo não informado na nota de origem)"** não é aceito pelos **Emissores Públicos Nacionais** para emissão de NFS-e. Este código específico não está entre as opções válidas de **exigibilidade do ISS** permitidas pelas prefeituras que utilizam o padrão ABRASF. O sistema deve enviar apenas os códigos de **1 a 7**, conforme especificado na documentação técnica da prefeitura.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)