# Java.util.ConcurrentModificationException ocorre ao tentar logar no Coletor SuperWaba com o WildFly

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733174-Java-util-ConcurrentModificationException-ocorre-ao-tentar-logar-no-Coletor-SuperWaba-com-o-WildFly](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733174-Java-util-ConcurrentModificationException-ocorre-ao-tentar-logar-no-Coletor-SuperWaba-com-o-WildFly)  
> **ID:** `360043733174` | **Última Atualização:** 2026-07-22T15:59:22Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16418071527447)

 MENSAGEM:**

'java.util.ConcurrentModificationException'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16418071531927)

 SITUAÇÃO:**

Ao tentar logar no Coletor SuperWaba, após a troca da Aplicação Jboss 4.0 para WildFly, ocorre a mensagem a seguir.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16418086182167)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16418071540887)

 Acesse o diretório de instalação Coletor SuperWaba, nos computadores que apresentaram o problema e exclua os arquivos temporários, deixando apenas os arquivos: **WMS.exe**, **WMS.pdb** e **WMS.prc**.

Ex: C:\SuperWaba\WMS

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360058926214)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16418071544599)

 Após a exclusão repita o procedimento em todos os computadores que usam o aplicativo Coletor SuperWaba e acesse novamente o coletor.

 

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360058926234)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16418071546263)

 CAUSA:**

Ocorre pois os arquivos temporários na pasta de instalação do SuperWaba não são suportados pelo WildFly.