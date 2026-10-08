# cvc-type.3.1.3: The value '-XX' of element 'vICMS' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227893-cvc-type-3-1-3-The-value-XX-of-element-vICMS-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227893-cvc-type-3-1-3-The-value-XX-of-element-vICMS-is-not-valid)  
> **ID:** `360043227893` | **Última Atualização:** 2026-07-22T16:06:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514746063767)

 MENSAGEM:**

cvc-pattern-valid: Value '-XX' is not facet-valid with respect to pattern '0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?' for type 'TDec_1302'.
cvc-type.3.1.3: The value '-XX' of element 'vICMS' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514746067607)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514736213783)

 Mensagem ocorre quando informado um "**Vlr.ICMS"** **negativo** para determinado produto. Certifique-se que essa situação está ocorrendo, selecionando os itens da nota >> "**Outras Opções"** >> "**Consultar/alterar dados dos impostos do item"**:

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514736218263)

 Localizado o item com o valor incorreto para o imposto ICMS, verifique se as configurações realizadas para o cálculo desse imposto foram realizadas corretamente.  Caso tenha dúvida sobre como realizar essa análise, recomendamos as orientações do artigo "[Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050753)".

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514736219671)

 Caso a configuração esteja incorreta, realize os devidos ajustes, redigite o cabeçalho da nota e gere um novo lote. 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514746074775)

 Caso não localize nenhuma divergência nos cadastros, avalie com cautela as informações de 'Desconto' inseridas nos itens e rodapé da nota. Essa situação pode ser causada por descontos inseridos acima de 100% do total da NF-e, gerando valores negativos indevidos.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514746076311)

 OBSERVAÇÕES:**

Se nenhuma das situações acima for diagnosticada, recomendamos inutilizar a numeração dessa NF-e e realizar um novo faturamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514746079511)

 CAUSA:**

Mensagem ocorre quando informado um 'Vlr.ICMS' negativo para determinado produto da respectiva nota fiscal eletrônica.


---

### 🔗 Links e Referências Internas:

- [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050753)