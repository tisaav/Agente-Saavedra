# Driver de conexão com o banco de dados está desatualizado

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360052313713-Driver-de-conex%C3%A3o-com-o-banco-de-dados-est%C3%A1-desatualizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052313713-Driver-de-conex%C3%A3o-com-o-banco-de-dados-est%C3%A1-desatualizado)  
> **ID:** `360052313713` | **Última Atualização:** 2026-07-22T15:29:56Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588518897815)

 MENSAGEM:**

Driver de conexão com o banco de dados está desatualizado.

A versão do banco de dados XX.X é mais recente que a versão do driver de conexão XX.X

Isto pode afetar o desempenho do sistema com relação ao carregamento de telas e a gravação de informações.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588518906519)

 SOLUÇÃO:**

Orientações a serem seguidas com apoio do T.I e/ou DBA da empresa:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588518909207)

 Efetuar o download do OJDBC no site da Oracle *(De acordo com a versão do seu banco de dados);*

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588518914967)

 Atualizar o driver de conexão com o banco de dados por este baixado da versão 12.2.X.X.X, conforme a versão do banco atualmente.

 

![Observa__o.png](https://ajuda.sankhya.com.br/hc/article_attachments/12633902349847)

 Vale ressaltar a importância de renomear o arquivo para "ojdbc.jar"

 

Esta troca é feita no caminho:

/home/mgeweb/wildfly_producao/modules/custom/ojdbc/main

- Parar o Wildfly;

- Substituir o arquivo neste caminho descrito acima com o usuário mgeweb.

- Iniciar novamente o Wildfly