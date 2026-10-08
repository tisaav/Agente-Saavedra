# Obtenção de Imagens de Produtos via API

> **Módulo:** Melhores Praticas | **Subseção:** Configurações Sankhya  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36396748479383-Obten%C3%A7%C3%A3o-de-Imagens-de-Produtos-via-API](https://ajuda.sankhya.com.br/hc/pt-br/articles/36396748479383-Obten%C3%A7%C3%A3o-de-Imagens-de-Produtos-via-API)  
> **ID:** `36396748479383` | **Última Atualização:** 2026-07-22T14:23:06Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36396748470423)

 SITUAÇÃO:**

Alguns clientes desejam integrar sistemas externos ao Sankhya e precisam exibir as imagens dos produtos em suas aplicações. 

Embora o produto possua imagem vinculada no cadastro, muitos usuários não sabem qual rota utilizar, como interpretar a resposta retornada pela API ou como salvar o arquivo recebido. 

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36441969272855)

OBSERVAÇÃO:**

Até o momento, a integração de imagens está disponível apenas pela** API legada**, não havendo suporte para esse recurso na API pública.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36396748471191)

SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36441962838935)

 **Monte a URL da imagem.

Utilize o padrão da API legada para obter a imagem do produto:

 

```text
https://api.sankhya.com.br/gateway/v1/mge/Produto@IMAGEM@CODPROD=<CODPROD>.dbimage
```

 

Exemplo:

```text
https://api.sankhya.com.br/gateway/v1/mge/Produto@IMAGEM@CODPROD=2.dbimage
```

 

Substitua **<CODPROD>** pelo código do produto desejado.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36442467841943)

 **Envie uma requisição GET no Postman.

Configurações de requisição:

- 

**Método:** GET

- 

**URL:** conforme o padrão ou exemplo acima

- 

**Headers recomendados:**

 

```text
Authorization: Bearer XXXXXX (Substitua XXXXX pelo token válido gerado previamente)
Content-Type: image/jpeg
```

 

- 

**Body:** selecione a opção **None**

Nenhum parâmetro adicional é necessário.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36442467843735)

 **Interprete o retorno.

Ao executar a rota, a API retornará a imagem em **formato binário**.

Se o Postman estiver exibindo no modo JSON, o contéudo pode aparecer assim:

 

```text
ÿØÿà JFIF ...
```

 

Isso é esperado e indica que a imagem foi retornada de forma correta.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36442461414039)

 Salve e visualiza a imagem

Clique em **''Save Response to file'' **e salve o arquivo com uma extensão de imagem, como:

 

```text
produto.jpg
```

 

Depois de salvar, basta abrir o arquivo - a imagem será exibida normalmente. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36396740140055)

CAUSA:**

A integração de imagens no Sankhya funciona por meio do endpoint **.dbimage**, que sempre retorna o arquivo em formato binário.

Dessa forma, o sistema externo apenas recebe esse conteúdo e pode salvá-lo ou exibi-lo diretamente, sem necessidade de realizar conversões adicionais.

Esse método garante que qualquer aplicação consiga consumir as imagens de forma rápida e padronizada.