# Informado idEstrangeiro e Operação não é com consumidor final (NT2015/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043061853-Informado-idEstrangeiro-e-Opera%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-com-consumidor-final-NT2015-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043061853-Informado-idEstrangeiro-e-Opera%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-com-consumidor-final-NT2015-002)  
> **ID:** `360043061853` | **Última Atualização:** 2026-07-22T16:09:10Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094598167)

 MENSAGEM:**

[721- Rejeição]: Informado idEstrangeiro e Operação não é com consumidor final (NT2015/002)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094598807)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094599959)

 **Caso seja realizada uma operação para o Exterior, o parceiro da NF-e deve estar classificado como 'Consumidor Final Não Contribuinte' e o CFOP deve iniciar-se com 7.

- Cadastro do Parceiro, aba "**Fiscal"**, campo "**Classificação ICMS"**= 'Consumidor Final Não Contribuinte'

- Cadastro da "****[TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" (Caminho de acesso:* Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*), aba "**Livro Fiscal"**, em ' CFOP's para Fora do Estado': verifique com Contador o CFOP a ser utilizado, respeitando a regra de iniciar em 7.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094600727)

 Na tela "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso:* Configuração » Cadastro » Parceiro*), aba "**Identificação"**, o campo "**Identificação de Estrangeiro"** deve ser preenchido:

 

![Captura_de_tela_2023-05-10_110127.png](https://ajuda.sankhya.com.br/hc/article_attachments/14494307142551)

 

A informação neste campo tem a finalidade de informar na geração da NF-e a tag <idEstrangeiro> no caso de operação com o exterior, ou para comprador estrangeiro. Assim, informa-se o número do passaporte ou outro documento legal que identifique a pessoa estrangeira; este campo pode permanecer vazio para outras situações. A informação aqui inserida, deve conter no mínimo 5 e no máximo 20 caracteres/números.

Para mais informações sobre configurações relacionadas a parceiro estrangeiro, verificar o artigo: [Como cadastrar Parceiro ESTRANGEIRO ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535474)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458226982551)

 Caso não trate-se de uma Operação para o Exterior:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094599959)

 Se for realizada uma Operação Nacional (Estadual/Interestadual), analise:

- Campo "**Identificação de Estrangeiro"** não deverá estar preenchido;

- CFOP não iniciará em 7;

- Endereço do Parceiro da NF-e, a UF que está sendo utilizada não poderá ser simbolizada por EX.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094600727)

 Após os ajustes, realize um novo lançamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094602263)

 CAUSA:**

Quando for emitida uma NF-e com Destinatário do Exterior, onde o Destino da Mercadoria ocorre dentro do Brasil, podendo ser uma Operação Estadual ou Interestadual e a Operação não for igual a "1 - Consumidor Final", será retornado a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474094603031)

 OBSERVAÇÃO:**

([NT](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=)[2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=)) - Nota Técnica.


---

### 🔗 Links e Referências Internas:

- [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)
- [Como cadastrar Parceiro ESTRANGEIRO ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535474)