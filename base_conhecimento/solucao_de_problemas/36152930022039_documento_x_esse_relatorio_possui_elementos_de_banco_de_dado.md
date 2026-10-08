# Documento X: Esse relatório possui elementos de banco de dados, portanto precisa ser autorizado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36152930022039-Documento-X-Esse-relat%C3%B3rio-possui-elementos-de-banco-de-dados-portanto-precisa-ser-autorizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/36152930022039-Documento-X-Esse-relat%C3%B3rio-possui-elementos-de-banco-de-dados-portanto-precisa-ser-autorizado)  
> **ID:** `36152930022039` | **Última Atualização:** 2026-07-22T14:23:39Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36152930008087)

 **MENSAGEM:**

Documento 80229: Esse relatório possui elementos de banco de dados, portanto precisa ser autorizado

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622276973207)

 **SITUAÇÃO:**

Ao tentar imprimir um pedido/nota a mensagem de erro é apresentada:

 

![Imagem](https://p23.zdusercontent.com/attachment/9618168/ORGrgRAJVhi1F4HCPtf8yKRPW?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..xgHdQx9O6sTKxdLVCYN32Q.eWRLbFczUYLpZopZepBhs4RnqaHoTxBUnxVboEaQcoduFysX8CoMlCF5XD3By0VmHbiYOM1RYE-Bto5jQnMGTkOJfYgoYO7p6yQi6KRuIqYynXY6PVDw1oKBpjVq2P_MAMs3ssCqtpK7fH2x7bUPHWjd8c3QmFsfAwwRxU5Ew0lBY_QTrQ0fbOR4iZp2FtBuhYIsFopPzJCouzGupB2I2KOZzd6IwB7hc8IO-UudipuEo3_fkjQtv-h2IwlShpk8xv5XvVqmxbO32Cwh8eU_HUXA__-zONXLgPBzr1HCunL-i6xEToXTrAJ_R2wkvE9F.cSH2XsmnNmectyo9uGD0gw)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36152946476951)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622276973463)

 Acesse a tela ****[''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622276973591)

 Localize a** **''TOP'**'** utilizada no processo.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622293237527)

 Em seguida, clique na aba **''NF-e/NFC-e/CF-e'' **e localize no campo** ''Modelo de impressão de nota fiscal''** o modelo atual utilizado no processo.

 

![image (55).png](https://ajuda.sankhya.com.br/hc/article_attachments/36622276974999)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622293238935)

 Após verificar qual modelo está configurado na ''TOP'', acesse a tela ****[''Modelos de Nota Fiscal/Duplicatas/Boleto(s)''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s) ( Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622276976535)

 **Pesquise** pelo **código do modelo** encontrado no passo 3.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622293240855)

 Em seguida, na aba **''Geral'**' verifique qual relatório formatado está associado no campo** ''Número do relatório modelo”**.

(Este é o relatório que requer autorização para permitir a impressão).

 

![image (56).png](https://ajuda.sankhya.com.br/hc/article_attachments/36622276977047)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36152930009879)

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622293242135)

 Após identificar qual relatório formatado está sendo utilizado, acesse a tela ****[''Autorização de Customizações''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es)** **(Configurações » Avançado » Autorização de Customizações), e realize a liberação na aba **''Relatórios''**.

 

![autorização.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622293242391)

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36622293243159)

 Feito a liberação será possível a impressão.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36152946483863)

CAUSA:**

A mensagem ocorre porque o relatório formatado utilizado pela TOP para impressão requer liberação na tela ''Autorização de Customizações''.

Sem essa liberação, o sistema impede a execução do relatório.


---

### 🔗 Links e Referências Internas:

- [''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [''Modelos de Nota Fiscal/Duplicatas/Boleto(s)''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s)
- [''Autorização de Customizações''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es)