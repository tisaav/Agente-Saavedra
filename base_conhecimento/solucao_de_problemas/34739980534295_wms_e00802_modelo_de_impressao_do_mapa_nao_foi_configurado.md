# WMS_E00802: Modelo de impressão do mapa não foi configurado

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34739980534295-WMS-E00802-Modelo-de-impress%C3%A3o-do-mapa-n%C3%A3o-foi-configurado](https://ajuda.sankhya.com.br/hc/pt-br/articles/34739980534295-WMS-E00802-Modelo-de-impress%C3%A3o-do-mapa-n%C3%A3o-foi-configurado)  
> **ID:** `34739980534295` | **Última Atualização:** 2026-07-22T14:26:46Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34739980516375)

 **MENSAGEM**

[WMS_E00802] O modelo de impressão do mapa não foi configurado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35443713471383)

 **SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta **gerar um mapa de separação** no sistema WMS, mas o relatório de separação manual não foi devidamente configurado no parâmetro correspondente.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34739964156695)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35443713476375)

 Acesse o **Sankhya Place** e selecione a aba **"Pacotes"**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35443714665751)

 Pesquise por **"Mapa de Separação Manual"** e instale o pacote.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35443714668311)

 Acesse a tela **"Relatórios Formatados"** (Configurações » Avançado » Relatórios Formatados).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35443713481367)

 Pesquise o relatório **"Mapa de Separação Manual"** baixado do Place e anote o número do relatório.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35443713484311)

 Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35443714674455)

 Busque pelo parâmetro **"RELMAPSEPMANPED"** e informe o número do relatório anotado no passo 4.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34739964160535)

 **CAUSA**

A mensagem é exibida porque o **parâmetro "RELMAPSEPMANPED"** não possui um relatório de separação manual configurado, impedindo a geração do mapa de separação no sistema WMS.