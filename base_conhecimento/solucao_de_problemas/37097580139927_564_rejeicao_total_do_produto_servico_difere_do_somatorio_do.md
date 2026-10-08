# 564 Rejeição: Total do Produto / Serviço difere do somatório dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097580139927-564-Rejei%C3%A7%C3%A3o-Total-do-Produto-Servi%C3%A7o-difere-do-somat%C3%B3rio-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097580139927-564-Rejei%C3%A7%C3%A3o-Total-do-Produto-Servi%C3%A7o-difere-do-somat%C3%B3rio-dos-itens)  
> **ID:** `37097580139927` | **Última Atualização:** 2026-09-11T14:04:45Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580109591)

 **MENSAGEM**

564 Rejeição: Total do Produto / Serviço difere do somatório dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580110359)

 **SITUAÇÃO**

Ao emitir uma NF-e (modelo 55) ou NFC-e (modelo 65), o sistema identificou uma divergência entre o valor informado no campo Total dos Produtos e Serviços (vProd) no grupo de totais da nota fiscal e o somatório dos valores dos itens que compõem este total.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580110871)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580111767)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580113431)

 Selecione o TOP utilizado na nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580119319)

 Na aba **''****Desp. Acessórias''**, verifique as seguintes configurações:

- 

**“ICMS proporcional ao ICMS dos itens”** – Selecione todas as opções.

- 

**“PIS proporcional ao PIS dos itens”** – Selecione todas as opções.

- 

**“IPI proporcional ao IPI dos itens”** – Selecione todas as opções.

- 

**“COFINS proporcional ao COFINS dos itens”** – Selecione todas as opções.

- 

**“S.T. proporcional ao S.T. dos itens”** – Selecione todas as opções.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580120215)

 Verifique se todos os itens da nota fiscal que devem compor o valor total estão com o campo **"indTot"** configurado corretamente:

- 

Valor **"1"**: indica que o valor do item compõe o valor total da NF-e

- 

Valor **"0"**: indica que o valor do item não compõe o valor total da NF-e 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580121623)

 Após realizar as configurações necessárias, inutilize a NF-e rejeitada, exclua-a do sistema e emita uma nova nota fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580123159)

 Ao emitir a nova nota, verifique se o valor total dos produtos (**vProd**) corresponde exatamente ao somatório dos valores dos itens cujo campo **indTot** esteja preenchido com **“1”**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097580124055)

 **CAUSA**

A rejeição 564 ocorre quando o valor informado no campo Total dos Produtos e Serviços (Campo: total / ICMSTot / vProd - ID: W07) no grupo de totais da NF-e/NFC-e é diferente do somatório dos valores dos produtos (Campo: det / prod / vProd - ID: I11) de todos os itens que possuem o campo indTot (ID: I17b) com valor igual a "1".

Esta divergência pode ocorrer devido a:

- 

Arredondamentos incorretos nos valores dos itens

- 

Configuração inadequada do campo indTot nos itens da nota

- 

Falha na proporcionalização automática dos impostos nos itens

- 

Erro de cálculo manual ao informar o valor total dos produtos