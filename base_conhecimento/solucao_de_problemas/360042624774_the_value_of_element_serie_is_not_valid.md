# The value '' of element 'Serie' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624774-The-value-of-element-Serie-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624774-The-value-of-element-Serie-is-not-valid)  
> **ID:** `360042624774` | **Última Atualização:** 2026-07-22T16:08:39Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482834154135)

 MENSAGEM:**

cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsSerieRps'. cvc-type.3.1.3: The value '' of element 'Serie' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482862120087)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458167866007)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP *

"**Outras Opções**"(...)>>"**Controle de Numeração**".

 

![The_value____of_element__Serie__is_not_valid.png](https://ajuda.sankhya.com.br/hc/article_attachments/14536719263255)

 

Ao clicar nesta opção será aberto o pop-up "**Controle Numeração TOP**". Caso a numeração da empresa tenha série, esta deve ser informada e o 'Tipo de Numeração', por exemplo, ser 'Empresa/Série', 'Matriz/Série' (...). 

*O "***Tipo de Numeração***" é configurado na aba "***Impressão***" da TOP.*

Importante: As Prefeituras determinam como será a composição da SÉRIE, se utilizará Alfa Numérico ou apenas Número ou Letras.

**Exemplo:** Séries: U, 1A, 1.

O lançamento da série pode ser feito manualmente na nota, caso não tenha sido informado no faturamento, ou tratar-se de um lançamento manual.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482834162071)

 CAUSA:**

Quando for emitida uma NF-e/NFS-e e não for informado valor no campo 'Série' do Cabeçalho da Nota, apresentará esta rejeição.