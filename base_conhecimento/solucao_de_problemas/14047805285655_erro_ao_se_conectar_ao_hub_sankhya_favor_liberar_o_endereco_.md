# Erro ao se conectar ao HUB Sankhya, Favor liberar o endereço 'grupo.sankhya.com.br' porta 443 no seu servidor

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14047805285655-Erro-ao-se-conectar-ao-HUB-Sankhya-Favor-liberar-o-endere%C3%A7o-grupo-sankhya-com-br-porta-443-no-seu-servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/14047805285655-Erro-ao-se-conectar-ao-HUB-Sankhya-Favor-liberar-o-endere%C3%A7o-grupo-sankhya-com-br-porta-443-no-seu-servidor)  
> **ID:** `14047805285655` | **Última Atualização:** 2026-07-22T14:59:35Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868255594647)

 MENSAGEM:**

Erro ao se conectar ao HUB Sankhya, Favor liberar o endereço 'grupo.sankhya.com.br' porta 443 no seu servidor!

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868292571031)

SOLUÇÃO:**

Verifique as regras de permissões de Firewall/ Proxy no servidor de aplicação e certifique-se de que a porta 443 e endereço 'grupo.sankhya.com.br' esteja liberada.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868255603991)

 Passos para verificar as regras de permissões de Firewall/ Proxy:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Acesse as configurações do Firewall/ Proxy do servidor;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Procure pelas regras de permissões de saída;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Certifique-se de que a porta 443 do endereço 'grupo.sankhya.com.br' esteja liberada nas regras de permissões de saída.

Outra solução, é verificar a data e hora do servidor de aplicação em que o serviço Wildfly Sankhya está rodando. É importante que a data e hora do servidor estejam corretas, pois caso contrário, pode ocorrer problemas de autenticação durante a conexão com o HUB Sankhya.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868292578839)

 Passos para verificar e ajustar a data e hora em ambiente Linux:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Acesse o terminal do servidor;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Digite o comando "date" para verificar a data e hora atual;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Se a data e hora estiverem incorretas, digite o comando "date -s 'YYYY-MM-DD HH:MM:SS'" para ajustar a data e hora. Substitua 'YYYY-MM-DD HH:MM:SS' pela data e hora corretas;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Verifique novamente a data e hora digitando o comando "date" e certifique-se de que a data e hora foram ajustadas corretamente.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868255608215)

 Passos para verificar e ajustar a data e hora em ambiente Windows:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Clique no botão "Iniciar" e digite "Data e Hora" na barra de pesquisa;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Clique em "Alterar data e hora" para abrir as configurações de data e hora;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Certifique-se de que a data e hora estejam corretas e ajuste-as, se necessário;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702262935)

 Clique em "OK" para salvar as alterações.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868292584599)

 Depois de seguir esses passos, reinicie o serviço Wildfly Sankhya e tente novamente se conectar ao HUB Sankhya.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868292585239)

 **OBSERVAÇÃO:**

É importante notar que, em alguns casos, o erro também pode ocorrer quando o serviço do HUB da Sankhya está com instabilidade. Nesses casos, a correção do erro não depende das configurações de Firewall/Proxy ou da data e hora do servidor. Caso seguir os passos para verificar e corrigir o erro, mas o problema persistir, é recomendável entrar em contato com o Service Desk da Sankhya para confirmar se o serviço do HUB está funcionando corretamente. Em caso de instabilidade do serviço do HUB, será necessário aguardar a normalização para que a conexão seja restabelecida.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16868292586519)

CAUSA:**

O erro ocorre quando a conexão com o HUB Sankhya falha devido à porta 443 e o endereço 'grupo.sankhya.com.br' não estar liberada no servidor;

Data e Hora do Servidor de aplicação incorretas;

Serviço HUB da Sankhya com instabilidade;