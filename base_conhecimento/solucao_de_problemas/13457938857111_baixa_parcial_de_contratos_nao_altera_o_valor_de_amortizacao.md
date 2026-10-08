# Baixa parcial de contratos não altera o valor de amortização do contrato, veja o que fazer

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/13457938857111-Baixa-parcial-de-contratos-n%C3%A3o-altera-o-valor-de-amortiza%C3%A7%C3%A3o-do-contrato-veja-o-que-fazer](https://ajuda.sankhya.com.br/hc/pt-br/articles/13457938857111-Baixa-parcial-de-contratos-n%C3%A3o-altera-o-valor-de-amortiza%C3%A7%C3%A3o-do-contrato-veja-o-que-fazer)  
> **ID:** `13457938857111` | **Última Atualização:** 2026-07-22T15:00:10Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17083735936151)

 SITUAÇÃO:**

Ao realizar a baixa parcial de uma parcela de Loteamento o sistema está trazendo o campo **"Valor de amortização contrato"** igual ao da parcela original.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17083735941271)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17083735946775)

 O campo Vlr. Amortização Contrato terá o valor da soma de amortização do contrato, de acordo com o detalhamento de amortização do contrato contido no título.

E esse valor só muda quando há um recálculo na parcela, como reajuste, transferência, etc.

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13457837407639)

**

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450720284823)

 O comportamento do sistema se trata da seguinte forma:

No processo de baixa ou estorno de uma parcela, o campo Vlr. Amortização Contrato: (**"TIMVLRAMORTCONTRATO"**) não é alterado. Ainda que a baixa seja parcial ou total, o sistema considera no campo Vlr. Amortização Contrato o mesmo valor da amortização do Tipo de Detalhamento que corresponde a parcela em questão.
Uma opção que o sistema alteraria o campo Vlr. Amortização Contrato é quando for alterado o campo "**Valor",** da aba **"Detalhamentos p/ Loteamento"**. Porém, o sistema atualiza o campo Vlr. Amortização Contrato com a mesma informação do Campo Valor.