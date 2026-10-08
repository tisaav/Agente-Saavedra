# Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ Controle: XPTO Validação do estoque: XPTO

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133094-Estoque-insuficiente-Empresa-X-Produto-YYYY-Local-ZZZZZ-Controle-XPTO-Valida%C3%A7%C3%A3o-do-estoque-XPTO](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133094-Estoque-insuficiente-Empresa-X-Produto-YYYY-Local-ZZZZZ-Controle-XPTO-Valida%C3%A7%C3%A3o-do-estoque-XPTO)  
> **ID:** `360043133094` | **Última Atualização:** 2026-08-13T18:57:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147789340951)

 MENSAGEM:**

[CORE_E04176] Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ

[CORE_E04794] Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ Controle: XPTO Validação do estoque: XPTO.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147789366807)

 CAUSA**:

 Ocorre quando no lançamento de um item não foi inserido os dados para buscar o item em estoque.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147789344535)

 SOLUÇÃO**:

Para um melhor controle e gerenciamento do Estoque, identifique as validações de estoque dos produtos do lançamento, como:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147795305495)

 Realize a validação de Estoque do Grupo de Produtos: *[Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602054)*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147795312919)

 Verifique se o produto possui estoque, considerando Empresa, Local e Controle (quando houver): *[Comercial » Gerente » Gerência de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111253)* ou *[Comercial » Consulta » Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)*

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147789352855)

 Se houver estoque físico, considere verificar se há inconsistências entre estoque físico e do sistema em: *[Configurações » Avançado » Verificação de Saldo de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054)*

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147795320599)

 Se o produto for lançado pela Consulta de Produtos, selecione o item de acordo com seu Local e Controle, para que o sistema carregue esses dados para a grade de itens.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147789360151)

 Verifique se as Notas de Compras dos Produtos estão devidamente lançados e confirmados, caso identifique inconsistências, considere efetuar Ajuste de Estoque através da melhor prática via Inventário de Ajuste de estoque.

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18133344111511)

** Importante:**

Verifique o processo produtivo e caso necessário, realize a alteração do modelo de nota e pedido, para um que esteja configurado corretamente para a empresa desejada.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16147795327383)

 Observação:**

Esta mensagem pode ocorrer nos casos em que o pedido de origem reservou o estoque, mas o campo da TOP de origem, aba **"Validações"**: **Validar Estoque p/ Reservar:** estava desmarcado. Nesse caso, ao tentar faturar esse pedido pela opção normal "Faturar" irá emitir a mensagem de estoque insuficiente.


---

### 🔗 Links e Referências Internas:

- [Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602054)
- [Comercial » Gerente » Gerência de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111253)
- [Comercial » Consulta » Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)
- [Configurações » Avançado » Verificação de Saldo de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054)