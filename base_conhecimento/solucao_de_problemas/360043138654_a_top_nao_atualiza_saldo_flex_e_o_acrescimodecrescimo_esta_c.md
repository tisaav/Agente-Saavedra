# A TOP não atualiza saldo FLEX e o acréscimo/decréscimo está calculado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138654-A-TOP-n%C3%A3o-atualiza-saldo-FLEX-e-o-acr%C3%A9scimo-decr%C3%A9scimo-est%C3%A1-calculado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138654-A-TOP-n%C3%A3o-atualiza-saldo-FLEX-e-o-acr%C3%A9scimo-decr%C3%A9scimo-est%C3%A1-calculado)  
> **ID:** `360043138654` | **Última Atualização:** 2026-07-22T16:04:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309937824151)

 MENSAGEM:**

A TOP não atualiza saldo FLEX e o acréscimo/decréscimo está calculado. Nota de Nro Único: XXXXX.

[ORA-06512]: em "SANKHYA.TRG_INC_TGFITE_FLEX", line 147

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TGFITE_FLEX'

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309980295831)

 **SITUAÇÃO:**

Ao lançar uma NF-e de Devolução, ocorre a mensagem.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309937838487)

 **CAUSA:**

Ao clicar para devolver, tentar faturar ou duplicar um lançamento, o sistema carrega as informações quanto ao Flex do pedido/nota e tenta incluir nesta nova nota. Com isso, caso a TOP de devolução não esteja configurada para trabalhar com flex, ocorre a mensagem.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309937829399)

 **SOLUÇÃO:**

Para correção siga os passos abaixo.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309980300567)

 Acesse o caminho *Comercial » Arquivo » Cadastros » ****[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)*

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309937835031)

 Selecione a TOP Destino que está sendo utilizada no procedimento que retornou a mensagem de validação.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309937836567)

 Aba "**Geral", **Campo "**Atualizar Acréscimos/Decréscimos",** marque a opção que seja **diferente** de "**Não Atualizar".**


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)