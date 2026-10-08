# 1041 Rejeição: Valor do IBS da UF difere do calculado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141392523671-1041-Rejei%C3%A7%C3%A3o-Valor-do-IBS-da-UF-difere-do-calculado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141392523671-1041-Rejei%C3%A7%C3%A3o-Valor-do-IBS-da-UF-difere-do-calculado-nItem-999)  
> **ID:** `37141392523671` | **Última Atualização:** 2026-07-22T17:49:48Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141358456727)

 **MENSAGEM**

1041 Rejeição: Valor do IBS da UF difere do calculado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141392514199)

 **SITUAÇÃO**

Ao emitir um documento fiscal, o sistema retorna uma rejeição relacionada ao **valor do IBS da Unidade Federada** informado no documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141358457751)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141392515095)

 Acesse as telas** ''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se os valores informados para o cáculo do IBS da UF estão corretos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141392517399)

 Na aba** ''Tributação'**' na seção **''Alíquotas''**, verifique se a **''% Estado'' **está configurada corretamente para o produto e operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109011456151)

 Verifique se os valores de **"Base de Cálculo"** (vBC) estão corretos no documento fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141358462487)

 Certifique-se de que os valores de **"Diferimento"** (vDif) e **"Devolução de Tributo"** (vDevTrib), caso informados, estão corretos.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141392519063)

 Recalcule o valor do IBS da UF utilizando a fórmula:

```text
vIBSUF = (vBC × (pIBSUF / 100)) - vDif - vDevTrib.
```

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109011457303)

 Após as correções, emita novamente o documento fiscal para validar se o cálculo está sendo realizado corretamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141358464919)

 **CAUSA**

Esta rejeição ocorre devido a uma **inconsistência no cálculo do valor do IBS da Unidade Federada**. Conforme a regra de validação UB35-10, quando informado o grupo IBS de competência das Unidades Federadas (gIBSUF), o valor do IBS Estadual (vIBSUF) deve ser calculado pela fórmula: vIBSUF = (vBC × (pIBSUF / 100)) - vDif - vDevTrib.

O erro pode ocorrer por diversos motivos, como:

- 

Alíquota do IBS da UF (pIBSUF) configurada incorretamente;

- 

Base de cálculo (vBC) informada com valor incorreto;

- 

Valores de diferimento (vDif) ou devolução de tributo (vDevTrib) informados incorretamente;

- 

Erro no cálculo automático realizado pelo sistema.

De acordo com a Lei Complementar 214/2025, que regulamenta a Reforma Tributária, é fundamental que os valores do IBS sejam calculados corretamente para garantir a conformidade fiscal dos documentos eletrônicos.