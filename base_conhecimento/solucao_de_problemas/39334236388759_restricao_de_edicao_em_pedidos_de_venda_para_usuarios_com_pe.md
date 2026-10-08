# Restrição de edição em pedidos de venda para usuários com permissão de consulta e faturamento

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39334236388759-Restri%C3%A7%C3%A3o-de-edi%C3%A7%C3%A3o-em-pedidos-de-venda-para-usu%C3%A1rios-com-permiss%C3%A3o-de-consulta-e-faturamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39334236388759-Restri%C3%A7%C3%A3o-de-edi%C3%A7%C3%A3o-em-pedidos-de-venda-para-usu%C3%A1rios-com-permiss%C3%A3o-de-consulta-e-faturamento)  
> **ID:** `39334236388759` | **Última Atualização:** 2026-09-18T17:02:04Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334236376471)

 **SITUAÇÃO**

Um usuário com perfil configurado apenas para consulta e faturamento tenta realizar a alteração de valores nos itens de um pedido de venda na tela **"Central de Vendas"** (Comercial » Consulta » Portal de Vendas), porém o sistema permite a edição ou apresenta comportamento inesperado, contrariando a restrição de acesso esperada para o seu nível de permissão.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334236376983)

 **CAUSA**

A causa raiz está relacionada à configuração de permissões no **"Controle de Acessos"** (Configurações » Controle de Acesso » Acessos). O perfil do usuário pode estar com a permissão de **"Alterar"** habilitada para a topologia da tela ou para o tipo de movimento específico, sobrepondo a restrição de apenas leitura necessária para o faturamento.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334236383511)

 **SOLUÇÃO**

Para garantir que usuários com acesso apenas à consulta e faturamento não alterem valores, siga os passos abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334243736599)

 Acesse a tela **"Acessos"** (Configurações » Controle de Acesso » Acessos).
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334236384151)

 Selecione o usuário ou o grupo de usuários desejado na árvore de acesso.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334236384535)

 Localize a tela **"**Comercial » Consulta » Portal de Vendas**"** e verifique as marcações de permissão.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334243740439)

 Remova a marcação do botão **"Alterar"** para garantir que a edição esteja bloqueada.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334243741207)

 Certifique-se de que a permissão de **"Faturar"** esteja ativa para permitir o processo de faturamento, enquanto a edição dos campos de valor permanece restrita.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334236385431)

 Salve as alterações realizadas no **"Acessos"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334236385815)

 Solicite que o usuário desconecte e conecte novamente no sistema para que as novas permissões sejam aplicadas.