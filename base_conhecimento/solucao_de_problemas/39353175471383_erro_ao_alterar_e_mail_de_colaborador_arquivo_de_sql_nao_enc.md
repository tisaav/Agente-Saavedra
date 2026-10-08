# Erro ao Alterar E-mail de Colaborador - Arquivo de SQL Não Encontrado

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39353175471383-Erro-ao-Alterar-E-mail-de-Colaborador-Arquivo-de-SQL-N%C3%A3o-Encontrado](https://ajuda.sankhya.com.br/hc/pt-br/articles/39353175471383-Erro-ao-Alterar-E-mail-de-Colaborador-Arquivo-de-SQL-N%C3%A3o-Encontrado)  
> **ID:** `39353175471383` | **Última Atualização:** 2026-07-29T13:22:56Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39353129852823)

 **Mensagem**

Arquivo de SQL não encontrado

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39353175468695)

 **Situação**

Ao tentar realizar alterações no cadastro de colaboradores, especificamente ao modificar informações de e-mail na tela **"Configuração Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários), aba **"endereços"**, o sistema apresenta erro informando que um arquivo SQL não foi encontrado, impedindo a conclusão da operação.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39353129853463)

 **Solução**

Para resolver este erro, siga os passos abaixo:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39353175470231)

 Verifique a versão atual do sistema acessando o menu **"Ícone do seu usuário" (localizado no canto superior direito)** e clicando em **"versão"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41355762884119)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41355762885527)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41355762885911)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39353129853719)

 **Para verificar as versões de módulo e sistema mais atuais, o faça por meio do link:**

[https://downloads.sankhya.com.br/consulta-versao?c=1](https://downloads.sankhya.com.br/consulta-versao?c=1)

**Para informações sobre o processo de atualização, siga este documento: **

https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39353129853975)

 Clique na aba **"Administração"** e verifique se há atualizações pendentes para os módulos instalados.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41355762886423)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41355762887319)

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39353129854359)

 Realize a atualização do sistema para a versão mais recente disponível, inicialmente em ambiente de teste.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39353175470615)

 Após a atualização em ambiente de teste, valide se o incidente foi corrigido tentando realizar a alteração do e-mail do colaborador novamente.
 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39353129854615)

 Confirmada a correção, aplique a atualização no ambiente de produção.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39353175470871)

 **Causa**

Este erro ocorre quando arquivos SQL necessários para executar determinadas operações no sistema estão ausentes ou não foram corretamente instalados. Isso pode acontecer devido a:

 

- 

**Versão desatualizada** do sistema que não contém os arquivos SQL necessários para processos específicos.
 

1. 

**Instalação incompleta** de módulos ou atualizações anteriores.
 

1. 

**Arquivos corrompidos** ou removidos acidentalmente do diretório do sistema.
 

1. 

**Falta de sincronização** entre os componentes do sistema após atualizações.
 

A atualização para a versão mais recente do sistema garante que todos os arquivos SQL necessários estejam presentes e corretamente configurados, permitindo o funcionamento adequado de todas as funcionalidades.


---

### 🔗 Links e Referências Internas:

- [https://downloads.sankhya.com.br/consulta-versao?c=1](https://downloads.sankhya.com.br/consulta-versao?c=1)