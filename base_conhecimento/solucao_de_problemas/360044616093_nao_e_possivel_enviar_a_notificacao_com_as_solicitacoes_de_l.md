# Não é possível enviar a notificação com as solicitações de liberação pois o liberador "XXXXX" não está cadastrado como destinatário de SMS

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616093-N%C3%A3o-%C3%A9-poss%C3%ADvel-enviar-a-notifica%C3%A7%C3%A3o-com-as-solicita%C3%A7%C3%B5es-de-libera%C3%A7%C3%A3o-pois-o-liberador-XXXXX-n%C3%A3o-est%C3%A1-cadastrado-como-destinat%C3%A1rio-de-SMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616093-N%C3%A3o-%C3%A9-poss%C3%ADvel-enviar-a-notifica%C3%A7%C3%A3o-com-as-solicita%C3%A7%C3%B5es-de-libera%C3%A7%C3%A3o-pois-o-liberador-XXXXX-n%C3%A3o-est%C3%A1-cadastrado-como-destinat%C3%A1rio-de-SMS)  
> **ID:** `360044616093` | **Última Atualização:** 2026-07-22T15:54:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789289206551)

 MENSAGEM:**

[CORE_E03070] Não é possível enviar a notificação com as solicitações de liberação pois o liberador "XXXXX" não está cadastrado como destinatário de SMS.
Verifique se está cadastrado na tela de Destinatários e preencha o campo "Celular".

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789316012311)

 SITUAÇÃO:**

Ao tentar confirmar a liberação de limites de um documento, a seguinte mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789289216407)

 CAUSA:**

Ocorre quando o usuário que possui alçada para algum evento que está cadastrado para 'receber SMS' com a notificação da solicitação de liberação de limites, não está cadastrado em Destinatários e/ou não possui o número do telefone celular vinculado a este cadastro.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789316019479)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789289223319)

 Configurações » Avançado » Envio de Mensagens » Destinatários:

- Se a rotina de Liberação de Limites, envia um SMS para o celular do liberador, é preciso cadastrar o celular nesta tela e vincular o usuário Liberador.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789316032023)

 Caso não faça o uso de envio de SMS, pode desmarcar o envio de SMS acessando:

- Configurações » Controle de Acesso » Usuários

- Botão: Outras Opções>>Liberação de Limites

- Selecione os eventos e desmarque a opção 'Envio SMS'

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789289230231)

 Após o ajuste, volte a selecionar os usuários novamente para liberação de Limites.