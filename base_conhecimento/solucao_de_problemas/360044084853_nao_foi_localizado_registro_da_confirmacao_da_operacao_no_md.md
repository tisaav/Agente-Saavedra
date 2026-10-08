# Não foi localizado registro da confirmação da operação no MD-e para esta chave da NF-e

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044084853-N%C3%A3o-foi-localizado-registro-da-confirma%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-no-MD-e-para-esta-chave-da-NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044084853-N%C3%A3o-foi-localizado-registro-da-confirma%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-no-MD-e-para-esta-chave-da-NF-e)  
> **ID:** `360044084853` | **Última Atualização:** 2026-07-22T16:02:22Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191317022743)

 MENSAGEM:**

[CORE_E02963] Não foi localizado registro da confirmação da operação no MD-e para esta chave da NF-e.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191332203671)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191317026583)

 Caso **não trabalhe** com validação dos eventos de MD-e (Manifesto do Destinatário), verifique a configuração abaixo no cadastro do 'Tipo de Operação' utilizado para o respectivo lançamento:

- Tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros), Aba **CT-e/MD-e**,  Campo** "Exigir confirmação do MD-e antes da confirmação": **desmarcado

 

![cte.png](https://ajuda.sankhya.com.br/hc/article_attachments/14686213116439)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191317036055)

 Realizado o ajuste acima, refaça o lançamento (essa é uma marcação histórica, assim exclua o lançamento atual e realize outro).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191332206103)

 Caso trabalhe com esta validação do MD-e, mantenha a configuração acima e verifique se o evento de Ciência da Operação (Botão **"MD-e"** » **"Ciência da Operação"**) foi devidamente realizado para essa chave NF-e. Em caso de erros para executar essa confirmação da operação, busque possíveis soluções em nossa Central de Ajuda, persistindo acione o Service Desk Sankhya.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191332207511)

 CAUSA:**

Mensagem apresentada quando configurado o 'Tipo de Operação' para exigir confirmação do MD-e antes da confirmação e essa não for executada.