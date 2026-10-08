# Não encontramos o Custo ou a Cotação para calcular a Base da Substituição Tributária

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043144334-N%C3%A3o-encontramos-o-Custo-ou-a-Cota%C3%A7%C3%A3o-para-calcular-a-Base-da-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043144334-N%C3%A3o-encontramos-o-Custo-ou-a-Cota%C3%A7%C3%A3o-para-calcular-a-Base-da-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria)  
> **ID:** `360043144334` | **Última Atualização:** 2026-07-22T16:04:07Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120782374679)

 MENSAGEM**:

[CORE_E00268] Não encontramos o Custo ou a Cotação para calcular a Base da Substituição Tributária.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120782378007)

 SOLUÇÃO**:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120777985431)

 Acesse o cadastro da TOP utilizada no lançamento e verifique se realmente o campo "**Usa Cus.Méd.Base ST?" **precisa estar marcado. Em caso negativo, desmarque o mesmo e realize um novo teste de faturamento.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120782385815)

 Tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** *(Caminho de acesso: Comercial » Arquivos » Cadastros)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120782385815)

 Aba **"Impostos"**,  campo **"Usa Cus.Méd.Base ST?"**

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14628236533399)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120782387863)

 Se a opção mencionada no item anterior for realmente necessária, verifique na tela de **"[Variação de Custos de Produtos](Varia%C3%A7%C3%A3o%20de%20Custos%20de%20Produtos)"** se todos os produtos envolvidos no faturamento possuem custo e se algum deles não possuir, utilize a rotina de **"[Atualização de Custos de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)"** ou o processo de atualização de custos definidos pela empresa.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120782392087)

 Verifique também os parâmetros **"COTCSTDEVTOP"** e **"COTCSTDEVDIA"**, pois quando preenchidos, podem influenciar na ocorrência desta mensagem.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120777996055)

 Ajustadas as marcações, custos e parâmetros, tente realizar um novo faturamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120782396823)

 CAUSA:**

Mensagem apresentada ao realizar faturamento com Tipo de Operação definido como Usa Cus.Méd.Base ST, e o sistema não encontra valores para compor tal cálculo.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Atualização de Custos de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)