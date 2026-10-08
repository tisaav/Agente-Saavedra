# 1007 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota municipal [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141374193431-1007-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-municipal-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141374193431-1007-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-municipal-nItem-999)  
> **ID:** `37141374193431` | **Última Atualização:** 2026-07-22T14:19:25Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382847895)

 **MENSAGEM**

1007 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota municipal [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141374187799)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal (modelo 55) ou Nota Fiscal de Consumidor Eletrônica (modelo 65), o documento foi rejeitado porque foi informado o grupo de redução de alíquota municipal para um CST do IBS/CBS que não permite esse tipo de informação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382849943)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382850199)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST utilizado no item rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141374190871)

 Verifique se o CST informado possui o indicador que **não permite** o uso de redução de alíquota (ind_gRed = 0).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382851607)

 Escolha uma das seguintes opções:

- 

Altere o CST para um que permita a informação de redução de alíquota municipal (ind_gRed = 1).

- 

Remova o grupo de redução de alíquota municipal (gIBSMun/gRed) da nota fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382851735)

 Acesse a tela** ''Central de Vendas'' **(Comercial » Rotinas » Central de Vendas) e localize a nota rejeitada.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382852375)

 Edite a nota fiscal e ajuste o item com a rejeição, aplicando a correção escolhida no passo 3.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382852759)

 Salve as alterações e tente emitir a nota fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141382853271)

 **CAUSA**

Esta rejeição ocorre quando é informado o grupo de redução de alíquota municipal (gIBSMun/gRed) para um CST do IBS/CBS que possui o indicador que não permite o uso de redução de alíquota (ind_gRed = 0).

Cada CST possui indicadores específicos que determinam quais grupos de informações podem ou não ser utilizados na nota fiscal. Quando um grupo de informação é utilizado em desacordo com o que é permitido pelo CST, a Sefaz rejeita o documento fiscal.

De acordo com a regra de validação UB45-10, se o CST possui indicador que não permite o uso de Redução de Alíquota (ind_gRed = 0), o grupo de Redução de Alíquota Municipal (gIBSMun/gRed) não deve ser informado, exceto em casos específicos previstos na legislação.