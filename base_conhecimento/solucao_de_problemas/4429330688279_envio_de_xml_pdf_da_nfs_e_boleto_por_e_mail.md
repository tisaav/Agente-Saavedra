# Envio de XML, PDF da NFS e boleto por e-mail 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4429330688279-Envio-de-XML-PDF-da-NFS-e-boleto-por-e-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/4429330688279-Envio-de-XML-PDF-da-NFS-e-boleto-por-e-mail)  
> **ID:** `4429330688279` | **Última Atualização:** 2026-08-28T16:48:15Z

---

Para realizar a configuração do envio de XML, NF-s (PDF) e boleto por e-mail, os cadastros a seguir devem ser verificados: 

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450978611735)

 Cadastro da TOP, aba **"Impressão"**, campo **"Imprimir Pix/Boleto/Duplicata"**: Na confirmação;

**Observação:** Caso a TOP não gere financeiro esse campo deve ser configurado como "Proibido" para que o sistema envie somente o PDF da NFS.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450978611735)

 Cadastro da TOP, aba **"E-mails da Top"**, vincule o Tipo Parceiro e o modelo a ser utilizado;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450978611735)

 Cadastro de Parceiro, aba **"Informações"**, campo **"Geração de boleto nas centrais"**: enviar e-mail ou imprimir e Enviar e-mail;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450978611735)

 Cadastro de Parceiro, aba Informações, campo **"Tipo geração boleto"**: Enviar E-mail;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450978611735)

 Cadastro de Parceiro, aba **"NFe campo E-mail p/ envio NF-e/CT-e"** deve estar preenchido;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450978611735)

 Cadastro Tipo de Negociação, aba **"Característica Imprimir boleto/duplicata?":** Na confirmação

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450978611735)

 Configure o e-mail no cadastro de **"Configurações > Cadastros > Empresas / Aba Endereço"**. Caso esse campo não esteja preenchido, não será enviado o XML nem o BOLETO, apenas a DANFE. 

 

Os parâmetros que influenciam a rotina são: 

**"NFSEGERARBOLETO":** Sim, conforme Cadastro de Parceiros

 

![Imagem](/attachments/token/VjOBVHmRVMEYns1i6qu5HWgdh/?name=inline-1839314193.png)

**"ENVEMAILNFSE":** Ligado

![Imagem](/attachments/token/Wdr4in0Cz3sZ1BPXvhM7CRUHq/?name=inline-1287076278.png)

 

O parceiro receberá dois e-mails, devido sistema verificar o cadastro da Top para o Danfe (aba Email da top) e o cadastro do parceiro (aba **"NFe/NFSe"**) para envio do XML. Poderá verificar os e-mails enviados pela tela Fila para envio de e-mail de nota/pedido. 

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4429264327319)