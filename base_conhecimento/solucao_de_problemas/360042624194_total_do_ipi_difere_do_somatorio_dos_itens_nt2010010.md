# Total do IPI difere do somatório dos itens (NT2010/010)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624194-Total-do-IPI-difere-do-somat%C3%B3rio-dos-itens-NT2010-010](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624194-Total-do-IPI-difere-do-somat%C3%B3rio-dos-itens-NT2010-010)  
> **ID:** `360042624194` | **Última Atualização:** 2026-07-22T16:08:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447570415639)

 MENSAGEM:**

[538-Rejeição]: Total do IPI difere do somatório dos itens (NT2010/010).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447548917399)

 SOLUÇÃO:**

Para correção siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447548920343)

 Acesse "****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)" (Caminho de acesso: *Comercial » Preferências » Empresa*), Aba: "**Propriedades"** e verifique se o campo: "**Trabalha com IPI" ** está marcado (se equiparado a Indústria);

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447570431895)

 Acesse "****[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)" (Caminho de acesso: *Configurações » Cadastros » Parceiros*), Aba: "**Fiscal"** e verifique o campo: "**Código Sit.Trib.IPI** **Saída**:" está preenchido com: 99- Outras Saídas

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447570434199)

 Acesse "****[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)" (Caminho de acesso: *Configurações » Cadastros » Produtos*), Aba: "**Impostos"** e confirmar os itens:

- "**Tem IPI na venda**" = marcado

- "**Tem IPI na Compra"** = marcado

- 
**"Código Sit.Trib.IPI Saída**:" = 99-Outras Saídas

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447548926743)

 Acesse *Configurações » Cadastros » Produtos* e verifique no Produto o Código do IPI, e pesquise o nesta tela e ajuste os campos:

- 
**"Cód.Sit.Trib.IPI Saída:**"= 99-Outras Saídas

- 
**"Cód.Sit.Trib.IPI Entrada:"** = 49-Outras Entradas

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447548928663)

 Após o ajuste, gere uma nova nota de Devolução e um Lote.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447548929687)

 OBSERVAÇÃO: **

Deve consultar o contador da empresa para saber qual** **Cód.Sit.Trib.IPI correto a ser usado no seu lançamento.

** **

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447548931351)

 CAUSA:**

Quando for emitida uma NF-e com o Total do IPI da NF-e diferente do somatório do valor do IPI de cada item, será retornado a rejeição.

O cálculo do Total do IPI é feito a partir do somatório do valor do IPI de cada item.

Dependendo do Cód.Sit.Trib.IPI usado no lançamento, o IPI será calculado no sistema e não será carregado para o XML, por ser uma CST de IPI não prevista no grupo de tags.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447548929687)

 OBSERVAÇÃO:**

([NT2010/010](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AtaVevRXCIQ=)) Nota Técnica.


---

### 🔗 Links e Referências Internas:

- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)