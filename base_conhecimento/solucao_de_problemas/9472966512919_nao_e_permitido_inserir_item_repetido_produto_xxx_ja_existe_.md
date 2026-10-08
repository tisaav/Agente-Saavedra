# Não é permitido inserir item repetido. Produto XXX já existe na sequência X

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9472966512919-N%C3%A3o-%C3%A9-permitido-inserir-item-repetido-Produto-XXX-j%C3%A1-existe-na-sequ%C3%AAncia-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/9472966512919-N%C3%A3o-%C3%A9-permitido-inserir-item-repetido-Produto-XXX-j%C3%A1-existe-na-sequ%C3%AAncia-X)  
> **ID:** `9472966512919` | **Última Atualização:** 2026-07-22T15:07:45Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296909183511)

 MENSAGEM:**

[CORE_E04344] Não é permitido inserir item repetido. Produto XXX já existe na sequência X.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296909191703)

 SITUAÇÃO:**

Ao lançar produto repetido na NF-e a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296909195287)

 CAUSA:**

Ao tentar inserir um produto repetido na nota, mas a configuração da TOP e dos parâmetros não estão configurados para aceitar.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296909199383)

 SOLUÇÃO:**

Acesse a tela **Preferências*** (Caminho de acesso à tela: Configurações » Avançado » Preferências) *e verifique se os parâmetros abaixo estão ligados:

- 
**ACEITARPRODREPE**-Aceitar prod.repetido para Exec.diferente?   

- 
**ACEITARPRODREP**-Aceitar produto repetido?

![Aceitar 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296909200279)

![Aceitar produto repetido 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296909211287)

Verifique também no cadastro do **Tipo de Operação TOP** *(Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP)* a Opção: **Aceitar Produto Repetido. **

**Importante: Na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), o campo "Aceitar Produto Repetido" deve estar configurado igual a "Sim".**

![top 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296969815447)


---

### 🔗 Links e Referências Internas:

- [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)