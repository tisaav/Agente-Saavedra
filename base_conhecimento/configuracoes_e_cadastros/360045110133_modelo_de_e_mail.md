# Modelo de E-mail

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133-Modelo-de-E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133-Modelo-de-E-mail)  
> **ID:** `360045110133` | **Última Atualização:** 2026-07-29T13:56:23Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310912050327)

 **Módulo:** Configurações > Cadastros
```

Nesta tela efetua-se a configuração dos modelos de e-mail que serão utilizados na [Régua de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a), sendo que, os modelos poderão ser aplicados em várias réguas simultaneamente.

Acesse os links abaixo para conhecer as funcionalidades dessa tela:

#### ****

[Aba Geral](#abageral)[Aba Conteúdo](#abacontedo)

[Editando a variável Lista de títulos](#editandoavarivellistadettulos)[Formatadores de TXT](#formatadoresdetxt)

| Funcionalidades da tela |  |
| --- | --- |
|  |  |
|  |  |

### **Aba Geral**

Nesta aba serão realizadas as configurações iniciais pertinentes ao envio dos e-mails.

![Modelo_de_Email.png](https://ajuda.sankhya.com.br/hc/article_attachments/8582212377495)

No campo **"Tipo de modelo"** é indicado o modelo utilizado no despacho dos e-mails. Esse campo possui as opções:

- Régua de Cobrança;

- Liberação de Limites;

- NF-e;

- Pix Cobrança;

- Acordo de Verba;

- Agenda de Recursos.

Para utilizar a opção Liberação de Limites é preciso selecionar uma das opções **"Por e-mail"**, **"Por notificação no SankhyaOm"** ou **"Ambos"** disponíveis no campo **"Notificar solicitante de liberações"** da aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao) do [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) e posteriormente, vincular o e-mail no campo **"Modelo de e-mail p/ Liberação de Limites"** da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

Ainda sobre a opção Liberação de Limites, quando acessar a tela [Régua de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a) para realizar as configurações dessa tela, não serão disponibilizados os modelos de e-mail do tipo Liberação de Limites para utilização nela.

Referente a opção NF-e deve-se, obrigatoriamente, informar uma **"Conta SMTP"**. Além disso, para utilizar um Modelo de E-mail do tipo NF-e exclusivo para uso, informe o modelo criado anteriormente na tela Preferências da Empresa, aba NF-e/NFC-e, campo **"Modelo de E-mail NF-e"**.

A conta responsável pelo envio dos e-mails será informada no campo **"Conta SMTP"**.

O campo **"Responder para"** será preenchido quando o remetente desejar responder o e-mail.

[[voltar ao topo]](#top)

### **Aba Conteúdo**

Esta aba é utilizada para construir os modelos de e-mail, sendo que eles poderão ser reaproveitados em qualquer evento de e-mail seja qual for a Régua de Cobrança.

![Aba Conteúdo.png](https://ajuda.sankhya.com.br/hc/article_attachments/19575220047639)

O tema do e-mail poderá ser especificado de forma direta através do campo **"Assunto"**, como também tem a possibilidade de formatar o texto através de variáveis que poderão ser adicionadas através do botão auxiliar de edição do assunto 

![ME03.png](https://ajuda.sankhya.com.br/hc/article_attachments/8582563997463)

 **"Assunto"**. Ao acioná-lo, terá a exibição de um pop-up de mesma nomenclatura contendo as variáveis disponíveis:

![ME3.png](https://ajuda.sankhya.com.br/hc/article_attachments/8582568726039)

Esse recurso está disponível também para o corpo do e-mail através do botão **"Variáveis"**.

![Variáveis.png](https://ajuda.sankhya.com.br/hc/article_attachments/19575220050327)

As opções do campo Tipo de modelo da aba [Geral](#abageral), permitem o uso das seguintes variáveis nesta aba:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458065304855)

 **Tipo de modelo = ****Liberação de Limites**

Para esse tipo de modelo pode-se utilizar as variáveis relacionadas ao processo de [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites), como exemplo:

- Código do Evento

- Nome do Evento

- Código Usuário Solicitante

- Nome Usuário Solicitante

- Dh Solicitação

- Valor limite

- Valor solicitado

- Valor liberado

- Código Usuário Liberador

- Nome Usuário Liberador

- Dh Liberação

- Observação do Liberador

- Status

**Nota: **a variável Status deve ser preenchida com **"Aprovada"**, **"Negada"** ou **"Liberada parcialmente"**, conforme a situação do documento na TSILIB, após o processamento da liberação:

- **Aprovada:** REPROVADO = ‘N’ AND VLRATUAL <= VLRLIBERADO

- **Liberada parcialmente:** REPROVADO = ‘N’ AND VLRATUAL > VLRLIBERADO AND VLRLIBERADO <> 0

- **Negada:** REPROVADO = ‘S’ AND VLRLIBERADO = 0

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458065304855)

 **Tipo de modelo = ** **NF-e**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19458381331991)

 Dados da NF-e:**

- 

  - 

#CHAVE_ACESSO

  - 

#NUMNOTA

  - 

#SERIE

  - 

#DATAEMISSAO

  - 

#AUTORIZACAO

  - 

#AMBIENTE_ENVIO

  - 

#TP_EMISAO

  - 

#VLRNOTA

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19458381331991)

 Dados do Emitente (TSIEMP):**

- 

  - 

#RAZAOSOCIAL_EMITENTE

  - 

#NOMEFANTASIA_EMITENTE

  - 

#CNPJ_EMITENTE

  - 

#ENDERECO_EMITENTE

  - 

#MUNICIPIO_EMITENTE

  - 

#UF_EMITENTE

  - 

#TELEFONE_EMITENTE

  - 

#EMAIL_EMITENTE

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19458381331991)

 Dados do Destinatário (TGFPAR):**

- 

  - 

#RAZAOSOCIAL_DESTINATARIO

  - 

#CNPJCPF_DESTINATARIO

  - 

#ENDERECO_DESTINATARIO

  - 

#MUNICIPIO_DESTINATARIO

  - 

#UF_DESTINATARIO

  - 

#TELEFONE_DESTINATARIO

  - 

#EMAIL_DESTINATARIO

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19458381331991)

 Dados do Rodapé (TISEMP):**

- 

  - 

#EMAIL_REMETENTE

  - 

[Logomarca Sankhya](https://www.sankhya.com.br/wp-content/uploads/2021/02/logosankhya-1.png). 

**

![9b9087f0-c329-4e14-b4cf-dd5f134049e0](https://ajuda.sankhya.com.br/hc/article_attachments/32052726946071)

 IMPORTANTE: Limitação na exibição de imagens no corpo do e-mail**

Para fazer o uso de imagens no campo Conteúdo, quando o Tipo de Modelo for igual à NF-e, deve-se fazer o upload do arquivo imagem em um site de hospedagem de imagem (OneDrive, Drive, entre outras) para posteriormente ser copiada para o campo. Pois o serviço responsável por processar o envio de e-mails converte imagens inseridas no campo Conteúdo para o formato Base64, e servidores de webmail como Gmail, Outlook, Hotmail, Roundcube, entre outros, não oferecem suporte à exibição direta de imagens em Base64 no corpo da mensagem.

✅ Este não é um problema do ERP Sankhya, mas sim uma limitação do próprio protocolo dos serviços de e-mail.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458065304855)

** Tipo de modelo = Agenda de Recursos**

Para este tipo de modelo é possível empregar as variáveis associadas ao processo de [Agenda de Recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604574):

- Nome Contato;

- Cód. Parceiro;

- Nome Parceiro;

- Razão Social Parceiro;

- Dt. Início Agendamento;

- Dt. Final Agendamento;

- Número OS;

- Número Projeto;

- Número SubOS;

- Cód. Etapa do Projeto;

- Descr. Projeto;

- Número do Contrato;

- Nome do Executante.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458065304855)

** Tipo de modelo = Acordo de Verba **

Para esse tipo de modelo pode-se utilizar as variáveis relacionadas ao processo da tela Verbas:

- Nome da Empresa;

- Responsável;

- Parceiro;

- Contato;

- Número da Verba;

- Operação;

- Data do Acordo;

- Data Limite;

- Natureza;

- Forma de pagamento/recebimento;

- Valor da Verba;

- Parcelas.

**Nota:** somente as variáveis apresentadas na aba Conteúdo serão válidas quando os modelos do campo Tipo de Modelo forem definidos como NF-e, Pix Cobrança ou Régua de cobrança.

[[voltar ao topo]](#top)

### **Editando a variável Lista de títulos**

A variável &{LISTA_TITULOS} por padrão exibe os campos **"Data de Vencimento"**, **"Valor Líquido"**, **"Linha Digitável"** e **"Número Único do Financeiro"**. Sendo que, é possível editá-la colocando à sua frente qualquer campo da tabela TGFFIN. Abaixo, alguns exemplos:

&{LISTA_TITULOS:DTVENC}: A descrição do campo será de acordo com o banco de dados;

&{LISTA_TITULOS:DTVENC=Vencimento}: Neste caso, a descrição do campo corresponderá aos dados inseridos após o sinal de igual;

&{LISTA_TITULOS:NUMCONTRATO=Contrato};

&{LISTA_TITULOS:NUMCONTRATO};

&{LISTA_TITULOS:NUMNOTA=Título,DTNEG=Data da Emissão,DESDOBRAMENTO=Parcela,DTVENC=Vencimento,VLRDESDOB=Valor}.

**Nota:** a variável &{LISTA_TITULOS} terá a seguinte ordenação: Data de Vencimento, Número da Nota e Desdobramento.

[[voltar ao topo]](#top)

### **Formatadores de TXT**

É possível utilizar formatadores de TXT para editar o corpo do texto, como também a função PDES que já existe nas formatações de TXT.

**Observação:** a variável &{TOTAL_DEBITO} não possui uma formatação padrão, para que seu formato seja em moeda é necessário utilizar a seguinte formatação:

- Total débito: R$ FORMATNUMERIC(&{TOTAL_DEBITO})

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16646767763095)

 Acesse também:

[Formatando arquivos TXT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-W)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Régua de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a)
- [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao)
- [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)
- [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites)
- [Logomarca Sankhya](https://www.sankhya.com.br/wp-content/uploads/2021/02/logosankhya-1.png)
- [Agenda de Recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604574)
- [Formatando arquivos TXT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-W)