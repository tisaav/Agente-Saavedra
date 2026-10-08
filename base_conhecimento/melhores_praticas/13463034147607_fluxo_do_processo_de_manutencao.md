# Fluxo do Processo de Manutenção

> **Módulo:** Melhores Praticas | **Subseção:** Documentação de processos  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/13463034147607-Fluxo-do-Processo-de-Manuten%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/13463034147607-Fluxo-do-Processo-de-Manuten%C3%A7%C3%A3o)  
> **ID:** `13463034147607` | **Última Atualização:** 2026-07-22T16:11:17Z

---

O processo de manutenção é um fluxo de atividades que envolvem a correção ou o esclarecimento de dúvidas dos produtos Sankhya. Através deste processo que entram as dúvidas provenientes do Service Desk (SD) ou das demandas de correções de funcionalidades nativas que não estão funcionando conforme o projeto e parametrização.

As características da Manutenção, são:

- Pequenos hotfix (correções de erros);

- Requerem entendimento do Problema (causa de 1 ou mais Incidentes);

- Têm ciclo de vida curto (semanas).

#### **Informações e Priorização de Chamados**

Caso você precise de:

- 
**Informações sobre o andamento de um chamado:** confira o status do seu ticket na Central de Ajuda;

- 
**Priorização de um chamado:** entre em contato com seu gerente de relacionamento.

#### **Fluxo do Processo de Manutenção**

O processo de Manutenção possui o seguinte fluxo de tarefas:

![Fluxograma__10_.png](https://ajuda.sankhya.com.br/hc/article_attachments/13765250375447)

Conforme fluxo acima, primeiramente, o Solicitante (Cliente/Consultor) abre no Zendesk um Ticket de Incidente ou Dúvida.

Esse Ticket é avaliado no **Nível 1 (N1)** do SD. Sendo que, caso o SD consiga tratá-lo, ele deve devolver para o Solicitante o esclarecimento da dúvida, a resolução do Incidente ou o paliativo do Problema. 

Porém, se for identificado no N1 que se trata de um Problema, o chamado é encaminhado para o **Nível 2 (N2)**. Neste nível, caso conheça a tratativa, deve-se devolver o chamado com ela. 

No entanto, se no N2 constatar que se trata de um Problema, deve-se abrir um Flow que gera automaticamente a OS de Manutenção. 

Após a abertura da OS para a Manutenção, são realizadas as seguinte etapas:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13464832756631)

Na etapa de **"Triagem da OS"** é determinada a Célula responsável pela tratativa e verifica-se às pré-condições de Manutenção.

```text
** Responsável: **Tech Lead de QA de Sustentação
```

```text
** Ações:**
```

1. 

```text
Determinar a Célula responsável pela tratativa;
```

1. 

```text
Checar se o Teste de Entrada feito pelo SD está completo ou não;
```

1. 

```text
Se estiver completo, enviar a OS para o Diagnóstico;
```

1. 

```text
Se não estiver, se possível, fazer o Teste de Entrada;
```

1. 

```text
Se não for possível fazer o Teste de Entrada, a OS será encaminhada para a 
Sessão de Diagnóstico para que seja repassado o feedback ao pessoal do SD.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13465067857303)

O intuito dessa etapa é acelerar a curva de aprendizado dos envolvidos e acelerar o processo de tratativa da Indústria e do Service Desk. Além disso, é verificado se a OS se trata de uma dúvida ou um problema.

```text
**Responsável: **QA de Sustentação (Responsável, mediador); DEV (perspectiva 
técnica): Tech Lead ou Desenvolvedor Sênior da questão; PO/APO (perspectiva de 
negócio) e SD (perspectiva de atendimento).
```

```text
** Ações: **
```

1. 

```text
Se estiver faltando algo para o Diagnóstico, dar o feedback para o SD de forma
clara, direta e transparente;
```

1. 

```text
Se for uma dúvida, esclarecer e passar para a próxima;
```

1. 

```text
Discussão do problema;
```

1. 

```text
Se necessário, avaliar regras de negócio x código-fonte implementado;
```

1. 

```text
Se for um problema, seguir para etapa de **"Estruturar a Solução"**;
```

1. 

```text
Se não, explicar por que não é um problema, orientar as devidas tratativas e 
retornar OS para SD.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13466125572119)

