# A TOP de origem atualizou o estoque, a TOP de destino não pode atualizar

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360049378473-A-TOP-de-origem-atualizou-o-estoque-a-TOP-de-destino-n%C3%A3o-pode-atualizar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049378473-A-TOP-de-origem-atualizou-o-estoque-a-TOP-de-destino-n%C3%A3o-pode-atualizar)  
> **ID:** `360049378473` | **Última Atualização:** 2026-07-22T15:31:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606601729815)

 MENSAGEM**:

[CORE_E04614] A TOP de origem atualizou o estoque, a TOP de destino não pode atualizar. 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606558705047)

 CAUSA:**

Mensagem apresentada realizar faturamento ou devolução através do sistema, quando o campo 'Atualização do estoque' da TOP de Origem for igual a TOP de Destino.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606558708887)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606601747735)

 Identifique os 'Tipos de Operação' envolvidos nesse processo: TOP de Origem  e TOP de Destino.

**Exemplo:** Faturamento de um 'Pedido de compra' para 'Nota de Compra':

- TOP de Origem : PEDIDO DE COMPRA

- TOP de Destino:  NOTA DE COMPRA

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606601752471)

 Acesse a tela **'Tipos de Operação-TOP'** *(Comercial » Arquivo » Cadastros), aba: ESTOQUE *e verifique a configuração do campo 'Atualização do Estoque' de ambas. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606558725911)

 A atualização de estoque não deverá ser a mesma para TOP Origem e TOP Destino. Reveja o processo utilizado e sintonize com o usuário que acompanhou a implantação do sistema para alinhar a parametrização adequada ao cenário da empresa.

De forma geral para o exemplo do item 1:

- TOP de Origem : PEDIDO DE COMPRA >>*** Atualização do estoque = [RESERVAR ou NENHUMA]***

- TOP de Destino: NOTA DE COMPRA >>*** Atualização do estoque = [ENTRAR]***

Entenda que **se o seu pedido de compra ENTROU com estoque, não consta nas melhores práticas que a sua nota de compra também ENTRE com estoque**. 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606601763863)

 Realizados os ajustes, refaça o faturamento. Lembre-se que se o lançamento referente a TOP que teve alteração de informações deve ser feito novamente do zero.