# E0472 Rejeição: A data de emissão do documento informado na DPS não pode ser posterior à data de competência da DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225721331735-E0472-Rejei%C3%A7%C3%A3o-A-data-de-emiss%C3%A3o-do-documento-informado-na-DPS-n%C3%A3o-pode-ser-posterior-%C3%A0-data-de-compet%C3%AAncia-da-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225721331735-E0472-Rejei%C3%A7%C3%A3o-A-data-de-emiss%C3%A3o-do-documento-informado-na-DPS-n%C3%A3o-pode-ser-posterior-%C3%A0-data-de-compet%C3%AAncia-da-DPS)  
> **ID:** `37225721331735` | **Última Atualização:** 2026-07-22T14:15:41Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225688544279)

 **MENSAGEM**

E0472 Rejeição: A data de emissão do documento informado na DPS não pode ser posterior à data de competência da DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225721318551)

 **SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o usuário informou um documento fiscal cuja **data de emissão é posterior à data de competência** declarada na DPS. Esta inconsistência temporal viola as regras de validação da Sefaz, resultando na rejeição do documento eletrônico.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225721319319)

 **SOLUÇÃO**

Para corrigir esta rejeição, ajuste as datas do documento fiscal seguindo os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225688546967)

 Verifique a **"Data de Competência"** informada na DPS que está sendo transmitida.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225721323159)

 Acesse o documento fiscal vinculado à DPS e localize o campo **"Data de Emissão"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225688548631)

 Certifique-se de que a **"Data de Emissão"** do documento seja **igual ou anterior** à **"Data de Competência"** da DPS.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225721325079)

 Caso a data de emissão esteja incorreta, ajuste-a para uma data válida que respeite a regra de validação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225688549783)

 Salve as alterações realizadas no documento fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225688550295)

 Reenvie a DPS para autorização junto à Sefaz.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225688550807)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida a cronologia temporal** dos documentos fiscais vinculados à DPS. A **data de emissão** do documento não pode ser **posterior à data de competência** declarada, pois isso caracteriza uma **inconsistência lógica**: um documento não pode ser emitido em uma data futura em relação ao período de competência ao qual ele se refere. Esta validação garante a **integridade e veracidade** das informações prestadas ao fisco.