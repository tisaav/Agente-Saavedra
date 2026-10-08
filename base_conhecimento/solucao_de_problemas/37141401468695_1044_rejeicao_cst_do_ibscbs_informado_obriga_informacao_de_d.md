# 1044 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Municipal [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141401468695-1044-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Municipal-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141401468695-1044-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Municipal-nItem-999)  
> **ID:** `37141401468695` | **Última Atualização:** 2026-07-22T14:19:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141385772183)

 **MENSAGEM**

1044 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Municipal [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141401464343)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal (modelo 55) ou Nota Fiscal de Consumidor Eletrônica (modelo 65), o documento foi rejeitado pela SEFAZ porque foi utilizado um CST do IBS/CBS que exige a informação de diferimento Municipal, porém o grupo de diferimento não foi informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141401464727)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141401465111)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se o CST utilizado na operação que está gerando a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38111686272023)

 Confirme se o CST selecionado possui o **indicador de diferimento** (ind_gDif) igual a 1, o que significa que este CST **exige a informação de diferimento**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141401465495)

 Acesse a tela** ''Produtos'' **(Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está configurado corretamente para a tributação do IBS Municipal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141385773079)

 Acesse a tela de** "Tipos de Operação - TOP"** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) e verifique se a TOP utilizada na operação está configurada corretamente para o IBS Municipal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141401466775)

 Na nota fiscal que está sendo emitida, acesse a aba "Impostos" e verifique se o grupo de IBS Municipal (gIBSMun) está sendo preenchido.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141385773207)

 Adicione o grupo de diferimento (gDif) dentro do grupo de IBS Municipal, informando:

- 

Percentual de diferimento (pDif): percentual do imposto que será diferido

- 

Valor do diferimento (vDif): valor calculado pela fórmula vDif = vBC x (pIBSMun / 100) x (pDif / 100)

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141385774487)

 Verifique se o valor do diferimento (vDif) está sendo calculado corretamente, conforme a fórmula:

```text
vDif = vBC x (pIBSMun / 100) x (pDif / 100).
```

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141401467415)

 Após realizar as configurações necessárias, tente emitir a nota fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141401467543)

 **CAUSA**

Esta rejeição ocorre quando o CST do IBS/CBS utilizado na operação possui o **indicador de diferimento** (ind_gDif) igual a 1, o que significa que este CST **exige a informação do grupo de diferimento** para o IBS Municipal, porém este grupo não foi informado no documento fiscal.

De acordo com a regra de validação UB40-10 da SEFAZ, quando o CST possui indicador que exige o uso de diferimento (ind_gDif = 1), o grupo de Diferimento (gIBSMun/gDif) deve ser obrigatoriamente informado no documento fiscal. Caso contrário, a nota será rejeitada com o código 1044.

O diferimento é um mecanismo de postergação do pagamento do imposto para uma etapa posterior da cadeia de comercialização. Quando um CST exige diferimento, é necessário informar o percentual e o valor do diferimento para que a nota fiscal seja aceita pela SEFAZ.