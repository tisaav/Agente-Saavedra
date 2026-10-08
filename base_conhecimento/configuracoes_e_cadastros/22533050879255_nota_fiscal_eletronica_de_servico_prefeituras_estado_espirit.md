# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Espírito Santo

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/22533050879255-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Esp%C3%ADrito-Santo](https://ajuda.sankhya.com.br/hc/pt-br/articles/22533050879255-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Esp%C3%ADrito-Santo)  
> **ID:** `22533050879255` | **Última Atualização:** 2026-07-29T13:41:32Z

---

Neste artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Espírito Santo, para conhecê-las acesse os links abaixo:

#### ****

[Alfredo Chaves/ES](#01JFJ9ZX5N2NYX58DJZGRFRTTM)[João Neiva/ES](#Jo%C3%A3oNeiva/ES)

[Anchieta/ES](#Anchieta/ES)[Linhares/ES](#Linhares/ES)

[Aracruz/ES](#Aracruz/ES)[Pinheiros/ES](#h_01H98JRWGWASH5BM9G335273E9)

[Cariacica/ES](#cariacica/es)[Serra/ES](#Serra/ES)

[Colatina/ES](#Colatina/ES)[Viana/ES](#Viana/ES)

[Guarapari/ES](#h_01H98JRWGW54QPQ8M2N94RTS7Z)[Vila Velha/ES](#Vila%20Velha/ES)

[Ibiraçu/ES](#Ibira%C3%A7u/ES)[Vitória/ES](#Vit%C3%B3ria/ES)

| Cidades |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

 

### 
**Alfredo Chaves/ES**

O município de Alfredo Chaves/ES utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- 
**Cadastros Básicos**

  - 
[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **3200300**.

  - 
****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a "Inscrição Municipal" da sua empresa está devidamente preenchida.

- 
**Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

  - 
**Código de Serviço Municipal:** preencha o campo "Cód. Trib. Município" com a formatação exigida pela prefeitura. Exemplo: **140101**.

  - 
**Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o** ****"Código CNAE"** (ex: 4520001) e o** ****"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

- 
**Configuração para IBS e CBS (Reforma Tributária)** Para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:

  - 
**Cadastro de** [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)**:** na [aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), [seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.

  - 
****[Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**:** na [aba Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF) da TOP, certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.

- 
**Regras de Emissão e Particularidades**

  - 
**Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](#top)

### **Anchieta/ES**

Os seguintes cadastros estão envolvidos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533050864151)

 Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de **Anchieta**, sendo este 3200409 e o **"Cód. município SIAFI"** 5607.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533051501463)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e defina no campo **"Regime esp. trib. ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533051505687)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

********

| Código | Descrição |
| --- | --- |
| 1 | Exigível |
| 2 | Não incidência |
| 3 | Isenção |
| 4 | Exportação |
| 5 | Imunidade |
| 6 | Exigibilidade suspensa por decisão judicial |
| 7 | Exigibilidade suspensa por procedimento administrativo |

####  

#### **Cancelamento**

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

********

| Código | Descrição |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

 

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

Esta prefeitura permitirá a [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

**

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27653944523159)

 Informações adicionais acerca da Emissão de NFS-e no município de Anchieta:**

- Nesta prefeitura, ao realizar a emissão de NFSe com tomador do exterior ou ISS retido, o sistema emitirá a nota sem erros;

- 
Para emitir uma nota fiscal com variados cadastros de serviços, habilite a marcação **"Enviar itens de NFSe separados no JSON"** no cadastro de [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e);

- 
Caso queira cadastrar o envio da nota para mais de um e-mail, preencha o campo** "E-mail específico p/ envio NFSe"** na aba [NF-e/NFS-e/CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e), no cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) e habilite a marcação** "Envia múltiplos e-mails no JSON"** no cadastro de Cidades, aba NFS-e;

- 
Será possível, ainda, calcular a redução do imposto no cálculo automaticamente, basta que o campo **"Tipo de dedução de base do ISS"** da aba [Alíquota de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss), do cadastro de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), esteja definida com a opção** "Materiais"** e o campo** "Percentual de ISS"** possua o valor a ser deduzido.

[[voltar ao topo]](#top)

### 
**Aracruz/ES**

O sistema encontra-se apto para emitir NFS-e para o município de Aracruz.

**Observação:** a cidade suporta o cancelamento e a [Substituição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
**Cariacica/ES**

O sistema encontra-se apto para emitir NFS-e para o município de Cariacica.

**Observação:** a cidade não suporta o cancelamento de nota de serviço via webservice, este deverá ser feito diretamente na prefeitura.

[[voltar ao topo]](#top)

### 
**Colatina/ES**

O sistema encontra-se apto para emitir NFS-e para o município de Colatina.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### ****

### **Guarapari/ES**

O município de Guarapari/ES utiliza o **Emissor Nacional** (Portal Nacional) para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- 
**Cadastros Básicos**

  - 
[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal" **com o código IBGE **3202405**.

  - 
****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a** "Inscrição Municipal"** e o **"Cód. Regime Tribut." **(ex: Lucro Presumido) da sua empresa estão devidamente preenchidos.

- 
**Série e Numeração (Exigência de 5 dígitos)** Por utilizar o Portal Nacional, a prefeitura exige que a série da nota tenha exatamente 5 caracteres. Configure da seguinte forma:

  - 
**Preferências da Empresa:** (Caminho: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)) preencha o **"Prefixo Série NFS-e Padrão Nacional"** com 2 dígitos, usando números de **00 a 49**.

  - 
****[TOP (Tipos de Operação)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top)**:** (Caminho: botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)) configure a **"Série Padrão Nacional" **com 3 dígitos (ex: de **001 a 999**) e ative a numeração automática.

- 
**Configurações do Serviço:** acesse o cadastro de ****[Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas[Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

  - 

**Código de Serviço Municipal:** o Portal Nacional exige um formato específico. Adicione o dígito "01" ao final do código original do serviço. 

Exemplo: se o serviço for *14.01*, preencha como **14.01.01**.

- 
**Preenchimento obrigatório:** não esqueça de informar o** "Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE"** (ex: 47.89-0-99) e o** "Código NBS" **(ex: 120011000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

- 
**Regras de Emissão e Particularidades**

  - 
**Ative o Padrão Nacional:** lembre-se de ativar a marcação****["Emitir NFS-e Padrão Nacional"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#:~:text=%22Emitir%20NFS%2De%20Padr%C3%A3o%20Nacional%22%2C) nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

  - 
**Múltiplos Itens e E-mails:** para incluir vários serviços diferentes na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no [cadastro da Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades).

  - 
**Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com ISS retido e para clientes do exterior normalmente (mediante preenchimento correto do endereço estrangeiro do tomador).

  - 
**Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros.

  - 
**Atenção às Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40% de dedução) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem esse amparo legal resultarão em rejeição pelo portal.

[[voltar ao topo]](#top)

### **Ibiraçu/ES**

O sistema encontra-se apto para emitir NFS-e para o município de Ibiraçu.

**Observação:** a cidade suporta o cancelamento de nota de serviço e [substituição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

[[voltar ao topo]](#top)

### **João Neiva/ES**

Os seguintes cadastros estão envolvidos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533050864151)

 Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de João Neiva, sendo este 3203130 e o **"Cód. município SIAFI"** 5721.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533051501463)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e  defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 0 | Tributação Normal |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |
| 7 | Autônomo |
| 8 | Média Empresa |
| 9 | Grande Empresa |
| 10 | Empresa Individual de Responsabilidade Limitada (EIRELI) |

 

Configure os campos **"Usuário NFS-e"** e **"Senha NFS-e"** de acordo com os dados cadastrados na prefeitura no momento da autorização da emissão de NFS-e. Lembrando que, os dados informados nestes campos são diferentes do usuário e senha utilizados para acessar o ambiente da prefeitura.

#### **Cancelamento**

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

********

| Código | Descrição |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

 

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

[[voltar ao topo]](#top)

### 
**Linhares/ES**

O sistema encontra-se apto para emitir NFS-e para o município de Linhares.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
**Pinheiros/ES**

O município de Pinheiros/ES utiliza o **Emissor Nacional** (Portal Nacional) para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

**Cadastros Básicos**

- 
****[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o** "Mun. domicílio fiscal"** com o código IBGE **3204104**.

- 
**Empresas:** confirme se a **"Inscrição Municipal" **e o** "Cód. Regime Tribut."** (ex: Lucro Presumido) da sua empresa estão devidamente preenchidos.

**Série e Numeração (Exigência de 5 dígitos):** Por utilizar o Portal Nacional, a prefeitura exige que a série da nota tenha exatamente 5 caracteres. Configure da seguinte forma:

- 
**Preferências da Empresa:** (Caminho: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)) preencha o **"Prefixo Série NFS-e Padrão Nacional" **com 2 dígitos, usando números de **00 a 49**.

- 
**TOP (Tipos de Operação):** (Caminho: botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)) configure a **"Série Padrão Nacional"** com 3 dígitos (ex: de **001 a 999**) e ative a numeração automática.

**Configurações do Serviço:** Acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

- 
**Código de Serviço Municipal:** o Portal Nacional exige um formato específico. Adicione o dígito "01" ao final do código original do serviço. Exemplo: se o serviço for *14.01*, preencha como **14.01.01**.

- 
**Preenchimento obrigatório:** não esqueça de informar o **"Código de Tributação Municipal"** (ex: 14.01.01.001), o **"Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE" **(ex: 47890990) e o **"Código NBS"** (ex: 120011000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

**Regras de Emissão e Particularidades**

- 
**Ative o Padrão Nacional:** lembre-se de ativar a marcação **"Emitir NFS-e Padrão Nacional"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

- 
**Múltiplos Itens e E-mails:** para incluir vários serviços diferentes na mesma nota ou enviar o documento para diversos e**-mails, ative as opções "Enviar itens de NFSe separados no Json" e** "Enviar múltiplos e-mails no Json" no [cadastro da Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades).

- 
**Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com ISS retido e para clientes do exterior normalmente (mediante preenchimento correto do endereço estrangeiro do tomador).

- 
**Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros.

- 
**Atenção às Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40% de dedução) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem esse amparo legal resultarão em rejeição pelo portal.

[[voltar ao topo]](#top)

### 
******Serra/ES**

A emissão de NFS-e pode ser realizada via API para o município de Serra. Para isso, basta configurar o código IBGE do município no parâmetro **"Utilizar emissão NFS-e SMARAPD pelo Broker? - NFSSMARAPDBROKR"**. Caso não esteja configurado, a emissão será realizada via Sankhya (nativo) conforme o cadastro descrito abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533050864151)

 Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Serra, sendo este 3205002 e o **"Cód. município SIAFI"** 5699.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533051501463)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e   defina no campo **"Regime esp. trib. ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |

 

Ainda nesta aba, configure os campos **"Usuário NFS-e"** e **"Senha NFS-e"** de acordo com os dados cadastrados na prefeitura no momento da autorização da emissão de NFS-e. Lembrando que, os dados informados nestes campos são diferentes do usuário e senha utilizados para acessar o ambiente da prefeitura.

A marcação **"Considera valor líquido para NFSe?"** deve estar acionada para que o desconto informado nos itens seja considerado no valor do serviço enviado para prefeitura.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533051505687)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

********

| Código | Descrição |
| --- | --- |
| 1 | Exigível |
| 2 | Não incidência |
| 3 | Isenção |
| 4 | Exportação |
| 5 | Imunidade |
| 6 | Exigibilidade suspensa por decisão judicial |
| 7 | Exigibilidade suspensa por procedimento administrativo |

 

**Observação:** a cidade suporta o cancelamento de nota de serviço e [substituição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

#### **Cancelamento**

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

********

| Código | Descrição |
| --- | --- |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

[[voltar ao topo]](#top)

### 
**Viana/ES**

Os seguintes cadastros estão envolvidos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533050864151)

 Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Viana, sendo este 3205101 e o **"Cód. município SIAFI"** 5701.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533051501463)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e  defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 0 | Tributação Normal |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |
| 7 | Autônomo |
| 8 | Média Empresa |
| 9 | Grande Empresa |
| 10 | Empresa Individual de Responsabilidade Limitada (EIRELI) |

 

Configure os campos **"Usuário NFS-e"** e **"Senha NFS-e"** de acordo com os dados cadastrados na prefeitura no momento da autorização da emissão de NFS-e. Lembrando que, os dados informados nestes campos são diferentes do usuário e senha utilizados para acessar o ambiente da prefeitura.

#### **Cancelamento**

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

********

| Código | Descrição |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

 

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

[[voltar ao topo]](#top)

### 
******Vila Velha/ES**

O sistema encontra-se apto para emitir NFS-e para o município de Vila Velha.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Vitória/ES**

Os seguintes cadastros estão envolvidos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533050864151)

 Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Vitória, sendo este 3205309 e o **"Cód. município SIAFI"** 5705.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22533051501463)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

********

| Código | Descrição |
| --- | --- |
| 1 | Exigível |
| 2 | Não incidência |
| 3 | Isenção |
| 5 | Imunidade |
| 6 | Exigibilidade suspensa por decisão judicial |
| 7 | Exigibilidade suspensa por procedimento administrativo |

 

**Nota:**** **esta prefeitura permitirá a [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

**

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27653944523159)

 Informações adicionais acerca da emissão de NFS-e no município de Vitória/ES: **

No campo **"Desconto Condicionado para NFS-e"**, disponível na aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) do cadastro do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), é possível configurar quais descontos aplicados no documento serão tratados como desconto condicionado no XML da NFS-e. Nele será possível selecionar uma das seguintes opções:

- 

Não usa;

- 

Financeiro;

- 

Nota;

- 

Ambos;

Dessa forma, o valor do desconto informado no campo configurado será tratado como desconto condicionado e registrado na tag** <DescontoCondicionado>** do XML.

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/27653938430743)

 Caso o documento tenha alguma redução na base de cálculo do ISS, o valor do desconto condicionado não será considerado no preenchimento dos valores de deduções na tag **<ValorDeducoes>**, logo, o valor registrado na tag **<DescontoCondicionado>** será tratado de forma independente e não interferirá na composição dos valores de dedução na tag <ValorDeducoes>.

Além disso, quando a base de cálculo do ISS for reduzida em 100%, a tag **<ValorDeducoes>** será composta exclusivamente pelos valores referentes à redução da base de cálculo, sem incluir outros elementos. Essa separação assegura precisão no cálculo dos tributos e conformidade com as normas fiscais aplicáveis.

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/27653938430743)

 Lembre-se que para o município de Vitória/ES não é possível utilizar a opção **"Financeiro"**, se a utilizar a seguinte mensagem surgirá:

***"A opção "Desconto Condicionado para NFS-e" na TOP está disponível para o município de Belo Horizonte - MG e João Pessoa - PB exclusivamente quando configurada como "Financeiro".***

***Código: CORE_E00577"***

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27654036900247)

 Para saber mais sobre essa opção acesse o artigo: Tipo de Operações - TOP, aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse).

#### **Cancelamento**

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

********

| Código | Descrição |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

 

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

**Observação:** a emissão da NFS-e, no cabeçalho da nota é possível preencher o campo **"Cidade de Prestação do Serviço"** para indicar a cidade em que o serviço foi prestado.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos)
- [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)
- [aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF)
- [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse)
- [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e)
- [NF-e/NFS-e/CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e)
- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...)
- [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)
- ["Emitir NFS-e Padrão Nacional"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#:~:text=%22Emitir%20NFS%2De%20Padr%C3%A3o%20Nacional%22%2C)