# Base não pode ser registrada como produção, pois ela não possui informações sobre o nó

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002031022-Base-n%C3%A3o-pode-ser-registrada-como-produ%C3%A7%C3%A3o-pois-ela-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-o-n%C3%B3](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002031022-Base-n%C3%A3o-pode-ser-registrada-como-produ%C3%A7%C3%A3o-pois-ela-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-o-n%C3%B3)  
> **ID:** `1500002031022` | **Última Atualização:** 2026-07-22T15:25:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287564863767)

 MENSAGEM**:

Base não pode ser registrada como produção, pois ela não possui informações sobre o nó.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287564868887)

 SOLUÇÃO**:

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287539075351)

 Faça o login com usuário SUP;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287564874007)

 Acesse a tela: *Administração do Servidor » Aba 'Registro de base de dados*;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287564877079)

 Identifique a base registrada como PRODUÇÃO. Caso necessite de ser substituída, proceda com o ajuste, caso não, deverá registrar a nova base como Teste, Treinamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287564881047)

 CAUSA**:

Ocorre quando o cliente já possui uma base de PRODUÇÃO registrada e o mesmo está tentando registrar uma outra base de Produção. A aplicação só permite o registro de apenas 1 (uma) base de Produção, os restantes podem ser registrados como Teste, Treinamento, quantas bases desejar.