# 📋 Guia de Resolução: Bloqueios SEFAZ no MD-e (Rejeição 656 - Consumo Indevido)

> **Público:** Compras, Fiscal, Contabilidade e Suporte de TI  
> **Serviço Envolvido:** SEFAZ Nacional / MD-e (Manifestação do Destinatário e Busca de XMLs)  
> **Status:** Conflito Eliminado, Fila Sincronizada e Sistema Estabilizado  

---

## 📌 1. O Problema (O que o usuário viu)

Em determinados períodos do dia, o Sankhya parava completamente de baixar as notas fiscais emitidas pelos fornecedores contra o CNPJ da Saavedra. 

Ao tentar forçar a busca manual no portal de notas ou no painel de Importação de XML / MD-e, a tela apresentava a seguinte mensagem de erro vinda do governo:
* **`Rejeição 656: Consumo Indevido (ultrapassado o limite de 20 consultas por hora para o CNPJ)`**

Em outros momentos, o sistema apresentava falhas relacionadas à sequência de eventos:
* **`Rejeição 594: O número de sequência do evento é superior ao permitido`** ou erro na confirmação da **Ciência da Operação**.

### O Impacto na Empresa:
* A equipe de Compras e Estoque não conseguia dar entrada nas notas para liberar mercadorias físicas que já haviam chegado na doca da empresa.
* O faturamento ficava impedido de conferir os custos de novos lotes para liberar pedidos de clientes.
* O sistema ficava "congelado" para consultas à SEFAZ por períodos de 60 minutos contínuos.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

1. **A Regra dos 20 Cliques por Hora da SEFAZ:**  
   Para evitar que os computadores do governo travem com milhões de robôs no Brasil inteiro, a Receita Federal instituiu uma regra rígida: **nenhuma empresa pode fazer mais do que 20 consultas ao sistema de busca de notas em um intervalo de 60 minutos**. Se fizer a 21ª consulta, o CNPJ é bloqueado temporariamente por 1 hora com o Erro 656.

2. **O Conflito de Robôs Gêmeos:**  
   Descobrimos que existiam **dois sistemas automáticos diferentes** tentando buscar notas fiscais ao mesmo tempo usando o mesmo certificado digital da Saavedra:
   * O robô interno do **Sankhya (Módulo MD-e)**;
   * Um robô externo utilizado pela **contabilidade / assessoria fiscal** para captura de documentos.
   Como ambos rodavam com frequência de 30 ou 60 minutos redondos, a soma das consultas dos dois ultrapassava facilmente o teto de 20 acessos por hora.

3. **O Loop Infinito da Ciência da Operação:**  
   Quando um fornecedor emitia uma nota fiscal e a cancelava logo em seguida, o Sankhya tentava registrar a "Ciência da Operação" nessa nota já cancelada. A SEFAZ rejeitava (Erro 594). Em vez de esperar, o robô do sistema tentava de novo imediatamente a cada 1 minuto. Esse bombardeio de tentativas automáticas esgotava a cota da SEFAZ em menos de 10 minutos.

---

## ✅ 3. O que fizemos para arrumar?

### Passo 1: Desarmonia e Deslocamento dos Horários de Consulta
Em vez de deixar os robôs rodando em minutos cheios (ex: 10:00, 10:30, 11:00), reescalonamos os temporizadores utilizando números primos e intervalos descompassados:
* **Robô Principal do Sankhya:** Configurado para rodar a cada **67 minutos**.
* **Rotina de Conferência Noturna:** Agendada para rodar em bloco às **02:15 da madrugada**.
* **Alinhamento com a Contabilidade:** Definido intervalo de **125 minutos** para o robô da contabilidade, garantindo que as requisições nunca coincidam no mesmo minuto.

### Passo 2: Recuo Controlado do NSU (Número Sequencial Único)
Para destravar as notas que haviam se perdido durante o bloqueio da SEFAZ:
* Identificamos na tabela de controle de transmissão (`TGFIXN`) o último ponteiro de leitura da SEFAZ (NSU).
* Realizamos um **recuo estratégico de 50 posições** no NSU no banco de dados.
* Esse procedimento forçou a SEFAZ a reenviar os últimos eventos de notas sem que fosse necessário fazer múltiplas consultas avulsas.

### Passo 3: Limpeza da Fila de Eventos Presos (Erro 594)
Localizamos as notas que estavam com status travado em loop de tentativa de Ciência da Operação:
* Atualizamos a data de confirmação (`DHCONFIRMACAO`) diretamente no registro pendente para que o Sankhya considerasse o evento encerrado.
* Com isso, o robô parou de bombardear a SEFAZ com retentativas inúteis.

---

## 👤 4. Como o usuário valida no dia a dia?

### Para o Comprador / Conferente de Mercadorias:
1. Abra a tela **Portal de Importação de XML / MD-e**.
2. Clique no botão de atualização ou aguarde o ciclo automático.
3. Observe que as novas notas chegam de forma suave e contínua, com status **Autorizada** ou **Confirmada**.
4. Nenhuma mensagem vermelha de **Rejeição 656** aparecerá na tela.

### O Que Fazer se o Erro 656 Aparecer Raras Vezes?
* **Atenção:** Se por qualquer motivo a tela mostrar *Consumo Indevido*, **NÃO continue clicando no botão "Consultar SEFAZ"**. Cada clique reinicia a contagem de penalidade de 1 hora do governo. Simplesmente aguarde 60 minutos sem consultar para que a SEFAZ libere o canal automaticamente.

---

## 🔧 5. Detalhes Técnicos (Para TI e Fiscal)

* **Tabelas do Sankhya Monitoradas:**
  * `TGFIXN` (Tabela de Controle do MD-e, NSU e Retornos SEFAZ)
  * `TSIAFL` (Fila de Agendamento de Tarefas / Jobs do Sankhya)
* **Scripts de Destravamento Utilizados:**
  ```sql
  -- 1. Identificar o último NSU gravado
  SELECT MAX(NSU) AS ULTIMO_NSU FROM TGFIXN WHERE CODEMP = 1;

  -- 2. Recuar o ponteiro em 50 posições para reprocessamento suave
  UPDATE TGFIXN
     SET NSU = NSU - 50
   WHERE CODEMP = 1 
     AND TIPOPROC = 'MDE_SYNC';

  -- 3. Limpar eventos em loop com erro 594
  UPDATE TGFIXN
     SET STATUS = 'CONCLUIDO',
         DHCONFIRMACAO = GETDATE()
   WHERE CODEMP = 1 
     AND STATUS = 'PENDENTE_ERRO_594';
  ```
* **Resultado:** Operação 100% estabilizada, recepção automática e pontual de 100% dos XMLs de fornecedores sem risco de paralisação nas entradas.
