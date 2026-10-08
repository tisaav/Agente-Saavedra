# CFOP de operação interestadual e idDest <> 2

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042719394-CFOP-de-opera%C3%A7%C3%A3o-interestadual-e-idDest-2](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042719394-CFOP-de-opera%C3%A7%C3%A3o-interestadual-e-idDest-2)  
> **ID:** `360042719394` | **Última Atualização:** 2026-08-18T16:35:30Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511811138455)

 **MENSAGEM:**

[732 - Rejeição]: CFOP de operação interestadual e idDest <> 2.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511805042199)

 SOLUÇÃO:**

A solução dessa rejeição é corrigir a incompatibilidade entre o "Destino" (Dentro/Fora do Estado) desse lançamento e a CFOP informado nos Itens:

![tABELA.png](https://ajuda.sankhya.com.br/hc/article_attachments/360060886913)

Dessa forma seguem algumas orientações:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511805043223)

 Se o CFOP foi informado manualmente, faça o ajuste de forma manual, verificando com seu Contador qual o CFOP compatível com essa operação.

Importante: A informação de CFOP poderá ser visualizada na Central de Compras/Vendas na linha correspondente a cada produto lançado.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511805046039)

 Se o CFOP foi gerado pela TOP, confira na aba "**Livro Fiscal",** do cadastro do Tipo de Operação utilizado, se essas informações foram inseridas corretamente.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511805050135)

 **Verifique na tela **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)" **(Caminho de acesso: *Comercial » Arquivo » Cadastros » Alíquotas*), para a alíquota correspondente a esse lançamento, em "**outras opções**", se existe alguma "Conversão de CFOP" cadastrada indevidamente.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511805052311)

 IMPORTANTE:**

- O CFOP só poderá ser editada manualmente, se no cadastro da TOP utilizada essa informação estiver em branco.

- Se existirem ajustes na TOP e/ou ALÍQUOTAS DE ICMS, essa nota deverá ser inutilizada/excluída, e o lançamento refeito.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511805054359)

 CAUSA:**

Quando for emitida uma NF-e com Operação de destino (idDest) diferente de "2 - Interestadual" e o CFOP dessa Operação for Interestadual (CFOP iniciado por 2 ou 6), será retornado a rejeição.


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)