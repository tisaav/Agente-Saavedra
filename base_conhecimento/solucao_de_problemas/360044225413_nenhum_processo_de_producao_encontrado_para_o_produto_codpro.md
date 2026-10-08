# Nenhum processo de produção encontrado para o produto Cód.Produto = "XX" na planta Cód.Planta = "Y"

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044225413-Nenhum-processo-de-produ%C3%A7%C3%A3o-encontrado-para-o-produto-C%C3%B3d-Produto-XX-na-planta-C%C3%B3d-Planta-Y](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044225413-Nenhum-processo-de-produ%C3%A7%C3%A3o-encontrado-para-o-produto-C%C3%B3d-Produto-XX-na-planta-C%C3%B3d-Planta-Y)  
> **ID:** `360044225413` | **Última Atualização:** 2026-07-22T16:00:12Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292401371031)

 MENSAGEM:**

[PROD_E00322]: Nenhum processo de produção encontrado para o produto Cód.Produto = "XX" na planta Cód.Planta = "Y".

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292429322391)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292429331735)

 Certifique-se que a planta de manufatura configurada para o respectivo processo produtivo é a mesma inserida no lançamento da O.P.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292401401239)

 Caso sejam MP'S com controle por lista verifique se a opção **"Planejamento por Controle"** foi marcada para o respectivo produto:

Produção » Rotinas » Planejamento de Produção (MRP I) >> Conf. >> Aba Produtos >> 'Planejamento por Controle':

- 
**Planejamento por Controle:** quando marcado, significa que o cálculo de demanda do MPS irá considerar o controle do produto (controle adicional do tipo lista). Dessa forma, será gerado um registro de necessidade de produção para cada produto/controle. Essa configuração faz sentido apenas para produtos com controle adicional do tipo Lista.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292401410711)

 Ainda referindo-se a situação de controle por lista, valide se não existem espaços em branco indevidos inseridos no campo **"Controle"** das respectivas MP'S no processo produtivo.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292429358103)

 CAUSA:**

Mensagem apresentada quando não localiza-se um processo de produção correspondente aos dados do lançamento de O.P realizado, tal como: Planta, Controle.