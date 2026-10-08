# E0496 Rejeição: O CEP informado para o endereço nacional do fornecedor não existe ou não pertence ao município do endereço do fornecedor.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225926563095-E0496-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-fornecedor-n%C3%A3o-existe-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-do-endere%C3%A7o-do-fornecedor](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225926563095-E0496-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-fornecedor-n%C3%A3o-existe-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-do-endere%C3%A7o-do-fornecedor)  
> **ID:** `37225926563095` | **Última Atualização:** 2026-07-22T14:15:28Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225926537879)

 **MENSAGEM**

E0496 Rejeição: O CEP informado para o endereço nacional do fornecedor não existe ou não pertence ao município do endereço do fornecedor.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942940823)

 **SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e, o documento foi **rejeitado pela SEFAZ** com a mensagem E0496, indicando que o **CEP cadastrado para o fornecedor** (emitente) está **incorreto ou não corresponde ao município** informado no endereço do cadastro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942941463)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942943511)

 Acesse a tela ****["Empresas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) (Configurações » Cadastros » Empresas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225926542615)

 Localize a **empresa emitente** da nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942946327)

 Na aba **"Endereço"**, verifique o conteúdo do campo **"CEP"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942947607)

 Confira se o **CEP informado está correto** e se **corresponde ao município cadastrado** no sistema. Para isso:

- 

Acesse o site dos ****[''Correios''](https://buscacepinter.correios.com.br/app/endereco/index.php).[https://buscacepinter.correios.com.br/app/endereco/index.php](https://buscacepinter.correios.com.br/app/endereco/index.php)

- 

Consulte o **CEP correto** usando o endereço completo da empresa.

- 

Verifique se o **município retornado** pela consulta corresponde ao **município cadastrado no sistema**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942947991)

 Caso o CEP esteja incorreto ou não corresponda ao município cadastrado, atualize o campo **“CEP”** com a informação válida obtida na consulta.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225926551319)

 Se necessário, clique no **ícone dos Correios** ao lado do campo ''**CEP''** para preencher automaticamente os campos de endereço.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942948759)

 Após realizar as alterações, **salve** as informações no cadastro da empresa.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225942949015)

 Acesse a tela ****["Central de Vendas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225926552855)

 Localize a nota fiscal rejeitada, redigite os dados do cabeçalho e gere um novo lote para transmissão.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37651066648599)

 Se a nota continuar sendo rejeitada, **inutilize ou exclua a NF-e** rejeitada e refaça o **lançamento do documento fiscal**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225926553623)

 **CAUSA**

A rejeição ocorre quando o **CEP informado no cadastro do fornecedor** (emitente) **não existe na base dos Correios** ou **não pertence ao município** que foi cadastrado no endereço da empresa. A SEFAZ valida se o CEP corresponde ao município informado, e qualquer **divergência entre essas informações** resulta na rejeição do documento fiscal.


---

### 🔗 Links e Referências Internas:

- ["Empresas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas)
- ["Central de Vendas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)