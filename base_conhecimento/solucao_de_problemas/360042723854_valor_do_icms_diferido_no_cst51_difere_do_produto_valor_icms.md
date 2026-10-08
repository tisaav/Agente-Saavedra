# Valor do ICMS Diferido no CST=51 difere do produto Valor ICMS Operação e percentual diferimento

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042723854-Valor-do-ICMS-Diferido-no-CST-51-difere-do-produto-Valor-ICMS-Opera%C3%A7%C3%A3o-e-percentual-diferimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042723854-Valor-do-ICMS-Diferido-no-CST-51-difere-do-produto-Valor-ICMS-Opera%C3%A7%C3%A3o-e-percentual-diferimento)  
> **ID:** `360042723854` | **Última Atualização:** 2026-07-22T16:06:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513211573655)

 MENSAGEM:**

[352 - Rejeição]: Valor do ICMS Diferido no CST=51 difere do produto Valor ICMS Operação e percentual diferimento. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513227662999)

 S****OLUÇÃO:**

Para correção siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513227666327)

 Verifique a grade de itens do lançamento, selecionando o produto » Outras opções » Consultar/alterar dados de impostos do item e refaça os cálculos do Valor do ICMS da Operação (vICMSOp) e a Alíquota de Diferimento (pDif) e corrija o Valor do ICMS Diferido (vICMSDif).

Há uma tolerância para mais ou para menos de R$ 0,01 de diferença do valor calculado sem aproximações.

Veja abaixo um exemplo de como os valores ficam no XML:

orig>7</orig>
<CST>51</CST>
<modBC>3</modBC>
<vBC>429.82</vBC>
<pICMS>18.00</pICMS>
<vICMSOp>77.37</vICMSOp>
<pDif>33.3333</pDif>
<vICMSDif>25.80</vICMSDif>
<vICMS>51.57</vICMS>

Realizando os cálculos temos:
vBC** 429.82** a 18% temos = 77,3676 onde arredonda 0,0024

Se aplicarmos 33,33% diferimento: 77.37 X 33,33% = 25,7874 e se for arredondar chega a 25,7900 e não 25.80

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513211584663)

 IMPORTANTE:**

- Se o cálculo vem de alguma rotina de força de vendas (WMW, Landix ou Terceiros), verifique com o distribuidor do Software de Força de Vendas se o cálculo e arredondamento está sendo feito corretamente.

- Caso tenha digitado os valores manualmente no lançamento, ajuste manualmente para o correto.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513211585303)

 CAUSA:**

Quando for emitida uma NF-e, com CST de ICMS igual a 51 - "Diferimento" e o Valor do ICMS Diferido (vICMSDif) for diferente do produto (multiplicação) do Valor do ICMS da Operação (vICMSOp) e a Alíquota de Diferimento (pDif), será retornado a rejeição.