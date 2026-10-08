# Nota não possui informações sobre COFINS e esta informação é obrigatória para NF-e

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657513-Nota-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-COFINS-e-esta-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657513-Nota-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-COFINS-e-esta-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-NF-e)  
> **ID:** `360043657513` | **Última Atualização:** 2026-07-22T16:04:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521773975)

 MENSAGEM:**

Nota não possui informações sobre COFINS e esta informação é obrigatória para NF-e.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136502073239)

 SITUAÇÃO:**

Ao tentar confirmar/aprovar uma NF-e de Venda, Devolução de Compra (Emissão Própria), ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521781015)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136535941655)

 Tela **"[Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)" ***(Comercial » Arquivos » Cadastros)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521782807)

 Aba **"Impostos",** Campo **"Tem COFINS": **marcado

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521782807)

 Aba **"Livro Fiscal"**, Campo **"Atualização de Livro de ICMS": **diferente de Não Atualiza

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136502076823)

 Tela **"[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)" ***(Comercial » Preferências)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521782807)

 Aba **"Propriedades"**,  Campo **"Calcula COFINS": **marcado

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521785495)

 Tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** *(Configurações » Cadastros)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521782807)

 Aba **"Impostos"**, Campo **"Grupo COFINS": **informe o grupo

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521788567)

 Tela** "[Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS)"** (Caminho para acesso: *Comercial » Arquivo » Cadastros » Alíquotas)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521782807)

 Crie uma Alíquota de COFINS, considerando o tipo de Movimento e os campos (*) marcados como obrigatórios.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521782807)

 Considere selecionar o **Tipo** adequadamente e o **Cód. sit. tributária** (seguindo orientações do contador).

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521782807)

 Feito o cadastro, insira o **Grupo** criado no cadastro do Produto, conforme dito no item 3.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136521791127)

 CAUSA:**

Por se tratar de uma Nota Fiscal Eletrônica, é imprescindível que se tenha o cálculo de COFINS. Mesmo que a incidência da Alíquota seja 0(zero), é preciso criar uma Alíquota com incidência zero, para que no ato da confirmação/aprovação da NF-e seja gerado os dados de COFINS no XML da NF-e.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)
- [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS)