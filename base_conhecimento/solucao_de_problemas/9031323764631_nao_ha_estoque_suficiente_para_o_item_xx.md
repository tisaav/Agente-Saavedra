# Não há estoque suficiente para o item XX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9031323764631-N%C3%A3o-h%C3%A1-estoque-suficiente-para-o-item-XX](https://ajuda.sankhya.com.br/hc/pt-br/articles/9031323764631-N%C3%A3o-h%C3%A1-estoque-suficiente-para-o-item-XX)  
> **ID:** `9031323764631` | **Última Atualização:** 2026-07-22T15:11:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233253911)

 MENSAGEM:**

[CORE_E03881]: Não há estoque suficiente para o item XX.

[CORE_E01251] Não há estoque suficiente para o item XX.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673249225751)

 CAUSA:  **

Ao vender um item do kit que não possui estoque suficiente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233257367)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673249209111)

 Verifique as seguintes informações:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 Parâmetro **"****LOCALPADRAO"** *(Caminho de acesso: Configurações » Avançado » Preferências);*

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/9188249345559)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 Veja qual a validação do Grupos de Produtos/Serviços, aba Estoque *»*Validação;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15855753937815)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 Se componente realmente possui estoque;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 Habilite o parâmetro **"****CONTROLECOMPON" ***(Caminho de acesso: Configurações » Avançado » Preferências).*

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9188247109911)

 

***

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450849916311)

*NOTA: **

Para trabalhar com local padrão definido nos componentes do kit, habilite o parâmetro **"Mostrar o controle na aba de componentes - CONTROLECOMPON"**.

Assim, quando ligado, será apresentado no Cadastro de Produtos, aba **"Componentes"**, o campo **"Controle"** (que engloba o local).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673249216663)

 Para processo de venda de KIT com Lote através da Explosão Automática de Lotes:

"A Explosão Automática de Lotes é uma funcionalidade disponível na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas),  em que, ao lançar um item em uma nota de venda ou pedido de venda, caso o produto seja controlado por lote e data de validade, será precisará informar o lote de cada item, porém, com essa funcionalidade, não será necessário informar o Lote (CONTROLE)."

**[Explosão Automática de Lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg1MTI3MDM3MTMsInRpY2tldF9pZCI6MTc3OTE0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY1MDIyODkzNn0.ZLXlEAL59X9Mi_pqBJv2LwtKsExnCfrrWW2gTRvIeCw)**

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233287319)

 A explosão de lote para componente de KIT não funciona para "KIT Independente", parâmetro "**CONFKITIND**" *(Caminho de acesso: Configurações » Avançado » Preferências)* = Ligado. 

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/9188260252695)

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 Para que seja possível explodir o lote do componente **"LOTAUTKIT"** *(Caminho de acesso: Configurações » Avançado » Preferências), * o sistema necessita que as seguintes condições sejam atendidas: 

 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/9188313089815)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 O "Grupo de Produtos" do componente utilizado na operação deve validar estoque, ou seja, não pode ser igual a **"Não valida"** ou **"Pela Empresa, mas aceita"**. 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 O **"Local"** que contém estoque do produto em questão não pode estar contido no parâmetro **"DESCLOCALKIT"*** (Caminho de acesso: Configurações » Avançado » Preferências)*.

 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/9188316072087)

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 Deve haver estoque no mesmo "Local" e "Empresa", informado na aba **"Componentes do cadastro do produto KIT"** para este componente. 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233275287)

 A soma de: ESTOQUE" - "RESERVADO" - "WMSBLOQUEADO" deve ser maior que zero. 

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16673233292055)

 OBSERVAÇÃO:**

Quando habilitando o parâmetro LOTAUTKIT *(Caminho de acesso: Configurações » Avançado » Preferências)*, o sistema tem um controle automático por data de validade de lote para kit. Ao fazer a venda o sistema encontra o lote com a data mais próxima do vencimento. 

 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/9188313089815)

Na baixa dos produtos componentes do kit, se não encontrar Matéria Prima suficiente não é permitido a inclusão do Produto Acabado.
Ou seja, se o componente tem controle por lote tem que seguir as configurações de explosão de lote.

 

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [Explosão Automática de Lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg1MTI3MDM3MTMsInRpY2tldF9pZCI6MTc3OTE0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY1MDIyODkzNn0.ZLXlEAL59X9Mi_pqBJv2LwtKsExnCfrrWW2gTRvIeCw)