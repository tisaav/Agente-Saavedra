# Erro ao gerar nota de devolução de venda - código MGE_EV_203

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39264725706391-Erro-ao-gerar-nota-de-devolu%C3%A7%C3%A3o-de-venda-c%C3%B3digo-MGE-EV-203](https://ajuda.sankhya.com.br/hc/pt-br/articles/39264725706391-Erro-ao-gerar-nota-de-devolu%C3%A7%C3%A3o-de-venda-c%C3%B3digo-MGE-EV-203)  
> **ID:** `39264725706391` | **Última Atualização:** 2026-08-31T01:35:37Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39264725676439)

 **Mensagem**

[MGE_EV_203] Não possui quantidade de itens pendentes para devolução, verifique em "Outras Opções" no menu "Documentos Relacionados".

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39264725678487)

 **Situação**

Ao tentar gerar uma nota fiscal de devolução de venda pelo Portal de Vendas ou pela Central de Vendas, o sistema não localiza itens pendentes na nota de origem selecionada.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39264680157207)

 **Solução**

Para resolver esta situação, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39264725681559)

 Acesse a nota fiscal de venda original na Central de Vendas (Comercial > Movimentação > Central de Vendas).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39264680162327)

 Clique em "Outras Opções" > "Documentos Relacionados".

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39264725683607)

 Localize a nota de devolução já gerada para essa nota de origem.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39264680166551)

 Se a devolução necessária já existir, prossiga a partir dela em vez de tentar gerar uma nova.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39264680168471)

 Se já existirem uma ou mais devoluções parciais, confirme se todos os itens da nota original já foram devolvidos, nesse caso, não há mais saldo para uma nova devolução. 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39264725695767)

 **Causa**

Essa mensagem só aparece quando **já existe uma nota de devolução gerada anteriormente para essa mesma nota de origem**, seja total ou por meio de devoluções parciais que já consumiram todos os itens disponíveis. O sistema identifica esse vínculo automaticamente antes de exibir o erro, por isso, sempre haverá uma devolução relacionada a ser encontrada.