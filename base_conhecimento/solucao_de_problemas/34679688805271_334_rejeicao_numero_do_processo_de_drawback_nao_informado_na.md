# 334 Rejeição: Número do processo de drawback não informado na importação

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34679688805271-334-Rejei%C3%A7%C3%A3o-N%C3%BAmero-do-processo-de-drawback-n%C3%A3o-informado-na-importa%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/34679688805271-334-Rejei%C3%A7%C3%A3o-N%C3%BAmero-do-processo-de-drawback-n%C3%A3o-informado-na-importa%C3%A7%C3%A3o)  
> **ID:** `34679688805271` | **Última Atualização:** 2026-07-22T14:26:52Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34679688787223)

 **MENSAGEM**

334 Rejeição: Número do processo de drawback não informado na importação

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35689289378455)

 **SITUAÇÃO**

Ao tentar processar a Nota Fiscal Eletrônica de importação com CFOP **"3127"** ou **"3211"**, o sistema apresenta a rejeição informando que o número do processo de drawback não foi informado. O usuário estava lançando produtos importados e não preencheu o campo obrigatório referente ao regime drawback na adição da declaração de importação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34679641964055)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35689289380375)

  Abra a **"Nota Fiscal Eletrônica"** na central de compras.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35689289385239)

  Clique no botão **"Outras Opções"** do item e selecione **"Declaração de Importação e Adições"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34679641965207)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35689318694167)

  No pop-up da **"Declaração de Importação"**, preencha corretamente o campo **"Nro. Ato Conc. regime DrawBack"** para cada produto.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34679688790551)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35689289393943)

  Repita o procedimento para todos os produtos da NFe que utilizam os CFOP **"3127"** ou **"3211"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35689289394839)

  Para conferência, gere o XML da NFe e pesquise pela TAG **"nDraw"** para certificar que foi gerada corretamente em todos os produtos com os CFOP citados.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34679688792215)

 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34679641967767)

 **CAUSA**

A rejeição ocorre quando o campo **"Nro. Ato Conc. regime DrawBack"** não é informado na adição da declaração de importação para produtos lançados com CFOP **"3127"** ou **"3211"**.