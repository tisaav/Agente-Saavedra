# Ação de Database - Analytics Studio

> **Módulo:** Inteligência e Análise | **Subseção:** Ações e automações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/28045566571799-A%C3%A7%C3%A3o-de-Database-Analytics-Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/28045566571799-A%C3%A7%C3%A3o-de-Database-Analytics-Studio)  
> **ID:** `28045566571799` | **Última Atualização:** 2026-09-23T17:35:14Z

---

No [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio), as Ações de Database permitem executar diretamente operações como INSERT, UPDATE e DELETE nos registros do banco de dados, usando componentes como labels, tabelas e listas. 

![AcaodeDatabaseGeralSankhya.png](https://ajuda.sankhya.com.br/hc/article_attachments/28045566568855)

### **Como Adicionar uma Ação de Database**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28046984171415)

 **No componente desejado, acesse a área de** "Interações"**.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28046984178455)

 **Selecione a opção **"Ação de Database"**. Escolha entre criar uma nova ação ou selecionar uma ação de database já existente.

### **Configuração da Ação de Database**

Ao configurar uma ação de database, a interface exibirá os seguintes elementos:

- 
**Dicionário de Dados:** no lado direito, será exibido o dicionário com todas as tabelas e colunas disponíveis para manipulação via INSERTS, UPDATES e DELETES.

- 
**Variáveis de Filtro e Input: **todas as variáveis do contexto da tela e variáveis de input configuradas estarão disponíveis. Isso permite o uso de informações dinâmicas, como filtros aplicados ou dados inseridos pelo usuário, diretamente nas suas ações de database. Para mais detalhes sobre as variáveis, acesse o artigo [VIEW de SQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/28074561568023-VIEW-de-SQL).

### **Teste de Script**

Depois de configurar sua ação de database, é possível testar os scripts para garantir que estão funcionando conforme o esperado. Isso envolve testar o DML (Data Manipulation Language) e verificar se os comandos INSERT, UPDATE ou DELETE estão sendo executados corretamente. Após o teste, confirme a configuração da ação e o script será ativado nas interações do componente.

### **Exemplos**

**Deletando Vendedores**

Neste exemplo, será configurada uma ação de database para deletar vendedores diretamente de uma lista.

- 
**Componente:** lista de vendedores.

- 
**Interação: **ao clicar em um botão **"Excluir"**, a ação de database executa o seguinte script:

```text
DELETE FROM CAD_1026 WHERE ID = :ID_VENDEDOR
```

No script acima, :ID_VENDEDOR é uma variável que captura o ID do vendedor selecionado na lista. O sistema de variáveis do Analytics Studio garantirá que o delete seja aplicado corretamente.

#### **Criando Vendedores a partir de Inputs**

Neste caso, serão adicionados os inputs na tela (por exemplo, para nome, cidade, e salário do vendedor). Ao clicar no botão** "Salvar"**, a ação de database executará um INSERT com base nos valores desses inputs.

- 
**Componente:** Inputs de nome, cidade e salário.

- 
**Interação:** ao clicar no botão **"Salvar"**, a ação de database executa o script:

```text
INSERT INTO CAD_1026 (ID, DESCR, FOTO)

SELECT (MAX(ID)+1) AS ID, :INPUT__310, :INPUT__311

FROM CAD_1026
```

As variáveis :INPUT_310 e :INPUT_311 são preenchidas pelos valores dos inputs na tela.

#### **Atualização de Tarefa**

Neste exemplo, tem-se uma lista de tarefas, e cada tarefa possui um botão de **"Concluir"**. Ao clicar nesse botão, um UPDATE será feito para marcar a tarefa como concluída.

- 
**Componente:** Lista de tarefas com um botão Concluir.

- 
**Interação:** Ao clicar no botão Concluir, a ação de database executa o seguinte script:

```text
UPDATE CAD_1024 SET ID_STATUS = 2 WHERE ID = :ID_TAREFAS
```

A variável :ID_TAREFA é obtida a partir da linha selecionada na lista.

#### **Sequência de DML**

Em uma ação de database, é possível múltiplos comandos DML. Por exemplo, ao trabalhar com uma lista de tarefas, pode-se criar uma ação de database para marcar uma tarefa como concluída e, ao mesmo tempo, registrar essa tarefa na lista de tarefas concluídas.

- 
**Componente:** uma lista com as tarefas e outra lista com as tarefas concluídas.

- 
**Interação:** ao clicar no botão **"Concluir"**, a ação de database executa os seguintes scripts:

#### **UPDATE**

Primeiro, o status da tarefa é atualizado para **"Concluída"** na lista original de tarefas.

```text
UPDATE CAD_1024 SET ID_STATUS = 2 WHERE ID = :ID_TAREFAS
```

Aqui, :ID_TAREFA captura o ID da tarefa que está sendo concluída. A coluna STATUS da tarefa é alterada para Concluída.

#### **INSERT**

Em seguida, a tarefa é registrada na lista de tarefas concluídas.

```text
INSERT INTO CAD_1050 (ID, DESCR)

SELECT ID, DESCR, FROM CAD_1024 WHERE ID = :ID_TAREFAS
```

As informações da tarefa são copiadas da lista original de tarefas. A variável :ID_TAREFAS garante que a tarefa correta seja copiada para a lista de tarefas concluídas.

Assim, pode-se configurar a sequência de scripts em uma única ação de database, que serão executados na ordem definida.

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28156489363223)

 Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)


---

### 🔗 Links e Referências Internas:

- [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
- [VIEW de SQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/28074561568023-VIEW-de-SQL)
- [Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)