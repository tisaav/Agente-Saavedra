# Arquivo: '.xml' inválido, tag infProt é necessário

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575754-Arquivo-xml-inv%C3%A1lido-tag-infProt-%C3%A9-necess%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575754-Arquivo-xml-inv%C3%A1lido-tag-infProt-%C3%A9-necess%C3%A1rio)  
> **ID:** `360043575754` | **Última Atualização:** 2026-07-22T16:02:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16173018521111)

 MENSAGEM:**

[CORE_E03192]  Arquivo: '.xml' inválido, tag infProt é necessário.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16173002023831)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16173002027159)

 Situação pode ocorrer quando o arquivo XML está sendo gerado em conferência.

Em nosso sistema, essa geração ocorre no caminho:

- *Portal de Vendas » NF-e » Gerar XML NF-e em arquivo para conferência*

 

![portal_de_vendas11.png](https://ajuda.sankhya.com.br/hc/article_attachments/14690149718679)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16173018533143)

 O XML gerado conforme item 1 não gera as informações da tag <infProt>, visto que não recebeu os protocolos de aprovação da SEFAZ.

Dessa forma, utilize uma das opções abaixo para geração desse arquivo:

- *Portal de Vendas » NF-e » Gerar Arquivo XML de NF-e*

 

![portal_de_vendas12.png](https://ajuda.sankhya.com.br/hc/article_attachments/14690174972567)

 

- Tela **"Gerar Arquivo XML de NFe/NFSe/SAT"** (Caminho de acesso: *Comercial » Rotinas » Gerar Arquivo XML de NF-e/NFS-e/SAT*)

 

![gerar_xml.png](https://ajuda.sankhya.com.br/hc/article_attachments/14690158241175)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16173002033047)

 Caso o XML não tenha sido gerado em nosso sistema, solicite ao seu parceiro que refaça a geração, enviando um XML válido, constando informações referente tag mencionada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16173018539031)

 CAUSA:**

Ao realizar importação de XML, quando esse não contém a tag <infProt>, a mensagem é apresentada.