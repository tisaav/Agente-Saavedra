# Erro na autenticação do Portal de emissão de NFS-e de Florianopólis - SC

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30479563772695-Erro-na-autentica%C3%A7%C3%A3o-do-Portal-de-emiss%C3%A3o-de-NFS-e-de-Florianop%C3%B3lis-SC](https://ajuda.sankhya.com.br/hc/pt-br/articles/30479563772695-Erro-na-autentica%C3%A7%C3%A3o-do-Portal-de-emiss%C3%A3o-de-NFS-e-de-Florianop%C3%B3lis-SC)  
> **ID:** `30479563772695` | **Última Atualização:** 2026-07-22T14:35:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30479563755927)

 **MENSAGEM:**

"java.lang.Exception: Erro na autenticação com o provedor da prefeitura, verifique o usuário e senha cadastrado nas preferências da Empresa. Esse erro pode ter ocorrido por falta de conexão com a Internet."

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30479563760663)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30528194551831)

 Valide se as informações de login e senha no portal da Prefeitura de Florianopólis - SC estão corretos e funcionando normalmente.  

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30528184543511)

 Atenção: **não se esqueça de que no portal da prefeitura de Florianopólis - SC a autenticação é feita pelo **número da Inscrição Municipal do Prestador. **

 

![Erro na autenticação do Portal de emissão de NFS-e de Florianopólis 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/30528412458007)

 

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/30528184544151)

 Caso a **tentativa de login no portal da Prefeitura não se realize**, solicite uma recuperação de senha junto ao Provedor da Prefeitura. 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30528184544791)

 Por outro lado, se as credenciais de acesso ao portal da prefeitura estiverem corretas e o login acontecer normalmente, no Sankhya OM, acesse a tela **"Preferência da Empresa"** *(Comercial » Preferências » Empresa)*, vá até a aba **"Documentos Fiscais Eletrônicos", **depois clique na sub aba **"NFS-e >> Geral"** e cadastre o  **"Código do contribuinte da NFS-e", **que corresponde ao número da inscrição municipal. 

 

![Erro na autenticação do Portal de emissão de NFS-e de Florianopólis 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/30528412459159)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30528194556311)

 Por fim, **salve as alterações e tente gerar a Nota Fiscal novamente**. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30479563762199)

CAUSA:**

Problema ocorre devido falha na autenticação com o WebService do Provedor da Prefeitura. Uma vez que o portal da prefeitura de Florianopólis - SC usa a inscrição municipal para o login, e não o CNPJ como comumente acontece em outros portais.