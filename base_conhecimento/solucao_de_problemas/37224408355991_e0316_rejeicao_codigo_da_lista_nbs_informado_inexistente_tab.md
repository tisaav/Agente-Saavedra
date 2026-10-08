# E0316 Rejeição: Código da lista NBS informado inexistente tabela de NBS do sistema.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224408355991-E0316-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-lista-NBS-informado-inexistente-tabela-de-NBS-do-sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224408355991-E0316-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-lista-NBS-informado-inexistente-tabela-de-NBS-do-sistema)  
> **ID:** `37224408355991` | **Última Atualização:** 2026-07-22T14:16:39Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224424305047)

 **MENSAGEM**

E0316 Rejeição: Código da lista NBS informado inexistente tabela de NBS do sistema.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224408339863)

 **SITUAÇÃO**

Ao gerar o lote de uma NFS-e, o sistema apresenta a mensagem de rejeição informando que o **código NBS** (Nomenclatura Brasileira de Serviços) cadastrado **não existe na tabela oficial** de NBS do sistema.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224424305943)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224408342039)

 Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224424307095)

 Localize o serviço que está sendo utilizado na NFS-e rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37708140528919)

 Na aba **"Impostos"**, verifique o campo **"Código NBS"**. Confirme se o código informado está correto e se **existe na tabela oficial TLFNBS**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37708156897175)

 Caso o código esteja incorreto ou inexistente:

- 

Consulte a **tabela oficial de NBS** para identificar o código correto correspondente ao serviço prestado.

- 

Atualize o campo **"Código NBS"** com o código válido.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37708156899607)

 Verifique se a cidade está configurada para **enviar o Código NBS** no JSON.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37708156901655)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224408350615)

 Confirme se o campo **"Enviar o Código NBS no JSON"** está ativado.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224408351383)

 Caso a cidade possua uma **máscara NBS** configurada, certifique-se de que o código NBS cadastrado está no formato correto exigido pela máscara.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37708140540311)

 Salve as alterações realizadas no cadastro do serviço.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38166527240727)

 Acesse a tela ****[''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e gere um novo lote de envio para a NFS-e.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224408351767)

 **CAUSA**

A rejeição ocorre porque o **código NBS informado** no cadastro do serviço **não existe na tabela oficial TLFNBS** do sistema. Isso pode acontecer quando:

- 

O código foi digitado incorretamente.

- 

O código está desatualizado ou foi descontinuado.

- 

O código não corresponde à hierarquia válida da tabela NBS (por exemplo: 1, 1.1, 1.1.11).

- 

A cidade exige o envio do código NBS e o campo não foi preenchido ou está com valor inválido.


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)
- [''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)