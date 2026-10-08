# CFOP de Importação e não informado dados da DI

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042640674-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-da-DI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042640674-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-da-DI)  
> **ID:** `360042640674` | **Última Atualização:** 2026-07-22T16:07:39Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505113249815)

 MENSAGEM:**

[525 - Rejeição]: CFOP de Importação e não informado dados da DI.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505142746007)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505113254295)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*

- Aba: **"Geral"**

- Campo **"Digitar informações sobre Importação":** marque

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505113255191)

 Acesse: Portal Compras » Central de Notas.

Para cada item da nota, preencha os dados da **"DI-Declaração de Importação".**

Selecione o item e depois o  botão: **"Outras Opções"**(...)>>**"Declaração de Importação e Adições":**

 

![declara__o_de_importa__o.png](https://ajuda.sankhya.com.br/hc/article_attachments/12118200066583)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505142755479)

 Após os ajustes, gere o lote da nota novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505113259927)

 CAUSA:**

Quando for emitida uma NF-e com CFOP iniciado por 3, indicando uma Operação com o Exterior, de Entrada, e não for informado o Grupo de Declaração de Importação (DI), será retornada a rejeição "525 - CFOP de Importação e não informado dados da DI".

*Exceções a regra:*

A regra 525 não se aplica para os seguintes CFOP: 3.201, 3.202, 3.211, 3.503 e 3.553.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505113262871)

 OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte:](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)