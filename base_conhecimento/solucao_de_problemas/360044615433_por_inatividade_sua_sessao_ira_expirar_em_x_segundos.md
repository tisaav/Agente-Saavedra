# Por inatividade, sua sessão irá expirar em 'X' segundos

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615433-Por-inatividade-sua-sess%C3%A3o-ir%C3%A1-expirar-em-X-segundos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615433-Por-inatividade-sua-sess%C3%A3o-ir%C3%A1-expirar-em-X-segundos)  
> **ID:** `360044615433` | **Última Atualização:** 2026-07-22T15:55:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589607690903)

 MENSAGEM:**

"Por inatividade, sua sessão irá expirar em 'X' segundos.

Você ainda está aí?"

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589593365399)

 CAUSA:**

Mensagem apresentada quando para o usuário logado, cujo o tempo de inatividade foi atingido. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589593358231)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589593360023)

 Configuração por 'Usuário':

Acesse **"Usuários"** *(Caminho de acesso: Configurações » Controle de Acesso)*, aba **"Segurança": **é possível realizar essa definição no campo **"Tempo de Aplicativo inativo para finalizar":**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15298752069655)

 

- 

Este campo serve para informar a quantidade de minutos que o sistema poderá ficar aberto sem ser utilizado. Assim que essa quantidade de minutos for ultrapassada, o usuário terá que acessar novamente o sistema. Isso é uma questão de segurança e também tem como finalidade liberar licenças do sistema dos usuários que abrem o sistema, mas não estão utilizando o mesmo. Ao ser finalizada uma sessão a licença é "devolvida" para o SAS, o que permite que outro usuário tenha acesso ao módulo.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589593362327)

 Configuração Geral, por **parâmetro**

Na tela **"Preferências" ***(Caminho de acesso: Configurações » Avançado)* é possível realizar a mesma definição através da chave **"SESSIONTIMEOUT"**:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15298762777239)

 

- 

Quando o campo citado no item 1 estiver 0 ou em branco, será considerado o parâmetro acima. 

**Observação:  **Existe uma margem de erro de até 1 min para o tempo configurado.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589607698583)

 IMPORTANTE:**

O valor informado no cadastro de usuário tem prioridade quanto ao parâmetro global. Em caso do parâmetro global não ser configurado pelo usuário, o sistema vai considerar o padrão de instalação do servidor de aplicações (jboss), que é de 60 minutos (1 hora).

É possível configurar o tempo de timeout diferente para cada usuário realizando o passo 1 desse artigo ou um tempo padrão para todos usuários, deixando o campo em branco e definindo em preferências **SESSIONTIMEOUT **(passo 2 desse artigo)