Nesta etapa, deve-se orientar os Desenvolvedores a realizar a Manutenção de forma mais eficaz e eficiente possível, e ainda, reduzir a curva de aprendizado dos Desenvolvedores novatos.

```text
**Responsável: **TL ou DEV Sênior no assunto em questão
```

```text
**Ações: 
**
```

1. 

```text
Descrever em alto nível o ponto de Manutenção;
```

1. 

```text
Descrever em alto nível a Manutenção a ser feita;
```

1. 

```text
Orientar o DEV como ele pode ter certeza que a Manutenção foi bem sucedida.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13481348817943)

Esta etapa tem o intuito de reduzir o risco de retorno ou problemas decorrentes. Sendo que, é necessário que as Manutenções mais complexas e arriscadas sejam tratadas pelos veteranos (Pleno ou Sênior). 

```text
**Responsável:** Desenvolvedor Pleno, Sênior ou de Referência
```

```text
**Ações: 
**
```

1. 

```text
Realizar as OS priorizadas ou as mais antigas primeiro.
```

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/13479863610263)

O propósito nesta etapa é permitir que os Desenvolvedores Júnior ou Pleno tratem as Manutenções mais simples e de menor risco, acelerar a curva de aprendizado e aumentar a produtividade.

```text
**Responsável:** Desenvolvedor Júnior ou Pleno
```

```text
**Ações: 
**
```

1. 

```text
Realizar as OS priorizadas ou as mais antigas primeiro.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13479950854551)

Nesta etapa, o objetivo é aumentar a efetividade das Manutenções. 

```text
**Responsável: **Desenvolvedor Sênior, de Referência ou Tech Lead
```

```text
**Ações: **
```

1. 

```text
Avaliar a Estruturação da Solução contra as modificações feitas no Código 
Fonte;
```

1. 

```text
Avaliar pontos de risco e/ou futuros Incidentes, ou Problemas;
```

1. 

```text
Dar feedback quando necessário.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13479996295319)

O propósito nesta etapa é preparar o pacote para realização do Teste de Saída.

```text
**Responsável: **Desenvolvedor responsável pela Manutenção
```

```text
**Ações: **
```

1. 

```text
Checar se a correção não quebrou a versão da Branch da OS;
```

1. 

```text
Preparar o pacote para realização do Teste de Saída.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13480252032279)

Esta etapa, tem como finalidade garantir que a Manutenção foi efetiva.

```text
**Responsável: **Analista de QA
```

```text
**Ações: **
```

1. 

```text
Checar se o cenário do problema identificado na entrada da OS foi efetivamente
tratado;
```

1. 

```text
Checar se não teve efeito colateral.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13480354001303)

O intuito aqui, é garantir que a correção seja feita na versão original do problema e todas as versões superiores.

```text
**Responsável: **Desenvolvedor responsável pela Manutenção
```

```text
**Ações: **
```

1. 

```text
Solicitar o MR para a versão da OS (P1: GA > RC e DEV, P2/P3: DEV) e todas as 
DEV das versões superiores.
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13480527667223)

O propósito nesta etapa é evitar que os Desenvolvedores iniciantes alterem incorretamente a GA.

```text
**Responsável: **P1: TL ou SL responsável pela Célula da Manutenção; P2/P3: TL de QA
Delivery ou Merge Aprover da Semana.
```

```text
**Ações: **
```

1. 

```text
Checar as alterações feitas na Branch da OS;
```

1. 

```text
Se estiver tudo certo, aprovar o MR.
```

![Comunicar.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/13962133369111)

Nesta etapa é realizada a comunicação do retorno para o cliente após a correção de um problema ser concluído.

```text
**Responsável: **Service Desk (N1 e N2)
```

```text
**Ações:**
```

1. 

```text
O Service Desk envia para o cliente a correção feita com o Build para
download. Essa comunicação ocorre no mesmo dia da correção para problemas P1 
(após a etapa “Teste de Saída”) e 1 dia útil após a correção para problemas 
P2 e P3 (após a etapa “Regressão Diária”).
```