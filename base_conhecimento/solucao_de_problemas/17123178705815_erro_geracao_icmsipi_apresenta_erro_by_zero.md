# Erro Geração ICMS/IPI  apresenta erro:  By zero

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/17123178705815-Erro-Gera%C3%A7%C3%A3o-ICMS-IPI-apresenta-erro-By-zero](https://ajuda.sankhya.com.br/hc/pt-br/articles/17123178705815-Erro-Gera%C3%A7%C3%A3o-ICMS-IPI-apresenta-erro-By-zero)  
> **ID:** `17123178705815` | **Última Atualização:** 2026-07-22T14:53:50Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17123238643607)

 **MENSAGEM:**

Ao executar a rotina ***Geração ICMS/IPI*** apresenta seguinte erro:  / by zero.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17123208294551)

CAUSA:**

Ocorre quando o valor da BASE DE ICMS tem algum valor e o ICMS em questão não foi incluído.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17123223547799)

SOLUÇÃO:**

Não deve existir o cenário onde, nas notas lançadas no sistema, que serão levadas aos livros fiscais de ICMS/IPI, tenham BASE DE ICMS maior que zero e, não tenham VLR ICMS, pois durante os processamentos, há o calculo de divisão do valor do ICMS pela BASE ICMS, e isso causa a mensagem apresentada e citada nesse artigo, então se não há valores de ICMS na nota, a base deve estar zerada também.