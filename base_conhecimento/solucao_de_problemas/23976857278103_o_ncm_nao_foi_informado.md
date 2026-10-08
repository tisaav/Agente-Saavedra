# O NCM não foi informado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/23976857278103-O-NCM-n%C3%A3o-foi-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/23976857278103-O-NCM-n%C3%A3o-foi-informado)  
> **ID:** `23976857278103` | **Última Atualização:** 2026-07-22T14:47:57Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23976834696983)

 **MENSAGEM:**

[CORE_E06789] O NCM não foi informado

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23976834700695)

 **SOLUÇÃO:**

Para resolver a questão, acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)" **(Caminho: Configurações » Avançado » Preferências), busque pelo parâmetro **"VALUSOPRODNCM" **e verifique se no campo **"Texto" ** está descrita a letra 'S'. Caso não esteja, coloque a letra 'S'.

 

![O NCM não foi informado 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/23976834703639)

 

**Observação:** a inserção da letra 'S no campo Texto faz com que o sistema não realize a validação do campo NCM e passe a considerar a informação preenchida no campo **"Usado como"** do cadastro de Produtos/Serviços. Neste caso por se tratar de serviço, o campo Usado como é automaticamente preenchido com a letra 'S'. Dessa forma, estando preenchido o campo Texto com a letra 'S', o campo Usado como já estará cadastrado automaticamente com a letra 'S', a mensagem de erro deixará de ser apresentada. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23976857270039)

 **CAUSA:**

Ao cadastrar um Serviço, tendo o parâmetro VALUSOPRODNCM  configurado de maneira indevida, a mensagem é apresentada.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)