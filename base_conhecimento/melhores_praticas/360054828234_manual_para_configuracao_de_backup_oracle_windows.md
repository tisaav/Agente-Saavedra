# Manual para configuração de Backup Oracle Windows

> **Módulo:** Melhores Praticas | **Subseção:** Configurações Sankhya  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360054828234-Manual-para-configura%C3%A7%C3%A3o-de-Backup-Oracle-Windows](https://ajuda.sankhya.com.br/hc/pt-br/articles/360054828234-Manual-para-configura%C3%A7%C3%A3o-de-Backup-Oracle-Windows)  
> **ID:** `360054828234` | **Última Atualização:** 2026-07-22T15:28:03Z

---

- ****
- ****

| Este manual foi criado para fornecer as principais orientações na configuração da rotina de Backup do ERP Sankhya para Banco de Dados Oracle - Windows. Recomendados que essas orientações sejam seguidas por um profissional de T.I/banco de dados de sua empresa, na ausência desse vale ressaltar que em caso de dúvidas ou necessidade de apoio para validar essa configuração, um consultor de serviços de sua Unidade será acionado. |
| --- |

 

### **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149494156183)

 Download:**

- Execute o download do arquivo em anexo ao final desse artigo;

### 
**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468525079)

 ****Configuração do ****Backup (Criando a Pasta):**

Descompactar a pasta baixada acima, no disco onde será feito o backup; Neste manual, utilizaremos o **D:** como exemplo.

- Acesse o diretório D:

- Copie e cole o arquivo dentro do D:

- Clique com botão direito, vá na opção “Extrair AQUI”;

### 
**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468532119)

 ****Agendador de tarefas:**

- Clique na tecla Windows do teclado;

- Pesquise por agendador de Tarefas:

![Agendador e tarefas 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468539543)

- Clique em **“Biblioteca do agendador”**:

![biblioteca do agendador 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149494184599)

- No canto direito, clique em **Criar Tarefa**:

![Criar tarefas 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468551191)

Será aberta a janela abaixo:

![467.png](https://ajuda.sankhya.com.br/hc/article_attachments/360094883833)

### 
**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149494194455)

 ****Configurando o Agendamento:**

- Insira na primeira coluna “Nome” o nome do agendamento: "Backup Prod"

![prod 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468562327)

- Clique na aba “Disparadores” e clique em “NOVO...”:

![disparadores 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468566295)

Será aberto a janela abaixo, configure essa tela de acordo com o print abaixo, altere a data para a data atual da criação desse backup:

![novo disparador 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149494212247)

- Após as marcações, clique em OK.

### 
**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149494223767)

 ****Configurando Ações (triggers):**

- Clique na aba **Ações** e clique em “NOVO...”:

![ações 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468588439)

- Será aberto a tela abaixo, clique em 'procurar':

![nova ação 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468593687)

- Selecione o arquivo **“export.bat”**, que está no diretório **D:\backup\scripts**:

![902.png](https://ajuda.sankhya.com.br/hc/article_attachments/360094885013)

- Clique em OK;

****

****

- 
- 

****

- 
- 

| Importante: Agora repita o processo, nomeando as demais execuções para “Backup Full” e “Estatísticas”: Nome: Backup FULL (Aba Geral)  Diário - Data HOJE - Horario: 19:00 (Aba disparadores) Caminho: D:\backup\scripts\export_full.bat (Aba ações)  Nome: Estatísticas (Aba Geral)  Diário - Data HOJE - Horário: 21:00 (Aba disparadores) Caminho: D:\backup\scripts\estatísticas.bat (Aba ações) |
| --- |

### 
**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149494244503)

Editando os scripts: ***(Arquivos da pasta "Scripts" - No caso desse artigo: **D:/backup/scripts/export_full.bat**)*

- Os scripts possuem caminhos pré-definidos, que precisam ser alterados de acordo com o cliente.

- Para editá-los, clique com o botão direito do mouse e clique em “EDITAR”:

![903.png](https://ajuda.sankhya.com.br/hc/article_attachments/360094886033)

Ajuste os caminhos de acordo com o que foi configurado:

- Como no nosso exemplo, utilizamos o diretório D:, nota-se acima que ele está direcionado para o C:, logo, precisa ser ajustado.

Para ajustar, basta apagar o caminho errado e substituir pelo correto.

********

| Errado | Correto |
| --- | --- |
| SET DIRLOG=C:\backup\logs | SET DIRLOG=D:\backup\logs |
| SET DIREXP=C:\backup\exports | SET DIREXP=D:\backup\exports |

 

- Clique em Fechar e Salvar.

### **Teste:**

Para testar, clique duas vezes sobre o arquivo, ele vai apresentar uma tela do CMD, executando o backup. Conforme imagem abaixo:

![904.png](https://ajuda.sankhya.com.br/hc/article_attachments/360094886693)

Faça isso para todos os outros arquivos, editando seus caminhos de acordo com o diretório escolhido por você.

### **

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19149468606743)

 Conclusão:**

- Para concluir, acesse novamente o agendador de tarefas, clique com botão direito em cima de uma das opções que você criou, e clique em EXECUTAR.

- Logo após, acesse o diretório “EXPORTS” dentro do caminho D:\backup e **verifique se gravou o arquivo de backup**, assim como seus logs na pasta LOGS.

**Anexos:**