# Os valores de IBS/CBS não estão sendo gerados no XML da Nota Fiscal de Serviço

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39351023777943-Os-valores-de-IBS-CBS-n%C3%A3o-est%C3%A3o-sendo-gerados-no-XML-da-Nota-Fiscal-de-Servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/39351023777943-Os-valores-de-IBS-CBS-n%C3%A3o-est%C3%A3o-sendo-gerados-no-XML-da-Nota-Fiscal-de-Servi%C3%A7o)  
> **ID:** `39351023777943` | **Última Atualização:** 2026-09-25T02:25:56Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39351023774615)

 MENSAGEM**

Os impostos IBS e CBS estão sendo calculados corretamente no sistema, porém não constam no arquivo XML da nota fiscal emitida.

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39351000299799)

 SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço (NFS)** em ambiente de produção, o usuário verifica que os tributos **IBS (Imposto sobre Bens e Serviços)** e **CBS (Contribuição sobre Bens e Serviços)** são calculados corretamente pelo motor de cálculo do sistema. No entanto, ao consultar o arquivo XML da nota fiscal emitida e transmitida, as tags correspondentes ao **IBS** e à **CBS** não são apresentadas.

A situação pode ocorrer mesmo quando todas as configurações necessárias para a **Reforma Tributária** já foram realizadas, incluindo a parametrização de **alíquotas**, **cClassTrib** e **CST** dos novos tributos.

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39351000300439)

 SOLUÇÃO**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39351000300695)

 Acesse a nota pelo Portal de Vendas e abra-a na Central de Vendas. Em seguida, localize a **grade de Itens** da nota e acesse a aba **Consultar/Alterar Dados do Imposto do Item da Nota**. 

Confirme se os tributos **IBS** e **CBS** estão sendo calculados corretamente.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39351000301207)

 Verifique se os campos relacionados à **Reforma Tributária** estão devidamente preenchidos no cadastro do serviço (Aba > Serviços), incluindo as informações necessárias para o cálculo do **IBS** e da **CBS**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43680805196695)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39351000303383)

 No **Portal de Vendas**, acesse botão **NFS-e > Gerar JSON** e consulte o arquivo JSON da nota para verificar se as informações referentes aos tributos **IBS** e **CBS** estão sendo geradas corretamente.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39351023776279)

 Para validar se as notas fiscais estão sendo geradas com as informações corretas.

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39351000304919)

 CAUSA**

O sistema **Sankhya** já está preparado para calcular e gerar os grupos de tributos **IBS**, **CBS** e **IS**, conforme as **Notas Técnicas da Reforma Tributária**. No entanto, o **XML de retorno do Portal Nacional** não apresenta essas tags enquanto não houver obrigatoriedade estabelecida para sua inclusão.