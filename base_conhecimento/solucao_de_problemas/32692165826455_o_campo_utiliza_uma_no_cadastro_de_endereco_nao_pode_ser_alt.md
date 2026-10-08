# O campo Utiliza U.M.A no cadastro de endereço não pode ser alterado

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32692165826455-O-campo-Utiliza-U-M-A-no-cadastro-de-endere%C3%A7o-n%C3%A3o-pode-ser-alterado](https://ajuda.sankhya.com.br/hc/pt-br/articles/32692165826455-O-campo-Utiliza-U-M-A-no-cadastro-de-endere%C3%A7o-n%C3%A3o-pode-ser-alterado)  
> **ID:** `32692165826455` | **Última Atualização:** 2026-07-22T14:30:45Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32692165817623)

 **MENSAGEM:**

[CORE_E07359]** **O campo Utiliza U.M.A no cadastro de endereço não pode ser alterado pois existe estoque registrado. Para alterá-lo é necessário que não haja estoque no endereço.
 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32692165818135)

SOLUÇÃO:**

**Como verificar e alterar um endereço no WMS:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33015916792343)

Acesse o caminho: WMS > Consultas > Estoque / Endereçamento WMS.

Filtre pelo endereço desejado, no campo Faixa de endereços, insira o CodEnd do endereço que deseja consultar.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33015916793879)

 Verifique os produtos:
Confira quais produtos estão atualmente alocados nesse endereço.

 

**Caso precise alterar o endereço:**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33015916794775)

 Realize a movimentação dos produtos:
Antes de alterar o endereço, é necessário remover os produtos dele, você pode fazer isso de duas formas:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33015918912663)

 Pelo sistema:
WMS > Rotinas > Transferência entre Endereços

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33015918912663)

 Pelo coletor de dados:
Utilize a opção de transferência de endereço ou faça a movimentação proativa diretamente no equipamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32692165821335)

CAUSA:**

Ocorre quando tentamos alterar a configuração de UMA de um endereço que já tem estoque de produtos cadastrado.