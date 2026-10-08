# Erro 1521 - Não é permitida exclusão de evento de Registro Preliminar de Trabalhador

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32297632163991-Erro-1521-N%C3%A3o-%C3%A9-permitida-exclus%C3%A3o-de-evento-de-Registro-Preliminar-de-Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/32297632163991-Erro-1521-N%C3%A3o-%C3%A9-permitida-exclus%C3%A3o-de-evento-de-Registro-Preliminar-de-Trabalhador)  
> **ID:** `32297632163991` | **Última Atualização:** 2026-07-29T13:19:46Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32297647567767)

** MENSAGEM: **

**Erro 1521** - Não é permitida exclusão de evento de Registro Preliminar de Trabalhador se já houver evento de Admissão ou TSVE - Início definitivo (S-2200 ou S-2300) referenciando o mesmo evento de admissão preliminar.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32297632158231)

 **SITUAÇÃO:**

Esse erro ocorre quando se tenta excluir o evento S-2190 (Registro Preliminar de Trabalhador) após já ter sido enviado um evento S-2200 (Admissão) ou S-2300 (Trabalhador Sem Vínculo Empregatício) para o mesmo colaborador.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32297632158231)

 **SOLUÇÃO:**

Para corrigir esse erro, é necessário seguir uma ordem específica para a exclusão dos eventos: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32402231400599)

 Acesse o portal do **''eSocial''*** (Pessoal+''» ''Rotinas Folha''» ''Central do eSocial)* e verifique todos os eventos enviados para esse trabalhador;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32402276955671)

 Faça a exclusão dos eventos necessários em **ordem cronológica inversa**, ou seja, do evento mais recente para o mais antigo:

**Importante: **comece excluindo o evento S-2200 ou S-2300, conforme o caso. Somente após concluir essa exclusão com sucesso, o sistema permitirá remover o evento S-2190.

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32402276958999)

 **ATENÇÃO:**

Este procedimento deve ser realizado apenas quando for realmente necessário, preferencialmente no mês de admissão, e somente se ainda não houver folha calculada ou envios de eventos de alteração cadastral (S-2205) ou contratual (S-2206).

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32297647569175)

** CAUSA:**

A exclusão do registro preliminar não é permitida pelo sistema, pois já existem eventos posteriores vinculados ao mesmo contrato de trabalho.