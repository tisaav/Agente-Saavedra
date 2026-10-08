# Erro ao gerar lote ou cancelar lançamento fiscal: src-resolve: Cannot resolve the name 'TEnvEvento' to a(n) 'type definition' component

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32217854083351-Erro-ao-gerar-lote-ou-cancelar-lan%C3%A7amento-fiscal-src-resolve-Cannot-resolve-the-name-TEnvEvento-to-a-n-type-definition-component](https://ajuda.sankhya.com.br/hc/pt-br/articles/32217854083351-Erro-ao-gerar-lote-ou-cancelar-lan%C3%A7amento-fiscal-src-resolve-Cannot-resolve-the-name-TEnvEvento-to-a-n-type-definition-component)  
> **ID:** `32217854083351` | **Última Atualização:** 2026-07-22T14:31:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32554025389463)

 MENSAGEM:**

src-resolve: Cannot resolve the name 'TEnvEvento' to a(n) 'type definition' component

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32554009173271)

 SITUAÇÃO:**

Ao gerar lote ou cancelar um lançamento fiscal nos portais, ocorre o erro "src-resolve: Cannot resolve the name 'TEnvEvento' to a(n) 'type definition' component ".

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32217854070295)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32217822920087)

 Acesse a **"Administração do servidor"** e verifique se o registro da base está configurado.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32217854071063)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32217854071319)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32217854071959)

 Ainda na Administração do Servidor, limpe o cache, feche todas as telas e realize um novo teste.**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32217822922263)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32217854072599)

 Se o erro persistir, reinicie o sistema. Lembrando que esse processo vai parar a sua base, e pode demorar até 15 minutos para voltar. Então, sempre realize fora do horário de expediente ou com aviso prévio.**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32217822924951)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32217822919831)

 Para se **certificar se o serviço voltou**, acesse a tela **"Console NFe"** e, na aba **"Status do Serviço"**, selecione o CNPJ e o ambiente desejado e clique em **"Testar"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32217822925847)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32554009173911)

CAUSA:**

Este erro ocorre pois o Console NF-e, onde é configurado o certificado digital, perde a comunicação com a Sefaz.