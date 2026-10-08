# The value '0.00' of element 'vDup' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574294-The-value-0-00-of-element-vDup-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574294-The-value-0-00-of-element-vDup-is-not-valid)  
> **ID:** `360042574294` | **Última Atualização:** 2026-07-22T16:09:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474615922327)

 MENSAGEM:**

Erro durante validação do XML do lote: cvc-pattern-valid: Value '0.00' is not facet-valid with respect to pattern '0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?' for type 'TDec_1302Opc'.
cvc-type.3.1.3: The value '**0.00**' of element **'vDup**' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474571714327)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474571717015)

 Acesse a Nota Fiscal, aba: "**FINANCEIRO"**.

Verifique os valores de desdobramento de cada título se estão corretos e caso algum valor seja 0(zero), tente refazer o Financeiro- Através do botão "***Outras Opções" » **"**Refazer Financeiro"*****.**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474615926935)

 Se mesmo assim o título ficar com valor 0 (zero), procure analisar o Tipo de Negociação utilizado na nota para verificar se existe alguma fórmula que esteja resultando essa parcela em 0(zero). *Procure orientações de sua Equipe de Financeiro.*

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474571719447)

 Após ajustes da nota, gere lote novamente. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474571720471)

 CAUSA:**

Ocorre quando alguma parcela do título financeiro da nota, está com valor 0 (zero).