# Na emissão de uma NFS-e e impressão via Site da Prefeitura, a cidade impressa é a cidade do prestador e não do tomador

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043355653-Na-emiss%C3%A3o-de-uma-NFS-e-e-impress%C3%A3o-via-Site-da-Prefeitura-a-cidade-impressa-%C3%A9-a-cidade-do-prestador-e-n%C3%A3o-do-tomador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043355653-Na-emiss%C3%A3o-de-uma-NFS-e-e-impress%C3%A3o-via-Site-da-Prefeitura-a-cidade-impressa-%C3%A9-a-cidade-do-prestador-e-n%C3%A3o-do-tomador)  
> **ID:** `360043355653` | **Última Atualização:** 2026-09-02T20:22:37Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113568397079)

 SITUAÇÃO:**

A nota é emitida pelo sistema Sankhya, porém a impressão é realizada diretamente pelo site da prefeitura. Dessa forma, a impressão do campo **"Legenda do local da prestação do serviço"** está sendo preenchida com a cidade do Prestador. 

O caso é: 
Cidade do Prestador: **Nova Santa Rita **
Cidade do Tomador: Encantado 
Cidade de Prestação: Encantado [Deveria ser]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113554028055)

 SOLUÇÃO:**

Quando o provedor é IPMSISTEMAS e o local da prestação do serviço não é na mesma cidade do prestador, informe o código da cidade no campo **"Cidade de Prestação do Serviço"** no cabeçalho da nota, ao invés de informar no campo **"Cidade"**. 

Quando isso não ocorre a tag <**codigo_local_prestacao_servico**> é alimentada automaticamente pelo código de SIAFI da cidade da empresa prestadora do serviço.

Então temos o correto registro da informação conforme abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113568409879)

 Acesse: Comercial » Rotinas » Central de Vendas

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113568418967)

Cabeçalho da Nota:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113568418967)

Informe no campo a cidade de prestação do serviço.

![central_de_vendas.png](https://ajuda.sankhya.com.br/hc/article_attachments/14652921824919)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113554038807)

 Gere novamente o Lote para prefeitura e após isso, efetue a impressão.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113554043287)

 CAUSA:**

Ocorre quando não é informado Cidade de Prestação do Serviço no cabeçalho da nota, quando a prestação é diferente da cidade do Prestador, para provedores IPMSISTEMAS (Provedores de Sistemas de Gestão Publica, utilizada pelas Prefeituras, pode ser diferente em cada município).