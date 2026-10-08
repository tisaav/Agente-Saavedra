# 745 Rejeição: NF-e sem grupo do PIS [nItem:nnn]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141291328535-745-Rejei%C3%A7%C3%A3o-NF-e-sem-grupo-do-PIS-nItem-nnn](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141291328535-745-Rejei%C3%A7%C3%A3o-NF-e-sem-grupo-do-PIS-nItem-nnn)  
> **ID:** `37141291328535` | **Última Atualização:** 2026-07-22T14:19:37Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141291321879)

 **MENSAGEM**

745 Rejeição: NF-e sem grupo do PIS [nItem:nnn]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141342802583)

 **SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e), o sistema não incluiu as informações do grupo do PIS para um ou mais itens da nota. A SEFAZ rejeitou o documento fiscal, indicando qual item específico está sem a informação necessária através do número informado após "nItem:".

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141291322391)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141342803351)

 Acesse as telas** ''Alíquotas de PIS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141342803863)

 Verifique no campo **''Cód. sit. tributária''**, se a alíquota de PIS no item rejeitado está corretamente configurada para a operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141342804119)

 Acesse a tela ****[''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e identifique qual item está com problema.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141291323671)

 Selecione a nota rejeitada, clique no botão **"NF-e"** e selecione a opção **"Gerar XML da NF-e em arquivo para Conferência"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141291323927)

 Abra o XML gerado com o Internet Explorer ou Bloco de Notas e pressione **Ctrl+F** para buscar o número do item indicado na rejeição (nItem:nnn).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141291324951)

 Acesse a tela** ''Produtos''** (Configurações » Cadastros » Produtos » Produtos).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141291326231)

 Na aba **''Impostos''** verifique se o campo **''Grupo PIS''** está configurado corretamente.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38051312088471)

 Além disso, acesse a tela** ''Tipos de Operação - TOP'' **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a TOP utilizada está com as opções **"Tem PIS"** e **"Tem COFINS"** devidamente habilitadas.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38750002619287)

 Após os ajustes necessários, exclua o item da nota e faça o lançamento novamente ou fature o pedido novamente para gerar um novo lote.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141291326743)

 **CAUSA**

Quando for emitida uma NF-e sem as informações do grupo do PIS para um ou mais itens, a SEFAZ rejeitará o documento. Esta rejeição ocorre porque, de acordo com a legislação fiscal, é **obrigatório** informar os dados de tributação do PIS para cada item da nota fiscal, mesmo que seja uma situação de isenção, não incidência ou suspensão. A ausência dessas informações impede a correta validação e processamento do documento fiscal pelos sistemas da SEFAZ.


---

### 🔗 Links e Referências Internas:

- [''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)