# 1086 Rejeição: Total de Crédito Presumido do IBS UF difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097785520407-1086-Rejei%C3%A7%C3%A3o-Total-de-Cr%C3%A9dito-Presumido-do-IBS-UF-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097785520407-1086-Rejei%C3%A7%C3%A3o-Total-de-Cr%C3%A9dito-Presumido-do-IBS-UF-difere-da-soma-dos-itens)  
> **ID:** `37097785520407` | **Última Atualização:** 2026-07-22T14:20:30Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097785509271)

 **MENSAGEM**

1086 Rejeição: Total de Crédito Presumido do IBS UF difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097794179863)

 **SITUAÇÃO**

Ao tentar emitir um documento fiscal eletrônico (NF-e/NFC-e) que contém valores de crédito presumido do IBS UF, o sistema da Sefaz rejeita a operação porque o valor total do crédito presumido do IBS UF informado no documento não corresponde à soma dos valores informados em cada item.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097785511319)

 **SOLUÇÃO**

Para resolver esta rejeição, verifique se os valores de crédito presumido do IBS UF estão sendo calculados e totalizados corretamente:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097785511959)

 Acesse a tela****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097794183703)

 Verifique se a configuração do tipo de operação utilizado está correta para o cálculo do IBS.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097785515799)

 Na **''Impostos''**, na seção **''Reforma Tributária''**, verifique se o campo **''Tem IBS''** está configurado adequadamente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097794184983)

 Acesse as telas** ''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097794185495)

 Verifique se as configurações de crédito presumido estão corretas para os produtos envolvidos na operação.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097785517591)

 Revise os valores de **"Percentual do Crédito Presumido"** (pCredPres) e **"Código do Crédito Presumido"** (cCredPres) configurados para cada item da nota fiscal.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38000575099287)

 Certifique-se de que o sistema está calculando corretamente o valor do crédito presumido para cada item, seguindo a fórmula:

```text
vCredPres = (vIBSUF + vIBSMun) * (1 - pCredPres / 100).
```

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38193881224471)

 Após realizar as correções, tente emitir o documento fiscal novamente.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097785517975)

 **CAUSA**

Esta rejeição ocorre quando o valor total do crédito presumido do IBS UF informado no documento fiscal não corresponde à soma dos valores de crédito presumido informados em cada item. Isso pode acontecer devido a:

- 

Erro no cálculo do crédito presumido em um ou mais itens da nota fiscal;

- 

Inconsistência na aplicação dos percentuais de crédito presumido (pCredPres);

- 

Falha na totalização dos valores de crédito presumido do IBS UF no documento fiscal;

- 

Configuração incorreta das alíquotas de IBS ou dos parâmetros de cálculo do crédito presumido.

O sistema da Sefaz realiza uma validação matemática para garantir que o valor total do crédito presumido do IBS UF declarado no documento seja exatamente igual à soma dos valores de crédito presumido de cada item, conforme as regras estabelecidas na Lei Complementar nº 214/2025 para a Reforma Tributária.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)