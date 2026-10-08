# 267 Rejeição: Chave de Acesso referenciada inexistente.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098162779543-267-Rejei%C3%A7%C3%A3o-Chave-de-Acesso-referenciada-inexistente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098162779543-267-Rejei%C3%A7%C3%A3o-Chave-de-Acesso-referenciada-inexistente)  
> **ID:** `37098162779543` | **Última Atualização:** 2026-07-22T14:20:19Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098176294295)

 **MENSAGEM**

267 Rejeição: Chave de Acesso referenciada inexistente.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098162765591)

 **SITUAÇÃO**

Esta rejeição ocorre quando você tenta emitir uma NF-e que referencia outra nota fiscal (como em casos de devolução, complemento ou nota de crédito/débito), mas a chave de acesso da nota referenciada não foi encontrada na base de dados da SEFAZ, ou seja, a nota referenciada ainda não foi autorizada ou não existe.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098162766743)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098162767895)

 Acesse a tela ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098162768663)

 Verifique o status da NF-e que está sendo referenciada está como **''Aprovada''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098176303383)

 Se a nota referenciada foi emitida em **contingência** (tpEmis=2, 4 ou 5), primeiro regularize-a para que seja aprovada pela SEFAZ, e só depois emita a nova nota que a referencia.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098162772759)

 Na aba **''NF-e/NFS-e''** verifique se o campo **''Chave NF-e referenciada'' **está informado corretamente com a chave de acesso.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098162774039)

 Caso a nota esteja emitindo uma** devolução**, acesse a tela ****[''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)** **(Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37989923996951)

 Na aba **''NF-e/NFC-e/CF-e''**, verifique se o campo **''NF-e'' **está configurado com a finalidade correta.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38193737990935)

 Após confirmar que a nota referenciada está **aprovada** e a chave está **correta**, gere novamente o lote da NF-e que estava sendo rejeitada.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098162775191)

 **CAUSA**

Esta rejeição ocorre quando uma NF-e é emitida referenciando a chave de acesso de outra NF-e (modelo 55) que ainda não foi autorizada ou não existe na base de dados da SEFAZ. Isso pode acontecer nos seguintes casos: 

- 

A NF-e referenciada ainda está em processamento ou foi rejeitada;

- 

A NF-e referenciada foi emitida em contingência e ainda não foi regularizada;

- 

A chave de acesso informada está incorreta ou com dígito verificador inválido;

- 

Tentativa de emitir uma nota de devolução antes da aprovação da nota de venda original.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38479257493143)

 OBSERVAÇÃO:** Para notas complementares (finNFe=2), a regra de validação é diferente e permite a emissão mesmo que a nota original ainda não tenha sido autorizada.


---

### 🔗 Links e Referências Internas:

- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)