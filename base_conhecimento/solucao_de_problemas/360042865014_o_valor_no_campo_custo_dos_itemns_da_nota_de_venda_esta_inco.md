# O valor no campo Custo do(s) item(ns) da Nota de Venda, esta incorreto

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865014-O-valor-no-campo-Custo-do-s-item-ns-da-Nota-de-Venda-esta-incorreto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865014-O-valor-no-campo-Custo-do-s-item-ns-da-Nota-de-Venda-esta-incorreto)  
> **ID:** `360042865014` | **Última Atualização:** 2026-07-22T16:05:53Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109286029463)

 SITUAÇÃO:**
Ao realizar emissão de Nota pela tela Central de Vendas no SankhyaW, o custo dos itens está com valor incorreto (TGFITE.CUSTO)

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109286031639)

 **SOLUÇÃO:**
Considere o Comportamento da Aplicação, conforme abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109286033175)

 Acesse: Configurações » Avançado » Preferências, pesquise pelo parâmetro:** "GOL-TIPOCUSTO"** e veja qual valor está no campo: **'INTEIRO'**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109273569815)

 Considere os seguintes valores suportados pelo parâmetro:

0- Custo de Reposição
1- Custo Gerencial
2- Custo Variável
3- Custo Médio sem ICMS
4- Custo Médio com ICMS
5- Entrada Sem ICMS
6- Entrada Com ICMS

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14535745978263)

 

Este parâmetro pode ser configurado pelas preferências do Gerente On-Line » Margem de Contribuição campo **"Custo a ser considerado"**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109646480919)

 Acesse (*Comercial » Consulta » Variação de Custos de Produtos*), pesquise pelo Código do Produto e determine qual será o custo a ser considerado e insira no parâmetro um dos códigos acima. 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109286037399)

 Acesse a Nota de Venda novamente e redigite o produto para que seja apresentado o custo, conforme a necessidade da empresa.

Este parâmetro também influenciará no Indicador de Analise de Rentabilidade, que pode ser acessado pelo botão: "**Outras Opções(...)" » "Rentabilidade"** do Cabeçalho da Nota e também na Margem de Contribuição, pelos indicadores do Gerente On-Line.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109528766743)

 CAUSA:**

Configurações Inadequada no parâmetro GOL-TIPOCUSTO.