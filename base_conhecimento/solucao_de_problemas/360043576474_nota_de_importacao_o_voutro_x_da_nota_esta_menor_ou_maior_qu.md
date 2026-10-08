# Nota de importação: o <vOutro> 'X' da nota está MENOR  ou MAIOR que a soma do <vOutro> 'Y' dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043576474-Nota-de-importa%C3%A7%C3%A3o-o-vOutro-X-da-nota-est%C3%A1-MENOR-ou-MAIOR-que-a-soma-do-vOutro-Y-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043576474-Nota-de-importa%C3%A7%C3%A3o-o-vOutro-X-da-nota-est%C3%A1-MENOR-ou-MAIOR-que-a-soma-do-vOutro-Y-dos-itens)  
> **ID:** `360043576474` | **Última Atualização:** 2026-07-22T16:02:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363318796311)

 MENSAGEM:**

[CORE_E01565] Nota de importação: o <vOutro> 'X' da nota está MENOR que a soma do <vOutro> 'Y' dos itens.

[CORE_E01566] Nota de importação: o <vOutro> 'X' da nota está MENOR que a soma do <vOutro> 'Y' dos itens.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363324294807)

 SOLUÇÃO:**

O sistema compara os valores de ICMS (Itens) + Valor das Despesas Aduaneiras (Declaração de Importação de cada item) + Vlr.PIS Importação (D.I) + Vlr.COFINS (D.I) com o valor inserido em Vlr.Destaque.

Suponhamos o caso abaixo:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14358759515031)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14358830826391)

 

- Nesse caso, **Vlr.Destaque** seria: 522,52 (ICMS) + 48,00 (PIS) + 220,57 (COFINS) + 214,50 (Aduaneiras) = 1.005,59.

Se constatado divergência nessa comparação, o erro será apresentado. 

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363318800023)

 IMPORTANTE:**

**"VOUTITEMSEMICMS'- Importação, tag vOutro do item sem valor do ICMS"**

Em determinados casos, empresas podem optar por não destacar o ICMS para compor o Valor de Destaque (**vOutro**), então poderá optar por desligar o parâmetro VOUTITEMSEMICMS.

O valor será composto pelo: "Valor das Despesas Aduaneiras + Vlr.PIS Importação + Vlr.COFINS Importação" do item.