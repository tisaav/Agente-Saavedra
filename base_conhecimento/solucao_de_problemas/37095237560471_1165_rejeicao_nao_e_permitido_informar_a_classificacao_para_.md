# 1165 Rejeição: Não é permitido informar a classificação para subapuração do IBS na ZFM na NFC-e modelo 65 [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095237560471-1165-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-a-classifica%C3%A7%C3%A3o-para-subapura%C3%A7%C3%A3o-do-IBS-na-ZFM-na-NFC-e-modelo-65-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095237560471-1165-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-a-classifica%C3%A7%C3%A3o-para-subapura%C3%A7%C3%A3o-do-IBS-na-ZFM-na-NFC-e-modelo-65-nItem-999)  
> **ID:** `37095237560471` | **Última Atualização:** 2026-07-22T14:21:49Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095239416855)

 **MENSAGEM**

1165 Rejeição: Não é permitido informar a classificação para subapuração do IBS na ZFM na NFC-e modelo 65 [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095239417751)

 **SITUAÇÃO**

Ao tentar emitir uma NFC-e (modelo 65) com informações de classificação para subapuração do IBS na Zona Franca de Manaus (ZFM), a nota fiscal foi rejeitada pela SEFAZ com a mensagem de erro 1165.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095237541143)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095239420951)

 Acesse a tela ****[''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095239424663)

 Verifique se o modelo de documento fiscal está configurado como NFC-e (modelo 65).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095237547159)

 Na aba **"NF-e/NFC-e/CF-e"**, confirme se o campo **"Modelo do Documento"** está configurado como **"65 - Nota Fiscal Eletrônica de Venda a Cosumidor''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095237548055)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095237548695)

 Verifique as configurações de CST do IBS e CBS utilizadas na operação.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38015507282967)

 Remova qualquer informação relacionada à **classificação para subapuração do IBS na ZFM** que esteja sendo enviada na NFC-e.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38015507283863)

 Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e certifique-se de que não estão sendo configurados benefícios fiscais da ZFM para documentos modelo 65 (NFC-e).

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095237551511)

 **CAUSA**

A rejeição ocorre porque, de acordo com as regras de validação da SEFAZ (regra UB131-10), **não é permitido informar a classificação para subapuração do IBS na Zona Franca de Manaus (ZFM) em documentos fiscais do modelo 65 (NFC-e)**.

Esta restrição está alinhada com a Lei Complementar 214/2025, que estabelece tratamentos diferenciados para a ZFM, mas que são aplicáveis apenas para documentos fiscais modelo 55 (NF-e).

Os benefícios fiscais relacionados à ZFM, incluindo créditos presumidos e classificações específicas para subapuração do IBS, são exclusivos para operações documentadas por NF-e (modelo 55), não sendo aplicáveis às operações de varejo documentadas por NFC-e (modelo 65).


---

### 🔗 Links e Referências Internas:

- [''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)