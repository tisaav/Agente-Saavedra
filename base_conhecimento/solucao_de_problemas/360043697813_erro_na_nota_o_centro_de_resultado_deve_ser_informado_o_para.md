# Erro na nota. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697813-Erro-na-nota-O-Centro-de-Resultado-deve-ser-informado-O-par%C3%A2metro-EXIGCRCFR-est%C3%A1-ligado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697813-Erro-na-nota-O-Centro-de-Resultado-deve-ser-informado-O-par%C3%A2metro-EXIGCRCFR-est%C3%A1-ligado)  
> **ID:** `360043697813` | **Última Atualização:** 2026-07-22T16:02:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164217168407)

 MENSAGEM:**

[CORE_E02406] Erro na nota. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164255425047)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164217173015)

 Quando o parâmetro **"EXIGCRCFR"** estiver ligado, o sistema exigirá que o usuário indique o **"Centro de Resultado"** nas seguintes telas:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164255435159)

 Movimentos lançados nas Centrais (Compra/Venda/Mov.Interna);

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164255435159)

 Tela Rateio de Receitas e Despesas;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164255435159)

 Financeiros das centrais;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164255435159)

 Movimentação financeira;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164255435159)

 Modelo de Notas e Pedidos;

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14712097445911)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164255437335)

 Dessa forma, para que a mensagem deixe de ser apresentada, o campo **"Centro de Resultado"** deve ser devidamente preenchido nas respectivas telas, conforme processo realizado no momento da apresentação da mensagem. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164217180695)

 Caso seja identificada a necessidade de não mais trabalhar com a exigência dessa informação 'Centro de Resultado', o parâmetro deverá ser **desligado** através da tela **"Preferências"** *(Configurações » Avançado)* - chave **"EXIGCRCFR"**:

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164217187735)

 OBSERVAÇÕES:**

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458194983959)

 Se a rejeição ocorre no momento de utilizar a rotina** "[Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)"**, verifique na tela **"Empresa"** (Comercial *»* Preferências), aba **"Modelo de Importação de XML"**, os modelos vinculados. 

Após isso, acesse a tela **"[Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)"** *(Caminho de acesso: Comercial » Consulta)*, localize os respectivos modelos e valide a configuração do campo 'Centro de Resultado', para solução da mensagem apresentada. 

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458194983959)

 Se a rejeição ocorre no momento de utilizar a rotina **"[Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633-Ajuste-de-Estoque-)"**, verifique na tela **"Empresa"** *(Caminho de acesso: Comercial » Preferências)*, aba **"Estoque/Preço"**, os modelos de ajuste de entrada e ajuste de saída vinculados.

Após isso, acesse a tela **"[Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)"** *(Caminho de acesso: Comercial » Consulta)*, localize os respectivos modelos e valide a configuração do campo **"Centro de Resultado"**, para solução da mensagem apresentada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16164217194903)

 CAUSA:**

Ao realizar lançamentos financeiros e/ou nas Centrais, caso o campo Centro de Resultado não seja informado e o parâmetro EXIGCRCFR esteja ligado, será apresentada a mensagem.


---

### 🔗 Links e Referências Internas:

- [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)
- [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)
- [Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633-Ajuste-de-Estoque-)