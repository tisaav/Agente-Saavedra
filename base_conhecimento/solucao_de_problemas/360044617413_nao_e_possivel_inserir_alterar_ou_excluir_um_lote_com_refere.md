# Não é possível inserir, alterar ou excluir um lote com referência fora do período contábil

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617413-N%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-alterar-ou-excluir-um-lote-com-refer%C3%AAncia-fora-do-per%C3%ADodo-cont%C3%A1bil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617413-N%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-alterar-ou-excluir-um-lote-com-refer%C3%AAncia-fora-do-per%C3%ADodo-cont%C3%A1bil)  
> **ID:** `360044617413` | **Última Atualização:** 2026-07-22T15:52:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806528965911)

 MENSAGEM:**

[CORE_E02206]: Não é possível inserir, alterar ou excluir um lote com referência fora do período contábil.

[CORE_E00826] Não é possível inserir, alterar ou excluir um lote com referência fora do período contábil.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806537915031)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806537917335)

  Acesse: *Contabilidade » Preferências » Empresa*

Selecione a empresa que corresponde o Lote e acesse a aba "Exercício".

Caso esteja tentando excluir um Lote do Período/Ano 2018, por exemplo, e se Período/Ano atual é 2019, ajuste os seguintes campos:

- **Inicio Período Contábil**

- **Fim do Período Contábil **

- **Referência**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806528974871)

 Após ajustar os campos, para a referência e o período em que o lote representa, salve e tente excluir novamente.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806528977047)

 Após a exclusão, volte novamente para o período/ano vigente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806528978071)

 CAUSA:**

Ocorre quando se tenta excluir um Lote de um Período/Referência, que não seja do Período/Ano atual.