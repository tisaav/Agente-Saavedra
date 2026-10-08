# CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043196813-CFOP-de-devolu%C3%A7%C3%A3o-de-mercadoria-para-NF-e-que-n%C3%A3o-tem-finalidade-de-devolu%C3%A7%C3%A3o-de-mercadoria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043196813-CFOP-de-devolu%C3%A7%C3%A3o-de-mercadoria-para-NF-e-que-n%C3%A3o-tem-finalidade-de-devolu%C3%A7%C3%A3o-de-mercadoria)  
> **ID:** `360043196813` | **Última Atualização:** 2026-07-22T16:06:46Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512580530839)

 MENSAGEM:**

[328 - Rejeição]: CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512580535831)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512580540055)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*

- Aba: **"NF-e/NFC-e"**

- Campo **"NF-e":** Devolução ou Complementar

 

![CFOP_de_devolu__o_de_mercadoria_para_NFe_que_n_o_tem_finalidade_de_devolu__o_de_mercadoria.png](https://ajuda.sankhya.com.br/hc/article_attachments/14626263946647)

 

A rejeição ocorre porque está sendo utilizada uma CFOP de DEVOLUÇÃO e no cadastro da TOP o campo "**NF-e"** da aba Impressão foi definido diferente de 'Devolução' ou 'Complementar'. 

Após o ajuste, inutilize a numeração da nota e gere uma nova.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512580541463)

 Caso a NF-e emitida não seja uma devolução, por exemplo, um retorno de remessa, revise o CFOP utilizado.

Sintonize junto ao seu contador o CFOP correto e realize os devidos ajustes:

- Tela **"[Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" **(Caminho de acesso: *Comercial » Arquivo » Cadastros/Financeiro » Arquivos » Cadastros*)

- Aba **"Livro Fiscal", **Campo **: ** **"CFOP'S"**;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512580543767)

 Caso não se trate de uma **NF-e de Estorno,** o campo abaixo deve estar desmarcado.

- Tela **"Tipo de Operação - TOP"**  » aba **"NF-e/NFC-e"**
Campo **"NF-e de estorno": **desmarcado

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512580545047)

 Após ajustes na TOP, a nota deve ser inutilizada/excluída e um novo faturamento realizado.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512607708567)

 CAUSA:**

Quando for emitida uma NF-e com CFOP de Devolução de Mercadoria e a Finalidade da NF-e (finNFe) for diferente de 2 - "NF-e Complementar" ou 4 - "Devolução de Mercadoria", será retornada a rejeição "328 - CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria".

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512580549655)

 OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)) - Nota técnica


---

### 🔗 Links e Referências Internas:

- [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)