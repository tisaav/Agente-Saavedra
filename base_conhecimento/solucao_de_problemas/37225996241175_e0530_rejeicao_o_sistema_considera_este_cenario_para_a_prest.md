# E0530 Rejeição: O sistema considera este cenário para a prestação de serviço informada na DPS uma exportação de serviço. Não é permitido ao emitente da DPS informar que a prestação de serviço se trata de uma operação tributável.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225996241175-E0530-Rejei%C3%A7%C3%A3o-O-sistema-considera-este-cen%C3%A1rio-para-a-presta%C3%A7%C3%A3o-de-servi%C3%A7o-informada-na-DPS-uma-exporta%C3%A7%C3%A3o-de-servi%C3%A7o-N%C3%A3o-%C3%A9-permitido-ao-emitente-da-DPS-informar-que-a-presta%C3%A7%C3%A3o-de-servi%C3%A7o-se-trata-de-uma-opera%C3%A7%C3%A3o-tribut%C3%A1vel](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225996241175-E0530-Rejei%C3%A7%C3%A3o-O-sistema-considera-este-cen%C3%A1rio-para-a-presta%C3%A7%C3%A3o-de-servi%C3%A7o-informada-na-DPS-uma-exporta%C3%A7%C3%A3o-de-servi%C3%A7o-N%C3%A3o-%C3%A9-permitido-ao-emitente-da-DPS-informar-que-a-presta%C3%A7%C3%A3o-de-servi%C3%A7o-se-trata-de-uma-opera%C3%A7%C3%A3o-tribut%C3%A1vel)  
> **ID:** `37225996241175` | **Última Atualização:** 2026-07-22T14:15:24Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225996230679)

 **MENSAGEM**

E0530 Rejeição: O sistema considera este cenário para a prestação de serviço informada na DPS uma exportação de serviço. Não é permitido ao emitente da DPS informar que a prestação de serviço se trata de uma operação tributável.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225996232343)

 **SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** ou um **Documento de Prestação de Serviços (DPS)**, o sistema identificou que a operação se caracteriza como uma **exportação de serviço**, porém o documento foi configurado indicando que a prestação é uma **operação tributável** pelo IBS e CBS. Esta inconsistência entre a natureza da operação e a tributação informada resulta na rejeição do documento pela Sefaz.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226011826839)

 **SOLUÇÃO**

Para resolver esta rejeição, ajuste a configuração da operação para refletir corretamente que se trata de uma exportação de serviço, seguindo os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226011827863)

 Acesse a tela **"Tipo de Operação"** (Configurações » Cadastros » Tipo de Operação) e localize o **TOP** utilizado na emissão do documento rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38098830689943)

 Na aba **"IBS e CBS"**, verifique o campo **"Código de situação tributária - CST"** configurado para a operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38098814862231)

 Para operações de **exportação de serviços**, configure o **CST** apropriado que identifique a operação como **não tributável** ou **isenta**, conforme previsto na legislação da Reforma Tributária:

- 

Utilize o **CST 41** (Não tributada) ou outro código específico para exportação, conforme orientação da legislação vigente.

- 

Certifique-se de que o **CST** selecionado esteja compatível com operações de exportação de serviços.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225996237847)

 Ainda na aba **"IBS e CBS"**, verifique se os campos relacionados à tributação estão configurados corretamente:

- 

Confirme que não há indicação de **operação tributável** quando se tratar de exportação.

- 

Verifique se os campos de **alíquota** e **base de cálculo** estão zerados ou não aplicáveis.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225996238487)

 Acesse a tela **''Parceiros'' **(Configurações » Cadastros » Parceiros).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225996239127)

 Na aba** ''Identificação''**, verifique se o tomador do serviço está identificado corretamente como **pessoa física ou jurídica domiciliada no exterior**, quando aplicável.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225996239383)

 Acesse a tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38098830691991)

 Ao emitir o documento, na grade** ''Cabeçalho''** certifique-se de que o campo **"Cidade de Prestação do Serviço"** esteja preenchido corretamente, indicando o município onde o serviço será prestado ou deixando em branco quando se tratar de exportação.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38098814865431)

 Salve as alterações realizadas e emita novamente o documento fiscal.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226011830167)

 **CAUSA**

A rejeição ocorre porque o sistema identificou que a prestação de serviço se enquadra como uma **exportação de serviço**, que pela legislação da **Reforma Tributária** (Lei Complementar nº 214/2025) é uma operação **não tributável** pelo IBS e CBS.

Entretanto, o documento foi emitido com configurações que indicam tratar-se de uma **operação tributável**, gerando uma **inconsistência** entre a natureza da operação e a tributação informada. A Sefaz não permite que exportações de serviços sejam declaradas como operações tributáveis, resultando na rejeição do documento com o código **E0530**.