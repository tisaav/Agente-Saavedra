# A conta selecionada possui configuração inválida

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31489470157591-A-conta-selecionada-possui-configura%C3%A7%C3%A3o-inv%C3%A1lida](https://ajuda.sankhya.com.br/hc/pt-br/articles/31489470157591-A-conta-selecionada-possui-configura%C3%A7%C3%A3o-inv%C3%A1lida)  
> **ID:** `31489470157591` | **Última Atualização:** 2026-07-22T14:32:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31959593483799)

 MENSAGEM:**

[CTB_E00173] A conta selecionada possui configuração inválida

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31959579470231)

 SITUAÇÃO:**

Ao realizar o processo de [Zeramento de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116453-Zeramento-de-Contas) é possível se deparar com esse erro.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31959579473687)

Primeiramente, confira  a regra de negócio que nos leva a este cenário:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31959579479959)

 O sistema realiza a validação das contas informadas na tela de "**Zeramento de contas"**, nos campos:

- Conta prejuízo

- Conta lucro

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/31489860619287)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31959593501719)

 Em seguida, o sistema faz outra validação. Que consiste em verificar, na tela **"Plano de contas",** os seguintes campos destas contas contábeis identificadas no passo 1:

- Centro de Resultado obrigatório

- Projeto obrigatório

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/31489860622999)

**Se estes campos estiverem com as marcações acionadas,** o sistema apresentará a mensagem de alerta citada acima, porque as contas de Resultado do Exercício não podem obrigar estas informações.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31489907650711)

SOLUÇÃO:**

**Assim, se faz necessário desativar tais marcações na tela de Plano de Contas.**


---

### 🔗 Links e Referências Internas:

- [Zeramento de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116453-Zeramento-de-Contas)