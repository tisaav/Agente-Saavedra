# Erro 675 - Não é permitida a exclusão de evento de Admissão S-2200, Trabalhador Sem Vínculo S-2300 e Registro Preliminar S-2190 quando já existirem outros eventos trabalhistas para o mesmo vínculo/contrato

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/27891663096215-Erro-675-N%C3%A3o-%C3%A9-permitida-a-exclus%C3%A3o-de-evento-de-Admiss%C3%A3o-S-2200-Trabalhador-Sem-V%C3%ADnculo-S-2300-e-Registro-Preliminar-S-2190-quando-j%C3%A1-existirem-outros-eventos-trabalhistas-para-o-mesmo-v%C3%ADnculo-contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/27891663096215-Erro-675-N%C3%A3o-%C3%A9-permitida-a-exclus%C3%A3o-de-evento-de-Admiss%C3%A3o-S-2200-Trabalhador-Sem-V%C3%ADnculo-S-2300-e-Registro-Preliminar-S-2190-quando-j%C3%A1-existirem-outros-eventos-trabalhistas-para-o-mesmo-v%C3%ADnculo-contrato)  
> **ID:** `27891663096215` | **Última Atualização:** 2026-07-29T13:18:56Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/27912453313303)

**MENSAGEM**

Erro 675 - Não é permitida a exclusão de evento de Admissão S-2200, Trabalhador Sem Vínculo S-2300 e Registro Preliminar S-2190 quando já existirem outros eventos trabalhistas para o mesmo vínculo/contrato.
 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/27912453316247)

**SITUAÇÃO**

Mensagem de erro apresentada ao tentar realizar o envio do evento de exclusão de qualquer um dos eventos: S-2200/ S-2300/ S-2190 pela **"Central do eSocial"** (Pessoal+ >> Rotinas Folha >> Central do eSocial).
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/27912465118999)

**CAUSA**

Existem eventos do trabalhador enviados ao eSocial com data posterior aos eventos de cadastro (S-2200/ S-2300/ S-2190). O eSocial não permite a exclusão para manter a integridade cronológica dos dados trabalhistas.
 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/27912453319703)

**SOLUÇÃO**

Verifique no portal do eSocial quais eventos periódicos, não periódicos e Serviços Especializados em Segurança e Medicina do Trabalho (SESMT), do trabalhador em questão, já foram enviados.
 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450171033879)

 Caso a exclusão do cadastro seja necessária, é imprescindível que todos os eventos com data posterior à admissão sejam excluídos em ordem cronológica inversa, ou seja, do mais recente para o mais antigo.
 

**Atenção Especial para o S-2190:** Para excluir o S-2190 (Registro Preliminar), primeiro exclua o S-2200 ou S-2300 que o referencia.