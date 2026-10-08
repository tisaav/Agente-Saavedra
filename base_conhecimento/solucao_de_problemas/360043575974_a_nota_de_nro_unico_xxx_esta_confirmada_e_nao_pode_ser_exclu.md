# A nota de Nro. Único XXX está confirmada e não pode ser excluída pelo Portal de importação de XML

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575974-A-nota-de-Nro-%C3%9Anico-XXX-est%C3%A1-confirmada-e-n%C3%A3o-pode-ser-exclu%C3%ADda-pelo-Portal-de-importa%C3%A7%C3%A3o-de-XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575974-A-nota-de-Nro-%C3%9Anico-XXX-est%C3%A1-confirmada-e-n%C3%A3o-pode-ser-exclu%C3%ADda-pelo-Portal-de-importa%C3%A7%C3%A3o-de-XML)  
> **ID:** `360043575974` | **Última Atualização:** 2026-07-22T16:02:14Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16170925418775)

**MENSAGEM**

O sistema pode apresentar diferentes mensagens de erro ao tentar excluir uma nota fiscal:

- 

**"[CORE_E04305] A nota de Nro. Único XXX está confirmada e não pode ser excluída pelo Portal de importação de XML".**

- **A nota é NFe/NFSe e não pode ser excluida, deve ser cancelada. (Emissão Própria).**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16170974219543)

**SOLUÇÃO**

A solução varia conforme o tipo de vínculo que impede a exclusão:

**Cenário 1: Nota no Portal de Importação de XML**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16170925422487)

 No **"Portal de Importação de XML"** (Comercial >> Portal de Importação de XML), selecione a opção **"Abrir Documento"** para o registro.

![Portal de importação](https://ajuda.sankhya.com.br/hc/article_attachments/14692241691543)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16170925424791)

 Exclua o documento através da **"Central de Compras"** (Comercial >> Central de Compras).
 

**Cenário 2: Nota importada no Portal de Vendas (Emissão Própria).**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16170925422487)

 Acesse a tela **"Portal de vendas"** (Comercial >> Consulta).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16170925424791)

 As notas de **emissão própria** são inseridas no sistema já com o status **"Aprovada"**. Por esse motivo, elas não podem ser excluídas, apenas **canceladas**.

Para realizar o cancelamento, basta acessar o **Portal de Vendas**, selecionar a nota desejada e utilizar o **botão "Cancelar"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41815319925271)

 

Obs.: Clicar no botão Doc > documentos relacionados. Se tiver documento relacionado precisa desvincular 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16170925429015)

**CAUSA**

Ao excluir um registro no **Portal de Importação de XML**, caso esse registro possua o **Nro. Único da Nota** informado, será apresentada uma mensagem questionando se deseja excluir também a nota vinculada. Caso o usuário opte por prosseguir e a nota ainda não esteja confirmada, ela será excluída. Caso contrário, a mensagem informativa será exibida.