# Liberação de Job em Bases de Homologação

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35857279731607-Libera%C3%A7%C3%A3o-de-Job-em-Bases-de-Homologa%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/35857279731607-Libera%C3%A7%C3%A3o-de-Job-em-Bases-de-Homologa%C3%A7%C3%A3o)  
> **ID:** `35857279731607` | **Última Atualização:** 2026-07-22T14:24:29Z

---

Durante a instalação de pacotes em ambiente de homologação, como o pacote da Reforma Tributária, algumas tabelas podem não ser preenchidas automaticamente.
Isso ocorre porque, por padrão, o ambiente de homologação bloqueia a execução de jobs automáticos, a fim de evitar:

- 

O envio indevido de e-mails ou integrações externas;

- 

Processamentos desnecessários;

- 

Impactos de performance durante os testes.

Para permitir a execução de jobs específicos sem liberar toda a fila de agendamentos, é possível utilizar um argumento controlado na inicialização da JVM.

### **Passo a passo para liberação de Job**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36090852740631)

 **Parâmetro** ****''SERVERHOSTSCHED''** **: **

O parâmetro SERVERHOSTSCHED deve estar vazio ou não existir na base de homologação.

**Observação:** Esse parâmetro define o servidor responsável pela execução de agendamentos automáticos. Caso esteja preenchido, pode impedir a execução manual de Jobs específicos.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35857340103319)

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36090852741271)

 **Argumento **''-Dsankhyaw.schedule.disable=true''** : 

O argumento -Dsankhyaw.schedule.disable=true** **não deve existir na configuração da JVM. Esse parâmetro desabilita todos os jobs do sistema, o que impede qualquer execução, mesmo que controlada.

**Observação:** Portanto, não utilize o argumento -Dsankhyaw.schedule.disable=true em ambiente de homologação.

![image (35).png](https://ajuda.sankhya.com.br/hc/article_attachments/36090896515479)

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36090896516631)

 **Habilite apenas o(s) Job(s) necessário(s): 

Para executar somente os Jobs desejados, utilize o argumento: **''-Dsankhyaw.only.jobs=-22005''**

**Exemplo de uso:**

- 

**Linux:**

```text
./standalone.sh -Dsankhyaw.only.jobs=-22005

```

- 

**Windows:**

```text
standalone.bat -Dsankhyaw.only.jobs=-22005

```

**Observação: **Esse argumento faz com que somente o Job informado seja habilitado para execução, mantendo os demais desativados.

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36090896517143)

 **Execute múltiplos Jobs: 

Caso seja necessário rodar mais de um Job, informe os códigos separados por vírgula, sem espaços:

**''-Dsankhyaw.only.jobs=-22005,-22010,-22015''.**

Assim, o sistema executará apenas os Jobs listados, preservando o bloqueio dos demais.

É necessário Reiniciar o sistema após a inclusão do Job no argumento.

**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36090896518039)

 **Confirme execução: 

Após reiniciar o servidor com o argumento configurado:

1. 

Acesse a tela **“Controle de JOBs” **(Configurações» Avançado» Controle de Jobs);

1. 

Verifique se os Jobs informados estão ativos e em execução normal;

1. 

Caso não apareçam, confira no arquivo de log do servidor** (server.log)** se o argumento foi aplicado corretamente.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35857279727767)

 

#### 

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/36090852744599)

 **Pontos importantes: **

- 

O uso do argumento ''**-Dsankhyaw.only.jobs''** é temporário, válido apenas enquanto o servidor estiver iniciado com ele; 

- 

Após a execução do Job, remova o argumento e reinicie o servidor normalmente; 

- 

Esse procedimento é exclusivo para bases de homologação; 

- 

Em ambiente de produção, qualquer alteração em Jobs deve ser previamente avaliada pela equipe técnica responsável.

**Exemplo prático: Reforma Tributária**

Durante a instalação do **pacote de homologação da Reforma Tributária**, o Job responsável por atualizar as tabelas de apoio é o de **código**** −22005.**
Assim, o servidor deve ser iniciado com o seguinte argumento: -Dsankhyaw.only.jobs=-22005

Após a execução, as tabelas necessárias serão corretamente preenchidas, permitindo a continuidade dos testes de Reforma Tributária.

#### **Visão Geral da Execução de Jobs**

``

****``

``

| Etapa | Ação | Objetivo |
| --- | --- | --- |
| 1 | Deixar SERVERHOSTSCHED vazio | Evitar bloqueio na execução dos jobs |
| 2 | Não usar -Dsankhyaw.schedule.disable=true | Evitar bloqueio global de todos os jobs |
| 3 | Usar -Dsankhyaw.only.jobs=-22005 | Executar somente o job desejado |
| 4 | Separar múltiplos jobs por vírgula | Rodar mais de um job específico |
| 5 | Validar na tela “Controle de JOBs” | Confirmar ativação e status de execução |