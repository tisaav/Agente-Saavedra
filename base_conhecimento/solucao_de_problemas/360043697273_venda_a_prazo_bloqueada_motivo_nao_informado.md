# Venda a prazo bloqueada. Motivo não informado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697273-Venda-a-prazo-bloqueada-Motivo-n%C3%A3o-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697273-Venda-a-prazo-bloqueada-Motivo-n%C3%A3o-informado)  
> **ID:** `360043697273` | **Última Atualização:** 2026-08-10T19:22:22Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163839013143)

**MENSAGEM:**

[CORE_E04511] Venda a prazo bloqueada. Motivo não informado
[CORE_E04510] Venda a prazo bloqueada

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39596446522903)

**SITUAÇÃO:**

O sistema permite bloquear automaticamente vendas a prazo para clientes inadimplentes. Em alguns casos, o campo **"Motivo de bloqueio"** pode não ser preenchido automaticamente, exibindo mensagens genéricas.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163839014295)

**SOLUÇÃO:**

Para correção e configuração, siga os passos abaixo:

### **Configuração manual do motivo de bloqueio**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163807030167)

 Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros).
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163839022359)

 Selecione o parceiro utilizado no lançamento.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163839024151)

 Na aba **"Crédito"**, marque o campo **"Bloquear venda a prazo"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163807035927)

 Preencha o campo **"Motivo de bloqueio"** com a justificativa adequada e salve.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14499109765527)

 

### **Parâmetros complementares**

• **"DIASCAR"**: Define a carência para considerar o cliente em atraso.
• **"BLOQMATRIZ"**: Se ativo, o bloqueio da matriz reflete automaticamente em todas as filiais.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163807039511)

**CAUSA:**

Ocorre quando, no cadastro do parceiro, a opção **"Bloquear venda a prazo"** está selecionada e o campo **"Motivo de bloqueio"** não foi preenchido manualmente ou via processo automático de régua de cobrança.