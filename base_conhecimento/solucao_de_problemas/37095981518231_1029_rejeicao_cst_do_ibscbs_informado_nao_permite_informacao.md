# 1029 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Estadual [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095981518231-1029-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-diferimento-Estadual-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095981518231-1029-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-de-diferimento-Estadual-nItem-999)  
> **ID:** `37095981518231` | **Última Atualização:** 2026-07-22T14:21:29Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095981474967)

 **MENSAGEM**

1029 Rejeição: CST do IBS/CBS informado não permite informação de diferimento Estadual [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095995992215)

 **SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e ou NFC-e quando é informado o grupo de **diferimento estadual do IBS (gIBSUF/gDif)** em conjunto com um CST que não permite a utilização desse tipo de benefício fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095995994647)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095981482519)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique o tipo de operação utilizado na nota fiscal rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095995999767)

 Acesse as telas **''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o **CST** configurado para a operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095996002455)

 Verifique se o CST utilizado possui o indicador que **não permite** o uso de diferimento (ind_gDif = 0). Neste caso, será necessário utilizar um CST compatível com diferimento ou remover o grupo de diferimento estadual.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38273655522071)

 Para corrigir a situação, escolha uma das seguintes opções:

- 

Altere o CST para um que permita o uso de diferimento estadual (ind_gDif = 1), caso a operação realmente necessite deste benefício fiscal, ou

- 

Remova o grupo de diferimento estadual (gIBSUF/gDif) da configuração da alíquota, caso o benefício fiscal não seja aplicável à operação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095996006935)

 Após realizar as alterações, tente emitir a nota fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095981496855)

 **CAUSA**

A rejeição ocorre devido à regra de validação UB22-10 da Sefaz, que verifica se o CST do IBS/CBS informado no documento fiscal possui o indicador que permite o uso de diferimento estadual. Cada CST possui indicadores específicos que determinam quais benefícios fiscais podem ser aplicados.

Quando o indicador de diferimento (ind_gDif) do CST é igual a 0, significa que este CST não permite a utilização do grupo de diferimento estadual. Se mesmo assim o grupo for informado, a nota será rejeitada com o código 1029.