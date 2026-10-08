# Operação interestadual para Consumidor Final e valor do FCP informado em campo diferente de vFCPUFDest [nItem:nnn]

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043195373-Opera%C3%A7%C3%A3o-interestadual-para-Consumidor-Final-e-valor-do-FCP-informado-em-campo-diferente-de-vFCPUFDest-nItem-nnn](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043195373-Opera%C3%A7%C3%A3o-interestadual-para-Consumidor-Final-e-valor-do-FCP-informado-em-campo-diferente-de-vFCPUFDest-nItem-nnn)  
> **ID:** `360043195373` | **Última Atualização:** 2026-07-22T16:06:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511832333719)

 MENSAGEM:**

[876 - Rejeição]: Operação interestadual para Consumidor Final e valor do FCP informado em campo diferente de vFCPUFDest [nItem:nnn]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511856856727)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511832338071)

 Acesse: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*

Pesquise pela regra de ICMS que incidiu nos itens da nota e  ajuste o campo "**Aliq. Interna Destino"**, de acordo com as orientações do Contador.

Para facilitar a busca pela exceção de ICMS utilizada em cada item/lançamento verifique o conteúdo [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043874154-Como-identificar-qual-a-al%C3%ADquota-exce%C3%A7%C3%A3o-de-ICMS-utilizada-no-lan%C3%A7amento-)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511856879767)

 Após os ajustes, inutilize a numeração da NF-e atual e refaça o faturamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511832344599)

 CAUSA:**

Quando for emitida uma NF-e (modelo 55) interestadual (Campo: idDest = 2) para Consumidor Final (Campo: indFinal = 1) não contribuinte (Campo: indIEDest = 9) e o valor do FCP for informado em um campo diferente de vFCPUFDest, haverá a rejeição


---

### 🔗 Links e Referências Internas:

- [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043874154-Como-identificar-qual-a-al%C3%ADquota-exce%C3%A7%C3%A3o-de-ICMS-utilizada-no-lan%C3%A7amento-)