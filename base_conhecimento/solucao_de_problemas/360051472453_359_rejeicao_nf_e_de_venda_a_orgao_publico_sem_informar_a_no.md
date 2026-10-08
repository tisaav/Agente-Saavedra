# 359 - Rejeição: NF-e de venda a Órgão Público sem informar a Nota de Empenho

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360051472453-359-Rejei%C3%A7%C3%A3o-NF-e-de-venda-a-%C3%93rg%C3%A3o-P%C3%BAblico-sem-informar-a-Nota-de-Empenho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051472453-359-Rejei%C3%A7%C3%A3o-NF-e-de-venda-a-%C3%93rg%C3%A3o-P%C3%BAblico-sem-informar-a-Nota-de-Empenho)  
> **ID:** `360051472453` | **Última Atualização:** 2026-07-22T15:30:42Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15936614611735)

 MENSAGEM**:

359 - Rejeição: NF-e de venda a Órgão Público sem informar a Nota de Empenho.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15936576368919)

 CAUSA:**

NF-e com desoneração de ICMS motivada por venda a Órgão Público (**<motDesICMS>8</motDesICMS>**), sem informar Nota de Empenho.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15936614615191)

 SOLUÇÃO:**

Ao emitir uma NF-e que possui o campo motDesICMS = 8 (Desoneração de ICMS motivada por venda a órgão público), devemos obrigatoriamente informar a nota de empenho.

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15936576370967)

 Preencher, no cabeçalho da nota emitida, o campo "**Nota de Empenho**":

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15936576199063)

- Caso não localize esse campo, acesse a tela 'Configurador de Layout da nota' e adicione o mesmo. Para mais detalhes: [Como inserir um campo no layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973-Como-inserir-um-campo-no-layout-da-nota-)

**

![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15936614617879)

 Importante:**

********

| Caso a 'Nota de Empenho não deva ser informada, será necessário realizar os devidos ajustes no campo "Cód.Mot.Desoneração ICMS" da aba 'Geral' da regra de ICMS utilizada, inserindo um código diferente de [8], conforme as orientações do Contador (Tela: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS). Feito isso, refaça o faturamento. |
| --- |

 

**

![4](https://ajuda.sankhya.com.br/hc/article_attachments/15936576372503)

 OBSERVAÇÕES:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15936576375575)

 Implementação opcional, a critério da UF.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15936614621463)

 [Manual de Orientação do Contribuinte.](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)


---

### 🔗 Links e Referências Internas:

- [Como inserir um campo no layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973-Como-inserir-um-campo-no-layout-da-nota-)