# The content of element 'ICMS' is not complete

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101553-The-content-of-element-ICMS-is-not-complete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101553-The-content-of-element-ICMS-is-not-complete)  
> **ID:** `360043101553` | **Última Atualização:** 2026-07-22T16:08:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482554952855)

 MENSAGEM:**

vc-complex-type.2.4.b: The content of element 'ICMS' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":ICMS00, "http://www.portalfiscal.inf.br/nfe":ICMS10, "http://www.portalfiscal.inf.br/nfe":ICMS20, "http://www.portalfiscal.inf.br/nfe":ICMS30, "http://www.portalfiscal.inf.br/nfe":ICMS40, "http://www.portalfiscal.inf.br/nfe":ICMS51, "http://www.portalfiscal.inf.br/nfe":ICMS60, "http://www.portalfiscal.inf.br/nfe":ICMS70, "http://www.portalfiscal.inf.br/nfe":ICMS90, "http://www.portalfiscal.inf.br/nfe":ICMSPart, "http://www.portalfiscal.inf.br/nfe":ICMSST, "http://www.portalfiscal.inf.br/nfe":ICMSSN101, "http://www.portalfiscal.inf.br/nfe":ICMSSN102, "http://www.portalfiscal.inf.br/nfe":ICMSSN201, "http://www.portalfiscal.inf.br/nfe":ICMSSN202, "http://www.portalfiscal.inf.br/nfe":ICMSSN39, "http://www.portalfiscal.inf.br/nfe":ICMSSN900}' is expected.
erro.handshake=true

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482578532759)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482554963479)

 Acesse: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*

Identifique a regra de ICMS que incidiu na NF-e, acesse o cadastro de Alíquota e verifique o CST na aba: **"Geral"** e o CSOSN na aba: **"Simples Nacional".**

Empresas do Simples Nacional precisam destacar o CSOSN em suas NF-e's e existe uma relação/combinação de CST x CSOSN. 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482578541335)

 Contacte a área Fiscal/Contábil da Empresa para que seja informado corretamente a CST e CSOSN.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482578545559)

 Após os ajustes, inutilize a nota e fature novamente. Certifique os ajustes anteriormente feitos e gere Lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482554972951)

 CAUSA:**

Esta mensagem pode ocorrer quando o CST e o CSOSN informados nos itens não são compatíveis ou se um deles não foi preenchido.