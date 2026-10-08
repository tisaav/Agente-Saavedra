# Data de vencimento da parcela não informada ou menor que Data de Autorização

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102213-Data-de-vencimento-da-parcela-n%C3%A3o-informada-ou-menor-que-Data-de-Autoriza%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102213-Data-de-vencimento-da-parcela-n%C3%A3o-informada-ou-menor-que-Data-de-Autoriza%C3%A7%C3%A3o)  
> **ID:** `360043102213` | **Última Atualização:** 2026-07-22T16:08:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444199326871)

 MENSAGEM:**

[898-Rejeição]: Data de vencimento da parcela não informada ou menor que Data de Autorização [nOcor:999]-NT(2016/002).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444207302935)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444207303831)

 Abra a nota na "**Central de Notas**".

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444207306391)

 Localize a aba "**Financeiro**" e verifique se existe algum título com a data de vencimento anterior a data de geração de lote da nota.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444207307031)

 Em caso positivo, refaça o Financeiro:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444199336087)

 Acesse o botão: "**Outras Opções(...)"** do Cabeçalho da Nota e clique em "**Refazer Financeiro**".

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444207309591)

 Para títulos com vencimento a vista, a data de vencimento deverá ser igual a data atual.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444199337239)

 Certifique-se que os vencimentos tenham sido devidamente ajustados e gere um novo lote.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444207313687)

 IMPORTANTE:**

Caso ao refazer o financeiro, o vencimento continue sendo apresentado com data anterior a data atual, verifique o parâmetro **DTCALCVENC**, para compreender qual data está sendo considerada no cálculo e, assim, facilitar os ajustes.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444199340055)

 CAUSA:**

Ocorre quando o vencimento do(s) titulo(s) do financeiro da nota é menor que a data de autorização da NF-e.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444207314583)

 **OBSERVAÇÃO:**

**1-** (**NT2016/002**) Nota Técnica:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)