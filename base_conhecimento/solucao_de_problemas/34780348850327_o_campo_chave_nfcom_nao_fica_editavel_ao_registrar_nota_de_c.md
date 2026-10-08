# O campo "Chave NFCom" não fica editável ao registrar nota de compra de serviço de comunicação

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34780348850327-O-campo-Chave-NFCom-n%C3%A3o-fica-edit%C3%A1vel-ao-registrar-nota-de-compra-de-servi%C3%A7o-de-comunica%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/34780348850327-O-campo-Chave-NFCom-n%C3%A3o-fica-edit%C3%A1vel-ao-registrar-nota-de-compra-de-servi%C3%A7o-de-comunica%C3%A7%C3%A3o)  
> **ID:** `34780348850327` | **Última Atualização:** 2026-09-09T11:17:45Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/40620599628567)

**MENSAGEM**

[CORE_E08149] TOP com NFCom de Terceiros deve ter a chave NFCom informada com 44 caracteres e sem espaço em branco.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/34780348835095)

**SITUAÇÃO**

Ao registrar a nota de compra de serviço de comunicação, o sistema exige o preenchimento do campo **"Chave NFCom"**, porém o campo permanece não editável. Na tela **"Configurador de Layout da Nota"** (Configurações >> Avançado >> Configurador de Layout da Nota) não é possível marcar o campo **"Editável"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34780371250327)

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/34780348838807)

**SOLUÇÃO**

Para garantir o correto funcionamento e a editabilidade do campo, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/35706640935831)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP). Na aba **"NF-e/NFC-e/CF-e"**, configure o campo **"Modelo de documento"** para **"62 - Nota Fiscal Eletrônica de Serviços de Comunicação"**.
 

![27.png](https://ajuda.sankhya.com.br/hc/article_attachments/35706640938647)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/35706647425047)

 No mesmo cadastro da TOP, acesse a aba **"NFCom"** e configure o campo **"NFCom"** como **"Terceiros"**.
 

![26.png](https://ajuda.sankhya.com.br/hc/article_attachments/35706647425431)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/35706640946455)

 Caso o problema persista após a configuração da TOP, altere o layout da tela **"Central de Compras"** (Comercial >> Compras >> Central de Compras) de **Flex** para **HTML5**, pois o campo **"Chave NFCom"** possui funcionalidade de edição no layout HTML5.
 

**OBSERVAÇÕES:**

- 

Não configure o campo **"Chave NFCom"** como obrigatório no **"Configurador de Layout da Nota"**. O sistema valida automaticamente o preenchimento ao confirmar a nota e exibirá mensagem caso o campo esteja vazio.
 

1. 

A chave NFCom deve conter exatamente **44 caracteres numéricos**, sem espaços ou caracteres especiais.
 

1. 

Certifique-se de que não há configurações conflitantes na TOP.
 

![25.png](https://ajuda.sankhya.com.br/hc/article_attachments/35706640949911)

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/34780348837527)

**CAUSA**

O campo **"Chave NFCom"** permanece bloqueado se a TOP não estiver configurada corretamente para o modelo 62 (NFCom de Terceiros). Adicionalmente, o uso do layout **Flex** (que está em processo de descontinuação) pode restringir a editabilidade do campo em comparação ao layout **HTML5**. Erros de validação também ocorrem caso a chave contenha espaços em branco ou menos de 44 dígitos.