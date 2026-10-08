# Código do município inválido. Utilizar código da "Tabela de Municípios do IBGE"

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110514-C%C3%B3digo-do-munic%C3%ADpio-inv%C3%A1lido-Utilizar-c%C3%B3digo-da-Tabela-de-Munic%C3%ADpios-do-IBGE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110514-C%C3%B3digo-do-munic%C3%ADpio-inv%C3%A1lido-Utilizar-c%C3%B3digo-da-Tabela-de-Munic%C3%ADpios-do-IBGE)  
> **ID:** `360044110514` | **Última Atualização:** 2026-07-22T15:53:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591160010903)

 MENSAGEM:**

Código do município inválido. Utilizar código da "Tabela de Municípios do IBGE".
 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591199514391)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591199518615)

 Identifique no erro apresentado qual "participante/parceiro" está sendo validado. 

**Exemplo:**

|0150|000000006|**SANKHYA GESTÃO DE NEGÓCIOS** |01058|51254159000173||336122330119|3518800||Av Teste|1688||CUMBICA|

No registro 150, a posição 3 refere-se ao 'Nome Participante', ou seja, 'Sankhya Gestão de Negócios'.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591160016535)

 Realizada a identificação acima, acesse o cadastro do parceiro e verifique na aba **"Endereço"** a 'Cidade' do mesmo. 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591199523863)

 Acesse a tela **"Cidades"** *(Caminho de acesso: Configurações » Cadastros » Endereços)* e para o cadastros de cidade localizado no item 1, verifique a informação contida no campo **"Mun. domicílio fiscal":**

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591160022551)

 **Informe no campo citado anteriormente o "**Mun. domicílio fiscal**" conforme tabela do IBGE, disponível no link [http://www.ibge.gov.br/home/geociencias/areaterritorial/area.shtm.](http://www.ibge.gov.br/home/geociencias/areaterritorial/area.shtm)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591199529367)

 Realizado o ajuste, faça a geração de um novo arquivo do SPED e valide novamente no PVA. 
 

 
**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16591199532823)

 CAUSA:**
 
Mensagem apresentada ao validar o SPED Fiscal através do PVA, quando não informado ou informado um Cód.Município que difere do definido na 'Tabela de Municípios'.