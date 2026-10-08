# Mensagem "DlllnscE32 não carregada" ao tentar cadastrar um parceiro no FAST ou Mitra

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16995939136535-Mensagem-DlllnscE32-n%C3%A3o-carregada-ao-tentar-cadastrar-um-parceiro-no-FAST-ou-Mitra](https://ajuda.sankhya.com.br/hc/pt-br/articles/16995939136535-Mensagem-DlllnscE32-n%C3%A3o-carregada-ao-tentar-cadastrar-um-parceiro-no-FAST-ou-Mitra)  
> **ID:** `16995939136535` | **Última Atualização:** 2026-07-22T14:54:03Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16995928002199)

 **MENSAGEM: **

"DlllnscE32 não carregada".

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16995953391511)

CAUSA:**

Falta da DLL de comunicação/validação de IE do Sintegra. 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16995967853463)

SOLUÇÃO:**

Acessar o site do Sintegra([http://www.sintegra.gov.br/](http://www.sintegra.gov.br/)) e conferir se o CNPJ e IE do parceiro estão válidos:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16995654468759)

 

Validado os dados do parceiro, ainda no site do Sintegra, acesse o menu serviços e clique em download:

![serviços 22-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19257992730903)

![download 22-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19258031680791)

Localizar o tópico "Módulo para verificar a consistência das Inscrições Estaduais" e baixar a DLL de validação de Inscrições Estaduais:

 

![Sintegra 22-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19257992755863)

Faça o download, extraia e pegue apenas o arquivo "DllInscE32.dll". Feche o sistema(Mitra/Fast Service) e copie o arquivo para a pasta C:\Windows\SysWOW64 ou para a pasta de instalação do sistema.
 
Feito isto abra o sistema e tente realizar o cadastro novamente.