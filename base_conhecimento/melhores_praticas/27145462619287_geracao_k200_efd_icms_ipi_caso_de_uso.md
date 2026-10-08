# Geração K200 EFD ICMS IPI - Caso de uso

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/27145462619287-Gera%C3%A7%C3%A3o-K200-EFD-ICMS-IPI-Caso-de-uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/27145462619287-Gera%C3%A7%C3%A3o-K200-EFD-ICMS-IPI-Caso-de-uso)  
> **ID:** `27145462619287` | **Última Atualização:** 2026-07-22T14:39:58Z

---

**Registro K200:**

Este registro tem o objetivo de informar o estoque final escriturado no período de apuração informado no Registro K100, por tipo de estoque e por participante, nos casos em que couber, das mercadorias de tipos:

- 00 – Mercadoria para revenda

- 01 – Matéria-Prima

- 02 - Embalagem

- 03 – Produtos em Processo

- 04 – Produto Acabado

- 05 – Subproduto

- 06 – Produto Intermediário

- 10 – Outros Insumos 

 

**Observação: **essa informação existe no Campo TIPO_ITEM do Registro 0200

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450193024663)

 ****Existem duas formas de gerar o K200:**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165330252055)

 Cópia e/ou Contagem:**

Para gerar por esse formato é necessário que o parâmetro **"****GERAK200CTE" **esteja habilitado.

*>>Configurações » Avançado » Preferências *

 

![Geração K200 EFD ICMS IPI - Caso de uso 0.png](https://ajuda.sankhya.com.br/hc/article_attachments/27166101867927)

 

Com esse parâmetro ligado, na tela de **"Geração do EFD"** o campo "**Data de contagem p/k200" **fica disponível para informar a data de Cópia ou Contagem que o sistema deverá considerar para gerar no K200, a informação é buscada na TGFCTE.

- Se a data que informou é referente a cópia, o sistema vai buscar na TGFCTE as linhas de cópia de estoque que tiverem com sequência **1 **(indica que é informação gravada pela cópia)

**Exemplo:**

Na tela** "Cópia de Estoque"**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165916037783)

 Cópia executada em 31/05/2024**

 

![Geração K200 EFD ICMS IPI - Caso de uso 0.1.png](https://ajuda.sankhya.com.br/hc/article_attachments/27166108410007)

 

**No Dbexplorer**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165916037783)

 Consulta na TGFCTE**

 

![Geração K200 EFD ICMS IPI - Caso de uso 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/27166108412567)

 

Na tela** "EFD - Fiscal ICMS/IPI" **

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165916037783)

Data de cópia informada no campo Data da contagem p/ K200

 

![Geração K200 EFD ICMS IPI - Caso de uso 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/27166108414231)

 

*Informações geradas conforma a cópia *

|K200|31052024|1|99100,000|0||
|K200|31052024|21115-9|15550,000|0||

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165916037783)

 Se a data que informou é referente a contagem, o sistema vai buscar na TGFCTE as linhas de contagem de estoque que tiver com sequência **2 **(indica que é informação gravada pela cópia)

**Exemplo:**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165916037783)

**Contagem executada em 31/05/2024

 

![Geração K200 EFD ICMS IPI - Caso de uso 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/27166101874199)

 

Na tela** "EFD - Fiscal ICMS/IPI "**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165916037783)

 Data de cópia informada no campo Data da contagem p/ K200

 

![Geração K200 EFD ICMS IPI - Caso de uso 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/27166101875991)

 

Quando existe cópia e contagem na mesma data, o sistema abre um poup-up para escolher se a geração será pela cópia ou pela contagem.

 

![Geração K200 EFD ICMS IPI - Caso de uso 5.png](https://ajuda.sankhya.com.br/hc/article_attachments/27166101878679)

 

Selecionando pela contagem, as informações que o sistema busca são as que foram informadas através da rotina de Contagem de Estoque.

[https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque)

|K200|31052024|1|1000000,000|0||
|K200|31052024|21115-9|23548963,000|0||

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27165916043671)

 Considerando o Estoque:**

Nesse caso, o registro do inventário seria baseado no saldo de estoque que consta no sistema no último dia do período da referência, ou seja, o saldo que foi registrado no fechamento do SPED da competência em questão, sem realizar uma contagem física.

O Parâmetro GERAK200CTE deve estar desligado, assim o campo Data da contagem p/ K200  não será apresentado na tela de geração do EFD para informar a data. 

Ao gerar o arquivo, o mesmo irá considerar o estoque do último dia do mês que está gerando.

**Exemplo: geração do arquivo é referencia 05/2024, o estoque que será considerado na geração será do dia 31/05/2024.**

K200|31052024|1|99100,000|0||
|K200|31052024|21115-9|15550,000|0||


---

### 🔗 Links e Referências Internas:

- [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque)