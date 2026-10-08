# Como localizar e visualizar integrações financeiras da folha de pagamento

> **Módulo:** Pessoas+ | **Subseção:** Execução das Integrações Contábil e Financeira  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39374998886679-Como-localizar-e-visualizar-integra%C3%A7%C3%B5es-financeiras-da-folha-de-pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39374998886679-Como-localizar-e-visualizar-integra%C3%A7%C3%B5es-financeiras-da-folha-de-pagamento)  
> **ID:** `39374998886679` | **Última Atualização:** 2026-09-26T01:30:32Z

---

A integração financeira permite que os valores processados na folha de pagamento sejam transferidos automaticamente para o módulo financeiro do sistema. Este artigo orienta sobre como localizar essas integrações, identificar o número único financeiro (NUFIN) e solucionar problemas comuns durante o processo.
 

### **Como localizar a integração financeira**

Após realizar a integração financeira da folha de pagamento por meio da rotina: 'Gerenciador de folhas' **(****Pessoal+ » Rotinas Folha » Gerenciador de Folhas), no link abaixo, veja como realizar este processo de integração: **

[https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374-Integra%C3%A7%C3%A3o-Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374-Integra%C3%A7%C3%A3o-Financeira)

Com a integração efetuada, utilize o **"DBExplorer"** (Configurações » Avançado » DBExplorer) para consultar o número único da integração através da seguinte query:
 

**SELECT * FROM TFPBAS WHERE REFERENCIA = 'DD/MM/AAAA'**

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41246569960471)

**
 

Substitua **'DD/MM/AAAA'** pela data de referência da folha integrada e clique em 'executar'.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41246569960983)

 

No resultado da consulta, localize o campo **"NUFIN"**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41246569962903)

Ao pesquisar e aparecer o campo procurado, é necessário clicar em cima do mesmo visando que ele seja direcionado: 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41246594284311)

 

O campo contém o número único da integração financeira.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41246594288023)

Com esse número, acesse a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira) e realize a consulta para conferir se a integração foi realizada corretamente.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41246569965207)

 

###


---

### 🔗 Links e Referências Internas:

- [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374-Integra%C3%A7%C3%A3o-Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374-Integra%C3%A7%C3%A3o-Financeira)