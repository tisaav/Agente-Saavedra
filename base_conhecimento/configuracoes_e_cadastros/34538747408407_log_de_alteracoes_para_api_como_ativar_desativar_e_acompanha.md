# Log de Alterações para API: como ativar, desativar e acompanhar os registros de alteração

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34538747408407-Log-de-Altera%C3%A7%C3%B5es-para-API-como-ativar-desativar-e-acompanhar-os-registros-de-altera%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/34538747408407-Log-de-Altera%C3%A7%C3%B5es-para-API-como-ativar-desativar-e-acompanhar-os-registros-de-altera%C3%A7%C3%A3o)  
> **ID:** `34538747408407` | **Última Atualização:** 2026-07-29T13:43:14Z

---

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310540602135)

****

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310524956695)

****

1. 

| Versão miníma: a partir da 4.35b30  Telas: Log de Alterações para API (Configurações > Rotinas) |
| --- |

####  

#### **Sumário**
[Descrição](#h_01K3V0PG951B8PYGMCANJ3EZ2C)
[Pré-requisitos](#h_01K3TSX4FM7T10NR47SR6J2SW0)
[Jornada de uso](#h_01K3TSX4FY2RS58CZXYC2MH4BV)
[Como consultar os registros de alteração?](#h_01KHVK8ZMV82FWYX1CX45XQV71)
[Pontos de atenção](#h_01K3TSX4G3N0GFKN1BDGFCSVJG)

|  |
| --- |
|  |
|  |
|  |
|  |

###  

#### **Descrição**

A partir da versão 4.35, o controle de alterações no ERP Sankhya passou por uma atualização. A funcionalidade, antes acoplada ao sistema principal, foi migrada para um **micro módulo independente** chamado **Instance Logs Monitor MM**.

Essa mudança melhora o desempenho, facilita a manutenção e traz mais flexibilidade para o acompanhamento de alterações em dados, mantendo a compatibilidade com as versões anteriores.

 

#### **Pré-requisitos**

##### **O que você precisa saber?**

A principal mudança é que o processo de registro de alterações agora ocorre de forma **assíncrona**, com consumo e armazenamento realizados por jobs automáticos. Isso permite que o serviço funcione de forma desacoplada do ERP principal e com maior escalabilidade.

Apesar da nova arquitetura, o comportamento para o usuário final segue praticamente o mesmo. O sistema continua registrando alterações relevantes e oferecendo recursos como o uso de filtros por data de modificação (por exemplo, com o atributo **modifiedSince**).

 

##### **Como ativar ou desativar o log de alterações?**

#####  

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42310540607767)

 

O controle de ativação agora é feito **exclusivamente pela tela "Log de Alterações para API"**, que permite ligar ou desligar o serviço (ou Triggers especificas a partir da 4.36).

##### **Quando o log está ativado:**

- 

O switch da tela estará ligado.  

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42310540615447)

1. 

As alterações passam a ser registradas normalmente.

1. 

É possivel controlar quais entidades serão monitoradas a partir da ativação/inativação das Triggers correspondentes pelo controle na tela (recomendado) ou via Banco de Dados.

1. 

É necessário **reiniciar o Sankhya OM** após ativar para que os registros comecem a funcionar corretamente.
 

##### **Quando o log é desativado:**

- 

O switch da tela será desligado.

- 

O sistema **para de registrar alterações**.

- 

As configurações são aplicadas imediatamente.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310524970647)

 IMPORTANTE:** As configurações de log só entram em vigor completamente após o reinício do sistema. Se o log estiver ativado e você não reiniciar, os registros não funcionarão corretamente.

 

#### **Como consultar os registros de alteração?**

Após a ativação do serviço, as alterações registradas podem ser consultadas de duas formas:

**1. Pelo banco de dados**

- 

Os registros são gravados na tabela **TGLATS**.

**2. Pela API**

- 

Também é possível consultar as alterações pelo ''https://api.sankhya.com.br/logAlteracoesTabelas''

Consulte a documentação completa no ****[''Endpoint''](https://developer.sankhya.com.br/reference/get_logalteracoestabelas).

####  

#### **Jornada de Uso**

##### **Acompanhamento e funcionamento interno**

O Instance Logs Monitor MM conta com três processos automáticos que garantem o bom funcionamento:

##### **1. Coleta de alterações**

- 

Executa a cada minuto.

- 

Registra todas as alterações detectadas no sistema.

- 

Pode apresentar um pequeno atraso de até 1 minuto nas consultas.

##### **2. Limpeza de registros**

- 

Executa a cada hora.

- 

Remove registros antigos automaticamente, conforme o prazo configurado pelo parâmetro LOGTABMAXAGE  (padrão: 3 dias com máximo de 7 dias). 

##### **3. Atualização de entidades monitoradas**

- 

Executa uma vez ao dia.

- 

Garante que novas áreas do sistema sejam incluídas no monitoramento, sem necessidade de intervenção manual.

Todos esses processos são executados automaticamente após a ativação do serviço. Não é necessário configurá-los manualmente.

 

#### **Pontos de atenção**

##### **Ajuste de desempenho**

Se a sua base de dados tiver um volume muito alto de alterações, é possível ajustar o comportamento do consumo por meio de parâmetros técnicos. Esses ajustes envolvem:

- 

Intervalo entre execuções.

- 

Volume de alterações processadas por vez.

- 

Tamanho dos lotes de gravação.

Esses ajustes devem ser feitos com acompanhamento técnico especializado, pois podem afetar o desempenho do banco de dados.

 

##### **Compatibilidade com versões**

Mesmo que sua base ainda não esteja usando a versão mais recente do log, o micro módulo será instalado para garantir compatibilidade e permitir um possível downgrade. O sistema identifica automaticamente se a versão utilizada já é compatível com o novo modelo.

 

#### **Considerações finais**

A transição para o Instance Logs Monitor MM representa uma evolução importante no controle de alterações do ERP Sankhya. A arquitetura mais leve e desacoplada garante:

- 

Menor impacto nas atualizações do sistema.

- 

Melhor capacidade de escalar com o crescimento da base.

- 

Facilidade no monitoramento e ajuste de performance.

Para garantir o funcionamento ideal:

- 

Mantenha o serviço ativado apenas se realmente necessário.

- 

Reinicie o sistema após qualquer alteração no status do log.

- 

Monitore a carga do ambiente antes de realizar ajustes de performance.


---

### 🔗 Links e Referências Internas:

- [''Endpoint''](https://developer.sankhya.com.br/reference/get_logalteracoestabelas)