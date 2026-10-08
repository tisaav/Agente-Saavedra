# Cadastro de Carga Horária

> **Módulo:** Pessoas+ | **Subseção:** Jornada, Escalas e Calendário  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503-Cadastro-de-Carga-Hor%C3%A1ria)  
> **ID:** `38858116404503` | **Última Atualização:** 2026-08-12T19:14:36Z

---

**Módulo:** Pessoal+
**Caminho de Acesso: **Pessoal+ > Cadastros
**ID da Tela:  **br.com.sankhya.rh.CargaHoraria

## **Sumário**

[Descrição e Usabilidade](#h_01KK22J26Z03N30NW2PHV0VSRA)

1. [Descrição da Funcionalidade](#h_01KK22BJSPANCMHZB70MGR9G0Q)

1. [Pré-requisitos](#h_01KK22BJSXEK0C13CDPGF8B43V)

1. [Jornada de Uso](#h_01KK22BJT17XKWE63T2T7SFE5C)

1. [Pontos de Atenção](#h_01KK22BJVJB6N473Y0HT4W1T5W)

1. [Dicas de Usabilidade](#h_01KK22BJVQDNXPWB9Y6A3GMS0Q)

[Artigos Relacionados](#h_01KK22BJVSE3JXW4HZ26AXBE2R)

 

## **Descrição e Usabilidade**

### **1. Descrição da Funcionalidade**

A **Carga Horária** define a jornada de trabalho do colaborador, indicando os dias e horários previstos de **entrada, saída, intervalos e folgas**.

A legislação trabalhista estabelece uma jornada máxima de **44 horas semanais** para trabalhadores sob regime CLT. No sistema, o cadastro da carga horária permite controlar essa jornada e apoiar o cálculo correto de horas extras, atrasos, banco de horas e demais apurações de ponto.

Além disso, essas informações são utilizadas para a geração das informações enviadas ao **eSocial**.

No sistema existem dois conceitos principais:

- 

**Carga Horária:** utilizada quando o horário é flexível, sendo necessário apenas cumprir a quantidade de horas diárias prevista.

- 

**Jornada de Trabalho:** utilizada quando os horários de entrada e saída são fixos, permitindo ao sistema validar as batidas de ponto e identificar atrasos ou horas extras.

 

### **2. Pré-requisitos**

**Permissões necessárias**

- Deve **ter acesso liberado para a tela Carga Horária**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

**Configurações relacionadas**

Antes de cadastrar uma carga horária, verifique:

- 

Se a empresa já possui regras definidas de jornada ou escalas de trabalho.

- 

Se existem convenções ou acordos coletivos que impactam a jornada.

- 

Se os horários e intervalos já estão definidos para os funcionários.

 

### **3. Jornada de Uso**

Esta tela define o comportamento de cada carga horária em relação aos direitos trabalhistas, à flexibilidade de horários, integração com eSocial e conformidades com normas.

![cadastro-carga-horaria.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38901572237847)

 

#### **3.1 Cadastrar uma carga horária**

1. 

Acesse a tela **Carga Horária** (Pessoal+ > Cadastros).

1. 

Clique em **Cadastrar Identificação da Carga Horária**.

1. 

Preencha os campos principais:

  - 

**Descrição**: nome que identifique facilmente a jornada.

  - 

**Cód. Carga Horária**: pode ser gerado automaticamente ou manualmente, conforme a configuração definida por meio do botão 

![botão-configuração-da-tela-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/38901729792407)

 **Configuração da Tela**, opção **Numeração**.

  1. 

**Tipo Carga Horária**:

    - 

Carga Horária (horário flexível)

    - 

Jornada de Trabalho (horário fixo)

1. 

Informe o **Tipo de Jornada**, conforme o modelo de trabalho adotado pela empresa, como:

  - 

Jornada 12x36;

  - 

Jornada com folga fixa;

  - 

Jornada com folga variável;

  - 

Turno ininterrupto de revezamento;

  - 

Demais tipos de jornada.

1. 

Marque a opção **Possui Horário Noturno** caso a jornada inclua trabalho no período noturno.

1. 

Clique em 

![botão Salvar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/38901729799319)

 **Salvar [F7]**.

1. 

Configure as abas abaixo:

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38858101355287)

Aba Geral**

Nesta aba são definidas as configurações principais da carga horária.

Principais campos:

- 

**Ativa:** habilita a carga horária para uso.

- 

**Permite flexibilidade de horário:** permite variação no horário de entrada ou saída.

- 

**Considera redução de horas noturnas:** aplica a redução legal da hora noturna.

- 

**Compõe eSocial:** envia as informações da jornada ao eSocial.

Também é possível configurar **alternância de jornadas**, permitindo que colaboradores alternem entre escalas diferentes.

 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38858101355287)

**Aba Escala de Serviço**

Na aba **Escala de Serviço**, é possível definir escalas de trabalho.

Exemplo:
**Escala 5x2** → trabalha cinco dias e folga dois.

Para configurar:

1. 

Marque **Escalonar Dias de Trabalho **e informe:

  - 

o número de **Dias de Trabalho;**

  - 

o número de **Dias de Folga;**

  - 

**a Quantidade de Turnos.**

Também é possível configurar regras de feriados e DSR para a apuração do ponto.

- 

Considera Ocorrências nos Feriados

- 

Considerar Folga com percentual de DSR/Feriado

- 

Considera Súmula nº444 TST:

- 

Considerar feriado VA e VT:

 

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38858101355287)

Aba Intervalo**

Na aba **Intervalo**, configure as regras de descanso.

Defina:

- 

**Tipo**

  - 

Fixo

  - 

Variável

  - 

Sem intervalo

- 

**Duração em minutos**

- 

**Horário de início** e **término**

- 

**Aplica Tolerância**

A seção **Pausa** é destinada às indicações de pausas durantes os turnos da carga horária, com regras de tolerância, horas extras ou atrasos.

 

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38858101355287)

Aba Horário**

Na aba **Horário**, são definidos os horários de entrada e saída para cada dia ou sequência da escala.

Para cadastrar:

1. 

Clique em 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38902142902423)

 **Cadastrar Configurações de Ponto**.

1. 

Informe:

  - 

**Dia da semana ou sequência da escala**

  - 

**Turno**

  - 

**Entrada do turno**

  - 

**Saída do turno**

Também é possível configurar:

- 

Validação de **entrada e saída** no ponto;

- 

**Descanso semanal**;

- 

**Duração da jornada para o eSocial**.

1. 

Caso existam pausas durante o turno, utilize a **sub-aba Paradas Programadas** para registrar esses períodos.

1. 

Para agilizar o cadastro de outros dias ou turnos, utilize o botão 

![botao-duplicar FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/38902169389591)

 **Duplicar**.

1. 

Após finalizar as configurações, clique em 

![botão Salvar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/38901729799319)

 **Salvar [F7]**.

 

### **4. Pontos de Atenção**

- 

A carga horária influencia diretamente o **controle de ponto, cálculo de horas extras e banco de horas**.

- 

Certifique-se de cadastrar corretamente **intervalos e descansos semanais**.

- 

Para escalas fixas, é necessário cadastrar **todos os dias trabalhados e os dias de folga**.

- 

Alterações na carga horária podem impactar funcionários que já utilizam essa configuração.

- 

Quando uma carga horária estiver vinculada a colaboradores, a alteração dos horários seguirá as seguintes regras:

  - 

**Permite alteração quando:**

    - 

Não existirem registros de ponto nas tabelas **TFPPONFECHAMENTO** ou **TFPRPO** nos **últimos 2 meses** (contados da data atual).

  - 

**Não permite alteração quando:**

    - 

Existirem registros de ponto nesse período.

    - 

Nesse caso, o sistema apresentará a mensagem:

**“Não é possível alterar/excluir, pois existe lançamento para esta Carga Horária no módulo de Ponto.”**

  - 

**Carga horária sem vínculo**

    - 

Se a carga horária **não estiver vinculada a colaboradores**, todas as alterações de horários podem ser realizadas normalmente.

- 

Verifique se a opção **Compõe eSocial** está marcada quando a jornada precisa ser enviada ao governo.

 

### **5. Dicas de Usabilidade**

- 

Utilize descrições claras, como:
**"Escala 12x36 Noturna"** ou **"Jornada Comercial 44h"**.

1. 

Utilize o botão **Duplicar** para acelerar o cadastro de horários semelhantes.

1. 

Padronize as cargas horárias da empresa para facilitar a manutenção e o controle de ponto.

 

### **Artigos Relacionados**

- 

[Inclusão e Alteração de Carga Horária no Cadastro do Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/38911679393175)

- 

[Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

- 

[Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007)

- 

[Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)


---

### 🔗 Links e Referências Internas:

- [Inclusão e Alteração de Carga Horária no Cadastro do Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/38911679393175)
- [Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)