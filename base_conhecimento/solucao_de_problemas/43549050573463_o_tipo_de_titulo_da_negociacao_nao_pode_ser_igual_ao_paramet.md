# O Tipo de Título da negociação não pode ser igual ao parâmetro 'TIPTITCREDCLI'. Selecione outro tipo de negociação.

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43549050573463-O-Tipo-de-T%C3%ADtulo-da-negocia%C3%A7%C3%A3o-n%C3%A3o-pode-ser-igual-ao-par%C3%A2metro-TIPTITCREDCLI-Selecione-outro-tipo-de-negocia%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/43549050573463-O-Tipo-de-T%C3%ADtulo-da-negocia%C3%A7%C3%A3o-n%C3%A3o-pode-ser-igual-ao-par%C3%A2metro-TIPTITCREDCLI-Selecione-outro-tipo-de-negocia%C3%A7%C3%A3o)  
> **ID:** `43549050573463` | **Última Atualização:** 2026-09-24T19:43:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43741096804887)

 **MENSAGEM: **

Aviso
O Tipo de Título da negociação não pode ser igual ao parâmetro 'TIPTITCREDCLI'. Selecione outro tipo de negociação.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43741064869271)

 

### 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43549050568087)

 SITUAÇÃO

A mensagem é apresentada ao tentar iniciar uma venda no PDV WEB utilizando um **Tipo de Negociação** que possui, em suas parcelas, um **"Tipo de Título"** igual ao valor configurado no parâmetro **"TIPTITCREDCLI"**. O sistema impede esse procedimento para evitar conflitos de compensação de crédito.

 

### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43549050568471)

 SOLUÇÃO

Verifique o parâmetro global:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43549020309911)

 Acesse a tela **Preferências** (*Configurações » Avançado » Preferências*).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43549050569367)

 Localize o parâmetro **TIPTITCREDCLI** (Tipo de Título para Compensação de Crédito de Cliente) e anote o número configurado nele.

 

Ajuste o Tipo de Negociação:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43549020309911)

 Acesse a tela **Tipos de Negociação** (*Comercial » Arquivo » Cadastros » Tipos de Negociação*).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43549050569367)

 Selecione o tipo de negociação que você tentou utilizar na venda.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43549020311063)

 Na aba **Parcelas**, verifique o campo "Tipo de Título" de cada parcela.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43549050570263)

 Altere esse campo para um tipo de título **diferente** do valor anotado no parâmetro TIPTITCREDCLI.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/43549020311575)

 Salve as alterações e refaça o lançamento no PDV WEB.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43741096806039)

Importante:** Evite alterar o valor do parâmetro TIPTITCREDCLI na tela de Preferências para resolver esse erro, pois isso mudará a regra de compensação de crédito para todo o sistema. A correção recomendada é sempre ajustar as parcelas do Tipo de Negociação.

 

### 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43549050570647)

 CAUSA

A mensagem ocorre porque o sistema Sankhya não permite que o **"Tipo de Título"** configurado em uma negociação seja igual ao valor do parâmetro **TIPTITCREDCLI**, que é reservado para títulos de compensação de crédito de cliente. Essa restrição existe para evitar lançamentos financeiros indevidos e garantir a correta utilização dos títulos de crédito no processo de compensação.