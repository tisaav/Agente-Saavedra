# Não encontramos Produção p/Produtos com Filtro no período

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9403939895319-N%C3%A3o-encontramos-Produ%C3%A7%C3%A3o-p-Produtos-com-Filtro-no-per%C3%ADodo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9403939895319-N%C3%A3o-encontramos-Produ%C3%A7%C3%A3o-p-Produtos-com-Filtro-no-per%C3%ADodo)  
> **ID:** `9403939895319` | **Última Atualização:** 2026-07-22T15:08:02Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696640210967)

 MENSAGEM:**

[COM_E00549] Não encontramos Produção p/Produtos com Filtro no período.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696640217111)

 SITUAÇÃO:**

Ao realizar a Apropriação de Custos Indiretos de Produção, na tela Produção » Rotinas » Apropriação de Custos Indiretos de Produção (CIP)", apresenta a mensagem.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696640219671)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696640224279)

 Verifique se existe nota de produção, com a tarifa CIP dentro do período informado; 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696627152151)

 Caso alguma nota não contenha a tarifa CIP, verifique se o tipo de índice da tarifa é variável (execução de atividades). Para incluir a CIP, cancele a OP e lance uma nova OP, com um tempo de apontamento entre data hora início e data hora fim maior que zero minutos.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696640241175)

 CAUSA:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696640224279)

 Quando não existe nota de produção com a tarifa CIP no período informado;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18696627152151)

 Quando a configuração do tipo de índice da tarifa CIP está como *"Variável (execução de atividades)"* e o tempo de execução da atividade - entre a diferença de data hora início e data hora do fim do apontamento - for igual a zero, a CIP não é lançada na nota de produção.

* *