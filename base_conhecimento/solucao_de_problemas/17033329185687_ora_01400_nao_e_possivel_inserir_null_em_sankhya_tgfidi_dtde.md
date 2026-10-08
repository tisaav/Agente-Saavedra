# ORA-01400: não é possível inserir NULL em (SANKHYA , TGFIDI, DTDESEMBARACO

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/17033329185687-ORA-01400-n%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-NULL-em-SANKHYA-TGFIDI-DTDESEMBARACO](https://ajuda.sankhya.com.br/hc/pt-br/articles/17033329185687-ORA-01400-n%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-NULL-em-SANKHYA-TGFIDI-DTDESEMBARACO)  
> **ID:** `17033329185687` | **Última Atualização:** 2026-07-22T14:53:55Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17033271381271)

 **MENSAGEM:**

ORA-01400: não é possível inserir NULL em (SANKHYA , TGFIDI, DTDESEMBARACO.

 
**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17033313349143)

CAUSA:**

Ocorre na ausência da tag  <dDesemb> no xml utilizado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17033284905367)

SOLUÇÃO:**

O XML precisa ter a tag <dDesemb> conforme evidência abaixo:
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17033941131159)

 
Se o XML importado estiver sem essa TAG o sistema tenta inserir NULL, porém esse campo não é aceito com valor nulo na base.
 
Segue abaixo XML de exemplo com valor nulo.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17033963720727)

Temos o artigo abaixo que descreve esse processo: 
[Importar dados da DI-Declaração da Importação via XML - Nota de Nacionalização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043796574-Importar-dados-da-DI-Declara%C3%A7%C3%A3o-da-Importa%C3%A7%C3%A3o-via-XML-Nota-de-Nacionaliza%C3%A7%C3%A3o)
 
Outra alternativa seria diretamente na central de compras, necessário selecionar o produto em outras opções e em seguida clicar em "Declaração de Importação e Adições ".
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17034014532503)

 
Clique para inserir os dados da DI manual, campo da data do desembaraço.
 

![Imagem](/attachments/token/OWv4dbtpr8asrAZXIucF9XtYR/?name=image.png)

  
Segue o passo a passo que valida a orientação: [Central de Compras | Grade Itens > Botão Outras Opções](Central%20de%20Compras%20|%20Grade%20Itens%20>%20Bot%C3%A3o%20Outras%20Op%C3%A7%C3%B5es)


---

### 🔗 Links e Referências Internas:

- [Importar dados da DI-Declaração da Importação via XML - Nota de Nacionalização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043796574-Importar-dados-da-DI-Declara%C3%A7%C3%A3o-da-Importa%C3%A7%C3%A3o-via-XML-Nota-de-Nacionaliza%C3%A7%C3%A3o)