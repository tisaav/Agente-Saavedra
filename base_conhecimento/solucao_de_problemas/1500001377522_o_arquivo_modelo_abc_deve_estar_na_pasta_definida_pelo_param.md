# O arquivo modelo 'ABC' deve estar na pasta definida pelo parâmetro SERVDIRMOD, que neste caso é '/home/mgeweb/xxxyyy/'"

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001377522-O-arquivo-modelo-ABC-deve-estar-na-pasta-definida-pelo-par%C3%A2metro-SERVDIRMOD-que-neste-caso-%C3%A9-home-mgeweb-xxxyyy](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001377522-O-arquivo-modelo-ABC-deve-estar-na-pasta-definida-pelo-par%C3%A2metro-SERVDIRMOD-que-neste-caso-%C3%A9-home-mgeweb-xxxyyy)  
> **ID:** `1500001377522` | **Última Atualização:** 2026-07-22T15:25:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16285586337047)

 MENSAGEM**:

Ao tentar confirmar ou aprovar a nota apresenta mensagem "O arquivo modelo 'ABC' deve estar na pasta definida pelo parâmetro SERVDIRMOD, que neste caso é '/home/mgeweb/xxxyyy/".

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16285586343703)

 SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16285538760599)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16285586350487)

 Verifique o campo **"Modelo para Dados Adicionais de NF-e"** se o modelo informado está correto.

- Se precisar dos dados adicionais da nota:

A configuração deste modelo é na tela **"Modelos de Nota Fiscal/Duplicatas/Boleto(s)"**  e o sistema buscará no diretório configurado no parâmetro **"SERVDIRMOD"** o arquivo configurado no modelo.

- Se não precisar dos dados adicionais da nota:

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16285586353175)

 No campo Modelo para Dados Adicionais de NF-e retire a configuração e deixe o campo 'em branco'.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16285538774935)

 Após realizar a correção das configurações tente novamente aprovar a nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16285586363415)

 CAUSA:**

Mensagem de alerta ocorre quando configurado na TOP Modelos de Nota Fiscal/Duplicatas/Boleto(s) e este modelo TXT não existe no diretório do servidor onde esta instalado o sistema.