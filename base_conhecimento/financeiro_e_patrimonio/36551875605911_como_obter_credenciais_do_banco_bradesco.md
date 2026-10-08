# Como obter credenciais do Banco Bradesco?

> **Módulo:** Financeiro e Patrimônio | **Subseção:** Banking  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36551875605911-Como-obter-credenciais-do-Banco-Bradesco](https://ajuda.sankhya.com.br/hc/pt-br/articles/36551875605911-Como-obter-credenciais-do-Banco-Bradesco)  
> **ID:** `36551875605911` | **Última Atualização:** 2026-09-25T12:39:38Z

---

Para adquirir as credenciais do **Banco Bradesco** e ativar a funcionalidade de Boleto Simples, Híbrido ou PIX via API, siga as instruções abaixo:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551875593111)

 **Vincular  a SANKHYA como um PARCEIRO através da sua Conta Bradesco:**

1.1 Acesse o [Net Empresa](https://www.ne12.bradesconetempresa.b.br/ibpjlogin/login.jsf) do Bradesco e realize o login com seu usuário/senha

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551875594135)

1.2 Acesse a aba **‘Serviços Operacionais’**

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551853648023)

**

1.3 Clique em API :: **Integração com parceiros**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551853653015)

1.4 Preencha os dados

- Produto =** API **

- Serviço = **Integração com Parceiro**

- Tipo = **Contratação**

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551853653783)

**

1.5 Preencha os dados solicitados no cadastro

**Importante: **Em ‘Parceiro Integrador’ selecione o parceiro = **SANKHYA**

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551875599895)

**

1.8 Siga as etapas para que o usuário MASTER aprove  a solicitação

1.9 Certifique-se que a solicitação foi confirmada

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551875602071)

Feito isso, inicie o processo de geração das credenciais:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36551875603095)

 **Geração das Credenciais:**

**Importante:**

****

| Para facilitar sua integração, reunimos aqui o passo a passo disponibilizado pelo Bradesco para criação das credenciais. Caso surjam dúvidas ou seja necessário suporte durante o processo, o contato deve ser feito diretamente com o Bradesco, |
| --- |

**2.1 Inscrição ao Portal Developers**

Acessar o [Portal Developers](https://developers.bradesco.com.br/#iss=https%3A%2F%2Flogin.axway.com%2Fauth%2Frealms%2FBroker) e seguir as etapas demonstradas abaixo, conforme instruções Bradesco :

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473793431)

**

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473794327)

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473795223)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435015447)

 

**2.2 Acesso ao Portal Developers**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473797015)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473798167)

**2.3 Inscrição para os produtos desejados**

Nesta etapa, selecione apenas o produto — o que corresponde à modalidade de boleto ou ao serviço que o cliente vai utilizar:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473799191)

- Boleto Híbrido (boleto com QR Code para pagamento via PIX): selecione **Cobrança com QR Code**

- Boleto Simples (cobrança exclusivamente por código de barras ou linha digitável): selecione **Cobrança**

- Para PIX: selecione **PIX - Geração de QR Code**

**⚠️ Atenção**

Selecionar o produto errado para a modalidade de boleto contratada gera falha ao usar a API de boletos do Bradesco — o credenciamento é concluído, mas as chamadas à API retornam erro. Confirme com o cliente qual modalidade foi contratada (Boleto Híbrido ou Boleto Simples) antes de inscrever o produto no Portal Developers.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473804311)

Selecionado o produto, clique em ‘Inscrever-se’ para efetuar a assinatura no produto selecionado

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473805591)

**Importante !**

No próximo passo, atente-se a seguinte informação : Para Integração aos serviços Fintech só serão aceitas Credenciais geradas em **PRODUÇÃO**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435024791)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435025815)

 

**2.4 Registro da aplicação**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435027735)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473808791)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435029911)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473810455)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473811223)

Obs: Indicamos que todos os recursos ‘Produção’ sejam selecionados

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435034391)

 

**2.5 Geração das Credenciais**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473812631)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435036823)

 

**Importante:**

****

****

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42309696246807)

**

| Na etapa acima, no campo ‘Certificado Público no formato .pem .cer ou .crt’, deverá ser inserido o certificado baixado no SANKHYA. Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto Rápido :: Selecionar Conta Bradesco :: Etapa ‘Credenciais via API’ :: Campo ‘Baixar Certificado’ |
| --- |

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473815063)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435040279)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435041687)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782473819287)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36782435043607)