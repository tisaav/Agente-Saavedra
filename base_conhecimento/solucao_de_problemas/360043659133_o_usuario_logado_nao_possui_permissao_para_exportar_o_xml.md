# O usuário logado não possui permissão para exportar o XML.

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659133-O-usu%C3%A1rio-logado-n%C3%A3o-possui-permiss%C3%A3o-para-exportar-o-XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659133-O-usu%C3%A1rio-logado-n%C3%A3o-possui-permiss%C3%A3o-para-exportar-o-XML)  
> **ID:** `360043659133` | **Última Atualização:** 2026-08-01T01:10:57Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16136813804055)

**Mensagem**

[ECOM_E00023] O usuário logado não possui permissão para exportar o XML.

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/16136805329687)

**Situação**

Ao tentar exportar um arquivo XML, como por exemplo ao gerar o XML do CT-e pelo **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas) ou realizar o download de arquivos XML de notas fiscais, o sistema apresenta a mensagem de erro informando que o usuário não possui permissão para realizar esta operação.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16136805333271)

**Solução**

Para resolver o problema, configure as permissões necessárias no cadastro do usuário seguindo os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16136805335703)

 Acesse a tela **"Usuários"** (Configurações >> Controle de Acesso >> Usuários).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16136805338775)

 Localize e selecione o usuário que está enfrentando o problema de exportação.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/42386615007255)

 Acesse a aba **"Segurança"** no cadastro do usuário.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/42386591658007)

 Localize o campo **"Permite exportar relatórios?"** e marque esta opção para ativar a permissão.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/42386615008279)

 Localize o campo **"Pode Imprimir/Reimprimir Nota nas Centrais"** e marque esta opção para ativar a permissão.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14661315046167)

![6](https://ajuda.sankhya.com.br/hc/article_attachments/42386615010583)

 Clique no **"Botão Salvar"** para confirmar as alterações realizadas.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/42386615010839)

 Solicite ao usuário que saia do sistema e faça login novamente para que as novas permissões sejam aplicadas.

![8](https://ajuda.sankhya.com.br/hc/article_attachments/42386591659031)

 Teste a funcionalidade tentando novamente exportar o XML para verificar se o problema foi resolvido.

**Observações importantes:**

- Esta configuração é feita por usuário, sendo necessário repetir o processo para cada usuário que necessitar desta permissão.

1. A permissão **"Permite exportar relatórios?"** afeta não apenas a exportação de XML, mas também a exportação de relatórios em geral.

1. Se o problema persistir após seguir estes passos, verifique se o usuário possui todas as outras permissões necessárias para acessar a funcionalidade específica, como permissões na tela de CT-e ou nas centrais de vendas.

1. Quando utilizado via navegador Google Chrome, pode ser necessário também habilitar a opção de conteúdo não seguro nas configurações do navegador, alterando de "Bloqueado" para "Permitir".

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16136805341335)

**Causa**

O erro ocorre porque o usuário que está tentando realizar a operação de exportação de XML não possui as permissões necessárias configuradas no sistema. Especificamente, faltam as permissões de **"Permite exportar relatórios?"** e **"Pode Imprimir/Reimprimir Nota nas Centrais"** na aba de **"Segurança"** do cadastro do usuário.