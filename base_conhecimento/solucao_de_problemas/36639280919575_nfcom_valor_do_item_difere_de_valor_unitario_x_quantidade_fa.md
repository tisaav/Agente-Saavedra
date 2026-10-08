# NFCom - Valor do item difere de valor unitário x quantidade faturada [nItem: NNN]

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36639280919575-NFCom-Valor-do-item-difere-de-valor-unit%C3%A1rio-x-quantidade-faturada-nItem-NNN](https://ajuda.sankhya.com.br/hc/pt-br/articles/36639280919575-NFCom-Valor-do-item-difere-de-valor-unit%C3%A1rio-x-quantidade-faturada-nItem-NNN)  
> **ID:** `36639280919575` | **Última Atualização:** 2026-07-22T14:22:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639233047191)

 **MENSAGEM:**

Rejeição 435: Valor do item difere de valor unitário x quantidade faturada [nItem: NNN]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639233049751)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36687415373975)

 Acesse a tela ****[''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas). 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36687415376023)

 Localize o documento que foi rejeitado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36687415376407)

 No campo **''NFcom''**, clique em **''Gerar XML da NFCom em arquivo para conferência''**.

 

![image (69).png](https://ajuda.sankhya.com.br/hc/article_attachments/36687415376791)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36687430017303)

 Abra o XML gerado e confira o cálculo:

- 

**vProd** (Valor do Item) deve ser igual a **vItem × qFaturada**.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36687415378455)

 OBSERVAÇÃO:** considere uma tolerância de **± R$ 0,10**.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36687415378711)

 Se houver divergência, abra a nota na ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) e redigite os valores corretamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639280917527)

CAUSA:**

A **rejeição 435** ocorre quando uma **NFCom (modelo 66)** é emitida e o **Valor Total do Item (vProd)** é diferente do resultado da multiplicação do **Valor Unitário do Item (vItem)** pela **Quantidade Faturada (qFaturada)**.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36687415378455)

 OBSERVAÇÕES:**

- 

Não há exceções para esta regra de validação.

- 

Considere uma tolerância de **± R$ 0,10** para mais ou para menos.


---

### 🔗 Links e Referências Internas:

- [''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)