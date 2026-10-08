# Motivo: javax.ejb.CreateException: SQL-50001 O Centro de Resultado XXXX  não está cadastrado, não está ativo, ou não é analítico

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34382742634775-Motivo-javax-ejb-CreateException-SQL-50001-O-Centro-de-Resultado-XXXX-n%C3%A3o-est%C3%A1-cadastrado-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico](https://ajuda.sankhya.com.br/hc/pt-br/articles/34382742634775-Motivo-javax-ejb-CreateException-SQL-50001-O-Centro-de-Resultado-XXXX-n%C3%A3o-est%C3%A1-cadastrado-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico)  
> **ID:** `34382742634775` | **Última Atualização:** 2026-07-29T13:20:39Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34461123590935)

 **MENSAGEM**

Motivo: javax.ejb.CreateException: SQL-50001 O Centro de Resultado XXXX  não está cadastrado, não está ativo, ou não é analítico

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34461087236119)

 **SITUAÇÃO**

A mensagem de erro é apresentada ao tentar realizar a integração financeira da folha de pagamento pela tela **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34461087237655)

 **SOLUÇÃO**

Siga as orientações conforme o cenário identificado:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34461087238935)

  Se o **centro de resultado está inativo** e não será mais utilizado:

- 

Identifique onde o centro de resultado está cadastrado (exemplo: **"Empresas"**, **"Eventos"**, **"Departamentos"**, **"Rateios"**, entre outros).

- 

Substitua pelo centro de resultado que deverá ser utilizado a partir de agora.
 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34461087242903)

  Se o **centro de resultado está correto**:

- 

Ative o centro de resultado.

- 

Marque a opção **"Analítico"** para que a integração seja realizada com sucesso.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34461087245335)

 **CAUSA**

O erro ocorre quando o centro de resultado informado para a integração financeira está desativado ou não está marcado como analítico.