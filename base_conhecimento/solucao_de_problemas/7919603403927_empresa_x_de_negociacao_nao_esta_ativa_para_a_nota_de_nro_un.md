# Empresa X de negociação não está ativa para a nota de Nro Único: XXX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7919603403927-Empresa-X-de-negocia%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ativa-para-a-nota-de-Nro-%C3%9Anico-XXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/7919603403927-Empresa-X-de-negocia%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ativa-para-a-nota-de-Nro-%C3%9Anico-XXX)  
> **ID:** `7919603403927` | **Última Atualização:** 2026-07-22T15:12:39Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361645474071)

 MENSAGEM:**

[ORA-20101]: Empresa X de negociação não está ativa para a nota de Nro Único: XXX.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361645476887)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361630264343)

 Acesse a tela: "Configurador de Layout da Nota", localize o layout do pedido/nota de compra e disponibilize o campo **"Empresa da Negociação"**, conforme print abaixo.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14680319121943)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361645477655)

 Em seguida, na Central de Compras, caso a tela esteja aberta, feche e abra novamente para que o campo seja carregado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361630266391)

 Verifique o campo "Empresa da Negociação", que deve estar incorretamente informado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361645479575)

 Faça o ajuste e teste novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361630267543)

CAUSA:**

Acontece quando o arquivo XML vem com a informação de empresa negociação na tag e no momento da confirmação da nota na central o campo não existe no layout, ou caso exista, está oculto com valor incorreto.