# Referência REPETIDO para o produto 'X'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109354-Refer%C3%AAncia-REPETIDO-para-o-produto-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109354-Refer%C3%AAncia-REPETIDO-para-o-produto-X)  
> **ID:** `360044109354` | **Última Atualização:** 2026-07-22T15:55:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609489333655)

 MENSAGEM:**

[ORA-20101]: Referência REPETIDO para o produto 'X'

[ORA-06512]: em "SANKHYA.TRG_INC_UPT_TGFPRO_REFERENCIA", line 49

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPT_TGFPRO_REFERENCIA'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609489334807)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609482108439)

 Caso necessite cadastrar mais de um produto utilizando a mesma referência, o parâmetro abaixo deve estar **desligado**:

- Tela **"Preferências**" *(Caminho de acesso: Configurações » Avançado)*

- Chave **"VALCODBARREPET - Validar Códigos de Barras repetido?**"

- Campo **"Ligado/Desligado"**: desligado

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15021744231703)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609482111255)

 **Caso a repetição seja indevida, mantenha o parâmetro ligado e realize um filtro por referência, identificando os produtos que já a possuem e realizando os devidos ajustes.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609482113047)

 CAUSA:**

Ao efetuar o cadastro de um produto, informando no campo 'Referencia' uma informação já existente para outro produto, a mensagem será apresentada.