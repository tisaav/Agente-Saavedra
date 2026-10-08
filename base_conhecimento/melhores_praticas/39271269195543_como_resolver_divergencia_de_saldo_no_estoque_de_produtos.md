# Como resolver divergência de saldo no estoque de produtos?

> **Módulo:** Melhores Praticas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39271269195543-Como-resolver-diverg%C3%AAncia-de-saldo-no-estoque-de-produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39271269195543-Como-resolver-diverg%C3%AAncia-de-saldo-no-estoque-de-produtos)  
> **ID:** `39271269195543` | **Última Atualização:** 2026-08-31T01:38:51Z

---

Divergências no saldo de estoque podem ocorrer quando o sistema apresenta uma quantidade diferente da quantidade física real. Este artigo explica como identificar e corrigir essas inconsistências, garantindo que o estoque no sistema reflita a realidade do seu armazém.
 

As divergências podem acontecer por diversos motivos, como **geração de cópias de estoque antes da emissão de notas fiscais**, **intervenções diretas no banco de dados**, **desabilitação de triggers do sistema** ou **falhas em integrações**. É fundamental realizar verificações periódicas para manter a acuracidade dos dados.
 

 

### **Identificando a divergência no estoque**

Para identificar divergências de estoque, utilize a tela **"Gerência de Produtos"** (Comercial Arquivo Cadastros Produtos) e verifique as seguintes abas:
 

**Aba "Estoque":** apresenta o saldo atual do produto por empresa e local de armazenamento. Compare este saldo com a quantidade física real.
 

**Aba "Extrato":** exibe todo o histórico de entradas e saídas do produto, permitindo rastrear cada movimentação e identificar onde ocorreu a inconsistência.
 

Também é possível consultar o **"Kardex"** (Comercial Consulta Kardex) para visualizar o histórico detalhado de movimentações e validar se o saldo está correto.
 

 

### **Verificando cópias de estoque desatualizadas**

Um dos cenários mais comuns de divergência ocorre quando a **cópia de estoque é gerada antes da emissão da nota fiscal de saída**. Neste caso, a cópia não reflete a movimentação mais recente, apresentando um saldo incorreto.
 

Para corrigir esta situação, siga os passos:
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39271250171671)

 Acesse o **"Relatório de Cópia de Estoque"** (Comercial Relatórios Estoque Cópia de Estoque) e verifique a data de geração da cópia.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39271250171799)

 Compare a data da cópia com a data de emissão das notas fiscais de entrada e saída do produto.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39271250172567)

 Se identificar que a cópia foi gerada antes de alguma movimentação importante, gere uma **nova cópia de estoque** atualizada.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39271269190167)

 Gere o **"Relatório de Registro de Inventário"** (Estoque Relatórios Registro de Inventário) para validar se o saldo está correto após a nova cópia.

 

 

### **Corrigindo inconsistências através da verificação de saldo**

Para divergências mais complexas, utilize a tela **"Verificação de Saldo de Estoque"** (Estoque Avançado Verificação de Saldo de Estoque). Esta ferramenta identifica automaticamente inconsistências entre os lançamentos realizados nos portais e o saldo registrado no estoque.
 

Ao acessar esta tela, o sistema apresentará linhas com produtos que possuem divergências. Para corrigir:
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39271250171671)

 Identifique o produto com divergência na lista apresentada.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39271250171799)

 Selecione a linha correspondente ao produto. Obs: Se estiverem várias linhas na tela, ao clicar em Corrigir, todas as linhas serão corrigidas e não somente a que foi marcada/selecionada.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39271250172567)

 Clique no **"Botão Corrigir"** para que o sistema ajuste automaticamente o saldo.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39271269190167)

 Verifique novamente na **"Gerência de Produtos"** se o saldo foi corrigido corretamente.

 

### **Prevenindo futuras divergências**

Para evitar divergências de estoque, adote as seguintes práticas:
 

- 

Sempre gere a **cópia de estoque após a emissão das notas fiscais**, garantindo que todas as movimentações estejam refletidas.
 

1. 

Evite **intervenções diretas no banco de dados** sem orientação técnica adequada.
 

1. 

Mantenha os **objetos do sistema (triggers) habilitados** para garantir a integridade dos dados.
 

1. 

Realize **inventários periódicos** para validar a acuracidade do estoque.
 

1. 

Verifique regularmente a tela **"Verificação de Saldo de Estoque"** para identificar e corrigir inconsistências rapidamente.