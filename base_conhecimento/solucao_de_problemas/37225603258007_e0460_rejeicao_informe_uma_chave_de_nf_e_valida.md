# E0460 Rejeição: Informe uma chave de NF-e válida.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225603258007-E0460-Rejei%C3%A7%C3%A3o-Informe-uma-chave-de-NF-e-v%C3%A1lida](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225603258007-E0460-Rejei%C3%A7%C3%A3o-Informe-uma-chave-de-NF-e-v%C3%A1lida)  
> **ID:** `37225603258007` | **Última Atualização:** 2026-07-22T14:15:48Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225586914327)

 **MENSAGEM**

E0460 Rejeição: Informe uma chave de NF-e válida.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225603242647)

 **SITUAÇÃO**

Ao tentar transmitir uma NF-e que **referencia outra nota fiscal**, o sistema apresenta a mensagem de rejeição informando que a **chave de acesso informada não é válida**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225603244439)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38293927625879)

 Acesse a nota fiscal que está sendo transmitida e **localize o campo onde a chave de acesso foi informada**. Este campo pode estar:

- 

Acesse a tela** ''Central de Vendas'' **(Comercial » Rotinas » Central de Vendas) e/ou** ''Central de Compras'' **(Comercial » Rotinas » Central de Compras).

- 

Na aba **"NF-e"**, verifique o campo **"Chave NF-e Referenciada"**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225603246615)

 **Verifique se a chave de acesso informada possui 44 dígitos**. Chaves de NF-e válidas devem conter exatamente esta quantidade de caracteres numéricos.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225603247639)

 Consulte a validade da chave no ****[''Portal Nacional da NF-e''](http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=)

- 

Se a chave **não for localizada ou retornar como inexistente**, significa que ela está incorreta.

- 

Se a chave for localizada, **confirme se todos os 44 dígitos estão corretos**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225586918551)

 **Corrija a chave de acesso** no campo correspondente, informando a chave válida da nota fiscal que está sendo referenciada.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225586920087)

 Caso esteja realizando uma **devolução ou referenciando uma nota de entrada**, certifique-se de que a chave informada corresponde à **nota fiscal original que foi recebida**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225603249815)

 **Verifique se o modelo da nota referenciada é válido**. São aceitos apenas os modelos:

- 

**55** - Nota Fiscal Eletrônica (NF-e)

- 

**65** - Nota Fiscal Eletrônica do Consumidor (NFC-e)

- 

**59** - SAT-CF-e

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225586922135)

 Após corrigir a chave de acesso, **salve as alterações** e tente **transmitir a nota novamente**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225603251735)

 **CAUSA**

A rejeição ocorre quando o campo **"Chave NF-e Referenciada"** é preenchido com uma chave de acesso que:

- 

**Não possui 44 dígitos**.

- 

Contém **caracteres inválidos ou dígitos incorretos**.

- 

**Não existe na base da SEFAZ** ou está com informações inconsistentes.

- 

Foi **digitada incorretamente** no momento do lançamento da nota.