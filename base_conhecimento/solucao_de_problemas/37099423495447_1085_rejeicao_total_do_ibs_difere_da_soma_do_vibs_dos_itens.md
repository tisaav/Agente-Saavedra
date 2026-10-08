# 1085 Rejeição: Total do IBS difere da soma do vIBS dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37099423495447-1085-Rejei%C3%A7%C3%A3o-Total-do-IBS-difere-da-soma-do-vIBS-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37099423495447-1085-Rejei%C3%A7%C3%A3o-Total-do-IBS-difere-da-soma-do-vIBS-dos-itens)  
> **ID:** `37099423495447` | **Última Atualização:** 2026-09-11T13:23:53Z

---

[1085] Rejeição: Total do IBS difere da soma do vIBS dos itens. [vIBS informado: X.XX, vIBS calculado: X.XX]
 

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/37099423476887)

**Situação**

Ao emitir uma NF-e ou NFC-e, o sistema está calculando o **valor total do IBS de forma diferente do somatório dos valores de IBS de cada item** do documento fiscal, gerando uma inconsistência que resulta na rejeição pela SEFAZ.
 

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/37099435997079)

**Solução**

Para corrigir esta rejeição, siga as abordagens abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099435998103)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099435999639)

 Localize e selecione a TOP utilizada na nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099423485847)

 Na aba **"Despesas Acessórias"** verifique e marque as seguintes opções:

- 
**"ICMS proporcional ao ICMS dos itens": **marque todas as opções

- 
**"PIS proporcional ao PIS dos itens": **marque todas as opções

- 
**"IPI proporcional ao IPI dos itens": **marque todas as opções

- 
**"COFINS proporcional ao COFINS dos itens": **marque todas as opções

- 
**"S.T. proporcional ao S.T. dos itens": **marque todas as opções

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099436003607)

 Salve as alterações.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099423487639)

 Inutilize a NF-e rejeitada.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099436008599)

 Exclua a nota fiscal rejeitada.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099423490327)

 Realize um novo lançamento da nota fiscal utilizando a TOP ajustada. 

 

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/37099423491351)

**Causa**

Esta rejeição ocorre quando o valor total do IBS (Imposto sobre Bens e Serviços) informado no grupo de totais da NF-e ou NFC-e é **diferente do somatório** dos valores de IBS de cada item do documento fiscal.

De acordo com as regras de validação da SEFAZ, o valor total do IBS deve ser **exatamente igual** à soma dos valores de IBS de todos os itens da nota fiscal. Esta validação faz parte das novas regras implementadas pela Reforma Tributária (Lei Complementar nº 214/2025), que introduziu o IBS como um dos novos tributos do sistema tributário brasileiro.