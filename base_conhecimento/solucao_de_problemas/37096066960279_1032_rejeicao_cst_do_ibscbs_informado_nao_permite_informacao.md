# 1032 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota Estadual [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096066960279-1032-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Estadual-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096066960279-1032-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Estadual-nItem-999)  
> **ID:** `37096066960279` | **Última Atualização:** 2026-09-09T00:03:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096066942615)

 **MENSAGEM**

1032 Rejeição: CST do IBS/CBS informado não permite informação de redução de alíquota Estadual [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096098234903)

 **SITUAÇÃO**

Esta rejeição ocorre quando o usuário tenta emitir uma NF-e ou NFC-e utilizando um **CST do IBS/CBS** que não permite a informação de redução de alíquota Estadual, mas mesmo assim foi informado o grupo de redução de alíquota (gIBSUF/gRed) no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096098235799)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096098237463)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP utilizada na nota fiscal rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096098238999)

 Verifique na aba **"NF-e/NFC-e/CF-e"** se está configurado algum **CST do IBS/CBS** que não permite redução de alíquota estadual.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096066950039)

 Acesse a tela **"****Assistente de Configuração Integral da Reforma Tributária****"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique quais CSTs permitem redução de alíquota estadual.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096066951575)

 Escolha uma das seguintes opções para resolver o problema:

- 

Altere o **CST do IBS/CBS** na TOP para um que permita redução de alíquota estadual, caso realmente precise utilizar essa redução, ou

- 

Remova a informação de redução de alíquota estadual (grupo gIBSUF/gRed) mantendo o CST atual.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096066952855)

 Após realizar as alterações necessárias, tente emitir a nota fiscal novamente.
 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096098244503)

 **CAUSA**

A rejeição ocorre devido a uma **incompatibilidade** **entre o CST do IBS/CBS informado** e a tentativa de utilizar redução de alíquota estadual. Cada CST possui indicadores específicos que determinam quais recursos tributários podem ser utilizados com ele.

Neste caso, o CST informado possui o indicador **ind_gRed = 0**, o que significa que ele **não permite** a utilização do grupo de redução de alíquota estadual (gIBSUF/gRed). Esta validação está prevista na regra UB26-10 da Sefaz, que verifica se o CST utilizado é compatível com a redução de alíquota estadual informada no documento fiscal. A regra é aplicada tanto para NF-e (modelo 55) quanto para NFC-e (modelo 65).