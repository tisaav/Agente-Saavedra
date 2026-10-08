# Código de Hash no QR-Code difere do calculado

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042641494-C%C3%B3digo-de-Hash-no-QR-Code-difere-do-calculado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042641494-C%C3%B3digo-de-Hash-no-QR-Code-difere-do-calculado)  
> **ID:** `360042641494` | **Última Atualização:** 2026-07-22T16:07:31Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504754645143)

 MENSAGEM:**

[464 - Rejeição]: Código de Hash no QR-Code difere do calculado.(NT2016.002)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504754646551)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504718318999)

 Acesse o Site da SEFAZ Estadual e procure validar o certificado, acessando o ambiente de 'Nota Fiscal de Consumidor Eletrônica' e busque a informação do  'TOKEN'.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504718324759)

 Acesse: *Comercial » Preferências » Empresa*

- Aba: **"NF-e/NFC-e"**

- Campo: **"TOKEN NFC-e":** coloque neste campo o mesmo código, buscado anteriormente no Site da SEFAZ Estadual'

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504718327191)

 Após o ajuste, emita uma nota NFC-e para buscar as informações do Hash e gerar o QR-Code corretamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504754656663)

CAUSA:**

Quando for emitida uma NFC-e e o QR-Code calculado pelo sistema for diferente do calculado pela Sefaz, será retornado a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504754657943)

 OBSERVAÇÃO:**

([NT2016.002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)) - Nota Técnica