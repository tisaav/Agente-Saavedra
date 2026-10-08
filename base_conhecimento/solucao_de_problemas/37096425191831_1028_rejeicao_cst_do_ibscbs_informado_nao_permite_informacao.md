# 1028 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota da CBS [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096425191831-1028-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-CBS-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096425191831-1028-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-CBS-nItem-999)  
> **ID:** `37096425191831` | **Última Atualização:** 2026-07-22T14:21:21Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439144215)

 **MENSAGEM**

1028 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota da CBS [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439146263)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o sistema apresenta a rejeição acima, indicando que foi informado um grupo de redução de alíquota da CBS para um CST que não permite esse tipo de informação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439146775)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439148823)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST do IBS/CBS utilizado no item da nota fiscal que está gerando a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096425177623)

 Identifique o **CST do IBS/CBS** que está sendo utilizado no item rejeitado e verifique se este CST permite a informação de redução de alíquota da CBS. Consulte a **Tabela de Indicadores de CST do IBS e da CBS **para confirmar.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439152791)

 Se o CST utilizado não permitir redução de alíquota da CBS (indicador ind_gRed = 0), você tem duas opções:

- 

Remova a informação de redução de alíquota da CBS no cadastro da alíquota utilizada

- 

Altere para um CST que permita a informação de redução de alíquota da CBS.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096425182487)

 Para remover a informação de redução de alíquota retorne o passo 1, localize a alíquota utilizada e remova as informações do grupo **''% da Redução de Alíquota CBS''** (grupo: gCBS/gRed).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439154967)

 Caso opte por alterar o CST, selecione um que possua o indicador ind_gRed = 1, que permite a informação de redução de alíquota da CBS.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439156247)

 Após realizar as alterações necessárias, tente emitir a nota fiscal novamente. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096439157143)

 **CAUSA**

A rejeição ocorre porque foi informado o grupo de Redução de Alíquota da CBS (grupo: gCBS/gRed) para um CST do IBS/CBS que possui o indicador que não permite o uso de redução de alíquota (ind_gRed = 0). Cada CST do IBS/CBS possui indicadores específicos que determinam quais informações podem ou não ser utilizadas com ele.

Quando um CST tem o indicador ind_gRed = 0, significa que ele não permite a utilização do grupo de redução de alíquota da CBS, e qualquer tentativa de informar esse grupo resultará na rejeição 1028.