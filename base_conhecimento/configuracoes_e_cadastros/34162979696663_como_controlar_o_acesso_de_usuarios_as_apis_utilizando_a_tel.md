# Como controlar o acesso de usuários às APIs utilizando a tela Autorização de API

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34162979696663-Como-controlar-o-acesso-de-usu%C3%A1rios-%C3%A0s-APIs-utilizando-a-tela-Autoriza%C3%A7%C3%A3o-de-API](https://ajuda.sankhya.com.br/hc/pt-br/articles/34162979696663-Como-controlar-o-acesso-de-usu%C3%A1rios-%C3%A0s-APIs-utilizando-a-tela-Autoriza%C3%A7%C3%A3o-de-API)  
> **ID:** `34162979696663` | **Última Atualização:** 2026-09-25T14:04:10Z

---

```text
 Módulo: Configurações > Avançado              Versão disponível: A partir da 4.35
```

A partir da versão 4.35 do sistema, foi introduzida uma funcionalidade que permite **controlar quais usuários podem acessar as APIs** da plataforma. Esse recurso traz mais segurança para integrações, permitindo um nível de controle mais rigoroso para consumo de serviços por usuários de integrações.

## **Como ativar o controle de autorização de API**

Para começar a usar a funcionalidade, é necessário ativar uma configuração no ambiente do sistema. Sem essa ativação, qualquer alteração feita na tela **Autorização de API** **não terá efeito**.

A ativação é feita por meio do parâmetro de inicialização **-Dsnk.authorization.api.enable**. Para saber como configurar esse tipo de parâmetro no ambiente Wildfly, consulte o artigo ****[Configuração de argumentos para Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly).

**Importante:** após a ativação, **todas as chamadas de API passarão a ser verificadas**. Se algum usuário de aplicação consumidora não tiver permissão, **o acesso será bloqueado**. Por isso, **recomenda-se revisar suas integrações** antes de habilitar o controle.

Após ativar a funcionalidade, caso um usuário tente acessar um serviço para o qual não tem permissão, o sistema apresentará uma mensagem com o seguinte padrão de erro informando a restrição:

***“AA_E100003***

***"Acesso negado ao serviço: provedorDeServico.servico para o usuário: 99 - nomeUsuario"***

Exemplo de mensagem considerando o provedor CRUDServiceProvider serviçoloadRecords:

***“AA_E100003***

***"Acesso negado ao serviço: CRUDServiceProvider.loadRecords para o usuário: 22 - integracao"***

## **Visão geral da tela "Autorização de API"**

A tela oferece uma interface prática para configurar e acompanhar os acessos concedidos. Ela é dividida em três áreas principais:

### **1. Lista de APIs disponíveis**

No painel esquerdo da tela, é possível visualizar todas as APIs do sistema, organizadas em duas categorias:

- 
**Mais utilizadas:** serviços mais utilizados nas integrações, classificados por critérios que permitem oferecer um controle adicional.

- 
**Outros:** demais APIs serviços disponíveis no sistema.

### **2. Consulta de acessos**

Um painel que lista os acessos concedidos para os usuários.  

Essa consulta apresenta duas abas com agrupamentos diferentes:

- 
**Por usuário:** mostra quais serviços estão autorizados para cada usuário, incluindo a quantidade de serviços autorizados.

- 
**Por serviço:** exibe quais usuários têm permissão para utilizar cada serviço, também apresenta a quantidade de usuários que possuem acesso ao serviço.

### **3. Configuração de novos acessos**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34162979693463)

Para autorizar o uso de uma API no sistema, siga os passos abaixo:

1. Acesse a **lista de APIs disponíveis** no sistema.

1. Localize e selecione o serviço desejado, por exemplo: DatasetSP.loadRecords.

1. Clique em **Adicionar**.

Ao realizar essa ação, será exibido um **popup de seleção de usuário**, onde você poderá escolher o usuário que terá permissão para utilizar a API selecionada.

**⚠️ Atenção**

 No popup serão exibidos apenas os usuários cujo cadastro esteja com o **Tipo de Usuário** definido como **"Integração"**.

Para configurar um usuário como integração, acesse a tela de **Cadastro de Usuários**, localize o campo **"Tipo de Usuário"** e selecione a opção **"Integração"**.

Caso o campo não esteja visível, verifique nas configurações da tela se ele está disponível para seleção e vincule-o à grade.

 

## **Configuração de recursos específicos**

Algumas APIs permitem a definição de recursos específicos para liberação.

No caso da API DatasetSP.loadRecords, por exemplo, é possível configurar a **entidade** que o usuário poderá acessar.

- Ao selecionar a entidade **Parceiro**, o usuário estará autorizado a realizar chamadas para esse endpoint utilizando **exclusivamente** a entidade **Parceiro**.

**Códigos de resposta ao usuário**

Ao usar o controle de acesso de API, você pode se deparar com algumas mensagens de erro. Entender o que elas significam ajuda a resolver o problema rapidamente:

1. 
**Problemas Internos do Sistema (**AA_E100001, AA_E100004, AA_E100005, AA_E100007, AA_E100009, AA_E100008, AA_E100011**)**

Se você vir mensagens como **"Erro interno ao processar a request. Não foi possível atender a solicitação com os parâmetros informados, entre em contato com o suporte Sankhya" **ou **"Ocorreu um erro ao processar a solicitação, porém não foi possível identificar a causa. Entre em contato com o suporte"**, isso indica um problema no sistema.

**Como resolver:** Entre em contato com o suporte técnico da Sankhya para que eles investiguem a causa do problema.

1. 
**Falta de Informação na Chamada **(AA_E100006, AA_E100012**)**

A mensagem** "Atributo de autorização não encontrado na request. Não foi possível avaliar o payload da request, verifique o padrão de chamada"** significa que a API foi chamada sem alguma informação necessária para verificar a permissão.

**Como resolver:** Revise o padrão de chamada da API para garantir que todos os dados de autorização estejam sendo enviados corretamente.

1. 
**Usuário Sem Permissão (**AA_E100002, AA_E100003, AA_E100010**)**

Quando a mensagem diz **"O usuário não está autorizado a executar o serviço, conceda acesso ao usuário no recurso, serviço e atributo (caso necessário)"**, significa que o usuário que está tentando acessar o serviço não tem a permissão necessária.

**Como resolver:** Vá à tela **Autorização de API** e **dê a permissão que falta** para o usuário usar aquele serviço.

1. 
**Permissões Controladas pela Tela (**AA_E100013)

A mensagem **"Não é possível alterar permissões de acesso controladas via tela "Autorização de API"** **por outros meios que não a própria tela"** indica que as permissões gerenciadas pela tela **Autorização de API** só podem ser alteradas por essa mesma tela.

**Como resolver:** Acesse a tela **Autorização de API** para fazer qualquer mudança nessas permissões.

## **Recomendações finais**

- Ative a funcionalidade apenas quando tiver certeza de quais acessos precisam ser controlados.

- Antes de ativar, **valide suas integrações atuais** para evitar interrupções.

- Use a tela de forma contínua para revisar e ajustar os acessos conforme a necessidade do seu ambiente.


---

### 🔗 Links e Referências Internas:

- [Configuração de argumentos para Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly)