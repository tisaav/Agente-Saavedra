# CFOP de saída para NF-e de entrada(NT2010/010)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004553-CFOP-de-sa%C3%ADda-para-NF-e-de-entrada-NT2010-010](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004553-CFOP-de-sa%C3%ADda-para-NF-e-de-entrada-NT2010-010)  
> **ID:** `360043004553` | **Última Atualização:** 2026-07-22T16:10:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455448450583)

 MENSAGEM:**

[519- Rejeição]: CFOP de saída para NF-e de entrada"

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455432085655)

 SOLUÇÃO:**
Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455432092183)

 Acesse a tela: "**[Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"**: (Caminho de acesso:* Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)*

 Aba: "**Livro Fiscal"**

 - Campo "**Atualização de Livro ICMS"**: preencha com a respectiva finalidade da operação.

Campos:

- "**CFOP para FORA do Estado".**

- "**CFOP para DENTRO do Estado**".

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455448461719)

 Insira a CFOP correspondente a Natureza da Operação (preenchimento da tag <natOp>):

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455432103319)

 Se Movimentação de Entrada, CFOP's que inicia com 1, 2 e 3.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455432103319)

 Se movimentação de Saída, CFOP's que inicia com 5, 6 e 7.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455448474647)

 Preencha a informação de 'Atualização de Livro ICMS' dentro do XML a tag <tpNF>, onde 0 = Entrada e 1 = Saída. Dessa forma, a SEFAZ realiza verificação da tag <tpNF> com <CFOP>.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455432112535)

 Após os ajustes, faz-se necessário a inutilização de numeração e exclusão da nota para posterior lançamento de uma nova nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455448486039)

 CAUSA:**

Quando for emitida uma NF-e com CFOP de Saída (iniciado por 5, 6 ou 7) e o Tipo de Operação da NF-e for igual a "0 - Entrada", ocorrerá a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455432119703)

 OBSERVAÇÃO:**

(****[NT2010/010](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AtaVevRXCIQ=)) - Nota Técnica.


---

### 🔗 Links e Referências Internas:

- [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)