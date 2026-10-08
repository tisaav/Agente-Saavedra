# Os produtos dos itens da nota e sua origem são diferentes. Atualização cancelada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659333-Os-produtos-dos-itens-da-nota-e-sua-origem-s%C3%A3o-diferentes-Atualiza%C3%A7%C3%A3o-cancelada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659333-Os-produtos-dos-itens-da-nota-e-sua-origem-s%C3%A3o-diferentes-Atualiza%C3%A7%C3%A3o-cancelada)  
> **ID:** `360043659333` | **Última Atualização:** 2026-07-22T16:04:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135224523799)

 MENSAGEM:**

ORA-20101: Os produtos dos itens da nota e sua origem são diferentes. Atualização cancelada.
ORA-06512: em "SANKHYA.TRG_INC_UPD_TGFVAR", line 132
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPD_TGFVAR'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135224537623)

 SITUAÇÃO:**

Ao validar a importação de XML de nota de Devolução de venda, pelo Portal de Importação de XML.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135244680215)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135244681239)

 Identifique a Nota de Venda no sistema, seja através da Chave NF-e, referenciada no XML de devolução (Chave NFe <refNFe>), ou acessando o **"[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela)"** e identificando a Nota. Extraia do XML da nota de venda, acessando o botão: **"NFe"** » **"Gerar Arquivo XML de NFe"**, abra o xml pelo Notepadd++.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135244682135)

 Abra o XML da Nota de Devolução, através do Notepad++.

Identifique a sequência dos itens, através da tag **<det nItem="1"> **onde o número 1 é a sequência e, com isso, poderá comparar com a sequência dos itens da nota de venda. Efetue o ajuste da sequência diretamente no XML, para que a sequência do item no XML de Venda seja igual a sequência do item no XML de Devolução.

Salve a alteração no XML da devolução de venda.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135244684695)

 Importe novamente o XML de Devolução de Venda, através do Portal de Importação de XML.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135244685975)

 **CAUSA:**

Ocorre quando, em eventuais casos, a sequência dos itens no XML de Origem (Venda) está diferente da sequência do XML de Devolução de Venda, que está sendo importado, ocasionado quando a nota de Origem não foi lançada no sistema atual ou foi perdida da base e teve que ser lançado novamente.


---

### 🔗 Links e Referências Internas:

- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela)