# Invalid content was found starting with element 'EXTIPI'

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624894-Invalid-content-was-found-starting-with-element-EXTIPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624894-Invalid-content-was-found-starting-with-element-EXTIPI)  
> **ID:** `360042624894` | **Última Atualização:** 2026-07-22T16:08:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486386873623)

 MENSAGEM:**
cvc-complex-type.2.4.a: Invalid content was found starting with element 'EXTIPI'. One of '{"http://www.portalfiscal.inf.br/nfe":NCM}' is expected. Erro.handshake=true

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486408362903)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486408366487)

 Acesse a nota e na grade de itens verifique o campo: **"C.S.T IPI"**, identifique se o produto tem Incidência de IPI e ajuste o CST de IPI de Acordo com a Tributação de IPI.

Posteriormente, revise as configurações de Código Sit. Trib. IPI Saída e ou Entrada disponíveis no cadastro de 'Empresa, Parceiro, Produto, TOP e Alíquota de IPI'.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486408369303)

 Ainda na grade de Itens, verifique o campo **"NCM"**. Este deve conter o código NCM válido.
No cadastro de **["produtos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) **(Caminho de acesso:* Configurações » Cadastros » Produtos » Produtos*) há o campo **"NCM"**, na aba: **"Geral"**.
Quando devidamente preenchido, o valor desse campo é levado automaticamente para a NF-e.

Após os ajustes, redigite Empresa/Parceiro da nota e gere lote novamente. Caso seja necessário,inutilize a nota e fature novamente. Certifique os ajustes anteriormente feitos e gere lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486386890391)

 CAUSA:**

Esta mensagem ocorre quando existe inconsistência nas informações de CST IPI, ou até mesmo quando o NCM de algum produto foi informado incorretamente ou não foi informado.


---

### 🔗 Links e Referências Internas:

- ["produtos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)