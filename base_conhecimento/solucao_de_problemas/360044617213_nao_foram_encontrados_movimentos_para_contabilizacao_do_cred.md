# Não foram encontrados movimentos para contabilização do crédito PIS/COFINS do ativo imobilizado

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617213-N%C3%A3o-foram-encontrados-movimentos-para-contabiliza%C3%A7%C3%A3o-do-cr%C3%A9dito-PIS-COFINS-do-ativo-imobilizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617213-N%C3%A3o-foram-encontrados-movimentos-para-contabiliza%C3%A7%C3%A3o-do-cr%C3%A9dito-PIS-COFINS-do-ativo-imobilizado)  
> **ID:** `360044617213` | **Última Atualização:** 2026-07-22T15:53:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948477166103)

 MENSAGEM:**

Não foram encontrados movimentos para contabilização do crédito PIS/COFINS do ativo imobilizado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948480196887)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948480197911)

 Acesse: *Configurações » Cadastros » Produtos » Produtos - Aba: Bens*

- Sub aba **"Geral",** da aba **"Bens"**

- Valor Aquisição: devidamente preenchido;
- Tem Créd.PIS/COFINS sobre Dep.mensal: marcado
- Cód.Sit.Tributária PIS: devidamente preenchido
- Cód.Sit.Tributária COFINS: devidamente preenchido
- Alíquota PIS: devidamente preenchido
- Alíquota COFINS: devidamente preenchido
- Nro. Parcelas Apr. Cred. PIS/COFINS: devidamente preenchido

- Sub aba** "Depreciação",** da aba **"Bens"**

Preencha os campos desta sub-aba e marque a opção** "Tem depreciação"**.

Aba: **"Contas do Produto"**.

Efetue o vínculo das Contas de Débito e Crédito para Contabilização do Bem e do PIS/COFINS

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948477176983)

 Acesse: *MGEImobilizado » Rotinas » Cálculo da Depreciação Mensal*:

- Mensalmente ter efetuado o cálculo da Depreciação Mensal dos Bens.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948480208791)

**Acesse: *MGEImobilizado » Rotinas » Geração de Lote de Depreciação Fiscal*:

- Efetue a geração do Lote, para registros dos lotes de depreciação de bens para Contabilização.

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948480210455)

 **Acesse: *Contabilização » Rotinas » Contabilização dos Créditos de PIS/COFINS do Ativo Imobilizado*:

- Efetue a geração da Contabilização dos créditos de PIS/COFINS do Ativo. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948477186199)

CAUSA:**

Ocorre quando não foi efetuada a depreciação do ativo e/ou a Contabilização do ativo, antes de efetuar a contabilização dos créditos de PIS/COFINS.