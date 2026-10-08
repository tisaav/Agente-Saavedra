# E0266 Rejeição: CPF do intermediário informado na DPS é inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223104463511-E0266-Rejei%C3%A7%C3%A3o-CPF-do-intermedi%C3%A1rio-informado-na-DPS-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223104463511-E0266-Rejei%C3%A7%C3%A3o-CPF-do-intermedi%C3%A1rio-informado-na-DPS-%C3%A9-inv%C3%A1lido)  
> **ID:** `37223104463511` | **Última Atualização:** 2026-07-22T14:17:02Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223119541527)

 **MENSAGEM**

E0266 Rejeição: CPF do intermediário informado na DPS é inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223104451991)

 **SITUAÇÃO**

Ao transmitir uma **NF-e** ou **NFC-e** contendo informações de intermediário da operação na **Declaração de Prestação de Serviços (DPS)**, o sistema retorna a rejeição informando que o **CPF do intermediário** está inválido. Esta situação ocorre durante o processo de autorização do documento fiscal junto à SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223119542935)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223104453143)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223119544983)

 Localize o cadastro do **intermediário** informado na operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37798073719959)

 Na aba **"Identificação"**, localize o campo **"CNPJ / CPF"** e verifique se o **CPF informado** está correto e válido.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223104455703)

 Certifique-se de que o CPF possui **11 dígitos**, sem pontos, traços ou espaços em branco, e que o **dígito verificador** (últimos dois números) está correto.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223119547415)

 Caso o CPF esteja incorreto ou inválido, corrija a informação inserindo um **CPF válido** na Receita Federal do Brasil.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223119548439)

 Salve as alterações realizadas no cadastro do parceiro.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223104458263)

 Retorne ao documento fiscal e redigite as informações do **cabeçalho da nota**, incluindo os dados da **empresa** e do **intermediário**, para que o sistema recalcule os dados corretamente.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37798073721879)

 Gere um novo lote e transmita novamente a **NF-e** ou **NFC-e** para a SEFAZ. 
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37798049729431)

 OBSERVAÇÃO:** Caso o problema persista após as correções, inutilize a numeração do documento, exclua a nota e gere uma nova NF-e ou NFC-e com as informações corretas.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223104458903)

 **CAUSA**

A rejeição ocorre quando o **CPF do intermediário** informado na **Declaração de Prestação de Serviços (DPS)** está inválido, seja por conter **sequência numérica incorreta**, **dígitos verificadores inválidos**, ou por estar preenchido apenas com zeros. A SEFAZ valida o CPF informado e, caso não esteja em conformidade com as regras da Receita Federal, retorna a rejeição E0266.