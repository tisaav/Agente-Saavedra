# The value 'XXXXXXXX' of element 'xEnder' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365333-The-value-XXXXXXXX-of-element-xEnder-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365333-The-value-XXXXXXXX-of-element-xEnder-is-not-valid)  
> **ID:** `360043365333` | **Última Atualização:** 2026-07-22T16:05:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453261162519)

 MENSAGEM:**

cvc-maxLength-valid: Value 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' with length = 'X' is not facet-valid with respect to **maxLength '60'** for type #AnonType_xEndertransportatranspinfNFeTNFe'. 
cvc-type3.1.3: The value 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' of element 'xEnder' is not valid.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453293208727)

 SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela "****[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)" no **SankhyaW**, a nota ficará com Status: 'Aguardando Correção'. Acessando a opção (**...**)>>**Ver Acompanhamento,** é possível consultar o detalhe da rejeição a seguir.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453293212567)

 SOLUÇÃO:**

Para correção seguir os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453261169431)

 Identificar através da mensagem retornada, qual é o endereço causador da rejeição.

***Exemplo:***
The value '**Avenida MARIO GURGEL, 5030 SALA 101 SETOR CENTRO ADM AB'** of element 'xEnder' is not valid.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453293223447)

 A mensagem está validando a **quantidade de caracteres** utilizados na descrição do respectivo endereço. É possível identificar a quantidade de caracteres que foram utilizados e a quantidade esperada através da mensagem de validação. Veja o exemplo abaixo:

cvc-maxLength-valid: Value 'Avenida MARIO GURGEL, 5030 N. 5030 SALA 101 SETOR CENTRO ADM AB' **with length = '63'** is not facet-valid with respect to **maxLength '60'** for type 

- Tamanho Atual: 63 caracteres

- Tamanho Esperado: 60 caracteres

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453293228183)

 Para solucionar a rejeição, acesse o cadastro de** "[Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)** *(Caminho de acesso: Configurações » Cadastros)*, selecione o parceiro referente ao endereço rejeitado e na aba "**Endereço"** veja para qual dos campos é possível abreviar informações. Para o caso exemplificado seria possível abreviar o "**Complemento**":

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14395569114135)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453293235095)

 Realizado o ajuste, redigite os dados do cabeçalho e gere um novo lote da nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453261181719)

 CAUSA:**

Mensagem apresentada quando a quantidade de caracteres enviadas para a tag de endereço é maior que a quantidade aceita pela SEFAZ.


---

### 🔗 Links e Referências Internas:

- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)
- [Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)