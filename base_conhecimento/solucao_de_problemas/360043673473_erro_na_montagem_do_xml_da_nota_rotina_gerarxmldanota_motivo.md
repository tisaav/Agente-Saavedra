# Erro na montagem do XML da nota. Rotina GerarXMLDaNota. Motivo: Nota Número Único XXXXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673473-Erro-na-montagem-do-XML-da-nota-Rotina-GerarXMLDaNota-Motivo-Nota-N%C3%BAmero-%C3%9Anico-XXXXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673473-Erro-na-montagem-do-XML-da-nota-Rotina-GerarXMLDaNota-Motivo-Nota-N%C3%BAmero-%C3%9Anico-XXXXXX)  
> **ID:** `360043673473` | **Última Atualização:** 2026-07-22T16:03:40Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120888294167)

 MENSAGEM:**

Erro na montagem do XML da nota. Rotina GerarXMLDaNota. Motivo: Nota Número Único XXXXXX. O arquivo do modelo "\\hostname\pasta\nomearquivo.txt" não existe!!!

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917592727)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120888302103)

 Acesse Menu » Arquivos » Cadastros » Tipos de Operação:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917596311)

 "Modelo de Impressão de nota fiscal"**: Verifique o código informado aqui

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917596311)

 "Modelo para Dados Adicionais de NF-e"**: Verifique o código informado aqui

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14629212241431)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917597975)

 Acesse: Menu » Avançado » Modelos de Nota Fiscal/Duplicatas/Boletos:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917596311)

 **Encontre o código que foi verificado no cadastro de TOP. 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917596311)

 **No campo **"Caminho"** do cadastro do modelo, estará o mesmo caminho relatado na mensagem de erro.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917599255)

 Este caminho/endereço, deverá estar disponível e acessível na máquina local ou em um diretório compartilhado.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917601303)

 Solicite que a Equipe de TI faça as verificações necessárias para que o arquivo e o diretório estejam acessíveis.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120917604119)

 CAUSA:**

Ocorre quando o arquivo modelo de impressão ou o caminho/diretório não está acessível, geralmente se trata de um diretório compartilhado que pode estar em outro computador e este computador pode estar inacessível (fora da rede interna, desligado).