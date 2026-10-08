# Configuração do CAMPO LIVRE com formato inválido! Verifique o cadastro da conta bancária XX

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14714411789591-Configura%C3%A7%C3%A3o-do-CAMPO-LIVRE-com-formato-inv%C3%A1lido-Verifique-o-cadastro-da-conta-banc%C3%A1ria-XX](https://ajuda.sankhya.com.br/hc/pt-br/articles/14714411789591-Configura%C3%A7%C3%A3o-do-CAMPO-LIVRE-com-formato-inv%C3%A1lido-Verifique-o-cadastro-da-conta-banc%C3%A1ria-XX)  
> **ID:** `14714411789591` | **Última Atualização:** 2026-07-22T14:58:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782844674327)

 MENSAGEM:**

[CORE_E03771]: Configuração do CAMPO LIVRE com formato inválido! Verifique o cadastro da conta bancária XX.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782872344343)

 CAUSA:**

Ocorre quando o campo Usar geração da linha digitável está selecionado, mas a linha digitável não está informada.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782844677527)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782872334231)

 Acesse a configuração da conta bancária *(Caminho de acesso: Configurações » Cadastros » Bancários » Contas*), aba **"Boleto(s)/ Duplicatas"** e verifique se o campo **"Usar geração da linha digitável"** está selecionado. Sempre que este campo estiver selecionado é preciso que o campo **"Linha digitável"** também esteja devidamente preenchido.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782872336535)

 A marcação da linha Usar geração da Linha digitável será utilizada somente para os casos em que o sistema não esteja preparado para geração da linha digitável de forma automática, para tanto o sistema lê o código do banco informado no cadastro da conta para validar internamente se está ou não preparado para gerar essa informação.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782872341015)

 Na lista abaixo temos os bancos e respectivos códigos que o sistema está preparado para geração automática de nosso número e linha digitável.

001 - Banco Do Brasil
748 - Bansicredi
237 - Bradesco
341 - Itaú
356 - Banco Real
104 - Caixa Econômica
409 - Unibanco
399 - HSBC
151 - Nossacaixa
353 - Banco Santander
422 - Banco Safra
745 - CITIBANK
033 - Banco Santander Banespa
756 - Bancoob
021 - Banestes
085 - CECRED
041 - BANRISUL
070 - Banco de Brasília
707 - Banco DAYCOVAL
097 - CREDISIS

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14714395085719)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782872342935)

 IMPORTANTE: **

Essa opção é usada quando o sistema não está preparado para geração da linha digital de forma automática, em que se realiza a configuração conforme o manual do banco quando necessário.