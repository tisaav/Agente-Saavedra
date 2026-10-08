# 1049 Rejeição: Não é permitido o uso de Crédito Presumido na NFC-e modelo 65 [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097035612567-1049-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-uso-de-Cr%C3%A9dito-Presumido-na-NFC-e-modelo-65-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097035612567-1049-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-uso-de-Cr%C3%A9dito-Presumido-na-NFC-e-modelo-65-nItem-999)  
> **ID:** `37097035612567` | **Última Atualização:** 2026-07-22T14:20:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097035602839)

 **MENSAGEM**

1049 Rejeição: Não é permitido o uso de Crédito Presumido na NFC-e modelo 65 [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097060586007)

 **SITUAÇÃO**

A rejeição está relacionada à emissão de uma NFC-e (modelo 65) contendo informações de Crédito Presumido vinculadas ao IBS (Imposto sobre Bens e Serviços) ou à CBS (Contribuição sobre Bens e Serviços).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097060586263)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097035604631)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o tipo de operação utilizado está configurado para emissão de NFC-e (modelo 65).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097060587159)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está configurado para o modelo 65 (NFC-e).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097035606295)

 Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique as configurações de Crédito Presumido.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38279587543575)

 Certifique-se de que **não estão sendo informados** os grupos de Crédito Presumido para o IBS (gIBSCBS/gIBSCredPres) ou para a CBS (gIBSCBS/gCBSCredPres) nas operações com NFC-e.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097035606807)

 Caso seja necessário utilizar Crédito Presumido, **retorne o passo 1** e altere o modelo do documento fiscal para NF-e (modelo 55).

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097035607703)

 **CAUSA**

A causa desta rejeição está relacionada às regras de validação da SEFAZ para a Reforma Tributária (Lei Complementar nº 214/2025). De acordo com as regras UB73-05, UB78-05 e UB120-10, não é permitido o uso de Crédito Presumido em documentos fiscais do modelo 65 (NFC-e).

A NFC-e (Nota Fiscal de Consumidor Eletrônica) é destinada principalmente a operações de venda direta ao consumidor final, e por sua natureza simplificada, não comporta a utilização de mecanismos de Crédito Presumido do IBS ou da CBS, que são aplicáveis apenas em operações entre contribuintes documentadas por NF-e (modelo 55).