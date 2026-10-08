# E0700 Rejeição: O valor do tributo IRRF deve ser maior que zero e menor que o valor do serviço informado na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228138469399-E0700-Rejei%C3%A7%C3%A3o-O-valor-do-tributo-IRRF-deve-ser-maior-que-zero-e-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228138469399-E0700-Rejei%C3%A7%C3%A3o-O-valor-do-tributo-IRRF-deve-ser-maior-que-zero-e-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS)  
> **ID:** `37228138469399` | **Última Atualização:** 2026-07-22T14:14:19Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138457623)

 **MENSAGEM**

E0700 Rejeição: O valor do tributo IRRF deve ser maior que zero e menor que o valor do serviço informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138460439)

 **SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)** contendo informações de **retenção de IRRF**, o documento foi **rejeitado pela Sefaz** com a mensagem E0700. Esta rejeição ocorre quando o **valor do Imposto de Renda Retido na Fonte (IRRF)** informado no documento está **igual a zero, negativo ou superior ao valor total do serviço** prestado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138460695)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138461335)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento que foi rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138461847)

 Na grade **''Rodapé''**, clique na aba **''Impostos'' **e localize o campo **''Vlr. do IRF''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228121799703)

 Certifique-se de que o **valor do IRRF** atende aos seguintes critérios:

- 

Deve ser **maior que zero**;

- 

Deve ser **menor que o valor total do serviço** informado no documento.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228121800599)

 Caso o valor esteja **incorreto**, ajuste o **cálculo do IRRF** no financeiro ou na configuração de impostos:

- 

Acesse a tela **"Impostos"** (Configurações > Cadastros > Impostos) e verifique se o **tipo de imposto IR** está configurado corretamente como **"RETIDO"**;

- 

Verifique se os campos **"Base IRF"** e **"Vlr IRF"** no financeiro estão preenchidos com valores válidos e maiores que zero;

- 

Confirme se a **"Natureza de Rendimento"** associada ao financeiro está configurada adequadamente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138463895)

  Após realizar os ajustes necessários, **recalcule os impostos** do documento e verifique se o **valor do IRRF** está dentro dos parâmetros exigidos.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138465047)

  **Reemita o documento** e transmita novamente para a Sefaz. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228138466199)

 **CAUSA**

A rejeição E0700 ocorre quando o **valor do IRRF informado no Documento de Prestação de Serviços** não atende às regras de validação da Sefaz, que exigem que este valor seja **maior que zero e menor que o valor total do serviço**. Isso pode acontecer devido a:

- 

**Configuração incorreta** dos impostos no cadastro de **"Impostos"** ou no financeiro;

- 

**Cálculo automático do IRRF** resultando em valor zero ou negativo;

- 

**Valor do IRRF informado manualmente** de forma incorreta, sendo igual ou superior ao valor do serviço;

- 

**Falta de preenchimento** dos campos **"Base IRF"** ou **"Vlr IRF"** no financeiro;

- 

**Natureza de Rendimento** não configurada adequadamente para gerar a tributação correta.