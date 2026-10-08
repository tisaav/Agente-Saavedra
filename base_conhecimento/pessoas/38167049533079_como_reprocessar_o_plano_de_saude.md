# Como reprocessar o plano de saúde?

> **Módulo:** Pessoas+ | **Subseção:** Plano de Saúde  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079-Como-reprocessar-o-plano-de-sa%C3%BAde](https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079-Como-reprocessar-o-plano-de-sa%C3%BAde)  
> **ID:** `38167049533079` | **Última Atualização:** 2026-09-27T18:37:11Z

---

**Módulo: **Pessoal+
**Versão: **5.82.0
**Caminho de Acesso: **Pessoal+ > Rotinas Folha > Gerenciador de Folhas 
**ID da Tela:** br.com.sankhya.rh.GerenciadorFolha

 

### **Descrição e Usabilidade**

Esta funcionalidade permite **reprocessar os dados de plano de saúde** de funcionários e dependentes **a partir dos eventos lançados em movimento e calculados na folha**.

O objetivo é **preencher automaticamente os cadastros de plano de saúde** quando existirem descontos em folha, mas não houver cadastro correspondente, garantindo **consistência entre movimento, folha, cadastro e eSocial**, sem a necessidade de ajustes manuais.

 

### **Pré-requisitos**

#### **Permissões necessárias**

- 

Possuir acesso às telas:

  - 

Gerenciador de Folhas;

  - 

Configuração Funcionários;

  - 

Central do eSocial.

📌 O reprocessamento considera **apenas as empresas às quais o usuário já possui acesso**.

 

#### **Condições obrigatórias**

- 

Existirem **eventos de desconto de plano de saúde** lançados em movimento e calculados em folha;

- 

Funcionários e/ou dependentes **sem plano de saúde cadastrado**, mas com evento de desconto.

 

### **Jornada de Uso**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38167087451671)

 **Acessar o Gerenciador de Folhas**

1. 

Acesse a tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha) e clique no botão **Reprocessar plano de saúde **ao lado direito da tela.

![reprocessar-planosaudebt.png](https://ajuda.sankhya.com.br/hc/article_attachments/38196709265431)

1. 

No pop-up apresentado, serão exibidas **as empresas às quais o usuário tem acesso**.

1. 

Selecione uma ou mais empresas.

1. 

Selecione a **Referência inicial**;

⚠️O período não pode ser **anterior a 2025** nem **posterior ao ano informado**;

A partir desse período, o sistema define a **Referência inicial do Plano de Saúde** para colaboradores e dependentes ajustados.

1. 

Após preencher todos os campos, clique em **Iniciar reprocessamento**.

![reprocessamento-planosaude1.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38196709267863)

O sistema exibirá a mensagem de confirmação:

***"Atenção!***

***Os cadastros de plano de saúde de funcionários e dependentes sem cadastro serão atualizados com base nos eventos do período selecionado.***
***Esta ação é irreversível."***

Ao confirmar a ação, o sistema automaticamente:

- 

preenche o **código do plano de saúde** no cadastro do funcionário conforme o plano vinculado ao evento;

- 

define a **Referência inicial **do Plano de Saúde conforme o período informado;

- 

Marca automaticamente:

  - 

**Possui Plano de Saúde** no cadastro do funcionário;

  - 

**Dependente de Convênio Médico **no cadastro do dependente;

- 

Mantém os dados **inalterados** caso o plano já esteja corretamente cadastrado.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38185292382999)

 Processamento em lote**

- 

É possível selecionar **mais de uma empresa**;

- 

O sistema aplica o reprocessamento **em lote**, seguindo as mesmas regras para todas as empresas selecionadas.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38185292382999)

 Validações importantes**

- 

Se nenhuma empresa ou período for informado, o sistema exibirá uma mensagem de aviso solicitando o preenchimento;

- 

O reprocessamento **não altera folhas**, **não exige bloqueio/desbloqueio** e **não interfere em cálculos já realizados**.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38185292385687)

 Integração com o eSocial**

Após o ajuste, acesse a **Central do eSocial** (Pessoal+ > Rotina Folha) para gerar e enviar a **retificação do evento S-1210** dos períodos impactados.

As informações de plano de saúde são enviadas no grupo:
**infoIRComplem > planSaude**;

⚠️ Não é necessário refazer cálculos, nem reabrir a folha.

 

### **Pontos de Atenção**

- 

O processo é **irreversível**.

- 

Utilize apenas quando houver **desconto de plano de saúde sem cadastro correspondente**.

- 

Recomenda-se executar o reprocessamento **antes de novos envios ao eSocial**.

 

### **Dicas de Usabilidade**

- 

Verifique previamente se os eventos de plano de saúde estão corretos.

- 

Use o reprocessamento para **regularizar cadastros antigos ou incompletos**.

- 

Após o processamento, utilize a **Central do eSocial** para conferir as retificações geradas.

 

### **Artigos relacionados**

- [Cadastro e Vínculo de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)

- [Configuração de Tabelas de Faixas para Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519)

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)

- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)

- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)

- [Correção de dados do IRRF no eSocial (S-1210) para anos anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223)


---

### 🔗 Links e Referências Internas:

- [Cadastro e Vínculo de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)
- [Configuração de Tabelas de Faixas para Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)
- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)
- [Correção de dados do IRRF no eSocial (S-1210) para anos anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223)