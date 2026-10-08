# Como configurar a exibição de Nome Fantasia ou Razão Social do Parceiro

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24426984422423-Como-configurar-a-exibi%C3%A7%C3%A3o-de-Nome-Fantasia-ou-Raz%C3%A3o-Social-do-Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/24426984422423-Como-configurar-a-exibi%C3%A7%C3%A3o-de-Nome-Fantasia-ou-Raz%C3%A3o-Social-do-Parceiro)  
> **ID:** `24426984422423` | **Última Atualização:** 2026-07-31T04:08:06Z

---

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/42360726039959)

**  SITUAÇÃO**

A preferência "NOMERAZAOPARC" foi configurada para exibir a Razão Social, porém o sistema continua apresentando o Nome Fantasia do parceiro. Mesmo após alterar essa preferência para a opção "Razão Social", telas como o Portal de Vendas/Compras (Gerente On-line) continuam exibindo o Nome Fantasia.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/24426984414231)

**  SOLUÇÃO**

Para resolver este erro, corrija ou remova o parâmetro de apresentação da entidade parceiro. Siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/42360734910743)

  Acesse *Configurações » Avançado » Preferências* e confirme que o parâmetro **NOMERAZAOPARC – Apresentar Nome ou Razão Social do Parceiro** está definido como "Razão Social". Isso cobre o Portal de Vendas/Compras e as demais telas citadas na Causa.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/42360734910999)

 Se a Razão Social também precisar ser exibida nas Centrais (ex.: Central de Liberações, Central de Atendimento ao Cliente) ou em telas de Movimentação Financeira, verifique se existe o parâmetro **APRES.TGFPAR**. Caso não exista, crie-o em *Configurações » Avançado » Preferências*:

- Chave: `APRES.TGFPAR`

- Descrição: Apres. Razão Social nas Centrais e Mov. Financeira

- Módulo: Configurações

- Aba: Diversas (Tipo Texto)

- Texto: `RAZAOSOCIAL`

![3](https://ajuda.sankhya.com.br/hc/article_attachments/42360734911639)

 Reinicie o servidor de aplicação (ou solicite a atualização do cache de parâmetros) para que as alterações sejam recarregadas.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42360726042647)

 Acesse novamente as telas afetadas e confirme se a Razão Social passou a ser exibida. 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/24426991416343)

**  CAUSA**

Existem dois mecanismos independentes que controlam a exibição de Nome Fantasia x Razão Social do parceiro, e cada um afeta um conjunto diferente de telas:

- 
**NOMERAZAOPARC**: preferência de sistema (armazenada em cache) que controla o Portal de Vendas/Compras (Gerente On-line), sequência de visita, rota de entrega, dashboards comerciais/financeiros, emissão de cheques e notas de contingência.

- 
**APRES.TGFPAR**: chave dinâmica que define o Campo de Apresentação do Parceiro para as Centrais (ex.: Central de Liberações, Central de Atendimento ao Cliente) e para telas de Movimentação Financeira como parcelamento/renegociação.

O problema ocorre quando apenas um dos dois é configurado, ou quando o sistema não é reiniciado após a alteração, como ambos ficam em cache, a mudança só é aplicada após reinicialização do servidor (ou atualização do cache de parâmetros).