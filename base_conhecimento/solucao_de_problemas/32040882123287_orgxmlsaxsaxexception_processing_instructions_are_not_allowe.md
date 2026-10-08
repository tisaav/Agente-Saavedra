# org.xml.sax.SAXException: Processing instructions are not allowed within SOAP messages. Esse erro pode ter ocorrido por falta de conexão com a Internet

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32040882123287-org-xml-sax-SAXException-Processing-instructions-are-not-allowed-within-SOAP-messages-Esse-erro-pode-ter-ocorrido-por-falta-de-conex%C3%A3o-com-a-Internet](https://ajuda.sankhya.com.br/hc/pt-br/articles/32040882123287-org-xml-sax-SAXException-Processing-instructions-are-not-allowed-within-SOAP-messages-Esse-erro-pode-ter-ocorrido-por-falta-de-conex%C3%A3o-com-a-Internet)  
> **ID:** `32040882123287` | **Última Atualização:** 2026-09-16T14:26:18Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/32040839999895)

**MENSAGEM**

org.xml.sax.SAXException: Processing instructions are not allowed within SOAP messages. Esse erro pode ter ocorrido por falta de conexão com a internet.
 

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43533764626327)

**SITUAÇÃO**

Este erro ocorre durante operações que envolvem **comunicação com os servidores da SEFAZ**, como:
 

- 

Importação de XML no **"Portal de Importação de XML"** (Configurações >> Cadastros >> Portal de Importação de XML)

- 

Manifestação de destinatário no **"Portal de Importação de XML"** (Configurações >> Cadastros >> Portal de Importação de XML)
 

1. 

Dar **"Ciência automática"** em notas fiscais eletrônicas
 

1. 

Geração de **"CT-e"** (Configurações >> Cadastros >> Conhecimento de Transporte Eletrônico)
 

1. 

Geração de **"MDF-e"** (Configurações >> Cadastros >> Manifesto Eletrônico de Documentos Fiscais)
 

1. 

Consulta de **"MD-e/DF-e"** (Configurações >> Cadastros >> Manifestação do Destinatário)
 

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/32040882106775)

**SOLUÇÃO**

A solução depende da causa identificada. Siga as orientações abaixo:
 

1-Caso seja intabilidade da SEFAZ:

**Solução 1: Aguarde a normalização do serviço da SEFAZ**
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/32849688173719)

 Aguarde alguns minutos e tente realizar a operação novamente, pois o erro pode ser causado por **instabilidade momentânea nos servidores da SEFAZ**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/32849719225879)

 Verifique se outros usuários ou empresas estão enfrentando o mesmo problema no mesmo período.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/32849719228055)

 Consulte o **"Status dos serviços da SEFAZ"** no portal oficial do seu estado para confirmar se há instabilidade reportada.
 

2- Importação de XML com erro: 

**Solução 2: Atualize a versão de consulta do MD-e/DF-e**
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/32849688173719)

 Acesse a tela **"Configuração MD-e/DF-e"** (Configurações >> Cadastros >> Configuração MD-e/DF-e).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/32849719225879)

 Localize o campo **"Versão de consulta"** e altere para **"NT-2014 Distribuição"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/32849719228055)

 Salve as alterações e tente realizar a operação novamente.
 

3-Transmissão das notas: 

**Solução 3: Reimporte o certificado digital**
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/32849688173719)

 Acesse a tela **"Preferências"** (Configurações >> Empresa >> Preferências).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/32849719225879)

 Localize a aba de **"Configurações fiscais"** e reimporte o **"Certificado digital"** da empresa.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/32849719228055)

 Certifique-se de que o certificado está válido.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43533781132567)

 Salve as configurações e tente realizar a operação novamente.
 

**Solução 4: Habilite o modo síncrono para XML**
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/32849688173719)

 Acesse a tela **"Preferências"** (Comercial >> Preferências >> Empresa).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/32849719225879)

 Navegue até a aba **"Documentos Fiscais Eletrônicos"**, em cada sub-aba disponível (como **NF-e, NFC-e, CT-e, MDF-e**, entre outras, conforme utilizado), localize o campo **“Usar modo síncrono para envio do XML”**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/32849719228055)

 Altere o valor para **"Sim"** e salve.

![Print modo síncrono](https://ajuda.sankhya.com.br/hc/article_attachments/32040882109207)

 

*Nota: Para utilizar esta funcionalidade é necessário estar na versão 4.24b234, 4.25b238, 4.26b209, 4.27b85, 4.28b26 ou superior.*
 

 

**Solução 5: Atualize a nota técnica **
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/32849688173719)

 Acesse a tela **"Preferências"** (Configurações >> Empresa >> Preferências).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/32849719225879)

 Em todas as abas (como **NF-e, NFC-e, CT-e, MDF-e**, entre outras)  atualize todas para a **última nota técnica disponível**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/32849719228055)

 Salve as alterações e tente novamente.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43533781133591)

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/32040840001943)

**CAUSA**

Este erro ocorre quando há **falha na comunicação** entre o sistema e os servidores da SEFAZ, resultando em um retorno inválido (não XML). Isso pode ser causado por:
 

- 

Instabilidade momentânea nos servidores da SEFAZ;
 

1. 

Perda de conexão com a internet;
 

1. 

Versão de consulta desatualizada;
 

1. 

Certificado digital com problemas;
 

1. 

Necessidade de ativação do modo síncrono para o envio de MDF-e, conforme as novas determinações da SEFAZ.