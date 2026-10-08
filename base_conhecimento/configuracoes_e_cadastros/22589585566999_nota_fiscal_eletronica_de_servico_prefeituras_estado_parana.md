# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Paraná

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/22589585566999-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Paran%C3%A1](https://ajuda.sankhya.com.br/hc/pt-br/articles/22589585566999-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Paran%C3%A1)  
> **ID:** `22589585566999` | **Última Atualização:** 2026-07-29T13:41:44Z

---

Neste artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Paraná, para conhecê-las acesse os links abaixo:

#### ****

[Alto Paraná/PR](#h_01KPTGVFFZG74J968XBKTXMW9Z)[Maringá/PR](#maringpr)

[Apucarana/PR](#apucarana/pr)[Matinhos/PR](#h_01H98JRWH6K35EE7CYM83VBZRV)

[Araucária/PR](#Arauc%C3%A1ria/PR)[Nova Esperança/PR](#h_01H98JRWH6K35EE7CYM83VBZRV)

[Campina Grande do Sul/PR](#CampinaGrandedoSul/PR)[Palmas/PR](#Palmas/PR)

[Campo Largo/PR](#CampoLargo/PR)[Paranaguá/PR](#Paranagu%C3%A1/PR)

[Campo Mourão/PR](#campomourao/pr)[Pato Branco/PR](#patobranco/pr)

[Cascavel/PR](#cascavel/pr)[Pinhais/PR](#pinhais/pr)

[Cianorte/PR](#cianortepr)[Planalto/PR](#planaltopr)

[Cidade de Castro/PR](#cidadedecastro/pr)[Ponta Grossa/PR](#pontagrossapr)

[Cidade Gaúcha/PR](#h_01H98JRWH61JM1BEDX25PJ2XAW)[Rio Branco do Sul/PR](#RioBrancodoSul/PR)

[Colombo/PR](#Colombo/PR)[Rio Negro/PR](#rionegro/pr)

[Cornélio Procópio/PR](#Corn%C3%A9lioProc%C3%B3pio/PR)[Santo Antônio da Platina/PR](#SantoAnt%C3%B4niodaPlatina/PR)

[Curitiba/PR](#curitibapr)[São José dos Pinhais/PR](#s%C3%A3ojos%C3%A9dospinhais/pr)

[Fazenda Rio Grande/PR](#FazendaRioGrande-PR)[Sarandi/PR](#sarandi/pr)

[Floresta/PR](#h_01H98JRWH6M7AVWEYZKGAX2KK8)[Tamboara/PR](#01J6WAQV39P105J4WCATHP72EK)

[Francisco Beltrão/PR](#franciscobeltr%C3%A3o/pr)[Toledo/PR](#toledo/pr)

[Itaperuçu/PR](#Itaperu%C3%A7u/PR)[Umuarama/PR](#Umuarama/PR)

[Ivaiporã/PR](#ivaipor%C3%A3/pr)[União da Vitória/PR](#Uni%C3%A3odaVit%C3%B3ria/PR)

[Lapa/PR](#Lapa/pr)[#londrinapr](#londrinapr)[Varginha/PR](#varginha/pr)

[Londrina/PR](#londrinapr)[Wenceslau Braz/PR](#WenceslauBraz/pr)

[Marechal Cândido Randon/PR](#marechalc%C3%A2ndidorandon/pr)[Parâmetros que influenciam nesta rotina](#parametrosqueinfluenciamnestarotina)

| Cidades |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

### **Alto Paraná/PR**

O município de Alto Paraná/PR utiliza o **Emissor Nacional** (Portal Nacional) para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- 
**Cadastros Básicos**

  - 
****[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **4100608**.

  - 
**Empresas:** confirme se a "Inscrição Municipal" e o "Cód. Regime Tribut." (ex: Lucro Presumido) da sua empresa estão devidamente preenchidos.

- 
**Série e Numeração (Exigência de 5 dígitos)** Por utilizar o Portal Nacional, a prefeitura exige que a série da nota tenha exatamente 5 caracteres. Configure da seguinte forma:

  - 
**Preferências da Empresa:** (Caminho: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)) preencha o** "Prefixo Série NFS-e Padrão Nacional"** com 2 dígitos, usando números de **00 a 49**.

  - 
**TOP (Tipos de Operação):** (Caminho: botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)) configure a **"Série Padrão Nacional"** com 3 dígitos (ex: de **001 a 999**) e ative a numeração automática.

- 
**Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

  - 
**Código de Serviço Municipal:** o Portal Nacional exige um formato específico. Adicione o dígito **"01" **ao final do código original do serviço. Exemplo: se o serviço for *14.01*, preencha como **14.01.01**.

  - 
**Preenchimento obrigatório:** não esqueça de informar o **"Código de Tributação Municipal"** (ex: 14.01.01.001), o **"Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE"** (ex: 47890990) e o **"Código NBS"** (ex: 120011000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

- 
**Regras de Emissão e Particularidades**

  - 
**Ative o Padrão Nacional:** lembre-se de ativar a marcação **"Emitir NFS-e Padrão Nacional"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

  - 
**Múltiplos Itens e E-mails:** para incluir vários serviços diferentes na mesma nota ou enviar o documento para diversos e-mails, ative as opções** "Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no [cadastro da Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades).

  - 
**Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com ISS retido e para clientes do exterior normalmente (mediante preenchimento correto do endereço estrangeiro do tomador).

  - 
**Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros.

  - 
**Atenção às Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40% de dedução) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem esse amparo legal resultarão em rejeição pelo portal.

[[voltar ao topo]](#top)

### 
******Apucarana/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Apucarana.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Araucária/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Araucária.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Campina Grande do Sul/PR**

Os seguintes cadastros estão envolvidos:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Campina Grande do Sul, sendo este 1200401 e o **"Cód. município SIAFI"** 1390.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

 **Ainda na tela Cidades, aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e), será possível gerar a tag CNAE em cada item dos metadados do JSON para uma NFS-e com múltiplos itens. Para isso, ative a marcação **"Enviar itens de NFS-e separados no JSON"** e, em seguida, habilite a marcação **"Gerar CNAE para múltiplos itens no JSON"**.

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 **Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

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

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22675458190487)

 **No cadastro de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), informe no campo **"Cód. Trib. Município NFS-e"** o código de tributação no município disponibilizado pela prefeitura.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24157317012503)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e defina no campo **"Regime esp. tributação ISS (NFS-e)" **o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas: 

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |
| 7 | Optante pelo Simples Nacional |

 

**Nota: **esta prefeitura permitirá a [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

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

### **Campo Largo/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Campo Largo.

**Observação:** a cidade suporta o cancelamento e [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

[[voltar ao topo]](#top)

### 
******Campo Mourão/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Campo Mourão.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### **Cascavel/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Cascavel.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Cianorte/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Cianorte.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Cidade de Castro/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Cidade de Castro.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Cidade Gaúcha/PR**

O município de Cidade Gaúcha/PR utiliza o **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- 
**Cadastros Básicos**

  - 
****[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **4105607**.

  - 
****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.

- 
**Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

  - 
**Código de Serviço Municipal:** preencha o campo** "Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.

  - 
**Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)" **(ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

- 
**Regras de Emissão e Particularidades**

  - 
**Múltiplos Itens e E-mails:** para incluir vários serviços na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json" **e **"Enviar múltiplos e-mails no Json" **no cadastro da [Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral).

[[voltar ao topo]](#top)

### 
******Colombo/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Colombo.

**Observação:** a cidade suporta o cancelamento e [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

[[voltar ao topo]](#top)

### 
******Cornélio Procópio/PR**

Os seguintes cadastros estão envolvidos:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Cornélio Procópio, sendo este 4106407 e o **"Cód. município SIAFI"** 7525.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

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

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Geral) e defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |

 

**Observação:** a cidade suporta o cancelamento e a [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

[[voltar ao topo]](#top)

### 
******Curitiba/PR**

**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/37961899520279)

 A partir de 2026, o município passa a utilizar o Emissor Nacional de NFS-e.**

A emissão de NFS-e para o município de **Curitiba** poderá ser realizada via **API**, desde que seja ativado o parâmetro **“Utilizar emissor NFS-e em Curitiba pelo Broker? – NFSECURITBROKER”**.

Este parâmetro é **indispensável** para garantir a conformidade das emissões:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Curitiba, sendo este 4106902 e o **"Cód. município SIAFI"** 7535.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

 Série e Numeração das Notas**

O **Portal Nacional** exige que, para emissões via **webservice**, a série da NFS-e possua **5 caracteres**.

1. 

##### Configuração da Série

Acesse: **Preferências » ******[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)** » ******[Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)** » ******[NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e)** » ******[Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Geral)

- Configure o campo **“Prefixo Série NFS-e Padrão Nacional”** com **2 dígitos**, respeitando o intervalo de **00 a 49**.

#####    2. Configuração da Numeração

Acesse: **Comercial » Arquivo » Cadastros » ******[Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)

Na opção ****[Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...), localize ****[Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao) e configure:

- 
**Série – Padrão Nacional:** valor numérico entre **001 e 999**

- 
**Numeração da NFS-e:** conforme a política da empresa

**Recomendação:** utilizar **numeração automática**, como boa prática de controle fiscal.

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 Configurações do Serviço**

Acesse: **Configurações » Cadastros » ******[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)** » ******[Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)

Nas abas ****[Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), ****[Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss) e ****[Configuração por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa), conforme o cenário adotado pela empresa, revise principalmente os seguintes campos:

##### Código de Serviço Municipal

- Exemplo: para o serviço que anteriormente utilizava o código **01.02** na lista municipal, o novo código esperado será ****[01.02.01.001](http://1.2.1.1/).

##### Regra Geral

- No **Portal Nacional**, o campo deve ser preenchido com o **item da lista de serviços acrescido do dígito “01”** ao final.

- Em alguns municípios, também é exigido o complemento **“001”** como **código complementar nacional**.

- Consulte a documentação específica do município para validar o padrão exigido.

##### Código NBS

- Preencha com o **Código NBS (Nomenclatura Brasileira de Serviços)** correspondente ao serviço prestado, conforme a ****[tabela oficial da Nomenclatura Brasileira de Serviços](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/anexoviii-correlacaoitemnbsindopcclasstrib_ibscbs_v1-00-00.xlsx/@@download/file).

**Nota: **o município de **Curitiba** permitirá a **substituição de NFS-e via webservice**.

[[voltar ao topo]](#top) 

### 
******Floresta/PR**

Os seguintes cadastros estão envolvidos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o** "Mun. domicílio fiscal"** de Floresta, sendo este 4107900 e o **"Cód. município SIAFI" **74250.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

********

| Código | Descrição |
| --- | --- |
| 1 | Exigível |
| 2 | Não incidência |
| 3 | Isenção |
| 5 | Imunidade |
| 6 | Exigibilidade suspensa por decisão judicial |
| 7 | Exigibilidade suspensa por procedimento administrativo |

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e  defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 0 | Normal/Nenhum |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22675458190487)

 No cadastro de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), informe o** “Tipo de Serviço” **e preencha o campo **“Cód. Trib. Município NFS-e” **com o código de tributação fornecido pela prefeitura. Em seguida, insira no campo** “CNAE” **o código correspondente ao município, aqui utilize apenas números, sem pontos ou outros caracteres.

Consulte a legislação municipal ou o contador responsável para confirmar se o tipo de serviço e o CNAE estão corretos para a atividade da sua empresa.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

**

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26407189299991)

 Informações adicionais acerca da Emissão de NFS-e no município de Floresta:**

- 

Nesta prefeitura, ao realizar a emissão de NFSe com tomador do exterior ou ISS retido, o sistema emitirá a nota sem erros;

- 
Para emitir uma nota fiscal com variados cadastros de serviços, habilite a marcação **"Enviar itens de NFSe separados no JSON"** no cadastro de[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba[NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e);

- 
Caso queira cadastrar o envio da nota para mais de um e-mail, preencha o campo** "E-mail específico p/ envio NFSe"** na aba[NF-e/NFS-e/CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e), no cadastro de[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) e habilite a marcação** "Envia múltiplos e-mails no JSON"** no cadastro de Cidades, aba NFS-e;

[[voltar ao topo]](#top) 

### 
******Francisco Beltrão/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Francisco Beltrão.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top) 

### **Itaperuçu/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Itaperuçu.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top) 

### **Ivaiporã/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Ivaiporã.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Lapa/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Lapa.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top) 

### 
******Londrina/PR**

Os seguintes cadastros estão envolvidos:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Londrina, sendo este 4113700 e o **"Cód. município SIAFI"** 7667.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e  configure os campos **"Usuário NFS-e"** e **"Senha NFS-e"** de acordo com os dados cadastrados na prefeitura no momento da autorização da emissão de NFS-e. Lembrando que, os dados informados nestes campos são diferentes do usuário e senha utilizados para acessar o ambiente da prefeitura.  Informe também a frase de segurança fornecida pela Prefeitura.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse), para configurar o campo **"Cód. Natureza Oper. ISS (NFS-e)"**, deve-se atentar aos seguintes pontos:

- 

Para flexibilizar o cadastro de novas naturezas de operação no momento da implantação de novos provedores de NFS-e e novos municípios, foi criada a aba [Natureza da Operação ISS/Município](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanaturezadaoperaoissmunicpio) no cadastro de [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top);

- 

Esta aba somente estará disponível se o parâmetro **"Utilizar Cód. Nat. Operação ISS por Top/Empresa - NATOPEISSTOPEMP"** estiver habilitado;

- 

Deve-se incluir a empresa relacionada a emissão das notas e a natureza da operação relacionada ao município de domicílio fiscal da cidade em que a empresa se encontra.

**Nota:** com o parâmetro NATOPEISSTOPEMP ativado, o campo Cód. Natureza Oper. ISS (NFS-e) da aba NFS-e será retirado do cadastro de Tipos de Operação - TOP. A configuração desta aba evita a criação de uma TOP para cada empresa que tenha uma natureza de operação diferente; com este formato a mesma TOP pode ser utilizada por empresas que tenham naturezas diferentes.

**Observação:** para o cadastro de natureza da operação, os registros deverão ser incluídos via script ('SCRIPT_NATUREZAS_OPERACAO_ISS') do banco de dados na tabela TGFNAS.

#### **Cancelamento**

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

********

| Código | Descrição |
| --- | --- |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

[[voltar ao topo]](#top)

### 
******Marechal Cândido Randon/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Marechal Cândido Randon.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Maringá/PR**

Os seguintes cadastros estão envolvidos:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Maringá, sendo este 4115200 e o **"Cód. município SIAFI"** 7691.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

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
******Matinhos/PR**

O município de Matinhos/PR utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (IBS e CBS). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- 
**Cadastros Básicos**

  - 
****[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **4115705**.

  - 
****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.

- 
**Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

  - 
**Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município" **com a formatação exigida pela prefeitura. Exemplo: **140101**.

  - 
**Preenchimento obrigatório:** não esqueça de informar o** "Item da Lista de Serviços (LC 116)" **(ex: 1401), o **"Código CNAE"** (ex: 4763605) e o **"Código NBS" **(ex: 120013300, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

- 
**Configuração para IBS e CBS (Reforma Tributária):** para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:

  - 
**Cadastro de** [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)**:** na [aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), [seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.

  - 
****[Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**:** na [aba Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF) da TOP, certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.

- 
**Regras de Emissão e Particularidades**

  - 
**Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros, atualizando o status automaticamente no portal da prefeitura.

  - 
**Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com retenção de ISS e para clientes do exterior normalmente (mediante preenchimento correto do endereço do tomador).

  - 
**Múltiplos Itens e E-mails:** para incluir vários serviços na mesma nota ou enviar o documento para diversos e-mails, ative as opções** "Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json" **no cadastro da [Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral).

  - 
**Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](#top)

### 
******Nova Esperança/PR**

O município de Nova Esperança/PR utiliza o **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- 
**Cadastros Básicos**

  - 
****[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **4116901**.

  - 
****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a **"Inscrição Municipal" **da sua empresa está devidamente preenchida.

- 
**Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

  - 
**Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.

  - 
**Preenchimento obrigatório:** não esqueça de informar o** "Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS" **(ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

- 
**Regras de Emissão e Particularidades**

  - 
**Múltiplos Itens e E-mails:** para incluir vários serviços na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no cadastro da [Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral).

[[voltar ao topo]](#top)

### 
******Palmas/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Palmas.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### **Paranaguá/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Paranaguá.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Pato Branco/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Pato Branco.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Pinhais/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Pinhais.

Este municipio suporta o cancelamento de nota de serviço via webservice.

**Observações:**

- 

Configure o campo **"Cod. Trib. Município"** da tela [Alíquota de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS#abageral) com o código de tributação contendo 6 dígitos, apresentado na [Lista de serviço](https://nfe.sjp.pr.gov.br/servicos/issOnline2/atividades.php) do município.

  - 

exemplo: 010501

- 

Configure o **“Tipo serviço**” para corresponder ao item da Lista de serviço sem pontuação

  - 

exemplo: 0105

- 

Configure o campo “**CNAE”** contendo 7 dígitos

[[voltar ao topo]](#top)

### 
******Planalto/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Planalto.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Ponta Grossa/PR**

Os seguintes cadastros estão envolvidos:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Ponta Grossa, sendo este 4119905 e o **"Cód. município SIAFI"** 7777.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

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

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e  defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |
| 7 | Optante pelo Simples Nacional |

[[voltar ao topo]](#top)

### 
******Rio Branco do Sul/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Rio Branco do Sul.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice, mas não suporta a substituição.

**

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26407189299991)

 Informações adicionais acerca do "Regime Especial de Tributação"**

Para que o regime especial de tributação seja enviado na NFS-e, habilite a marcação **"Enviar o Regime Especial de Tributação no json?"** na aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e) da tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), assim para gerar automaticamente cada código de regime especial, o sistema fará as seguintes validações:

********

[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)[Documentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)[Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)[NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e)[Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)********

[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)[Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)****

[Alíquota de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS)[Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS#abageral)************

********

****

****

************

****

****

****

****

********

****************

********

********

[Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)[Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos)************

********

****

[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)[Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)************

| Validação | Código |
| --- | --- |
| Se na tela , aba        , sub-aba  > ,   o campo "ISS" estiver igual a "Tributado";  Na tela , aba , a marcação     "Retém ISS" estiver desabilitada;  Na tela , aba , o         campo "Cód. Tributação ISS" estiver com     a opção "00 - Tributado". | "0 - Tributada Integralmente" |
| Se na tela Empresa, aba Documentos     Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver igual a Tributado;  Em Parceiros, aba Fiscal, a marcação         Retém ISS estiver habilitada;  Na tela Alíquota de ISS, aba Geral, o campo   Cód. Tributação ISS estiver igual a "01 -   Tributado com ISS Retido". | "1 - Tributada Integralmente com ISSRF" |
| Se na tela Empresa, aba Documentos       Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver igual a Tributado;  Na tela Parceiros, aba Fiscal, a marcação     Retém ISS estiver desabilitada, mas a         marcação "Substituto Tributário - ISS",       habilitada;  Na tela Alíquota de ISS, aba Geral, o campo   Cód. Tributação ISS estiver igual a                 00 - Tributado. | "2 - Tributada Integralmente e sujeita à        Substituição Tributária" |
| Se na tela Empresa, aba Documentos       Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver igual a Tributado;  Na tela Parceiros, aba Fiscal, a marcação     Retém ISS estiver desativada;  Na tela Alíquota de ISS, aba Geral, o campo   Cód. Tributação ISS estiver igual a                 00 - Tributado e os campos "Perc.                     de dedução na base do ISS" e "Tipo           de dedução de base do ISS" preenchidos. | "3 - Tributada com redução da base de          cálculo" |
| Se na tela Empresa, aba Documentos       Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver igual a Tributado;  Na tela Parceiros, aba Fiscal, as marcações   Retém ISS e "Orgão público                       (NFS-e)" estiverem habilitadas;  Na tela Alíquota de ISS, aba Geral, o campo   Cód. Tributação ISS estiver igual a                   01 - Tributado com ISS Retido e                     os campos Perc. de dedução na base             do ISS e Tipo de dedução de base                 do ISS, preenchidos. | "4 - Tributada com redução da base de           cálculo com ISSRF" |
| Se na tela Empresa, aba Documentos       Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o  campo ISS estiver igual a Tributado;  Na tela Parceiros, aba Fiscal, as marcações:   Retém ISS, desabilitada e a                 marcação "Substituto Tributário - ISS",       habilitada;  Na tela Alíquota de ISS, aba Geral, o campo   Cód. Tributação ISS estiver igual a                 00 - Tributado, e os campos Perc.                 de dedução na base do ISS e Tipo                 de dedução de base do ISS preenchidos. | "5 - Tributada com redução da base de          cálculo e sujeita à Substituição                        Tributária" |
| Se na tela Empresa, aba Documentos      Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver com a opção "Isento"     selecionada. | "6 - Isenta" |
| Se na tela Empresa, aba Documentos     Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o  campo ISS estiver igual a                               "Não - Tributado" e o campo "Regime esp.   tributação ISS (NFS-e)", com a opção           "F - Imune" indicada. | "7 - Imune" |
| Se na tela Empresa, aba Documentos        Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver com a opção Não -   Tributado selecionada e o campo             Regime esp. tributação ISS (NFS-e), igual       a "G - Tributável Fixo". | "8 - Não Tributada - ISS regimo Fixo" |
| Se na tela Empresa, aba Documentos       Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver igual a Não - Tributado   e o campo Regime esp. tributação ISS           (NFS-e) estiver indicado com a opção             "2 - Estimativa". | "9 - Não Tributada - ISS regime                           estimativa" |
| Se na tela Empresa, aba Documentos         Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver igual a Não - Tributado;  No , aba ,         o campo "Classificação Cessão M. d. Obra"   estiver como "Construção Civil". | "10 - Não Tributada - ISS Construção Civil      recolhido antecipadamente" |
| Se na tela Empresa, aba Documentos         Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver com a opção Não -       Tributado selecionada e o campo Regime     esp. tributação ISS (NFS-e) estiver igual a     "N - Não Tributável". | "14 - Não Tributada" |
| Se na tela Empresa, aba Documentos       Fiscais Eletrônicos, sub-aba NFS-e > Geral,   o campo ISS estiver igual a Não - Tributado   e o campo Regime esp. tributação ISS           (NFS-e) estiver com a opção "N -                       Não Tributável" indicada;  Na tela , aba , o campo   "Natureza da Retenção na Fonte" estiver       preenchido com a opção "04 -     Recolhimento por Sociedade Cooperativa". | "15 - Não Tributada - Ato cooperado" |

 

**Nota:** com a marcação Enviar o Regime Especial de Tributação no json? desabilitada, o metadados **"regimeEspecialTributacao"** não será enviado no json.

[[voltar ao topo]](#top)

### 
******Rio Negro/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Rio Negro.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo](#top)

### 
**Santo Antônio da Platina/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Santo Antônio da Platina.

**Observação:** a cidade suporta o cancelamento e [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

[[voltar ao topo]](#top)

### 
******São José dos Pinhais/PR**

O sistema encontra-se apto para emitir NFS-e para o município de São José dos Pinhais.

**Observações:**

- 

Configure o campo **"Cod. Trib. Município"** da tela [Alíquota de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS#abageral) com o código de tributação contendo 9 dígitos, apresentado na [Lista de Atividade](https://nfe.sjp.pr.gov.br/servicos/issOnline2/atividades.php) do município São José dos Pinhais.

- 

A cidade não suporta o cancelamento de nota de serviço via web-service, este deverá ser feito diretamente na prefeitura.

- 

No [Cadastro de Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e), configure o campo **"Tipo de cancelamento para NFS-e"** com a opção **"Via prefeitura sem número de protocolo"**.

[[voltar ao topo]](#top)

### 
******Sarandi/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Sarandi.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Tamboara/PR**

O município de Tamboara/PR utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- 
**Cadastros Básicos**

  - 
[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o** "Mun. domicílio fiscal" **com o código IBGE **4126702**.

  - 
****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a **"Inscrição Municipal" **da sua empresa está devidamente preenchida.

- 
**Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

  - 
**Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.

  - 
**Preenchimento obrigatório:** não esqueça de informar o  **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o** ****"Código CNAE"** (ex: 4520001) e o** ****"Código NBS" **(ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

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

### 
******Toledo/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Toledo.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### 
******Umuarama/PR**

Os seguintes cadastros estão envolvidos:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Umuarama, sendo este 4128104 e o **"Cód. município SIAFI"** 7935.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

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

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e  defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |

 

**Observação: **a cidade não suporta o cancelamento e [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

[[voltar ao topo]](#top)

### 
******União da Vitória/PR**

Os seguintes cadastros estão envolvidos:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589677429655)

 **Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de União da Vitória, sendo este 4128203 e o **"Cód. município SIAFI"** 7937.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589758007191)

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

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22589818666647)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e  defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |

 

**Observação:** a cidade suporta o cancelamento e [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

### **Varginha/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Varginha.

[[voltar ao topo]](#top)

### 
******Wenceslau Braz/PR**

O sistema encontra-se apto para emitir NFS-e para o município de Wenceslau Braz.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)
- [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...)
- [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)
- [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos)
- [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)
- [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse)
- [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)
- [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Geral)
- [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)
- [Configuração por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa)
- [NF-e/NFS-e/CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e)
- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Natureza da Operação ISS/Município](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanaturezadaoperaoissmunicpio)
- [aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF)
- [Alíquota de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS#abageral)
- [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)