# Total do PIS difere do somatório dos itens sujeitos ao ICMS

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042643374-Total-do-PIS-difere-do-somat%C3%B3rio-dos-itens-sujeitos-ao-ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042643374-Total-do-PIS-difere-do-somat%C3%B3rio-dos-itens-sujeitos-ao-ICMS)  
> **ID:** `360042643374` | **Última Atualização:** 2026-07-22T16:07:21Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482465052695)

**MENSAGEM**

Rejeição 602: Total do PIS difere do somatório dos itens sujeitos ao ICMS.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39743033342231)

**SITUAÇÃO**

Ao realizar a emissão de uma nota fiscal, o sistema apresenta a rejeição 602, indicando que o valor total do PIS informado no cabeçalho da nota não corresponde à soma dos valores de PIS calculados em cada item da nota.

**CAUSA**

Esta rejeição ocorre quando há uma divergência entre o valor total do tributo acumulado nos itens e o valor total reportado no rodapé da nota, geralmente causado por diferenças de arredondamento ou parametrizações incorretas de impostos nos itens da nota.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482470023959)

**SOLUÇÃO**

Para corrigir esta situação, siga os passos abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482465060759)

 Acesse a tela **"Portal de vendas"** (Comercial >>consulta >> Portal de Vendas).
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482470030231)

 Localize a nota que apresentou a rejeição e clique na aba **"Itens"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482470032919)

 Verifique se o valor do PIS em cada item está calculado corretamente conforme a configuração de impostos definida na tela **"Alíquotas de PIS"** (Comercial >> Arquivo >> Cadastros >> Alíquotas).
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39743033343255)

 Certifique-se de que não existem itens com valores de PIS zerados que deveriam possuir tributação, ou vice-versa.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39743039884439)

 Revise os itens e as alterações se necessário 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39743033343895)

 Salve a nota e tente realizar a emissão novamente.