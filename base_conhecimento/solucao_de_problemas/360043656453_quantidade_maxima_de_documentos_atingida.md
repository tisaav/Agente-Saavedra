# Quantidade máxima de documentos atingida

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656453-Quantidade-m%C3%A1xima-de-documentos-atingida](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656453-Quantidade-m%C3%A1xima-de-documentos-atingida)  
> **ID:** `360043656453` | **Última Atualização:** 2026-07-22T16:04:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134672991895)

 MENSAGEM:**

Quantidade máxima de documentos atingida.

A quantidade máxima de 10 documento(s) aberto(s) simultaneamente foi atingida. Selecione um documento para ser substituído.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134691174679)

 SITUAÇÃO:**

Ao selecionar 10 ou mais documentos na tela de Portal de Vendas para devolução, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134691178647)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134672994327)

 Acesse: Configurações » Avançado » Preferências

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134672995607)

 Pesquise pelo parâmetro: **"MAXCENTRAIS** **- Qtd. máx. de Centrais abertas"**: Altere o valor do campo Inteiro, pode aumentar para um valor considerável de acordo com a quantidade de documentos que costuma abrir na central.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14633058457623)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134691180055)

 Após o ajuste, feche a tela de Portal de Vendas e abra os documentos novamente.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17803866701207)

 IMPORTANTE:**

Quando a quantidade definida for 1 (um) registro o sistema irá substituir automaticamente o registro atual pelo anterior. Sendo que, se o registro atual possuir alterações, a seguinte mensagem será apresentada: "O registro atual foi alterado, deseja salvar as alterações?". Após a seleção, o novo documento será carregado na Central.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134672998807)

 CAUSA:**

Ocorre quando a quantidade de notas aberta atingiu o limite estipulado pelo parâmetro MAXCENTRAIS, fazendo com que seja solicitado a troca de uma nota já aberta por outra que deseja abrir, então se faz necessário aumentar o valor do parâmetro.