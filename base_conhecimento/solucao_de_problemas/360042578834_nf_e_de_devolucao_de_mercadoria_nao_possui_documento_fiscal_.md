# NF-e de devolução de mercadoria não possui documento fiscal referenciado.(NT2013/005)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042578834-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-n%C3%A3o-possui-documento-fiscal-referenciado-NT2013-005](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042578834-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-n%C3%A3o-possui-documento-fiscal-referenciado-NT2013-005)  
> **ID:** `360042578834` | **Última Atualização:** 2026-07-22T16:09:07Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865677719)

 MENSAGEM:**

[321 - Rejeição]: NF-e de devolução de mercadoria não possui documento fiscal referenciado.(NT2013/005).

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474893523735)

 SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela Central de Vendas no SankhyaW.

Acessando a opção (...)>>Ver Acompanhamento, é possível consultar o detalhe da Rejeição a seguir:

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865686039)

 SOLUÇÃO:**

Para 'Devolução de Compra' ou 'Devolução de Venda' de emissão própria:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474893530135)

 Acesse: a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) *(Caminho de acesso: Comercial » Arquivo » Cadastros*)* » *aba: "**NF-e/NFC-e"**:

-  Campo **"Buscar NF de Origem p/ Referenciar na NF-e": **marque

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474893532823)

 Caso a marcação acima não tenha sido realizada, inutilize a numeração da devolução rejeitada, exclua. Realize a marcação da TOP e refaça o processo de devolução seguindo as orientações do próximo passo.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474893537431)

 Selecione a NF-e de Origem(Venda/Compra), clique no botão **"Devolv./Estor."**, selecione os produtos que serão devolvidos ou toda a nota.

Desta forma, o sistema irá preencher na Nota o 'Grupo de Documentos Referenciados', que significa os dados na nota de origem (Chave NFe <refNFe>).

**Lançamento "Avulso/Manual":**

Caso não possua a nota de origem lançada no sistema, é necessário possuir a chave NF-e referente a mesma e seguir as orientações abaixo:

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865694487)

 No configurador de layout da nota, para o respectivo tipo de movimento da nota de devolução, insira o campo **"Chave NF-e referenciada"**:

 

![NF-e_de_devolu__o_de_mercadoria_n_o_possui_documento_fiscal_referenciado..png](https://ajuda.sankhya.com.br/hc/article_attachments/14500887416727)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865696407)

 Inserido o campo, ao realizar o lançamento da devolução é essencial que esse campo seja devidamente preenchido com a informação referente chave da NF-e de origem. 

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474893551127)

 Confirme a NF-e gerada.

Para os casos nos quais a nota de origem esteja lançada no sistema e a ligação será feita manualmente:

- Acesse no cabeçalho da nota a opção: (...)>>"**Ligar a Devolução com Notas"**, esta opção liga a Devolução com uma Nota de Origem mais recente.

***ou***

- Digite os itens que estão sendo devolvidos na grade de Itens e, posteriormente, ligue a nota de Origem na opção (...) da grade de Itens >>"**Documentos Relacionados"**. Clique para Incluir(+) e informar o "**Número Único"**, "**Sequência do Item"** e "**Quantidade Atendida"**, todos obrigatórios. Estas informações deverão ser devidamente anotadas antes da nota de origem, para a correta ligação entre a Devolução com a Nota de Origem (compra/venda).

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865703063)

 Após o lançamento gere um novo lote da nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474893555095)

 CAUSA:**

Quando for emitida uma NF-e com finalidade igual à "4 - Devolução de mercadoria" e não for informado documento referenciado  que está sendo devolvido, será retornado a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474893557271)

 OBSERVAÇÕES:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865710359)

 ([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=jLEf0c3bSBI=)) - Nota Técnica.

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865710359)

 **Parâmetros**:

**"TOPCONSIGC-TOP para consignação de compra"**

Altera a descrição da Opção: 'Ligar a Devolução com Notas' para 'Ligar a Devolução com Notas de Consignação' 

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474865710359)

 Quando se tratar de uma devolução onde a Nota de Origem não é NF-e e não possui informações desta no sistema, use o campo "**ChaveNFeRef"** na nota de devolução para que seja gerado a devida tag, conforme abaixo:

`<``NFref``>`

`        ``<``refNFe``>99999999999999999999999999999999999999999999</``refNFe``>`

`</``NFref``>`


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)