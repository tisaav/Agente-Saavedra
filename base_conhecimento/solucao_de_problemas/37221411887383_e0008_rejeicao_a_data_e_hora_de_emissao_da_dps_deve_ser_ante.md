# E0008 Rejeição: A data e hora de emissão da DPS deve ser anterior ou igual à data do seu processamento (dhProc) pelo Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221411887383-E0008-Rejei%C3%A7%C3%A3o-A-data-e-hora-de-emiss%C3%A3o-da-DPS-deve-ser-anterior-ou-igual-%C3%A0-data-do-seu-processamento-dhProc-pelo-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221411887383-E0008-Rejei%C3%A7%C3%A3o-A-data-e-hora-de-emiss%C3%A3o-da-DPS-deve-ser-anterior-ou-igual-%C3%A0-data-do-seu-processamento-dhProc-pelo-Sistema-Nacional-NFS-e)  
> **ID:** `37221411887383` | **Última Atualização:** 2026-07-22T14:18:43Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411863319)

 **MENSAGEM**

E0008 Rejeição: A data e hora de emissão da DPS deve ser anterior ou igual à data do seu processamento (dhProc) pelo Sistema Nacional NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411864599)

 **SITUAÇÃO**

A **NFS-e** foi emitida com **data e hora de emissão posteriores ao momento de recebimento e processamento **do documento pelo Sistema Nacional NFS-e.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411865751)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221397286295)

 **Verifique o horário do servidor** do Banco de Dados junto à área de TI da empresa e confirme se o horário está **sincronizado com o horário oficial** da SEFAZ do seu Estado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221397287575)

 **Ajuste o fuso horário local** do servidor, caso esteja configurado incorretamente. Certifique-se de que o fuso horário está de acordo com a localização geográfica da empresa e com as **configurações da SEFAZ**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221397288599)

 Acesse a tela** ''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e verifique os seguintes campos:

- 

**"Dt. Neg.'' **(Data de Negociação)

- 

**"Data de Movimento"**

- 

**"Data de Faturamento"**

- 

Certifique-se de que estas datas estão **corretas e não estão adiantadas** em relação ao horário atual do servidor.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411870615)

 Acesse a tela **''Empresa'' **(Comercial » Preferências » Empresa).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221397292439)

 Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''** verifique o parâmetro **"Data p/ emissão do RPS na tag DataRecibo - DTPDTRECIBO"** e confirme qual data está sendo utilizada como data de emissão do RPS. As opções disponíveis são:

- 

Data do Sistema (sysdate)

- 

Data de Negociação

- 

Data de Movimento

- 

Data de Faturamento

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221397293207)

 Caso o parâmetro **"Obriga Dt.Negoc. ser igual a do servidor? - DTNEGSERV"** esteja habilitado, o sistema realizará a **alteração automática da data e hora** do documento para que estejam de acordo com o servidor.

- 

Se estiver desabilitado, o sistema questionará se você deseja manter ou ajustar as informações.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38353944001303)

 Após realizar os ajustes necessários, **reemita a NFS-e** com a data e hora de emissão **anterior ou igual** ao horário de processamento do Sistema Nacional NFS-e.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411880855)

 **CAUSA**

A rejeição E0008 ocorre quando a **data e hora de emissão** informadas na DPS (Declaração de Prestação de Serviços) são **posteriores à data e hora** em que o documento foi **recebido pelo Sistema Nacional NFS-e**. Isso pode ser causado por:

- 

**Horário do servidor adiantado:** O servidor onde o sistema está instalado possui horário adiantado em relação ao horário oficial da SEFAZ.

- 

**Diferença de fuso horário:** O fuso horário configurado no servidor não corresponde ao fuso horário da SEFAZ autorizadora, especialmente em períodos de horário de verão.

- 

**Datas incorretas nos campos:** As datas de negociação, movimento ou faturamento foram preenchidas com valores futuros ou incorretos.

- 

**Configuração inadequada de parâmetros:** Os parâmetros relacionados à data de emissão do RPS não estão configurados corretamente, gerando inconsistências entre a data informada e a data de processamento.