# Controle de Produtos por Local

> **Módulo:** Assistente de Melhores Praticas | **Subseção:** Estocagem  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32473717131031-Controle-de-Produtos-por-Local](https://ajuda.sankhya.com.br/hc/pt-br/articles/32473717131031-Controle-de-Produtos-por-Local)  
> **ID:** `32473717131031` | **Última Atualização:** 2026-07-30T13:47:05Z

---

### Descrição

A funcionalidade **Controle de Produtos por Local** permite configurar a subdivisão de estoques por local, que otimiza espaço, melhora a precisão do controle e agiliza as movimentações de entrada e saída.

Permite:

- Definir se a empresa deseja controlar estoques por local.

- Criar uma estrutura hierárquica de locais de armazenagem.

- Gerar máscara para controle dos locais.

- Atualizar o cadastro de produtos para utilizar locais.

### Como instalar

1. O sistema verifica automaticamente se já existem **locais cadastrados**.

1. Se houver, a instalação será interrompida com a mensagem: "Impossível prosseguir. Já existe uma estrutura de locais configurada. Ajustes devem ser feitos diretamente no cadastro de Locais."

1. Defina se deseja utilizar a subdivisão de estoques por local:

     3.1 **Sim:** A subdivisão será ativada e os locais poderão ser configurados.

     3.2** Não:** O controle será feito apenas por empresa.

1. Se respondeu **Sim**, monte a hierarquia dos locais usando o componente de árvore com botões de **Adicionar**, **Excluir** e **Renomear**.

1. A estrutura começa com o nó fixo chamado **Locais,** e pode conter até **4 níveis**.

1. Revise a estrutura montada e clique em **Instalar** para concluir.

### Detalhes da instalação

**Parâmetros atualizados**

- 
**UTILIZALOCAL** – Define se a empresa utilizará o controle por local, conforme resposta do usuário.

- 
**MASCLOCAL** – Define a máscara para estrutura dos locais, com base na hierarquia informada:

- Até 5 itens por nível: **1 dígito**.

- Até 50 itens: **2 dígitos**.

- Até 500 itens: **3 dígitos**.

- Até 5000 itens: **4 dígitos**.

- Mais de 5000: **5 dígitos**.

- Se houver espaço disponível nos 9 dígitos, incluir 1 nível extra com 1 dígito.

**Tabelas atualizadas**

**TGFLOC – Cadastro de Locais**

- Registros inseridos conforme a hierarquia definida.

- Campos preenchidos: **CODLOCAL**, **DESCRLOCAL**, **CODLOCALPAI**, **ATIVO = SIM**, **ANALITICO = SIM** (apenas no último nível).

**TGFPRO – Produtos**

- Atualização do campo **USALOCAL = 'S'** para produtos ativos que não sejam de uso interno, com exceção dos serviços (**USOPROD = ‘S'**).