# cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsCodigoNbs'. cvc-type.3.1.3: The value '' of element 'CodigoNbs' is not valid.

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18605974257303-cvc-minLength-valid-Value-with-length-0-is-not-facet-valid-with-respect-to-minLength-1-for-type-tsCodigoNbs-cvc-type-3-1-3-The-value-of-element-CodigoNbs-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/18605974257303-cvc-minLength-valid-Value-with-length-0-is-not-facet-valid-with-respect-to-minLength-1-for-type-tsCodigoNbs-cvc-type-3-1-3-The-value-of-element-CodigoNbs-is-not-valid)  
> **ID:** `18605974257303` | **Última Atualização:** 2026-07-22T14:52:17Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605974231319)

 **MENSAGEM:**

cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsCodigoNbs'.
cvc-type.3.1.3: The value '' of element 'CodigoNbs' is not valid.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606019968151)

CAUSA:**

O erro ocorre quando a prefeitura de Brasília espera que via Web Service seja encaminhado o Código NBS de acordo com serviço.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605988817303)

SOLUÇÃO:**

- Acesse o manual que está linkado abaixo e verificar qual o código correto de acordo com o serviço (CodigoNbs)

  - Link: [Manual NBS Brasília](https://drive.google.com/file/d/1b4iEQqeKHd3mH5RUDr86DRh7-juVB2_3/view?usp=sharing)

1. Após conferir qual o código, acesse a tela de "**Serviços**"

1. Aba > Impostos

1. Campo "Código NBS"

1. Insira o código no campo informado

1. Gere lote

1. Após a geração do lote caso o erro persista, retire o XML da tabela TGFNFSE campo XMLRPS e verifique se a tag <CodigoNbs> está preenchida corretamente de acordo com o código que foi informado

1. Caso não duplique a nota que a mesma será aprovada.