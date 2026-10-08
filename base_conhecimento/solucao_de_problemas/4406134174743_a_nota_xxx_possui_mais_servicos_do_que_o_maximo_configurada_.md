#  A nota XXX possui mais serviços do que o máximo configurada na cidade

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4406134174743--A-nota-XXX-possui-mais-servi%C3%A7os-do-que-o-m%C3%A1ximo-configurada-na-cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406134174743--A-nota-XXX-possui-mais-servi%C3%A7os-do-que-o-m%C3%A1ximo-configurada-na-cidade)  
> **ID:** `4406134174743` | **Última Atualização:** 2026-07-22T15:22:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370485790103)

 MENSAGEM:**

 A nota XXXX possui mais serviços do que o máximo configurada na cidade.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370485791767)

 SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370485793431)

 Localize a cidade da empresa, preenchida na tela** Configurações » Cadastros » Empresas,**  na aba **"Endereço"** e no campo **"Cidade"**; 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370485795607)

 Na tela **“Cidades", **localize o código informado no cadastro de empresas e preencha o campo **"****Quantidade Máxima p/ enviar itens NFS-e no Json"**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15695253985175)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370488602903)

OBSERVAÇÃO:**

Esta marcação serve apenas quando é realizado o envio de mais de um serviço em uma nota fiscal, o código da lista de serviço, o CNAE e o código de tributação do município deve3rão ser idênticos, assim enviamos mais de um serviço em uma mesma nota.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370485800983)

 Em seguida, redigitar a empresa no cabeçalho da nota e gere o lote novamente.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15695297175191)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370488605591)

 CAUSA:**

A mensagem é apresentada quando o campo não esta devidamente configurado com as quantidades e quando algum serviço que está sendo enviado tem o código da lista de serviço divergente um do outro.