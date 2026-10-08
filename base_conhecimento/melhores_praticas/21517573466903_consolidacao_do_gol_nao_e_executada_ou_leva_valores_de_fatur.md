# Consolidação do GOL não é executada ou leva valores de faturamento divergente

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/21517573466903-Consolida%C3%A7%C3%A3o-do-GOL-n%C3%A3o-%C3%A9-executada-ou-leva-valores-de-faturamento-divergente](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517573466903-Consolida%C3%A7%C3%A3o-do-GOL-n%C3%A3o-%C3%A9-executada-ou-leva-valores-de-faturamento-divergente)  
> **ID:** `21517573466903` | **Última Atualização:** 2026-07-22T14:50:07Z

---

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450450584215)

 As informações da consolidação do GOL (Gerente Online) podem ser utilizadas tanto para os relatórios com o filtro ‘Consolidação de Movimentos’ quanto para os cards de Faturamento e Lucratividade.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450450584215)

 Seguindo a configuração estabelecida na consolidação (*GOL » Preferências » Consolidação de Movimentos*), o sistema executa um Job no horário definido para popular a tabela TGFMGC, que é responsável por armazenar as informações de compra/venda dos produtos analisados.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450450584215)

Quando existem valores incorretos ou zerados no faturamento, as configurações abaixo podem auxiliar na correção do problema: 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863058982679)

 Na Administração do Servidor (*Configurações » Avançado*) verifique se existe o ‘Argumento da VM’ com o nome ‘-Dsankhyaw.schedule.=true’, caso esteja como 'true' o job de consolidação não executara.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863075428887)

 É necessário existir uma referência de Custo Variável para cada empresa analisada.

Acesse a tela Gerente On-Line - GOL (*Comercial » Gerente*), abra as configurações e acesse a aba *Margem de contribuição*.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863059002647)

OBSERVAÇÃO:**

O ano de referência deve ser anterior as notas de venda realizada.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/21863075447575)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863059023511)

 O produto vendido deve obrigatoriamente possuir um CUSTO com data igual ou anterior à emissão da nota de venda realizada.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863059034903)

 As TOP's de compra/venda devem possuir as configurações dos campos de 'Apoio a Decisão'. 

Acesse a tela Tipos de Operação - Top (*Comercial » Arquivo » Cadastros*); identifique a TOP correspondente; acesse a aba *Geral* e localize a opção 'Apoio a Decisão'.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863059002647)

OBSERVAÇÃO:**

Caso seja uma **TOP de devolução**, o 'Identificador de Devolução' precisa estar preenchido com a opção 'Sim'.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/21863059050775)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863059058967)

  Caso o tipo de operação esteja definido como 'Bonificação' os valores dessa operação não serão considerados na analise. 

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863075514647)

 O **tipo** e o **tamanho** dos campos entre as tabelas TGFPRO, TGFMGC e TGFMGC_TMP devem ser idênticos ao banco de dados.

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24818370089239)

 Verifique se a configuração da Consolidação está correta e se possui algum filtro que impeça a venda de ser buscada;

Acesse a tela Gerente On-Line - GOL (*Comercial » Gerente*); abra as configurações; acesse a aba *Consolidação de Movimentos - Consolidação *e em seguida a aba* filtros.*

 

***

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21863059002647)

*****OBSERVAÇÃO****:**

Caso a aba não seja apresentada, é necessário ativar o parâmetro 'GOL-CONSMOV - Usar Consolidação de Dados', através da tela Preferências (*Configurações » Avançado*).

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/21517573461015)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21517573462167)

CAUSA:**

Quando alguma configuração não está adequada, isso pode impedir a execução do Job consolidador ou resultar em informações de faturamento incompletas, podendo impactar a tomada de decisão.