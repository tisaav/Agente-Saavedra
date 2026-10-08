# E0341 Rejeição: Valor 0 para o Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço não é permitido na Sefin do Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224512770967-E0341-Rejei%C3%A7%C3%A3o-Valor-0-para-o-Mecanismo-de-apoio-fomento-ao-Com%C3%A9rcio-Exterior-utilizado-pelo-prestador-do-servi%C3%A7o-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224512770967-E0341-Rejei%C3%A7%C3%A3o-Valor-0-para-o-Mecanismo-de-apoio-fomento-ao-Com%C3%A9rcio-Exterior-utilizado-pelo-prestador-do-servi%C3%A7o-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e)  
> **ID:** `37224512770967` | **Última Atualização:** 2026-07-22T14:16:33Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224512758679)

 **MENSAGEM**

E0341 Rejeição: Valor 0 para o Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço não é permitido na Sefin do Sistema Nacional NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224512759575)

 **SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** no **Padrão Nacional**, o usuário informou o valor **"0" (zero)** no campo relacionado ao **Mecanismo de apoio/fomento ao Comércio Exterior** utilizado pelo prestador do serviço. A Sefin do Sistema Nacional NFS-e **não permite** que este campo seja preenchido com valor zero, resultando na **rejeição da nota** com a mensagem E0341.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224528463127)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224512761623)

 Acesse a tela **''Portal de Vendas'' **(Comercial » Consulta » Portal de Vendas) e localize a NFS-e que foi rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38323657030295)

 Verifique o campo relacionado ao **"Mecanismo de apoio/fomento ao Comércio Exterior"** e certifique-se de que ele **não esteja preenchido com o valor "0" (zero)**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224512762903)

 Caso o serviço prestado **não utilize** nenhum mecanismo de apoio/fomento ao Comércio Exterior, **deixe o campo em branco** ou remova o valor zero.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224528471703)

 Caso o serviço prestado **utilize** algum mecanismo de apoio/fomento ao Comércio Exterior, informe o **código válido correspondente** ao mecanismo utilizado, conforme orientações da Sefin.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224528474135)

 Salve as alterações realizadas no documento fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224528475031)

 Realize novamente a **transmissão da NFS-e** para a Sefin do Sistema Nacional. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224528477719)

 **CAUSA**

A rejeição ocorre porque a **Sefin do Sistema Nacional NFS-e** possui uma regra de validação que **não aceita o valor "0" (zero)** no campo destinado ao **Mecanismo de apoio/fomento ao Comércio Exterior**. Este campo deve ser preenchido com um **código válido** quando aplicável, ou deve permanecer **em branco** caso o prestador não utilize nenhum mecanismo de apoio/fomento. O preenchimento incorreto com valor zero resulta na **rejeição E0341** durante a transmissão da nota fiscal de serviço eletrônica.