# The data "X" is not legal for a JDOM character content

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32097196343447-The-data-X-is-not-legal-for-a-JDOM-character-content](https://ajuda.sankhya.com.br/hc/pt-br/articles/32097196343447-The-data-X-is-not-legal-for-a-JDOM-character-content)  
> **ID:** `32097196343447` | **Última Atualização:** 2026-07-24T12:42:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32405083171863)

 MENSAGEM:**

[COM_E00717] The data "X" is not legal for a JDOM character content: 0x1f is not a legal XML character

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32405117321495)

 SITUAÇÃO**

Ao realizar qualquer consulta na tela **"****Consulta de produtos"**, apresenta a mensagem de erro acima. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32097213451927)

SOLUÇÃO:**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32097213453463)

 **Acesse o cadastro do **Produto** citado na mensagem de erro e remova qualquer cactere especial que estiver na descrição. 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32097213453847)

 Feche a consulta de produtos, acesse a **"Administração do Servidor"** e limpe o cache do sistema. Após isso, realize um novo teste.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32405083182103)

 **CAUSA:****

O erro acontece porque o produto citado na mensagem possui algum caractere especial na sua descrição, no entanto, esse tipo de caractere não é válido para o sistema.