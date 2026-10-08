# A atualização de estoque deve ser diferente entre a TOP de origem e a TOP de destino

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043362733-A-atualiza%C3%A7%C3%A3o-de-estoque-deve-ser-diferente-entre-a-TOP-de-origem-e-a-TOP-de-destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043362733-A-atualiza%C3%A7%C3%A3o-de-estoque-deve-ser-diferente-entre-a-TOP-de-origem-e-a-TOP-de-destino)  
> **ID:** `360043362733` | **Última Atualização:** 2026-07-22T16:05:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114468547735)

 MENSAGEM:**

[CORE_E04610] A atualização de estoque deve ser diferente entre a TOP de origem e a TOP de destino.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114452984471)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114468558487)

 Identifique os Tipos de Operação envolvidos nesse processo: TOP de Origem  e TOP de Destino.

**Exemplo:** Emissão de uma devolução de compra.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114468564631)

 TOP de Origem : COMPRA

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114468564631)

 TOP de Destino: DEVOLUÇÃO DE COMPRA

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114453009047)

 Acesse a tela **"[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** *(Comercial » Arquivo » Cadastros) *e verifique a configuração do campo **"Atualização do Estoque"** de ambas. 

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14559560147095)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114453017879)

 A atualização de estoque não deverá ser a mesma para TOP Origem e TOP Destino. Reveja o processo utilizado e sintonize com o usuário que acompanhou a implantação do sistema para alinhar a parametrização adequada ao cenário da empresa.

De forma geral para o exemplo do item 1:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114468564631)

 TOP de Origem: COMPRA » campo **"Atualização do estoque": ENTRAR**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114468564631)

 TOP de Destino: DEVOLUÇÃO DE COMPRA » campo** "Atualização do estoque": BAIXAR**

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14559341843223)

 

Entenda que **se a sua compra gerou uma entrada de estoque**, **a devolução dessa compra gerou uma saída**. Não é possível prever um processo em que ambas as TOP'S irão gerar entrada, por exemplo.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114453022743)

 Realizados os ajustes, refaça o faturamento. Lembre-se que se o lançamento referente a TOP que teve alteração de informações deve ser feito novamente do zero. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114468599575)

 CAUSA:**

Mensagem apresentada ao realizar faturamento ou devolução através do sistema, quando o campo Atualização do estoque da TOP de Origem for igual a TOP de Destino.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)