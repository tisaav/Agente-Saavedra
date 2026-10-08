# TOP com 'Valor Líquido da origem' não pode ser lançada aqui

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9083951430935-TOP-com-Valor-L%C3%ADquido-da-origem-n%C3%A3o-pode-ser-lan%C3%A7ada-aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/9083951430935-TOP-com-Valor-L%C3%ADquido-da-origem-n%C3%A3o-pode-ser-lan%C3%A7ada-aqui)  
> **ID:** `9083951430935` | **Última Atualização:** 2026-07-22T15:10:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18952491291159)

 MENSAGEM:**

[CORE_E01488] TOP com 'Valor Líquido da origem' não pode ser lançada aqui.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18952491297303)

 SITUAÇÃO:**

Ao tentar lançar uma compra na central de compras a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18952491306263)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18952491315991)

 Revise a configuração do campo "Usar como preço" no **Tipo de operação TOP** *(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)* utilizada no lançamento. Para TOP de compra, o campo 'Usar como preço' não deverá estar selecionado como Valor Líquido da origem.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18952491318679)

 IMPORTANTE:**

Existe um processo Específico envolvendo o campo Usar como Preço, onde:

A opção Valor líquido da origem deverá ser utilizada nas TOP's de Remessa, nas quais a "Nota de Remessa" será gerada com o valor líquido da origem. Para mais informações acesse o [manual de Tipos de Operação.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18952470070551)

CAUSA:**

Ocorre ao definir o campo usar como preço como valor liquido da origem em TOP de compra.


---

### 🔗 Links e Referências Internas:

- [manual de Tipos de Operação.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)