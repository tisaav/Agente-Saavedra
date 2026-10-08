# Solução do erro: Quantidade da tarefa está fragmentada. Tarefa=X, Seq=Y, Prod=ZZZ, Qtd.orig=999,9, Qtd.dest=999,9

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043734154-Solu%C3%A7%C3%A3o-do-erro-Quantidade-da-tarefa-est%C3%A1-fragmentada-Tarefa-X-Seq-Y-Prod-ZZZ-Qtd-orig-999-9-Qtd-dest-999-9](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043734154-Solu%C3%A7%C3%A3o-do-erro-Quantidade-da-tarefa-est%C3%A1-fragmentada-Tarefa-X-Seq-Y-Prod-ZZZ-Qtd-orig-999-9-Qtd-dest-999-9)  
> **ID:** `360043734154` | **Última Atualização:** 2026-07-22T15:59:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305888331415)

 MENSAGEM**:

[SQL-50001]: Quantidade da tarefa está fragmentada. Tarefa=X, Seq=Y, Prod=ZZZ, Qtd.orig=999,9, Qtd.dest=999,9

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305888334231)

 SOLUÇÃO**:

Para correção siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305888337559)

 Acesse *Comercial » Preferências » Empresa*, aba **WMS** e marque a opção **"Permitir estoque fragmentado"**;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305888339351)

 Acesse *Configurações » Avançado » Preferências* e ligue o parâmetro **"FRAGMENTAESTWMS"**;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305859449367)

 Acesse *WMS » Cadastros » Endereço de Armazenamento* e marque o campo **"Permite Fragmentar Estoque"**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305888346903)

 CAUSA**:

Quando o produto permite separação fragmentada, trabalha com unidade que permite fragmentação e os parâmetros e marcações não estão habilitados.