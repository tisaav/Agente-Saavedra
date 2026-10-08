# Relatório de Conferência de Rubricas (S-1010)

> **Módulo:** Pessoas+ | **Subseção:** Eventos de Tabela do eSocial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41258999019159-Relat%C3%B3rio-de-Confer%C3%AAncia-de-Rubricas-S-1010](https://ajuda.sankhya.com.br/hc/pt-br/articles/41258999019159-Relat%C3%B3rio-de-Confer%C3%AAncia-de-Rubricas-S-1010)  
> **ID:** `41258999019159` | **Última Atualização:** 2026-09-27T19:04:57Z

---

**Módulo: **Pessoal+
**Versão Mínima:** 5.102
**Caminho de Acesso: Pessoal+ > Cadastros > Eventos**
**ID da Tela:** br.com.sankhya.rh.CadastroEventos

## **Sumário**

[Descrição e Usabilidade](#h_01KV835CNZHZCAE9CCAH7XKS77)

- [1. Descrição da Funcionalidade](#h_01KV828CEK1B9Q2WEBSEVG2TWD)

- [2. Pré-requisitos](#h_01KV828CEMFW0TWPT8V62QTDDF)

- [3. Jornada de Uso](#h_01KV828CERMQC6AEA6RRX9SYY3)

- [4. Pontos de Atenção](#h_01KV828CFZQJB79858GHXVGZ5G)

- [5. Dicas de Usabilidade](#h_01KV828CG1QZ9317AS7TRSYR07)

[Perguntas Frequentes (FAQ)](#h_01KV828CG4C7PZZ6RF4YP6KVPN)

[Artigos Relacionados](#h_01KV828CG91FZXNMGRSVBEMHVJ)

 

## **Descrição e Usabilidade**

O **Relatório de Conferência de Rubricas para eSocial (S-1010)** foi desenvolvido para facilitar a validação das rubricas enviadas ao eSocial, permitindo que a empresa consulte de forma centralizada as informações atualmente vigentes no ambiente governamental.

Através deste relatório é possível:

- conferir a parametrização das rubricas;

- validar incidências de INSS, IRRF e FGTS;

- identificar configurações inconsistentes;

- comparar rapidamente eventos cadastrados no sistema com o que está efetivamente enviado ao eSocial;

- apoiar auditorias internas e externas;

- realizar conferências periódicas relacionadas ao FGTS Digital, DCTFWeb e demais obrigações acessórias.

Diferentemente do Portal do eSocial, onde as informações precisam ser consultadas individualmente, este relatório apresenta uma visão consolidada de todas as rubricas enviadas com sucesso para determinado empregador.

 

### **1. Descrição da Funcionalidade**

A rotina exibe exclusivamente as informações que compõem o evento S-1010 (Tabela de Rubricas) enviadas com sucesso ao eSocial.

O relatório considera sempre a última versão vigente da rubrica existente no ambiente do eSocial, incluindo situações de retificação.

Dessa forma, você consegue visualizar exatamente quais configurações estão sendo utilizadas pelo governo para processamento dos eventos periódicos e não periódicos da empresa.

As informações são apresentadas em formato de grade e podem ser ordenadas, filtradas e exportadas.

 

### **2. Pré-requisitos**

Antes de utilizar o relatório, verifique:

- Acesso à tela **Eventos** (Pessoal+ > Cadastros) liberado pela rotina **Acessos **(Configurações > Controle de Acessos);

- Permissão de acesso ao empregador desejado;

- Existência de eventos S-1010 enviados com sucesso ao eSocial;

- Integração com o eSocial devidamente configurada.

| ⚠️ O relatório não exibe rubricas que nunca foram enviadas ao eSocial. |
| --- |

 

### **3. Jornada de Uso**

 

![relatorioconfrubricaS1010-pessoas+.gif](https://ajuda.sankhya.com.br/hc/article_attachments/41259732191255)

####  

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41259732191895)

 Acessar o relatório**

1. Acesse a tela **Eventos **(Pessoal+ > Cadastros).

1. 

Clique no botão **Conferência de Rubricas eSocial (S-1010)** no canto inferior direito da tela.

Será aberto um pop-up para seleção do empregador.

1. Informe o **Empregador** que deseja consultar.

1. Selecione o formato para exportação do relatório:

- PDF;

- Excel.

1. Clique em **Gerar relatório**.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41260194789783)

 Consultar as rubricas**

Após a carga dos dados, será apresentada uma grade contendo todas as rubricas enviadas ao eSocial por meio do evento S-1010.

O relatório disponibiliza as seguintes colunas:

- 

**Início da Validade**

Apresenta a data de início de vigência da rubrica considerada no último envio do S-1010 finalizado com sucesso.

Exemplo: 01/01/2025

- 

**Código do Evento**

Exibe o código da rubrica exatamente como cadastrado no sistema.

Exemplo: 1

- 

**Descrição do Evento**

Apresenta a descrição cadastrada para a rubrica.

Exemplo: Salário Base

- 

**Tipo da Rubrica**

Identifica o tipo enviado ao eSocial.

Exemplos: Provento

- 

**Natureza da Rubrica**

Exibe o código e a descrição da natureza da rubrica.

Exemplos: 1000 - Salário, vencimento, saldo

- 

**Incidência INSS**

Exibe o código de incidência previdenciária e sua descrição.

Exemplo: 11 - Mensal (base de cálculo do INSS)

- 

**Incidência IRRF**

Exibe o código de incidência do Imposto de Renda e sua descrição.

Exemplo: 11 - Rendimento tributável remuneração mensal

- 

**Incidência FGTS**

Exibe o código de incidência do FGTS e sua descrição.

Exemplo: 11 - Base de cálculo do FGTS mensal

 

### **4. Pontos de Atenção**

- O relatório não consulta diretamente o cadastro atual da tela Eventos. As informações exibidas refletem a última configuração enviada com sucesso ao eSocial.

- Caso uma rubrica tenha sido retificada, será apresentada somente a última versão vigente.

- Rubricas excluídas do eSocial não serão exibidas.

- Eventos que não compõem o eSocial também não serão apresentados.

- Alterações realizadas no cadastro da rubrica ainda não enviadas ao eSocial não serão refletidas neste relatório.

 

### **5. Dicas de Usabilidade**

- Utilize o relatório antes do fechamento mensal da folha.

- Realize conferências periódicas das incidências tributárias.

- Verifique a parametrização antes da geração da DCTFWeb.

- Utilize a exportação em Excel para auditorias internas.

- Consulte o relatório após retificações de S-1010 para validar o conteúdo efetivamente vigente no governo.

 

## **Perguntas Frequentes (FAQ)**

**1. O relatório mostra o cadastro atual da rubrica?**

Não.

O relatório apresenta a última informação enviada com sucesso ao eSocial.

**2. Alterei uma rubrica hoje e ela não aparece atualizada. Por quê?**

Porque a alteração ainda não foi enviada e processada pelo eSocial.

Enquanto isso não ocorrer, continuará sendo exibida a configuração vigente anteriormente.

**3. Rubricas excluídas aparecem no relatório?**

Não.

Rubricas excluídas do eSocial não são apresentadas.

**4. Eventos que não compõem o eSocial aparecem na consulta?**

Não.

Somente rubricas efetivamente enviadas através do evento S-1010 são exibidas.

**5. Qual informação prevalece em caso de retificação?**

Sempre será apresentada a última versão enviada e finalizada com sucesso.

**6. Posso utilizar este relatório para auditorias?**

Sim.

O relatório foi desenvolvido justamente para apoiar processos de auditoria, compliance e conferência de parametrizações.

**7. O relatório ajuda na conferência da DCTFWeb e FGTS Digital?**

Sim.

As incidências apresentadas correspondem às configurações utilizadas pelo eSocial para processamento das obrigações trabalhistas, previdenciárias e tributárias.

 

## **Artigos Relacionados**

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)

- [Histórico de envio das rubricas no eSocial (Evento S-1010)](https://ajuda.sankhya.com.br/hc/pt-br/articles/37087067045911)

- [Controle de Modificações de Eventos e Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663)

- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Histórico de envio das rubricas no eSocial (Evento S-1010)](https://ajuda.sankhya.com.br/hc/pt-br/articles/37087067045911)
- [Controle de Modificações de Eventos e Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)