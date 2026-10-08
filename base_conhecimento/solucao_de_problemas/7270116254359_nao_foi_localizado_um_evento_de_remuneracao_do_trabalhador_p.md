# Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7270116254359-N%C3%A3o-foi-localizado-um-evento-de-remunera%C3%A7%C3%A3o-do-trabalhador-para-o-per%C3%ADodo-e-com-mesmo-demonstrativo-de-pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/7270116254359-N%C3%A3o-foi-localizado-um-evento-de-remunera%C3%A7%C3%A3o-do-trabalhador-para-o-per%C3%ADodo-e-com-mesmo-demonstrativo-de-pagamento)  
> **ID:** `7270116254359` | **Última Atualização:** 2026-07-29T13:24:11Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513197779223)

 MENSAGEM**:

Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento. Ação Sugerida:
Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202 ou S-1207 no campo "Identificador de Recibo de Pagamento", obedecendo a relação:
.Se Tipo de Pagamento = [1], em S-1200;
.Se Tipo de Pagamento = [4], em S-1202;
.Se Tipo de Pagamento = [5], em S-1207

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513222286487)

 SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513222288535)

 Acesse a central do e-Social e verifique se o evento de remuneração (S-1200/S-2299) foi enviado sem erros ao portal do eSocial; 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16705033214359)

S-1200 enviado, para conferência acesse o Portal do eSocial na opção: **Folha de Pagamento >> Gestão de folha >> Trabalhadores >> Remuneração devida** e confira se todas as folhas que o funcionário teve no mês constam no portal (Exemplo: adiantamento, férias, normal);

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16705033214359)

S-2299 enviado, para conferência acesse o Portal do eSocial na opção: **Empregado >> Gestão de Empregados >> Desligamento** e verifique se a rubricas da rescisão foram enviadas (se tiver folha de adiantamento precisa constar aí também);

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513197789975)

 Caso não tenha enviado o evento de remuneração, envie e depois gere o S-1210 para envio;

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513222302871)

CAUSA:**

Essa mensagem de erro de validação ocorre no retorno do Evento S-1210 quando o evento de remuneração (S-1200 /S-2299) deste funcionário não foi enviado ou retornou com erros.