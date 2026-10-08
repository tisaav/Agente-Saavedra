# Documento XXXX: Não foi possível encontrar o modelo na tela de preferência da empresa na aba Estoque/Preço.

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37341372981015-Documento-XXXX-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-modelo-na-tela-de-prefer%C3%AAncia-da-empresa-na-aba-Estoque-Pre%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37341372981015-Documento-XXXX-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-modelo-na-tela-de-prefer%C3%AAncia-da-empresa-na-aba-Estoque-Pre%C3%A7o)  
> **ID:** `37341372981015` | **Última Atualização:** 2026-07-22T14:13:18Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37341381714071)

 **MENSAGEM:**

Documento XXXX: Não foi possível encontrar o modelo na tela de preferência da empresa na aba Estoque/Preço.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37341372976151)

 SITUAÇÃO: **

Ao tentar imprimir um **Pedido de Venda** no processo de **Expedição**, o sistema apresenta a mensagem acima e a impressão não é realizada.
 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37394256561047)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393764685591)

 Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa). 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393764687127)

 Selecione a empresa utilizada no Pedido de Venda.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393749447575)

 Na aba **''Estoque/Preço''**, sub-aba **''Expedição''** no campo **''Modelo''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393749448343)

 Selecione o modelo adequado conforme o padrão utilizado pela empresa.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393764698519)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393749451799)

 Retorne ao **Pedido de Venda** e realize novamente a impressão da expedição.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37394094148119)

 Após essa configuração, a impressão do pedido de expedição será realizada com sucesso.
 

##### 
**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37394078907799)

 OBSERVAÇÃO: **A configuração do modelo de expedição é **por empresa**. Caso existam múltiplas empresas no ambiente, o ajuste deve ser realizado e validado individualmente.  Certifique-se de que o modelo selecionado esteja corretamente cadastrado e ativo no sistema.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37341381715479)

CAUSA:**

O erro ocorre porque **não há um modelo de impressão de expedição configurado** nas preferências da empresa vinculada ao pedido.

Para que o sistema consiga gerar o documento de expedição, é obrigatório que exista um modelo de impressão definido. Quando esse campo não está preenchido, o sistema não encontra o layout necessário e impede a impressão.