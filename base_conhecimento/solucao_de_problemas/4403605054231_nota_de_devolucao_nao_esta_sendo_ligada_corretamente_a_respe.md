# Nota de Devolução não está sendo ligada corretamente à respectiva Nota de Venda via importação de xml

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4403605054231-Nota-de-Devolu%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-sendo-ligada-corretamente-%C3%A0-respectiva-Nota-de-Venda-via-importa%C3%A7%C3%A3o-de-xml](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403605054231-Nota-de-Devolu%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-sendo-ligada-corretamente-%C3%A0-respectiva-Nota-de-Venda-via-importa%C3%A7%C3%A3o-de-xml)  
> **ID:** `4403605054231` | **Última Atualização:** 2026-07-22T15:23:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16345165611287)

 MENSAGEM**:

Nota de Devolução não está sendo ligada corretamente à Nota de Venda via Portal de Importação XML. 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16345150178583)

 CAUSA:**

O incidente é causado pela ausência da tag de referência ***<NFref> <refNFe>**  *da nota de origem no xml de devolução. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16345150175383)

 SOLUÇÃO:**

Verifique no xml se consta o a tag ***<NFref> <refNFe> ***devidamente preenchida com a chave da nota de origem.  Observe também a tag ***<finNFe> ***se está com a Finalidade correta (4), no caso de devolução. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15081748304791)