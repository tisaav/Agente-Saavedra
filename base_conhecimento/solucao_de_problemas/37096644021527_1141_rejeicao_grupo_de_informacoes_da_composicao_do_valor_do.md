# 1141 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais não informado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096644021527-1141-Rejei%C3%A7%C3%A3o-Grupo-de-informa%C3%A7%C3%B5es-da-composi%C3%A7%C3%A3o-do-valor-do-IBS-e-da-CBS-em-compras-governamentais-n%C3%A3o-informado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096644021527-1141-Rejei%C3%A7%C3%A3o-Grupo-de-informa%C3%A7%C3%B5es-da-composi%C3%A7%C3%A3o-do-valor-do-IBS-e-da-CBS-em-compras-governamentais-n%C3%A3o-informado-nItem-999)  
> **ID:** `37096644021527` | **Última Atualização:** 2026-07-22T14:21:14Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096629910167)

 **MENSAGEM**

1141 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais não informado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096629912471)

 **SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e (modelo 55) quando é informado o grupo de **compras governamentais**, sem que o grupo de **composição do valor do IBS e da CBS** específico para esse tipo de operação esteja preenchido no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096644012055)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096629914775)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação utilizada está configurada corretamente para compras governamentais.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096644013591)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"Tipo de operação com o ente governamental"** está marcado como:

- 

**''1 – Fornecimento'' **ou,

- 

**''2 – Recebimento do pagamento''.**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096644014615)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38276486026135)

 Verifique se o **CST **selecionado é compatível com operações de compras governamentais.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096644017303)

 Na seção de **"Composição do Valor do IBS e CBS em Compras Governamentais"**, preencha os campos obrigatórios:

- 

Valor do IBS UF

- 

Valor do IBS Municipal Valor da CBS.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096629921431)

 Certifique-se de que a soma dos valores informados na composição (vTribIBSUF + vTribIBSMun + vTribCBS) seja igual ao resultado da soma dos valores de IBS UF, IBS Municipal e CBS calculados para o item.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096629921943)

 **CAUSA**

A rejeição 1141 ocorre devido à **inconsistência na configuração fiscal** para operações de compras governamentais. Conforme a regra de validação UB82a-10, quando o grupo de Compra Governamental (grupo: gCompraGov) é informado na NF-e, é **obrigatório** informar também o grupo de informações da composição do valor do IBS e da CBS específico para compras governamentais (grupo: gTribCompraGov).

Esta obrigatoriedade está relacionada às exigências da Lei Complementar 214/2025, que estabelece regras específicas para a tributação de operações com órgãos públicos no contexto da Reforma Tributária, determinando que a composição dos valores de IBS e CBS deve ser detalhada de forma específica nestas operações.