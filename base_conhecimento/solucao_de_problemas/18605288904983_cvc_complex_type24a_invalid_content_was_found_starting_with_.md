# cvc-complex-type.2.4.a: Invalid content was found starting with element 'xPag'

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18605288904983-cvc-complex-type-2-4-a-Invalid-content-was-found-starting-with-element-xPag](https://ajuda.sankhya.com.br/hc/pt-br/articles/18605288904983-cvc-complex-type-2-4-a-Invalid-content-was-found-starting-with-element-xPag)  
> **ID:** `18605288904983` | **Última Atualização:** 2026-07-22T14:52:20Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605288898327)

 **MENSAGEM:**

[CORE_E04895] cvc-complex-type.2.4.a: Invalid content was found starting with element 'xPag'.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605233575703)

CAUSA:**

Ocorre quando no XML não está sendo informado qual é o tipo de título (pagamento) referente a nota

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605272625431)

SOLUÇÃO:**

- Abra a nota em questão na central;

- No Rodapé da nota, campo 'Tipo de Título' verifique qual o tipo de título que está sendo utilizado na nota em questão;

- Acesse a tela 'Tipo de Título';

- Aba Geral ;

- Campo: 'Tipo de pgto para NFC-e / NF-e / CF-e'

- Preencha qual é o tipo de pagamento referente aquela nota/título

  - Exemplo: Tipo de título "Dinheiro"

  - Informar dinheiro no campo citado

- Após o ajuste acesse a central novamente e refaça o financeiro da nota

- Gere lote novamente.