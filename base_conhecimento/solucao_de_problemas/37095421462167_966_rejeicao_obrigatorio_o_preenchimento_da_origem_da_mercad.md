# 966 Rejeição: Obrigatório o preenchimento da origem da mercadoria [nItem:nnn]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095421462167-966-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3rio-o-preenchimento-da-origem-da-mercadoria-nItem-nnn](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095421462167-966-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3rio-o-preenchimento-da-origem-da-mercadoria-nItem-nnn)  
> **ID:** `37095421462167` | **Última Atualização:** 2026-07-22T14:21:43Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095421444375)

 **MENSAGEM**

966 Rejeição: Obrigatório o preenchimento da origem da mercadoria [nItem:nnn]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095453046295)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida com um ou mais itens do documento fiscal sem a informação da origem da mercadoria devidamente registrada, resultando na rejeição da nota pelo sistema.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095453046679)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095453047575)

 Acesse a tela de **"Produtos"** (Configurações » Cadastros » Produtos » Produtos). 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095421451415)

 Localize o produto que está apresentando a rejeição. O número do item com problema é indicado na mensagem de erro [nItem:nnn].

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095421452183)

 Na aba **"Fiscal"**, verifique o campo **"Origem da Mercadoria"** e selecione a opção adequada conforme a procedência do produto:

- 

**0 – Nacional:** exceto as indicadas nos códigos 3, 4, 5 e 8.

- 

**1 – Estrangeira – Importação direta:** exceto a indicada no código 6.

- 

**2 – Estrangeira – Adquirida no mercado interno:** exceto a indicada no código 7.

- 

**3 – Nacional:** mercadoria ou bem com **Conteúdo de Importação superior a 40% e inferior ou igual a 70%**.

- 

**4 – Nacional:** produção realizada em conformidade com os **Processos Produtivos Básicos (PPB)**.

- 

**5 – Nacional:** mercadoria ou bem com **Conteúdo de Importação inferior ou igual a 40%**.

- 

**6 – Estrangeira – Importação direta:** sem similar nacional, constante em lista da **CAMEX**.

- 

**7 – Estrangeira – Adquirida no mercado interno:** sem similar nacional, constante em lista da **CAMEX**.

- 

**8 – Nacional:** mercadoria ou bem com **Conteúdo de Importação superior a 70%**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095421454743)

 Salve as alterações no cadastro do produto.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095421455511)

 Retorne à tela de emissão da nota fiscal e gere um novo lote para transmissão. 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095453054487)

 **CAUSA**

A rejeição ocorre porque a legislação fiscal brasileira exige que seja informada a origem da mercadoria em todos os itens da nota fiscal.

Esta informação é fundamental para a correta aplicação da tributação, especialmente com a implementação da Reforma Tributária (Lei Complementar nº 214/2025), que estabelece diferentes alíquotas para o IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços) de acordo com a origem do produto.

A origem da mercadoria é um campo obrigatório que deve ser preenchido no cadastro do produto e transmitido no XML da nota fiscal. Quando este campo não é informado, a SEFAZ rejeita o documento fiscal, impedindo sua autorização.