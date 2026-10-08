# Tela Conferência PIS/COFINS não traz Valor da Base nas Saídas, somente nas entradas

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/17156001469079-Tela-Confer%C3%AAncia-PIS-COFINS-n%C3%A3o-traz-Valor-da-Base-nas-Sa%C3%ADdas-somente-nas-entradas](https://ajuda.sankhya.com.br/hc/pt-br/articles/17156001469079-Tela-Confer%C3%AAncia-PIS-COFINS-n%C3%A3o-traz-Valor-da-Base-nas-Sa%C3%ADdas-somente-nas-entradas)  
> **ID:** `17156001469079` | **Última Atualização:** 2026-07-22T14:53:42Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17156040206871)

SOLUÇÃO:**

O campo "Valor Base" embora esteja presente na tela, na geração das saídas, constatamos que o campo sempre será criado com o valor **zero**, não havendo possibilidades de se apresentar algum valor.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17281165191575)

 

Esse campo é calculado e apresenta os valores de base PIS/COFINS, nas **entradas**, porém como dito, nas saídas sempre será apresentado zero, visto que o seu cálculo nas saídas, não foi implementado durante a construção da tela.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17281166540823)