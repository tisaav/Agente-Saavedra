# Erro liberação de rescisão devido a S-2205 e S-2206 com data posterior à rescisão

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4405592111511-Erro-libera%C3%A7%C3%A3o-de-rescis%C3%A3o-devido-a-S-2205-e-S-2206-com-data-posterior-%C3%A0-rescis%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405592111511-Erro-libera%C3%A7%C3%A3o-de-rescis%C3%A3o-devido-a-S-2205-e-S-2206-com-data-posterior-%C3%A0-rescis%C3%A3o)  
> **ID:** `4405592111511` | **Última Atualização:** 2026-07-29T13:23:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370065855127)

 MENSAGEM:**

Ao acessar o menu **Avançado -> Liberar envio da folha para o eSocia**l, pesquisar pelo empregado e marcar a opção de rescisão, ao confirmar apresenta a seguinte mensagem: 

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4405957115543)

 

Para que seja possível liberar a rescisão, será necessário efetuar a exclusão dos eventos que foram enviados após a data da rescisão do contrato, pois para o eSocial a rescisão será sempre o último evento a ser enviado (S-2299).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057437719)

 SOLUÇÃO:**

Para se realizar a correção , siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370065898135)

 Realize uma nova geração dos eventos e, assim que finalizar, não libere nenhum evento.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057442455)

 Acesse: *MGEPessoal » Menu » Avançado » Consulta eventos por funcionários.*

Insira o código do funcionário, filtre a referência com a referência atual (Exemplo: de 08/2021 a 08/2021) e clique em aplicar.

 

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917789167383)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057448087)

 Localize o evento S-2205 ou S-2206, clique com o botão direito do mouse em cima dele, na opção **"Gerar evento como exclusão"** e confirme:

 

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917789174167)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057452951)

 Volte na Central do eSocial, clique em** ''Selecionar eventos Disponíveis"** e veja que o evento S-2205 ou S-2206 será apresentado na tela como exclusão, faça o envio.

 

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917789177623)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057459479)

 Acesse o cadastro do empregado, aba **“Registro de envio para o eSocial”**, clique com o botão direito, selecione a opção: **“Preencher data de alteração do S-2205 ou S-2206”**, informe a data anterior à rescisão.

 

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917781358231)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057466263)

 Gere novamente os eventos na Central do eSocial.

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057472407)

 Realize o envio do S-2205 ou S-2206 com a data alterada.

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057474711)

 Acesse a tela Avançado -> Liberar envio da folha para o eSocial, pesquise pelo empregado e marque a opção de Rescisão e faça a liberação da rescisão desejada.

 

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917781363351)

 

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370065930007)

 Gere novamente os eventos e realize o envio do S-2299 da rescisão.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370057483543)

 CAUSA:**

Cliente realiza alterações cadastrais ou contratuais com data posterior a rescisão e realiza o envio dos eventos S-2205 e S-2206. Ao tentar liberar a rescisão para envio, apresenta erro, pois o eSocial não aceita nenhum evento com data superior a da rescisão.