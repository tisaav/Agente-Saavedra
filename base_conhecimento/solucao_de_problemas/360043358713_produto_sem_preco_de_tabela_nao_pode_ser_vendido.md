# Produto sem preço de tabela, não pode ser vendido

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043358713-Produto-sem-pre%C3%A7o-de-tabela-n%C3%A3o-pode-ser-vendido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043358713-Produto-sem-pre%C3%A7o-de-tabela-n%C3%A3o-pode-ser-vendido)  
> **ID:** `360043358713` | **Última Atualização:** 2026-08-10T17:24:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116124448919)

 MENSAGEM:**

[CORE_E03243] "Produto sem preço de tabela, não pode ser vendido".

[CORE_E02958] "Produto sem preço de tabela, não pode ser vendido"

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116124475799)

 CAUSA:**

Ocorre quando temos um Produto sem custo ou preço de tabela devidamente definido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116140210583)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116124455703)

 Acesse a tela** "[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** *(Caminho de acesso: Configurações » Avançado » Preferências)*, verifique o parâmetro **"TIPTABPRECOS- Tabela de Preços por", **de acordo com o que está definido neste parâmetro, vincule uma tabela de preço.

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14601780734743)

 

Caso o produto não tenha um preço definido, a mensagem é apresentada ao usuário.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116140214935)

 Telas que podem ser usadas para consulta de preço:

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116124460695)

Comercial » Consulta » **"[Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos)"**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116124460695)

Comercial » Consulta » **"[Variação de Preços de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753-Varia%C3%A7%C3%A3o-de-Pre%C3%A7os-de-Produtos)"**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116124460695)

Comercial » Arquivo » **"[Tabelas de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os)"**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116124470039)

 Acesse Comercial » Arquivo » Cadastros » **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"**, aba **"Geral"**, verifique o Campo **"Usar como Preço"**: caso esteja diferente de **Preço de Venda**, se faz necessário o produto ter um custo de acordo com que está configurado nesta opção. Para verificar os custos do produto, acesse a tela de **"[Variação de Custo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)"**.

Parâmetros que influenciam nas configurações de Preço/Custo:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116140214935)

 CUSTOPORCONT** - estar habilitado e na tabela de preço não possuir informações no campo **"Controle"** para o produto e controle em questão.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116140214935)

 CUSTOPORLOC** - estar habilitado e na tabela de preço não possuir informações no campo **"Codlocal"** para o produto em questão.

Para essa ultima configuração é necessário também verificar se no **"[Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"**, Aba **"Medidas e Estoque"** se o produto possui o campo **"Usa Local"** devidamente marcado.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116140229015)

 OBSERVAÇÃO:**

Caso o lançamento seja em uma NF-e(Nota Fiscal Eletrônica) e o produto realmente tenha que ter valor unitário 0 (zero), o Tipo de Emissão deve ser: **Complementar** ou **Ajuste** e o parâmetro **"ACEITARVLRZERO"** ligado. A Sefaz rejeita NF-e de emissão Normal com valor zerado.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos)
- [Variação de Preços de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753-Varia%C3%A7%C3%A3o-de-Pre%C3%A7os-de-Produtos)
- [Tabelas de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Variação de Custo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)