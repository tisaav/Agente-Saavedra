# Não podemos agrupar produtos com unidades diferentes 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9800946327703-N%C3%A3o-podemos-agrupar-produtos-com-unidades-diferentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/9800946327703-N%C3%A3o-podemos-agrupar-produtos-com-unidades-diferentes)  
> **ID:** `9800946327703` | **Última Atualização:** 2026-07-22T15:06:03Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296843332375)

 MENSAGEM:**

[CORE_E04665] Não podemos agrupar produtos com unidades diferentes.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296888356119)

 SITUAÇÃO:**

Ao faturar dois pedidos agrupados tendo 2 unidades diferentes para o mesmo produto a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296843336215)

 CAUSA: **

Agrupar dois pedidos com mesmo produto porém unidades diferentes.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296843339415)

 SOLUÇÃO:**

Existe um parâmetro que faz essa validação quando se trata do mesmo produto porém com unidades diferentes. 

Assim, acesse a tela **Preferências** *(Caminho de acesso à tela: Configurações » Avançado » Preferências)* informe a chave **'Agrupar prod.repetido em qualquer faturamento? - AGRUPFATSEMP'** e desligue o mesmo.

![Agrupar 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296888422935)

Trata-se de comportamento. Se o parâmetro estiver ligado o sistema irá tentar agrupar os produtos repetidos nos pedidos em uma linha só e, se tiver unidade diferente, não irá ser agrupado e a mensagem será apresentada.**
**Sendo assim, deve-se ajustar um dos pedidos ou avaliar a possibilidade de trabalhar com este parâmetro desabilitado.

Existe ainda a possibilidade de faturar os pedidos separadamente.