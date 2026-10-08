#  Preço de venda não pode ser zero

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042871374--Pre%C3%A7o-de-venda-n%C3%A3o-pode-ser-zero](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042871374--Pre%C3%A7o-de-venda-n%C3%A3o-pode-ser-zero)  
> **ID:** `360042871374` | **Última Atualização:** 2026-07-22T16:05:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114624259351)

 MENSAGEM:**

[CORE_E04667] Preço de venda não pode ser zero.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114624265111)

 SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114624268823)

 **Acesse a tela **"Preferências"** *(Configurações » Avançado)*.

Chave **"TIPTABPRECO - Tabela de Preços por"**

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14559842334359)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659394839)

 De acordo com o definido acima, verifique se existe uma tabela de preço vinculada no respectivo cadastro. 

**Exemplo:** TIPTABPRECO =Tipo de Negoc.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659398039)

 Tela **"[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)["](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)** *(Caminho de acesso: Comercial » Arquivo » Cadastros),* Aba Características, Campo **"Tabela de Preço"**. 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114624280599)

 Realizada a conferência da tabela de preço conforme acima, certifique-se que existe preço/custo inserido para a respectiva tabela/itens do lançamento conforme próximos passos.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659408919)

 Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"*** (Caminho de acesso: Comercial » Arquivo » Cadastros),* Aba **"Geral"**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659398039)

 Verifique o Campo:** "Usar como Preço": **Caso esteja **diferente** de Preço de Venda, se faz necessário o produto ter um custo de acordo com que está configurado nesta opção. Para verificar os custos do produto acesse a tela de** "[Variação de Custo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)"**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659398039)

 Caso esteja como Preço de Venda, utilize a rotina Comercial » Consulta » **"[Variação de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753-Varia%C3%A7%C3%A3o-de-Pre%C3%A7os-de-Produtos)[de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753-Varia%C3%A7%C3%A3o-de-Pre%C3%A7os-de-Produtos)"** para identificar se existe preço para esse item.

 

**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114624286615)

 **Identificado o preço e/ou custo a ser utilizado, solicite apoio a um usuário certificado de sua empresa que tenha conhecimento no processo de precificação através das rotinas abaixo, para que o preço torne-se diferente de zero, e a mensagem seja sanada:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659398039)

 Atualização de preço de venda

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659398039)

 Tabelas de Preço

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114659398039)

 Atualização de Custos

Realizada a precificação, consulte nas rotinas de variação mencionadas no Item 1, sendo o preço devidamente apresentado prossiga com o lançamento. 

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17802233840663)

 IMPORTANTE:**

Caso o lançamento seja em uma NF-e (Nota Fiscal Eletrônica) e o produto realmente tenha que ter valor unitário 0(zero), o Tipo de Emissão deve ser: **Complementar **ou **Ajuste** e o parâmetro **"ACEITARVLRZERO"** ligado. A Sefaz rejeita NF-e de emissão Normal com valor zerado.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114624295063)

 CAUSA:**

Mensagem apresentada quando utilizado no lançamento um tipo de operação que use como preço um valor não localizado no sistema para o respectivo item.


---

### 🔗 Links e Referências Internas:

- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Variação de Custo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)
- [Variação de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753-Varia%C3%A7%C3%A3o-de-Pre%C3%A7os-de-Produtos)