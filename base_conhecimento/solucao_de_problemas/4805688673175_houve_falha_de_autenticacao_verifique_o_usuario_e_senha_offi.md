# Houve falha de autenticação. Verifique o usuário e senha - Office365

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4805688673175-Houve-falha-de-autentica%C3%A7%C3%A3o-Verifique-o-usu%C3%A1rio-e-senha-Office365](https://ajuda.sankhya.com.br/hc/pt-br/articles/4805688673175-Houve-falha-de-autentica%C3%A7%C3%A3o-Verifique-o-usu%C3%A1rio-e-senha-Office365)  
> **ID:** `4805688673175` | **Última Atualização:** 2026-07-22T15:18:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344233615383)

 MENSAGEM**:

CORE_E04536 - Houve falha de autenticação. Verifique o usuário e senha. Saiba mais!

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344218095511)

 CAUSA: **

O incidente ocorre quando mesmo o usuário e senha do e-mail tenha sido testado o login via navegador com sucesso.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344233620631)

 SOLUÇÃO:**

Use o Centro de administração do Microsoft 365 para habilitar ou desabilitar o AUTH SMTP em caixas de correio específicas:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344218105495)

 Abra o [Centro de administração do Microsoft 365](https://admin.microsoft.com/) e vá para: **Usuários** > **Usuários ativos.**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344233629207)

 Selecione o usuário e no sobrevoo exibido clique em **Email**.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344218114327)

 Na seção **Aplicativos de email,** clique em **Gerenciar aplicativos de email**.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344218118423)

 Verifique a **configuração SMTP autenticada:** caso esteja desmarcada/desabilitada, faça a marcação para que fique habilitada/check, conforme print abaixo.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15776028055063)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344218120983)

 Quando terminar, clique em **Salvar alterações**.

 

**Observação:** feito isso basta realize o teste de envio conforme abaixo.

**» Envio de Mensagens » Servidor SMTP**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15776001167639)