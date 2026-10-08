# CORE_E01793 - Tipo de Negociação Divergente! No cabeçalho da nota, o Tipo de Negociação informa X parcela(s). No XML Importado, está informando X parcela(s)

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34879400815383-CORE-E01793-Tipo-de-Negocia%C3%A7%C3%A3o-Divergente-No-cabe%C3%A7alho-da-nota-o-Tipo-de-Negocia%C3%A7%C3%A3o-informa-X-parcela-s-No-XML-Importado-est%C3%A1-informando-X-parcela-s](https://ajuda.sankhya.com.br/hc/pt-br/articles/34879400815383-CORE-E01793-Tipo-de-Negocia%C3%A7%C3%A3o-Divergente-No-cabe%C3%A7alho-da-nota-o-Tipo-de-Negocia%C3%A7%C3%A3o-informa-X-parcela-s-No-XML-Importado-est%C3%A1-informando-X-parcela-s)  
> **ID:** `34879400815383` | **Última Atualização:** 2026-07-22T14:26:29Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34879400809111)

 **MENSAGEM**

[CORE_E01793] Tipo de Negociação Divergente! No cabeçalho da nota, o Tipo de Negociação informa X parcela(s). No XML Importado, está informando X parcela(s). O Tipo de Negociação da nota deve ser alterado!

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35708319890711)

 **SITUAÇÃO**

Ocorre ao importar um arquivo XML de Nota Fiscal quando a quantidade de parcelas informada no XML é diferente da quantidade de parcelas definida no **"Tipo de Negociação"** do cabeçalho da nota. O usuário tenta importar o XML sem que o parâmetro adequado esteja ativado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34879400810263)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35708280354327)

  Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35708319893783)

  Localize o parâmetro **"Importa negociação divergente do xml da compra?" (IMPNEGDIVXMLCMP)** e altere para **"Ligado"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34879400811927)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35708280357015)

  Feche a tela da **"Central de Compras"**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35708280358551)

  Realize novamente a importação do XML.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34879414850839)

 **CAUSA**

O erro ocorre porque o parâmetro **IMPNEGDIVXMLCMP** está desligado, impedindo a importação de XMLs em que a quantidade de parcelas diverge da quantidade definida no **"Tipo de Negociação"** do cabeçalho da Nota Fiscal.