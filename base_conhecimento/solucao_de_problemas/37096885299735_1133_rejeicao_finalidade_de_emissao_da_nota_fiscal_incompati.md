# 1133 Rejeição: Finalidade de Emissão da Nota Fiscal incompatível com o CST [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096885299735-1133-Rejei%C3%A7%C3%A3o-Finalidade-de-Emiss%C3%A3o-da-Nota-Fiscal-incompat%C3%ADvel-com-o-CST-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096885299735-1133-Rejei%C3%A7%C3%A3o-Finalidade-de-Emiss%C3%A3o-da-Nota-Fiscal-incompat%C3%ADvel-com-o-CST-nItem-999)  
> **ID:** `37096885299735` | **Última Atualização:** 2026-07-22T14:21:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096885281687)

 **MENSAGEM**

1133 Rejeição: Finalidade de Emissão da Nota Fiscal incompatível com o CST [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096885281943)

 **SITUAÇÃO**

Ao tentar emitir uma nota fiscal eletrônica (NF-e) com transferência de crédito do IBS ou CBS, o sistema está rejeitando a operação porque a finalidade de emissão da nota fiscal não está configurada corretamente para o Código de Situação Tributária (CST) utilizado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096854482455)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096854483351)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize o tipo de operação que está sendo utilizado na nota fiscal rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096854486807)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique o campo **"NF-e"** e selecione a opção **"Nota de Débito"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096885288599)

 No campo **"Tipo de Nota Fiscal de Débito"**, selecione uma das seguintes opções:

- 

**"01 - Transferência de créditos para Cooperativas"**

- 

**"05 - Transferência de crédito de sucessão"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096885289751)

 Salve as alterações.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096854492951)

 Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária'' **(Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096885291671)

 Verifique se o CST do IBS/CBS utilizado na nota fiscal é compatível com operações de transferência de crédito.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096885293463)

 Certifique-se de que o grupo **"gTransfCred"** esteja sendo informado corretamente na nota fiscal para o CST utilizado.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37960869759767)

 Emita a nota fiscal novamente com as configurações corretas.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096854498583)

 **CAUSA**

Esta rejeição ocorre quando há uma incompatibilidade entre o CST (Código de Situação Tributária) do IBS/CBS informado na nota fiscal e a finalidade de emissão configurada. De acordo com as regras de validação da SEFAZ, quando um CST que exige informação do grupo de Transferência de Crédito (gTransfCred) é utilizado, a finalidade da nota fiscal **deve ser obrigatoriamente** "Nota de Débito" e o tipo de nota de débito deve ser "01 - Transferência de créditos para Cooperativas" ou "05 - Transferência de crédito de sucessão".

A validação UB106-30 da SEFAZ verifica especificamente se, quando informado o grupo IBSCBS\gTransfCred, a finalidade de emissão da nota fiscal (finNFe) é igual a 6 (Nota de Débito). Caso contrário, a nota é rejeitada com o código 1133.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)