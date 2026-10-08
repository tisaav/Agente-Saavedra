# Operação com ICMS-ST sem informação do CEST.(NT2015/003)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626014-Opera%C3%A7%C3%A3o-com-ICMS-ST-sem-informa%C3%A7%C3%A3o-do-CEST-NT2015-003](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626014-Opera%C3%A7%C3%A3o-com-ICMS-ST-sem-informa%C3%A7%C3%A3o-do-CEST-NT2015-003)  
> **ID:** `360042626014` | **Última Atualização:** 2026-07-22T16:08:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510468478359)

 MENSAGEM:**

[806 - Rejeição]: Operação com ICMS-ST sem informação do CEST.(NT2015/003)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510455058071)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510455060375)

 **Verifique na tela **"Preferências"**, buscando pela **chave "UFNFESEMCEST"** se o seu estado está informado neste parâmetro. Se estiver informado, esta é a principal causa de não estar sendo gerada informação de CEST no XML desta NF-e. Retire então o seu estado do texto e salve esta preferência. Caso não esteja informado nenhum estado, verifique o próximo passo desta solução.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510468487831)

 **Acesse: *Configurações » Cadastros » Produtos*

**Aba:** Impostos

- Campo: "**Código Especificador ST"**:' [**Preencher o campo, com o valor correspondente a Tabela**]

- Caso a empresa trabalhe com "**Impostos por Empresa"**, acesse a aba: **"Impostos/Informações ****por Empresa"** no cadastro de Produto e preencha o campo "**Código Especificador ST**:" de acordo com a empresa da nota.

- Quando a Substituição Tributária for realizada na compra, no cadastro do produto o campo Tipo de Substituição precisa estar preenchido como Revenda com Substituição Tributária (ST na Compra).

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510468493719)

 **Após o ajuste, redigite os itens na nota ou fature o pedido novamente. Gere o lote da NF-e e a mesma será autorizada.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510455072151)

 OBSERVAÇÕES:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510455060375)

 Caso não localize esse campo na tela de cadastro de produtos, acesse a opção "**Configuração da tela"** » Configurações. Digite "Cód" dentro de 'Campos Disponíveis' » Selecione o campo "**Código Especificador ST"** e arraste para o lado direito 'Campos Selecionados', através da seta "adicionar campo".

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510468487831)

 Caso não tenha a informação do CEST correspondente aos produtos será necessário acesso a Tabela do Código Especificador da Substituição Tributária disponível no link [https://www.codigocest.com.br/](https://www.codigocest.com.br/). Caso não encontre o código que necessita, poderá verificar com sua contabilidade.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510468493719)

 ([NT2015/003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=pLuHNFf7xvE=)) - Nota técnica

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510455073815)

 CAUSA:**

Quando for emitida uma NF-e de operação sem a informação do Código Especificador da Substituição Tributária (CEST), e o CST ou o CSOSN de ICMS for um da lista abaixo, será retornado a rejeição.

********

| CST | DESCRIÇÃO |
| --- | --- |
| 10 | Tributada com cobrança de ICMS por substituição tributária. |
| 30 | Isenta ou não tributada com cobrança de ICMS por substituição tributária. |
| 60 | ICMS cobrado anteriormente por substituição tributária. |
| 70 | Com redução de base de cálculo e cobrança de ICMS por substituição tributária. |
| 90 | Outros, desde que com a TAG vICMSST |

 

Para empresas optantes pelo Simples Nacional:

********

| CSOSN | DESCRIÇÃO |
| --- | --- |
| 201 | Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por substituição tributária. |
| 202 | Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por substituição tributária. |
| 203 | Isenção de ICMS do Simples Nacional para a faixa de receita, com cobrança do ICMS por substituição tributária. |
| 500 | ICMS cobrado anteriormente por substituição tributária ou por antecipação. |
| 900 | Outros, desde que com a TAG vICMSST. |