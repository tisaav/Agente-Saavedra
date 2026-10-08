# cvc-type.3.1.3: The value '0.00' of element 'pRedBC' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360060560434-cvc-type-3-1-3-The-value-0-00-of-element-pRedBC-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060560434-cvc-type-3-1-3-The-value-0-00-of-element-pRedBC-is-not-valid)  
> **ID:** `360060560434` | **Última Atualização:** 2026-07-22T15:25:48Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16301906980119)

 MENSAGEM**:

cvc-pattern-valid: Value '0.00' is not facet-valid with respect to pattern '0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?' for type 'TDec_0302Opc'.
cvc-type.3.1.3: The value '0.00' of element 'pRedBC' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16301906981271)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16301919832471)

 *Comercial » Rotinas » Central de Vendas*

 

Quando o produto houver incidência de Tributação CST (20 ou 70), deverá haver a redução de base de ICMS / ICMS-ST.

- Acesse a Nota pela Central de Notas e identifique nos itens qual a tributação que incidiu.

 

![cvc-type.3.1.3_The_value__0.00__of_element__pRedBC__is_not_valid_1.png](https://ajuda.sankhya.com.br/hc/article_attachments/15022797336087)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16301919833239)

 Identifique a Regra de ICMS que a nota foi calculada, podendo ser pelo 'Cód. Aliq. ICMS nos itens:

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500001892362)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16301906983063)

 Acesse o cadastro de Alíquotas de ICMS em: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*

No campo **"Alíquotas"** do lado superior esquerdo pode pesquisar pelo Código de Alíquotas de ICMS, ou Navegar pela árvore de regras, até encontrar a Regra de ICMS desejada.

 

3.1- Quando a CST for 20, deverá ter a porcentagem de redução de base de ICMS no campo, Redução da base, da aba: **"Geral".**

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500001942141)

 

3.2- Quando a CST for 70, deverá ter a porcentagem de redução de Base de ICMS-ST no campo **"Redução Base ST"**, da aba: **"Substituição Tributária"**.

 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500001942181)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453218540695)

 Nota**: lembre-se que para os ajustes recomendáveis, o contador da empresa deve dar o aval da porcentagem de redução que precisa ser inserida.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16301906985879)

 Após os ajustes fature novamente o pedido para nota ou redigite os itens da nota, para depois gerar o **lote**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16301919838103)

 CAUSA:**

Ocorre quando há incidência de tributação com CST 20 ou 70, porém não foram determinados os percentuais de redução de base, na configuração das Alíquotas de ICMS.