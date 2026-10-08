# The value '-XX' of element 'vUnTrib' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365413-The-value-XX-of-element-vUnTrib-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365413-The-value-XX-of-element-vUnTrib-is-not-valid)  
> **ID:** `360043365413` | **Última Atualização:** 2026-07-22T16:05:11Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453508440343)

 MENSAGEM:**

cvc-pattern-valid: Value '-XX' is not facet-valid with respect to pattern '0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?' for type 'TDec_1110v'.
cvc-type.3.1.3: The value '-XX' of element 'vUnTrib' is not valid.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453508444183)

 SITUAÇÃO:**

Ao realizar emissão de NF-e no **SankhyaW**, acessando o respectivo 'Portal' de emissão, na opção "**Outras Opções**" » "**Ver Acompanhamento"** é possível consultar a rejeição a seguir:

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453508445207)

 SOLUÇÃO:**

Para correção siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453476051351)

 Identifique no lançamento da nota, se existe **valor negativo** para algum dos itens, no campo "**Vlr.Unitário",** conforme exemplo abaixo:

 

![12.png](https://ajuda.sankhya.com.br/hc/article_attachments/360060892793)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453508452119)

 Para uma conferência mais efetiva, acesse o "**[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)"** » "**Botão NF-e"** »** "Gerar XML da NF-e" **em arquivo para conferência', através do XML gerado, confira as tags abaixo para todos os itens, até localizar o item que possui valor negativo:

<prod>
     <cEAN/>
     <cProd>**8585**</cProd>
     <xProd>**PRODUTO TESTE LU**</xProd>
     <NCM>**64029990**</NCM>
     <CFOP>**5102**</CFOP>
     <uCom>**CX**</uCom>
     <qCom>**1**</qCom>
     <vUnCom>**-129.9**</vUnCom>
     <vProd>**-129.90**</vProd>
     <cEANTrib/>
     <uTrib>**CX**</uTrib>

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453476053015)

 Identificado o item com valores incoerentes, realize os devidos ajustes na "**Central de Vendas**", redigite o cabeçalho da nota e gere um novo lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453476055831)

 CAUSA:**

Mensagem apresentada ao gerar lote de uma nota fiscal eletrônica com valores inconsistentes na tag <vUnCom>.


---

### 🔗 Links e Referências Internas:

- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)