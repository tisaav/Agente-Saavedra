# cvc-complex-type.2.4.a: Invalid content was found starting with element 'ISSQN'

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043660253-cvc-complex-type-2-4-a-Invalid-content-was-found-starting-with-element-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043660253-cvc-complex-type-2-4-a-Invalid-content-was-found-starting-with-element-ISSQN)  
> **ID:** `360043660253` | **Última Atualização:** 2026-07-22T16:04:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143851871511)

 MENSAGEM**:

cvc-complex-type.2.4.a: Invalid content was found starting with element 'ISSQN'. One of '{"http://www.portalfiscal.inf.br/nfe":IPI, "http://www.portalfiscal.inf.br/nfe":II, "http://www.portalfiscal.inf.br/nfe":PIS, "http://www.portalfiscal.inf.br/nfe":PISST, "http://www.portalfiscal.inf.br/nfe":COFINS, "http://www.portalfiscal.inf.br/nfe":COFINSST, "http://www.portalfiscal.inf.br/nfe":ICMSUFDest}' is expected.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143851873687)

 SOLUÇÃO**:

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143851875991)

 Acesse: *Configurações » Cadastros » Produtos » Serviço*
Aba: **Impostos**
Opção **"Calcular ICMS"**: marcado. Caso este campo esteja marcado, salvo a exceção de Nota Mista para 'Brasília-DF', deverá verificar a incidência deste imposto em uma nota de Serviço, e considerar **desmarcar** este campo no cadastro do serviço.

 

![servicos3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14634160328727)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143851878167)

 Após o ajuste, exclua o serviço da nota, lance novamente e transmita a nota de Serviço.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143851879831)

 CAUSA**:

Ocorre quando a Nota de Serviço está configurada para calcular ISS e ICMS ao mesmo tempo, salvo a nota Mista para Brasília-DF, deverá verificar a incidência de ICMS em uma Nota de Serviço e desmarcar a opção.