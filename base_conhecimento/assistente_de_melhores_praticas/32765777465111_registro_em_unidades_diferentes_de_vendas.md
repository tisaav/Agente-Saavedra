# Registro em Unidades Diferentes de Vendas

> **Módulo:** Assistente de Melhores Praticas | **Subseção:** Compras  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32765777465111-Registro-em-Unidades-Diferentes-de-Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/32765777465111-Registro-em-Unidades-Diferentes-de-Vendas)  
> **ID:** `32765777465111` | **Última Atualização:** 2026-07-22T14:30:28Z

---

### Descrição

A Unidade padrão dos produtos é aquela normalmente utilizada para as vendas e sobre a qual incidem os controles de custo, estoque e preço. No entanto, é possível registrar **unidades alternativas** para produtos cuja compra é realizada em volumes diferentes, como caixas ou fardos.

Essa funcionalidade permite:

- Coletar e aplicar unidades alternativas a produtos que ainda não possuem esse tipo de configuração.

- Definir se a unidade alternativa será utilizada como unidade de compra.

- Informar a quantidade equivalente entre as unidades e o fator de conversão (divisor ou multiplicador).

### Como instalar

1. Serão exibidos todos os produtos ativos que ainda não possuem unidades alternativas cadastradas.

1. Utilize filtros por **unidade, produto ou grupo** para facilitar a busca.

1. Selecione um ou mais produtos e clique em **"Atualizar Unidade Alternativa"**.

1. 

Um pop-up será aberto para preencher os dados:

4.1** Unidade Alternativa** (selecionada do cadastro)

4.2** Unidade de Compra** (Sim/Não – default: Sim)

4.3** Divide ou Multiplica** (com orientação de uso)

4.4** Quantidade** (fator de equivalência)

1. Será exibida a lista dos produtos com as unidades alternativas configuradas, para conferência.

1. Revise a grade e clique em **"Instalar"** para concluir a aplicação das alterações.

### Detalhes da instalação

**Tabela `TGFVOA` – Unidades Alternativas**

- Inclui registros de unidades alternativas para os produtos selecionados

- Os campos definidos são:

- `CODPROD`: Código do produto

- `CODVOL`: Unidade alternativa selecionada

- `DIVIDEMULTIPLICA`: M (multiplica) ou D (divide)

- `MULTIPVLR`: Quantidade informada

- `ATIVO` = S

**Tabela `TGFPRO` – Produtos**

- Para os produtos cuja opção "**Unidade de Compra**" foi marcada:

- Atualiza o campo `CODVOLCOMPRA` com a unidade alternativa definida

 

**

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32765762022935)

 Vale saber**

É crucial revisar cuidadosamente a lista de produtos com unidades alternativas configuradas antes de clicar em "Instalar". Certifique-se de que todas as quantidades e fatores de conversão estão corretos para evitar discrepâncias no controle de estoque e custos, impactando diretamente a lucratividade do seu negócio.