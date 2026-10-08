# Pelo menos uma Mat.Prima deve ter preço

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9455839975447-Pelo-menos-uma-Mat-Prima-deve-ter-pre%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/9455839975447-Pelo-menos-uma-Mat-Prima-deve-ter-pre%C3%A7o)  
> **ID:** `9455839975447` | **Última Atualização:** 2026-07-22T15:07:46Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15448070439063)

  MENSAGEM:**

[CORE_E01244]  Pelo menos uma Mat.Prima deve ter preço.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15448057391127)

 CAUSA:**

 Ocorre quando se realiza negociações com um produto 'KIT'. e nenhum de seus componentes possui preço de tabela.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15448070444951)

 SOLUÇÃO:**

Verificar as seguintes configurações para cálculo do preço do componente.

- 
**Tipos de operação TOP** *(Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP)*

**Usar como Preço:** Preço de Venda

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15448029833751)

 

- 
**Tabela de preços*** (Comercial » Arquivo » Tabelas de Preços)*

Criado uma tabela e adicionar o item com o seu preço.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/9455636998039)

- Cadastros de **Parceiros** *(Configurações » Cadastros » Parceiros) *

Aba Grupo ICMS/ISS por Empresa >> Adicionando a EMPRESA e a Tabela de Preço criada anteriormente 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15448066797463)

- Cadastro da **Empresa*** (Comercial » Preferências » Empresa)*

Aba Estoque/Preço>> Tabela de preço para venda Vincular tabela criada anteriormente

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15448083008791)

- **PARÂMETROS QUE INFLUENCIAM**

**TIPTABPRECOS: **Parceiro/Empresa (Conforme informado que a tabela de preço seria por parceiro e empresa)

**USARCODTABEMP: **Ligado

**PRECOPORCONT: **Desligado

**PRECOPORLOC: **Desligado