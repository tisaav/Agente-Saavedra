# Configurações de Login

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595874-Configura%C3%A7%C3%B5es-de-Login](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595874-Configura%C3%A7%C3%B5es-de-Login)  
> **ID:** `360044595874` | **Última Atualização:** 2026-07-29T13:44:49Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310598210967)

 **Módulo:** Configurações > Controle de Acesso
```

O Sankhya-Om por meio da configuração desta tela permite a utilização do login via autenticação no LDAP. Deste modo, é possível evitar problemas como o esquecimento das senhas. Vejamos sobre cada uma das **"Opções de Login"**:

- 
**Padrão:** utiliza o usuário e senha definidos no [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874) para realizar o login;

- 
**Login via LDAP:** permite o login utilizando as mesmas credenciais do servidor de domínio. Com esta opção selecionada:

1.As aplicações mobile e as integrações que utilizam a autenticação chamando o serviço Moblie Login serão afetadas. Deste modo, para os usuários em que o login e senha são utilizados para autenticar a integração, tem-se como sugestão que a marcação **"Ignorar login via LDAP"** localizada no Cadastro do Usuário, aba [Domínio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abadomnio), se encontre ativa para que o login e senha não sejam alterados;

2.Ao realizar o login pela primeira vez autenticando na rede, a senha de rede será salva internamente no Sankhya-Om. Ainda que se trate dos casos em que não houver comunicação com o servidor de domínio, será necessário utilizar o usuário e senha da rede para realizar o Login;

- 
**Login LDAP automático:** Esse tipo de login é efetuado de modo automático no sistema utilizando as credenciais da própria estação de trabalho (domínio/usuário). Sendo que, esta opção é aplicada somente para Windows e necessita da instalação do [WebConnection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection).

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4405933221655)

Com a opção de login definida, no campo **"Caminho do servidor/LDAP"** informe o domínio pelo qual o sistema irá se conectar.

Depois, preencha o **"Grupo de Rede Padrão"** ao qual o usuário tentará ser autenticado, como, por exemplo, Domínio\UsuárioRede.

**Nota:** o usuário SUP não é afetado pelas configurações realizadas nesta tela.


---

### 🔗 Links e Referências Internas:

- [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)
- [Domínio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abadomnio)
- [WebConnection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection)