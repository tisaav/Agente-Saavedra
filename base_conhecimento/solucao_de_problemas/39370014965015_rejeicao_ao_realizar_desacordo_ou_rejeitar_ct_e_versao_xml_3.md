# Rejeição ao Realizar Desacordo ou Rejeitar CT-e: Versão XML 3.0 Não Suportada

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39370014965015-Rejei%C3%A7%C3%A3o-ao-Realizar-Desacordo-ou-Rejeitar-CT-e-Vers%C3%A3o-XML-3-0-N%C3%A3o-Suportada](https://ajuda.sankhya.com.br/hc/pt-br/articles/39370014965015-Rejei%C3%A7%C3%A3o-ao-Realizar-Desacordo-ou-Rejeitar-CT-e-Vers%C3%A3o-XML-3-0-N%C3%A3o-Suportada)  
> **ID:** `39370014965015` | **Última Atualização:** 2026-09-02T20:17:32Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39370061597207)

 **MENSAGEM**

Rejeição: Cabecalho - Versao do arquivo XML não suportada [Versao 3 com vigencia encerrada (ATO COTEPE/ICMS 123/22), utilize a Versao 4.00]

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39370061597335)

 **SITUAÇÃO**

Esta mensagem de rejeição ocorre ao tentar realizar o desacordo da prestação de serviço de um CT-e ou ao tentar rejeitar um CT-e no sistema. O erro é apresentado pela SEFAZ quando o arquivo XML está sendo processado com a versão 3.00 do CT-e, que teve sua vigência encerrada conforme o Ato Cotepe/Icms 123/22.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39370061597463)

 **SOLUÇÃO**

Para resolver este erro, configure a empresa para utilizar a versão 4.00 do CT-e. Siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39370014962839)

 Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39370061597591)

 Navegue até a aba **"Documentos Fiscais Eletrônicos"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39370014963095)

 Acesse a seção **"CT-e"** e depois **"Geral"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39370014963223)

 Marque a opção **"Usar modo síncrono para envio do XML"**.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39370061598359)

 No campo **"Versão CT-e"**, selecione a opção **"Versão CT-e 4.00"**.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39370061598871)

 Salve as configurações realizadas.
 

Após realizar estas configurações, o arquivo será processado com sucesso utilizando a versão 4.00 do CT-e.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39370061599255)

 **CAUSA**

A rejeição ocorre porque a empresa está configurada para utilizar a versão 3.00 do CT-e, que teve sua vigência encerrada conforme determinação do Ato COTEPE/ICMS 123/22. A SEFAZ não aceita mais o processamento de arquivos XML nesta versão, sendo obrigatório o uso da versão 4.00 para envio e processamento de CT-e.