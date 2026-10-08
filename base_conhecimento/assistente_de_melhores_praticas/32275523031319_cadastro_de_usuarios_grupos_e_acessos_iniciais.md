# Cadastro de Usuários, Grupos e Acessos Iniciais

> **Módulo:** Assistente de Melhores Praticas | **Subseção:** Configurações Iniciais  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32275523031319-Cadastro-de-Usu%C3%A1rios-Grupos-e-Acessos-Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/32275523031319-Cadastro-de-Usu%C3%A1rios-Grupos-e-Acessos-Iniciais)  
> **ID:** `32275523031319` | **Última Atualização:** 2026-07-22T16:17:03Z

---

### Descrição

Cadastra usuários e os vincula a grupos já existentes no sistema. Quando associado a um grupo, o usuário herda automaticamente as permissões de acesso correspondentes. Também permite a definição de configurações de segurança, como a criação de uma senha inicial e a exigência de alteração no primeiro acesso.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32275503256855)

 Caso um novo grupo seja adicionado, seus acessos deverão ser configurados manualmente na tela de Acessos.

**Registros Individuais:**

Para cada usuário informado, o sistema realiza a inclusão no banco de dados de autenticação, associando:

• Dados coletados: nome, e-mail, grupo(s) associado(s) etc.

**Configurações padrão:**

• Senha inicial "Novo123".

• Campo "O usuário deve alterar a senha no próximo logon" marcado.

• Configura "A senha nunca expira" desmarcado.

### Como instalar

1. Clique em "**Iniciar**".

2. Confira os nomes dos grupos predefinidos e seu status. Se necessário, edite ou adicione um novo grupo.

2.1. Se for necessário editar um grupo, dê um duplo clique na linha que deseja editar, que será aberta em modo formulário.

2.2. Se desejar, clique em "**+**" para adicionar um novo grupo.

2.3. Clique em "**Salvar**" (ícone disquete).

3. Clique em "**Avançar**" e em "**+**" para adicionar os usuários que desejar. Associe-o ao grupo que ele pertence.

3.1. Preencha os campos do formulário com as seguintes informações:

• Nome de usuário (o nome que será exibido no sistema)

• Empresa

• E-mail (se o usuário ainda não possuir um Sankhya ID, receberá um e-mail para cadastramento)

• Grupo

3.2. Clique em "**Salvar**" (ícone disquete).

4. Clique em "**Avançar**".

5. Verifique o resumo com uma prévia dos grupos de usuários, e usuários que serão cadastrados.

6. Clique em "**Instalar**" para finalizar a configuração.

### Detalhes da instalação

**Atualização de Dados na Instalação**

1. 
**Cadastro de Usuário e  Grupo de Usuário**

  - 
**TSIGRU **– Cadastro de grupo de usuário

  - 
**TSIUSU **– Cadastro de usuário

### Como simular

Para acessar os cadastros realizados:

**Usuários**:

1. vá até Configurações > Controle de Acesso > Usuários.

1. Clique em "**Relatório**" e em "**Atualizar**".

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32275503257239)

**** Vale saber**

Usuários herdam automaticamente os acessos dos grupos, então organize os grupos primeiro para evitar retrabalho! A senha inicial é “Novo123”, mas lembre-se: o sistema vai pedir para trocá-la no primeiro login. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32275523029527)

 Ah, sem Sankhya ID? Sem problemas — o convite chegará por e-mail!