# 1091 Rejeição: Total de CBS difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141614368919-1091-Rejei%C3%A7%C3%A3o-Total-de-CBS-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141614368919-1091-Rejei%C3%A7%C3%A3o-Total-de-CBS-difere-da-soma-dos-itens)  
> **ID:** `37141614368919` | **Última Atualização:** 2026-07-22T14:19:00Z

---

1091 - Rejeição: Total de CBS difere da soma dos itens

 

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/37141614362391)

**SITUAÇÃO**

  Esta rejeição ocorre ao tentar transmitir ou aprovar uma NF-e ou NFC-e, quando o sistema identifica que o valor total da CBS (Contribuição sobre Bens e Serviços) informado no documento fiscal não corresponde à soma dos valores de CBS calculados nos itens individuais da nota.

 

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/37141597913111)

**SOLUÇÃO**

  Para corrigir esta rejeição, siga os procedimentos abaixo, verificando tanto as configurações do TOP quanto os dados da nota:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37141597913751)

  Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/37141614364183)

  Localize o **"Tipos de Operação - TOP"** utilizado na nota fiscal rejeitada e abra-o para edição.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/37141614364439)

  Na aba **"Impostos"**, na seção **"Reforma Tributária"**, verifique se o campo **"Tem CBS"** está habilitado.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/37141614365079)

  Salve as alterações realizadas no **"Tipos de Operação - TOP"**.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/37141597914135)

  Se o erro persistir, acesse a **"Central de Vendas"** (Comercial >> Consulta >> Central de Vendas), localize a NF-e e verifique os dados de imposto de cada item (clicando em **"Outras Opções do Item"** > **"Consultar/Alterar Dados de Imposto do Item"**) para validar a base de cálculo e alíquota de CBS.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/37141614366359)

  Realize o recálculo dos totais da nota fiscal para garantir a consistência dos valores.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/37141614366871)

  Caso a inconsistência persista, inutilize a NF-e rejeitada, exclua o registro e realize um novo lançamento da nota fiscal.

 

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/37141597914775)

**CAUSA**

  A rejeição 1091 ocorre devido a uma divergência entre o valor total da CBS declarado no totalizador da nota fiscal e a soma dos valores de CBS calculados nos itens individuais. Esta inconsistência pode ser causada por:

- O cálculo da CBS não estar configurado para ser proporcional aos itens no **"Tipos de Operação - TOP"** utilizado;

1. Erro de arredondamento ou truncamento nos cálculos dos impostos;

1. Configuração incorreta da alíquota de CBS no cadastro de alíquotas;

1. Base de cálculo da CBS incorreta em um ou mais itens da nota;

1. Alteração manual indevida nos valores de CBS que não foram refletidas no total do documento.

  De acordo com as regras da Reforma Tributária (Lei Complementar 214/2025), os valores de CBS devem ser calculados corretamente para cada item e o total do documento deve corresponder exatamente à soma dos valores de CBS de todos os itens.