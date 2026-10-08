# Erro na geração/envio do evento S-2240

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16645154941591-Erro-na-gera%C3%A7%C3%A3o-envio-do-evento-S-2240](https://ajuda.sankhya.com.br/hc/pt-br/articles/16645154941591-Erro-na-gera%C3%A7%C3%A3o-envio-do-evento-S-2240)  
> **ID:** `16645154941591` | **Última Atualização:** 2026-07-29T13:17:37Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16645111767959)

 MENSAGEM: **

Erro 1829 - Somente é permitido informar mais de um grupo de ambiente de trabalho [infoAmb] no caso de trabalhador avulso (código de categoria no RET igual a [2XX]). Elemento: /eSocial/evtExpRisco/infoExpRisco [] -----------------------------------Erro 632 - Já existe no evento um grupo com mesma chave de identificação. Elemento: /eSocial/evtExpRisco/infoExpRisco/infoAmb[2] [ nao localizado ]

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33229316703511)

 SITUAÇÃO: **

Ao tentar enviar o evento S-2240 (Condições Ambientais do Trabalho – Fatores de Risco), ocorre um erro durante o processo de envio

 

![taw.png](https://ajuda.sankhya.com.br/hc/article_attachments/33229287852695)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16645126548247)

 CAUSA:**

O erro ocorre devido a uma configuração incorreta na tela **"Configuração Funcionários" **(Configurações » Cadastros » Pessoal » Configuração Funcionários), especificamente na aba **"Ambiente de Trabalho"**, onde foram atribuídos dois ambientes simultaneamente ao mesmo colaborador.

Conforme as diretrizes do Manual de Orientação do eSocial (**MOS**), cada trabalhador deve estar vinculado a apenas um ambiente de trabalho por vez. A duplicidade de registros nessa aba viola essa regra, gerando uma inconsistência que impede o correto processamento das informações pelo sistema e, consequentemente, o envio do evento ao eSocial.

 

![taw1.png](https://ajuda.sankhya.com.br/hc/article_attachments/33229287855895)

 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16674213366679)

 SOLUÇÃO:**

É necessário revisar e corrigir a configuração do funcionário, mantendo apenas um único ambiente de trabalho ativo na aba Ambientes de Trabalho, conforme estabelecido pela legislação vigente e pelas diretrizes do Manual de Orientação do eSocial (MOS).