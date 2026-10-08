# E0714 Rejeição: Arquivo enviado com erro na assinatura

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228329318295-E0714-Rejei%C3%A7%C3%A3o-Arquivo-enviado-com-erro-na-assinatura](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228329318295-E0714-Rejei%C3%A7%C3%A3o-Arquivo-enviado-com-erro-na-assinatura)  
> **ID:** `37228329318295` | **Última Atualização:** 2026-09-25T00:03:28Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/37228329306007)

**MENSAGEM**

[E172] ou [E0714] Arquivo enviado com erro na assinatura.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/37228313127703)

**SITUAÇÃO**

O erro ocorre na transmissão da **Nota Fiscal de Serviço Eletrônica (NFS-e)**. A prefeitura ou o Ambiente Nacional não conseguiu validar a **assinatura digital** do arquivo enviado, e a nota não é autorizada.

Os cenários mais comuns são:

- Certificado digital vencido, revogado ou instalado incorretamente.

- Certificado de um CNPJ diferente do emitente da nota.

- Caracteres especiais nos textos da nota, que alteram o arquivo depois de assinado.

- Sistema desatualizado em relação ao layout ou ao padrão de assinatura exigido pelo município.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/37228313129239)

**SOLUÇÃO**

O erro de assinatura pode ter diferentes causas. Siga as verificações abaixo:

 

**Verificação 1: Validade do certificado digital**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37228313129751)

 Acesse a tela **"Console NFe"** (Comercial >> Configuração >> Console NFe).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/37228329310359)

 Confira se o certificado está dentro do prazo de validade. Se estiver vencido, providencie a renovação junto à autoridade certificadora.

 

**Verificação 2: Certificado correto para a empresa**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37228313129751)

 Confira se o certificado configurado pertence ao **mesmo CNPJ da empresa emitente**. Em ambientes com várias empresas ou filiais, é comum a empresa estar vinculada ao certificado de outra.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228329310359)

 Se houver mais de um certificado instalado no computador ou no servidor, confira se o sistema está usando o certificado atual e não um antigo com o mesmo nome.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228329310871)

 Para certificado **A3** (token ou cartão), confira se o dispositivo está conectado e se o driver está instalado.

 

**Verificação 3: Reinstalação do certificado**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37228313129751)

 Remova o certificado atual do repositório do sistema.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228329310359)

 Instale novamente o certificado digital e configure-o no Sankhya, vinculando-o à empresa correta.

 

**Verificação 4: Caracteres especiais na nota**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37228313129751)

 Revise a **descrição do serviço**, as **observações** e os dados do tomador (razão social e endereço).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228329310359)

 Remova caracteres especiais ou incomuns, como **&, <, >, aspas, emojis, quebras de linha e textos colados de outros programas** (Word, e-mail, WhatsApp).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228329310871)

 Salve a nota e transmita novamente.

 

**Verificação 5: Instabilidade no ambiente da prefeitura**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37228313129751)

 Se todas as verificações anteriores estiverem corretas, confira no site da prefeitura ou do provedor da NFS-e se há instabilidade ou manutenção.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228329310359)

 Se houver, aguarde a normalização e transmita novamente.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/37228313133463)

**CAUSA**

A prefeitura ou o Ambiente Nacional valida a assinatura digital para garantir que o arquivo foi gerado pelo emitente e não foi alterado depois de assinado. O erro ocorre quando essa validação falha. As principais causas são:

- Certificado digital vencido, revogado ou instalado incorretamente.

- Certificado vinculado a um CNPJ diferente do emitente.

- Certificado A3 desconectado ou sem driver.

- Caracteres especiais que alteram o conteúdo do arquivo depois da assinatura.

- Instabilidade no ambiente da prefeitura (menos comum).