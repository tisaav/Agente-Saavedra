# O valor do campo Xnome (Razão Social ou Nome do emitente) informado não é válido - (NFC-e Consumidor Padrão)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33941379478679-O-valor-do-campo-Xnome-Raz%C3%A3o-Social-ou-Nome-do-emitente-informado-n%C3%A3o-%C3%A9-v%C3%A1lido-NFC-e-Consumidor-Padr%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/33941379478679-O-valor-do-campo-Xnome-Raz%C3%A3o-Social-ou-Nome-do-emitente-informado-n%C3%A3o-%C3%A9-v%C3%A1lido-NFC-e-Consumidor-Padr%C3%A3o)  
> **ID:** `33941379478679` | **Última Atualização:** 2026-08-03T20:11:47Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33941370165655)

 **SITUAÇÃO: **

Ao tentar emitir uma **NFC-e **(Nota Fiscal de Consumidor Eletrônica), o sistema apresenta uma mensagem de erro relacionada à geração do XML, especificamente pela presença indevida da tag **<dest>**, que só deve ser gerada em situações específicas.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33941370169239)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34100245188759)

  **Verifique o parceiro informado na nota:** confirme se é um consumidor final sem CPF/CNPJ, geralmente cadastrado como **"Consumidor Não Identificado"**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34100226043543)

  Configure corretamente o parceiro padrão da NFC-e:  

- 

Acesse a tela **"Empresa"** (Comercial» Preferências» Empresa) e selecione a empresa correspondente; 

- 

Clique na aba **"Documentos Fiscais Eletrônicos"**, sub aba **"NFC-e", **e no campo **"Parceiro Padrão da NFC-e" **e selecione o parceiro cadastrado como ''**Consumidor Final padrão (sem identificação)''. **

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34100226045207)

 Observações**: 

- 

O parceiro Consumidor Final padrão (sem identificação) da nota deve ser o mesmo da configuração do parceiro padrão da empresa.

- 

Se a venda for para um cliente identificado (com CPF ou CNPJ), o sistema poderá gerar a tag **<dest>**, desde que os dados estejam completos e válidos.

- 

**Devolução de NFC-e : **Quando for necessário realizar a devolução de uma NFC-e (Nota Fiscal de Consumidor Eletrônica), deve-se emitir uma **NF-e (Nota Fiscal Eletrônica)** de devolução. Além disso, para a emissão da NF-e de devolução, é indispensável que o parceiro (cliente) esteja devidamente identificado com um **CPF ou CNPJ válido**. Essa informação é obrigatória para a validação fiscal do documento e para que a devolução seja autorizada pela SEFAZ.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33941370170007)

 **CAUSA: **

O erro ocorre quando o **"parceiro (cliente)"** utilizado na venda não corresponde ao **"Parceiro Padrão da NFC-e"** configurado no sistema. Dessa forma, o sistema entende que a nota deve conter dados de destinatário, gerando a tag **<dest>**, o que pode ser inválido em determinadas condições da NFC-e.