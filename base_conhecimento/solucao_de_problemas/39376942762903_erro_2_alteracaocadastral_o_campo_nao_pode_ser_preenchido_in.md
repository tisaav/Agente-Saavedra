# Erro 2 - AlteracaoCadastral O campo não pode ser preenchido: Indicador de preenchimento de cota

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39376942762903-Erro-2-AlteracaoCadastral-O-campo-n%C3%A3o-pode-ser-preenchido-Indicador-de-preenchimento-de-cota](https://ajuda.sankhya.com.br/hc/pt-br/articles/39376942762903-Erro-2-AlteracaoCadastral-O-campo-n%C3%A3o-pode-ser-preenchido-Indicador-de-preenchimento-de-cota)  
> **ID:** `39376942762903` | **Última Atualização:** 2026-07-29T13:23:20Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39376942748695)

 **Mensagem**

2 - AlteracaoCadastral - O campo não pode ser preenchido: Indicador de Preenchimento de Cota. Elemento: /eSocial/evtAltCadastral/alteracao/dadosTrabalhador/infoDeficiencia/infoCota [null]
 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39376939148951)

 **Situação**

Ao tentar enviar o evento **"S-2205"** (Alteração Cadastral) para o eSocial, o sistema retorna o erro informando que o campo **"Indicador de Preenchimento de Cota"** não pode ser preenchido. Este erro pode ocorrer quando há inconsistências no cadastro do funcionário relacionadas às informações de deficiência ou quando existe conflito com eventos posteriores já enviados ao eSocial.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39376939149207)

 **Solução**

Para resolver este erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39376939149335)

 Acesse a tela **"Configuração de Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize o funcionário que apresenta o erro.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39376942748823)

 Verifique se a opção **"Preenche Cota de PCD's"** está marcada indevidamente. Se o funcionário não é PCD ou não deve mais preencher a cota, desmarque esta opção.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40936136701207)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39376939149591)

 Caso o erro persista, acesse o portal do eSocial e identifique se há eventos conflitantes com data posterior ao evento que está tentando enviar. Utilize o código de recibo informado na mensagem de erro para localizar o evento.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39376939149847)

 Se identificar eventos **"S-2205"** ou **"S-2206"** com data posterior, exclua-os .
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39376939150231)

 Após a exclusão dos eventos conflitantes, retorne ao sistema e envie novamente o evento **"S-2206"** ou **"S-2205"**.
 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39376939150359)

 Valide se o evento foi recepcionado com sucesso pelo eSocial.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39376942749335)

 **Causa**

Este erro ocorre por dois motivos principais:

**1. Configuração incorreta do campo "Preenche Cota de PCD's":** quando a opção está marcada no cadastro do funcionário, mas não há informações de deficiência preenchidas, ou quando o funcionário não se enquadra mais como PCD.
 

**2. Conflito de eventos no eSocial:** quando existem eventos de alteração cadastral (**"S-2205"**) ou alteração contratual (**"S-2206"**) já enviados ao eSocial com data posterior à data do evento que está sendo enviado, criando uma inconsistência na linha do tempo dos eventos do funcionário.