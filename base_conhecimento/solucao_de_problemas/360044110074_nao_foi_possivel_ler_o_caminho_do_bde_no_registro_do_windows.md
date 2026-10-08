# Não foi possível ler o caminho do BDE no registro do Windows

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110074-N%C3%A3o-foi-poss%C3%ADvel-ler-o-caminho-do-BDE-no-registro-do-Windows](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110074-N%C3%A3o-foi-poss%C3%ADvel-ler-o-caminho-do-BDE-no-registro-do-Windows)  
> **ID:** `360044110074` | **Última Atualização:** 2026-07-22T15:53:56Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948890809367)

 MENSAGEM:**

Não foi possível ler o caminho do BDE no registro do Windows 
Chave KEY_LOCAL_MACHINE\SOFTWARE[\WOW6432NODE]\Borland\Database Engine

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948890799895)

 SITUAÇÃO:**

Ao tentar acessar o MGE/MITRA, ocorre a mensagem:

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948890820759)

 CAUSA:**

Ocorre quando os usuários não possuem permissões mínimas para gravar dados executados pelo BDE.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948931761431)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948931766935)

 Com o usuário Administrador do Sistema Operacional Windows, pesquise pela palavra 'Executar' ou aperte o botão do teclado 'Windows + R'. Acesse: Executar [Abrira um pop-up]

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360063053313)

 

Digite 'regedit' e clique em OK.

Navegue ate o caminho: 

KEY_LOCAL_MACHINE\SOFTWARE\Borland\Database Engine [**Para Sistema 32 Bits**]

KEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Borland\Database Engine [**Para sistema 64 Bits**]

 

**Exemplo:**

 

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360062172514)

 

Em Nomes de Grupo ou de Usuário adicione Administradores, depois os Usuários que utilizarão o sistema e, em Permissões, marque todas as opções da coluna Permitir, aplique e clique em OK.

 

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/360063053333)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948931778327)

 OBSERVAÇÃO:**

Este procedimento geralmente é executado pela Equipe de TI da Empresa, que possui permissões de **Administrador**.