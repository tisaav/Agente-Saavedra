# Agendador Geração - EFD Reinf

> **Módulo:** Fiscal e Contábil | **Subseção:** EFD-Reinf  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30530329831959-Agendador-Gera%C3%A7%C3%A3o-EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/30530329831959-Agendador-Gera%C3%A7%C3%A3o-EFD-Reinf)  
> **ID:** `30530329831959` | **Última Atualização:** 2026-09-15T17:31:40Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312546077719)

 Livros Fiscais > Arquivos         

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312546078615)

 **Versão disponível:** Livros Fiscais 5.8.19
```

Em ambientes com grande volume de processamento, a execução simultânea de múltiplas tarefas pode comprometer o desempenho do sistema. Para evitar sobrecarga e otimizar a utilização dos recursos, a funcionalidade de agendamento permite programar a execução de processos mais longos em horários de menor demanda.

Isso garante uma distribuição eficiente da carga de trabalho, aumentando a estabilidade, a performance e a confiabilidade das operações.

  

#### ****

[Preenchimentos iniciais](#Preenchimentosiniciais)

[Definindo data e horário de execução](#Definindodataehor%C3%A1riodeexecu%C3%A7%C3%A3o)

[Configurando a frequência](#Configurandoafrequ%C3%AAncia)

[Definindo os parâmetros](#Definindoospar%C3%A2metros)

[Gerenciando o histórico](#Gerenciandoohist%C3%B3rico)

| Como utilizar a rotina? |
| --- |
|  |
|  |
|  |
|  |
|  |

### 
**Preenchimentos iniciais**

Escolha um nome para identificar o agendamento e insira no campo **"Descrição agendamento"**. Esse nome deve ser claro e descritivo, pois ajudará na organização dos agendamentos futuros. 

O número do agendamento será gerado automaticamente e exibido no campo **"Nro. agendamento"**.

O campo **"Status Última Execução"** será atualizado automaticamente após cada execução, permitindo o acompanhamento do processamento.

Caso queira ativar o agendamento imediatamente, marque a opção **"Ativo"**.

[[voltar ao topo]](#top)

### 
**Definindo data e horário de execução**

Na aba **Horários**, defina quando e por quanto tempo o agendamento será executado:

1. No campo **"Próxima execução em"**, determine a data e o horário da próxima execução. Caso precise que a execução ocorra imediatamente, há a opção de forçar essa ação.

1. Em **"Data Final de execução"**, defina até quando o agendamento pode ser executado. Se não houver uma data limite, o sistema continuará a execução conforme a frequência definida.

[[voltar ao topo]](#top)

### 
**Configurando a frequência**

Na aba **Frequência Agendamento**, determine quando e com que frequência o agendamento será executado:

1. Escolha a data da **"1ª execução"**.

1. Selecione a periodicidade do agendamento: **Diário**, **Semanal** ou **Mensal**.

1. Para garantir a execução, defina pelo menos um horário e um mês.

[[voltar ao topo]](#top)

### 
**Definindo os parâmetros**

Na aba **Parâmetros**, insira as informações essenciais para a geração das notas:

1. Informe a **"Empresa"** responsável pela emissão das notas.

1. Escolha o **"Tipo de Ambiente"** no qual as notas serão processadas.

1. Defina a **"Data de referência"**.

Se a marcação **"Utilizar mês de geração como data de referência"** for ativada, o agendador não dependerá do campo **"Data de referência"** manualmente informado. Em vez disso, a cada execução, ele determinará automaticamente a data de referência com base no momento em que está sendo executado.

Isso permite maior flexibilidade e automação, garantindo que o processo sempre utilize a referência correta sem necessidade de ajustes manuais.

[[voltar ao topo]](#top)

### 
**Gerenciando o histórico**

Na aba **Histórico** acompanhe os registros de execução dos agendamentos já processados.

[[voltar ao topo]](#top)