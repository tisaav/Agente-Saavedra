# Processo D-1001 — Informações do Contribuinte

> **Módulo:** Fiscal e Contábil | **Subseção:** Processos do Portal da Reforma Tributária  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte](https://ajuda.sankhya.com.br/hc/pt-br/articles/41605447288983-Processo-D-1001-Informa%C3%A7%C3%B5es-do-Contribuinte)  
> **ID:** `41605447288983` | **Última Atualização:** 2026-09-09T18:14:28Z

---

**Módulo:** Portal da Reforma Tributária › DeRE
**Caminho de acesso:** Portal da Reforma Tributária › DeRE › D1001 — Inf. Contribuinte
**Versão mínima SankhyaOm 4.36:** 4.36b88 + erpcore-module 5.8.21 
**Versão mínima Livros:** 5.38

 
**🚨 Ambiente de testes**
Esta funcionalidade está em ambiente de testes. Todos os envios realizados aqui serão desconsiderados quando a funcionalidade entrar em produção. O governo federal ainda não liberou o serviço de transmissão oficial dos eventos da DeRE. Quando a Receita Federal disponibilizar a API, será necessário reenviar os eventos para obter o recibo definitivo.

Neste artigo

- [O que é e para que serve](#o-que-e)

- [Antes de começar](#antes-de-comecar)

- [Painel D-1001 — Informações do Contribuinte](#painel)

- [Como enviar o D-1001](#como-enviar)

- [Etapa 1 — Revisão](#etapa-1)

- [Etapa 2 — Dados DeRE](#etapa-2)

- [Etapa 3 — Atividades](#etapa-3)

- [Etapa 4 — Revisão Final](#etapa-4)

- [Tela de confirmação](#confirmacao)

- [Pontos de atenção](#pontos-atencao)

- [Perguntas frequentes](#faq)

## O que é e para que serve

O evento D-1001 — Informações do Contribuinte é o primeiro evento obrigatório da DeRE e identifica o contribuinte perante a Receita Federal: registra o regime tributário principal, os regimes secundários e as atividades exercidas conforme a legislação do IBS e CBS. Nenhum outro evento da DeRE pode ser transmitido sem que o D-1001 esteja processado com sucesso para o mesmo CNPJ raiz.

## Antes de começar

Para que uma empresa apareça no painel D-1001, o Administrador do sistema precisa habilitar o módulo DeRE para ela em Configurações › Empresas. Empresas sem habilitação não aparecem na grade, independentemente do regime tributário cadastrado no ERP.

**💡 Dica**
Para instruções sobre como habilitar o módulo DeRE por empresa, acesse [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria).

## Painel D-1001 — Informações do Contribuinte

Ao acessar DeRE › D1001 — Inf. Contribuinte, você vê a grade com todas as empresas habilitadas para DeRE e o status do último evento enviado para cada uma.

### Colunas da grade

- 
**Cód. Empresa** — código interno da empresa no ERP.

- 
**Razão Social** — nome da empresa.

- 
**CNPJ** — CNPJ completo da empresa.

- 
**Status** — situação do último evento D-1001 para aquela empresa: Sem evento (nenhum envio registrado), Não enviado (evento criado mas não transmitido), Processando (transmitido, aguardando retorno) ou Enviado (processado com recibo).

- 
**Ocorrência** — exibe Erro ou Aviso quando o último evento retornou ocorrências; vazio se não houver.

### Filtros disponíveis

Use os filtros Empresa, Status e Ocorrência para localizar empresas específicas na grade.

### Ações disponíveis

- 
**Iniciar** — abre o wizard para enviar o D-1001. Disponível para empresas com status Sem evento ou Não enviado (Inclusão) e Enviado (Alteração). Não disponível para empresas com status Processando.

- 
**Detalhes** — navega para o Histórico de Eventos filtrado pelo CNPJ da empresa selecionada.

- 
**Iniciar (N)** — ao marcar múltiplas empresas na grade, esse botão aparece no topo e inicia o wizard para todas as selecionadas simultaneamente.

## Como enviar o D-1001

O envio é feito por um wizard de 4 etapas. Clique em Iniciar na linha da empresa para abrir o wizard. Para enviar para várias empresas ao mesmo tempo, marque as empresas desejadas na grade e clique em Iniciar (N).

**ℹ️ Nota**
O wizard identifica automaticamente a operação correta: abre com Inclusão para empresas sem evento enviado e com Alteração para empresas que já possuem D-1001 com recibo. O badge da operação aparece ao lado do CNPJ e da Razão Social em cada etapa.

### Etapa 1 — Revisão

Revise os dados cadastrais da empresa antes de prosseguir. Nenhum campo é editável nesta etapa — as informações vêm do cadastro do ERP. Verifique se Razão Social, CNPJ, Regime Tributário, CNAE Principal, Logradouro, Município e CEP estão corretos.

Se algum dado estiver incorreto, corrija no cadastro da empresa no ERP antes de continuar. Clique em Continuar para avançar.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41605502230423)

### Etapa 2 — Dados DeRE

Informe o regime tributário e a natureza tributária da empresa.

- 
**Regime Principal** — selecione o regime tributário principal da empresa para fins de IBS e CBS. Opções disponíveis no MVP: 9 — Normas Gerais (empresas em geral), 1 — Serviços Financeiros ou 2 — Planos de Saúde.

- 
**Regimes Secundários** — marque até 3 regimes adicionais, quando a empresa exercer atividades em mais de um regime. O regime selecionado como principal não aparece nas opções secundárias.

- 
**Indicador de natureza tributária** — selecione 0 — Tributação regular para empresas sujeitas ao IBS e CBS, ou 1 — Imunidade ou não incidência para empresas com tratamento diferenciado.

**⚠️ Atenção**
O regime secundário não pode ser igual ao regime principal. O wizard bloqueia o avanço se você tentar selecionar o mesmo valor nos dois campos.

Clique em Continuar para avançar.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41605447281815)

### Etapa 3 — Atividades

Esta etapa aparece somente quando a empresa tem Regime 1 — Serviços Financeiros ou Regime 2 — Planos de Saúde selecionado como regime principal ou secundário. Se nenhum dos dois for aplicável, o wizard pula esta etapa automaticamente.

Selecione as atividades exercidas pela empresa conforme os regimes informados na etapa anterior:

- 
**Serviços Financeiros** — obrigatório quando o Regime 1 estiver selecionado (principal ou secundário). Use o campo de busca para filtrar as atividades disponíveis e marque todas que se aplicam.

- 
**Planos de Saúde** — obrigatório quando o Regime 2 estiver selecionado (principal ou secundário). O wizard bloqueia o avanço se nenhuma atividade for selecionada para o regime correspondente.

Clique em Continuar para avançar.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41605447282711)

### Etapa 4 — Revisão Final

Confira o resumo do evento antes de transmitir: a tabela exibe a operação, o CNPJ, a Razão Social e a competência de cada empresa que será incluída no envio.

**ℹ️ Nota**
Nesta etapa, o sistema valida o XML gerado antes de permitir o envio. Se a validação falhar, o erro é exibido em tela e o evento fica com status Não enviado no Histórico. Corrija os dados indicados e reinicie o wizard.

Quando o evento estiver validado, a mensagem "O evento foi validado e está pronto para transmissão. Clique em 'Concluir' para enviar." é exibida. Clique em Concluir para transmitir.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41605502237079)

### Tela de confirmação

Após o envio, o sistema exibe a tela de confirmação com a mensagem "Evento enviado com sucesso!" e um aviso lembrando que os endpoints de produção ainda não estão liberados. A partir daqui, você pode:

- 
**Consultar histórico** — acessa o Histórico de Eventos filtrado pelo envio que acabou de ser realizado.

- 
**Voltar para painel** — retorna à grade D-1001.

## 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42315407809815)

## Pontos de atenção

Em qualquer etapa do wizard, clicar em Cancelar exibe uma confirmação antes de descartar o preenchimento. Se confirmar o cancelamento, todos os dados informados nas etapas são perdidos e você retorna à grade D-1001.

## Perguntas frequentes

**Por que o botão Iniciar não aparece para uma empresa?**

O botão Iniciar não fica disponível para empresas com status Processando. Aguarde o processamento do evento atual antes de iniciar um novo envio. Acesse o Histórico de Eventos via botão Detalhes para acompanhar o andamento.

**A etapa de Atividades não apareceu no meu wizard. É um erro?**

Não. A Etapa 3 — Atividades só é exibida quando a empresa tem Regime 1 — Serviços Financeiros ou Regime 2 — Planos de Saúde selecionado (principal ou secundário) na Etapa 2. Para empresas com Regime 9 — Normas Gerais, o wizard pula essa etapa automaticamente e vai direto para a Revisão Final.

**Preciso reenviar o D-1001 quando o módulo entrar em produção?**

Sim. Todos os eventos transmitidos nesta fase são de teste e não têm validade fiscal. Quando a Receita Federal disponibilizar a API oficial, será necessário reenviar o D-1001 — e os demais eventos — para obter o recibo definitivo.

**Posso enviar o D-1001 para várias empresas ao mesmo tempo?**

Sim. Marque as empresas desejadas na grade e clique em Iniciar (N). O wizard percorre as mesmas 4 etapas, mas cada empresa aparece como um card independente, com seu próprio badge de operação e seus próprios campos para preenchimento.


---

### 🔗 Links e Referências Internas:

- [Tela Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria)