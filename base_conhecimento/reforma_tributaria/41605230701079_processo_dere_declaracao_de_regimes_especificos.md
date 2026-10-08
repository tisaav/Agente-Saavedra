# Processo DeRE — Declaração de Regimes Específicos

> **Módulo:** Reforma Tributaria | **Subseção:** Processos do Portal da Reforma Tributária  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605230701079-Processo-DeRE-Declara%C3%A7%C3%A3o-de-Regimes-Espec%C3%ADficos)  
> **ID:** `41605230701079` | **Última Atualização:** 2026-09-09T18:14:28Z

---

**Módulo:** Portal da Reforma Tributária › DeRE
**Caminho de acesso:** Portal da Reforma Tributária › DeRE
**Versão mínima SankhyaOm 4.36:** 4.36b88 + erpcore-module 5.9.5
**Versão mínima SankhyaOm 4.35:****** 4.35b777
**Versão mínima Livros:** 5.38.0

 
**🚨 Ambiente de testes**
Esta funcionalidade está em ambiente de testes. Todos os envios realizados aqui serão desconsiderados quando a funcionalidade entrar em produção. O governo federal ainda não liberou o serviço de transmissão oficial dos eventos da DeRE. Quando a Receita Federal disponibilizar a API, será necessário reenviar os eventos para obter o recibo definitivo.

 

Neste artigo

- [O que é e para que serve](#o-que-e)

- [Antes de começar](#antes-de-comecar)

- [Habilitação de módulos](#habilitacao-modulos)

- [Como funciona a estrutura de eventos](#estrutura-eventos)

- [Histórico de Eventos](#historico-eventos)

- [Perguntas frequentes](#faq)

 

## O que é e para que serve

O módulo DeRE no Portal da Reforma Tributária é o ponto central para cumprir a Declaração de Regimes Específicos (DeRE), obrigação acessória instituída pela Lei Complementar nº 214/2025 para apuração do IBS e CBS em setores com regras tributárias diferenciadas. Por meio dele, você gera, assina digitalmente e transmite os eventos obrigatórios à Receita Federal, além de acompanhar o status de cada envio com rastreabilidade completa dentro do Sankhya Om.

**💡 Dica**
Para mais informações sobre a DeRE, consulte o [site oficial da Declaração de Regimes Específicos](https://www.gov.br/sped/pt-br/assuntos/documentos-fiscais/dere).

## Antes de começar

Para que as empresas apareçam no módulo DeRE, o Administrador do sistema precisa habilitar o módulo DeRE para cada empresa na tela Portal da Reforma Tributária › Configurações › Empresas. Empresas sem habilitação não aparecem em nenhuma tela do módulo, independentemente do regime tributário cadastrado no ERP.

**💡 Dica**
Para instruções completas sobre como habilitar o módulo DeRE por empresa, acesse [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria#).

## Habilitação de módulos

Além da DeRE, o Portal da Reforma Tributária reúne outros módulos que o Administrador do sistema pode habilitar conforme a necessidade da empresa, como a DeRE, Assistente de Configuração Integral e Assistente de Configuração de Exceções. Cada módulo possui sua própria tela e seu artigo de documentação específico, acessíveis a partir do Portal da Reforma Tributária.

## Como funciona a estrutura de eventos

A DeRE é transmitida por meio de eventos eletrônicos em formato XML, assinados digitalmente com certificado ICP-Brasil. Cada tipo de evento tem uma finalidade específica e segue uma ordem obrigatória de envio: nenhum evento periódico pode ser transmitido sem que o D-1001 esteja processado com sucesso para o mesmo CNPJ raiz.

No Sankhya Om, cada tipo de evento tem seu próprio artigo de documentação com o passo a passo completo. Confira abaixo os eventos disponíveis:

- 
[DeRE — Evento D-1001: Informações do Contribuinte](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte).

## Histórico de Eventos

A tela Histórico de Eventos DeRE, acessível em [Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria#) › DeRE › Histórico de Eventos, reúne todos os eventos transmitidos e permite acompanhar o status de cada envio, baixar os XMLs gerados e excluir registros quando necessário.

### Colunas da grade

- 
**Cód. Empresa** — código interno da empresa no ERP.

- 
**Razão Social** — nome da empresa.

- 
**CNPJ** — CNPJ completo da empresa.

- 
**Evento** — código do evento transmitido (ex.: D-1001).

- 
**Operação** — tipo da operação realizada: Inclusão, Alteração ou Exclusão.

- 
**Status** — situação do evento: Enviado (verde), Processando (amarelo) ou Não enviado (cinza).

- 
**Ambiente** — indica se o evento foi gerado em ambiente de Teste ou de produção. No período atual, todos os eventos exibem Teste.

- 
**Data/Hora** — data e hora em que o evento foi gerado no sistema.

### Filtros disponíveis

Você pode combinar os filtros Empresa, Período, Status, Tipo do evento, Operação, Ambiente e Recibo para localizar eventos específicos na grade.

### Ações disponíveis

- 
**Baixar Envio** — faz o download do XML gerado no momento do envio do evento.

- 
**Baixar Retorno** — faz o download do XML de retorno recebido da Receita Federal, quando disponível.

- 
**Excluir** — remove o registro do histórico. Disponível somente para eventos sem recibo de processamento nesta versão.

**ℹ️ Nota**
Os XMLs baixados por Baixar Envio e Baixar Retorno são gerados em ambiente de testes e não têm validade fiscal. Guarde-os como referência para validação técnica; o reenvio em produção será necessário quando a API da Receita Federal for liberada.

## Perguntas frequentes

**Preciso reenviar os eventos quando o módulo entrar em produção?**

Sim. Todos os eventos transmitidos nesta fase são de teste e não têm validade fiscal. Quando a Receita Federal disponibilizar a API oficial, será necessário reenviar os eventos para obter o recibo definitivo e cumprir a obrigação acessória.

**Por que uma empresa não aparece no módulo DeRE?**

A empresa precisa ter o módulo DeRE habilitado pelo Administrador do sistema em Configurações › Empresas. Sem essa habilitação, a empresa não aparece em nenhuma tela do módulo, mesmo que tenha regime tributário cadastrado no ERP. Acesse [Tela Portal da Reforma Tributária](#) para instruções.

**Quem está obrigado a transmitir a DeRE?**

Estão obrigados os prestadores de serviços financeiros, as operadoras de planos de assistência à saúde (incluindo planos funerários e de saúde animal) e as entidades que explorem concursos de prognósticos. Empresas do Simples Nacional estão dispensadas, salvo opção pelo regime regular de IBS/CBS.

**Preciso configurar as alíquotas de CBS/IBS para cada empresa?**

Não necessariamente. O sistema permite configurar as alíquotas para todas as empresas de uma vez utilizando a "empresa zero". Caso essa opção não apareça na tela para uma empresa específica, isso normalmente indica que já existe uma configuração pré-existente no cadastro daquela empresa.


---

### 🔗 Links e Referências Internas:

- [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria#)
- [DeRE — Evento D-1001: Informações do Contribuinte](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte)