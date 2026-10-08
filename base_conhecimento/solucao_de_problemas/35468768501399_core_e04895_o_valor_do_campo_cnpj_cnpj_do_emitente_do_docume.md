# [CORE_E04895] O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é válido

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35468768501399--CORE-E04895-O-valor-do-campo-CNPJ-CNPJ-do-emitente-do-documento-fiscal-referenciado-informado-n%C3%A3o-%C3%A9-v%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/35468768501399--CORE-E04895-O-valor-do-campo-CNPJ-CNPJ-do-emitente-do-documento-fiscal-referenciado-informado-n%C3%A3o-%C3%A9-v%C3%A1lido)  
> **ID:** `35468768501399` | **Última Atualização:** 2026-07-22T14:25:08Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35468782566551)

 **MENSAGEM:**

[CORE_E04895] O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é válido. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35468768472343)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627209635863)

 Acesse a tela ****[''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal desejada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627195107991)

 Na aba **''Financeiro''**, no campo **''Tipo de Título''** valide o título utilizado no recebimento PIX/Cartão.

 

![tipo de titulo.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627313239575)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627209640343)

 Em seguida, acesse a tela ****[''Tipos de Título'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)**' **(Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627209640855)

 Na aba **''Geral''**, no campo** ''Parc.Administradora''**, identifique o parceiro ativo.

 

![Parc administradora.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627315639831)

 

O campo **"Parc. Administradora"** representa as empresas responsáveis por intermediar as transações realizadas com cartões de crédito entre os estabelecimentos comerciais e as instituições financeiras. Elas fornecem os equipamentos, como máquinas de cartões de crédito/débito e os sistemas necessários para que os estabelecimentos aceitem pagamentos com cartões.

No ícone 

![helptip FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/35468782575767)

 será apresentada a seguinte informação:

 

![image (58).png](https://ajuda.sankhya.com.br/hc/article_attachments/36627496441239)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627195110295)

 Após localizar o parceiro ativo, acesse a tela **''Parceiros'' **(Configurações » Cadastros » Parceiros) e abra o seu cadastro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627209641879)

 No campo **''Tipo de Pessoa''**, marque como **''Jurídica''**.

 

![Juridica.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627209643031)

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36627195113239)

 Já na aba **''Identificação''** no campo **“CNPJ/CPF”**, deve ser informado o CNPJ da instituição responsável pelo processamento das transações. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35468768486807)

CAUSA:**

Conforme a **Nota Técnica NT2023.004 – v1.11**, quando o valor **1** é informado na tag `**<tpIntegra>**`, o sistema passa a exigir o preenchimento do **CNPJ da instituição de pagamento** na tag `**<CNPJ>**`, correspondendo ao responsável pelo processamento da transação.

 

![Imagem](/attachments/token/jiSyB8yJmpLG8Lfd6GXQseg0h/?name=image.png)

 

Saiba mais em: [Notas Técnicas](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=)

                          [Nota Técnica 2023.004 - v.1.11](https://ajuda.sankhya.com.br/hc/pt-br/articles/24258905713815-Nota-T%C3%A9cnica-2023-004-v-1-11)


---

### 🔗 Links e Referências Internas:

- [''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
- [''Tipos de Título'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)
- [Nota Técnica 2023.004 - v.1.11](https://ajuda.sankhya.com.br/hc/pt-br/articles/24258905713815-Nota-T%C3%A9cnica-2023-004-v-1-11)