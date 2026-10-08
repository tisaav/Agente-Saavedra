# A soma dos impostos recuperáveis, não deve ser maior ou igual ao 'Valor total dos bens'

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/23769576133527-A-soma-dos-impostos-recuper%C3%A1veis-n%C3%A3o-deve-ser-maior-ou-igual-ao-Valor-total-dos-bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/23769576133527-A-soma-dos-impostos-recuper%C3%A1veis-n%C3%A3o-deve-ser-maior-ou-igual-ao-Valor-total-dos-bens)  
> **ID:** `23769576133527` | **Última Atualização:** 2026-07-22T14:48:04Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23769548244119)

 MENSAGEM:**

[CORE_E06906] A soma dos impostos recuperáveis, não deve ser maior ou igual ao 'Valor total dos bens'.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23769576131223)

 SOLUÇÃO:
**

Quando estamos lançando uma nota de compra de imobilizado, ou alterando alguma informação de um bem já lançado, o sistema analisa se o valor que o bem está calculando de CIAP (que pode ter somado ao seu valor, o FCP se nas preferências da empresa na aba BENS, o campo "Somar FCP na Base de Crédito do CIAP?" estiver marcado) está maior que o próprio valor do bem, que nesse momento estaria calculado com a seguinte fórmula:

 

(Quantidade negociada * valor unitário) + (substituição tributária (ST) + Valor de IPI) - (Descontos do item)

 

Nesse sentido, analise o motivo do valor do CIAP (e FCP se for o caso) estar maior que o valor do imobilizado, pois não é algo correto em um processo comum de lançamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23769548245015)

 CAUSA:**

Ao tentar incluir os bens no lançamento de uma nota de compra a mensagem é apresentada.