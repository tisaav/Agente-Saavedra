# Verificação em duas etapas está desativada na sua conta

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31675937800855-Verifica%C3%A7%C3%A3o-em-duas-etapas-est%C3%A1-desativada-na-sua-conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/31675937800855-Verifica%C3%A7%C3%A3o-em-duas-etapas-est%C3%A1-desativada-na-sua-conta)  
> **ID:** `31675937800855` | **Última Atualização:** 2026-07-22T14:32:28Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675937778839)

 **MENSAGEM:**

Como a verificação em duas etapas está desativada para sua conta, não é possível usar esse método como segunda etapa de verificação. Entre em contato com sua administrador para receber ajuda.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675937782423)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038485398679)

 Com o usuário/e-mail administrador do domínio, entre na tela **"Administrador"** do gerenciamento de domínios do google (ícone do meio da primeira linha):

 

![483235379_9038236932948320_9070003558016056424_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675935573911)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038481665559)

 Pesquise por **"Verificação em duas etapas"**:

 

![491368972_691647896665639_8466505896147273173_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675937783191)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038485402519)

 Nas configurações da verificação em duas etapas do domínio, selecione **"Permitir que os usuários ativem a verificação em duas etapas"** e em **"Aplicação"** deixe como** "Desativar"** (dessa forma não é obrigatório que todos os usuários façam essa configuração) e depois salve essas informações:

 

![489731383_1307837996986215_1436552418002906907_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675935578775)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038481669783)

 Entre no e-mail que estava sendo configurado como remetente em Servidor SMTP ou Contas SMTP. Em seguida, clique no perfil e depois em **"Gerenciar sua conta do google"**:

 

![491351925_1606664310040286_8280589423048572562_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675937784599)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038592290967)

 Depois pesquise por **"Verificação em duas etapas"**:

 

![491419391_663914893465484_3943023793068260763_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675935579671)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038592292247)

 Crie e/ou ative a verificação em duas etapas (após cadastrar alguma 2° verificação, precisa ativar):

 

![491340684_1206132641213490_3104887693648262996_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675935586199)

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038622070679)

 Quando ativado, vai ficar marcado da seguinte forma:

 

![491335155_1794249008182266_8808747576665658346_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675935586711)

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32038622071063)

 Agora a configuração **"Senhas de app"**:

 

![491340229_1203518521305284_3321562645148920042_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675937790103)

 

- 

Após criar a senha de app, salve a senha, pois não é possível revê-la depois (se perder essa, crie uma nova)

- 

Coloque na senha das configuração de "Servidor SMTP" e/ou "Contas SMTP" onde estiver configurando o remetente dos envios de e-mail

- 

Com isso, se as outras configurações no Servidor SMTP ou Contas SMTP estiverem certas, o envio deve funcionar.

 

**Observação:** pode ser que o sistema continue apresentando o erro "Houve falha de autenticação. Verifique o usuário e senha", verifique se no log aparece "Too many login attempts, please try again later.", pois no sistema esse erro pode aparecer mascarado pelo erro de autenticação. O "Too many login attempts, please try again later." é do google, informando que tiveram muitas tentativas de acesso e por isso bloqueou o e-mail temporariamente (geralmente de 12 a 24 hrs), aguarde esse período e tente o envio novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31675935569303)

CAUSA:**

Problema ocorre ao tentar configurar a verificação em duas etapas para posteriormente ativar a "Senhas de app" do google. Essa configuração é necessária, pois o servidor SMTP e as contas SMTP não aceitam mais a senha de login do e-mail. Durante o processo, é exibido o erro: "Houve falha de autenticação. Verifique o usuário e a senha.".

Erro aparece quando a verificação em duas etapas não está habilitada para uso naquele domínio.