# XML de resposta do serviço 'Consulta lote RPS' com formato inesperado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15412927675031-XML-de-resposta-do-servi%C3%A7o-Consulta-lote-RPS-com-formato-inesperado](https://ajuda.sankhya.com.br/hc/pt-br/articles/15412927675031-XML-de-resposta-do-servi%C3%A7o-Consulta-lote-RPS-com-formato-inesperado)  
> **ID:** `15412927675031` | **Última Atualização:** 2026-07-22T14:57:00Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581319635991)

 MENSAGEM:**

[CORE_E00499]: XML de resposta do serviço 'Consulta lote RPS' com formato inesperado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581319639959)

 SOLUÇÃO:**

Verifique junto à prefeitura, a quantidade máxima de notas suportadas em um lote. Configure no parâmetro **"****NFSEMAXNOTALOTE"**  o número que eles orientaram.

No campo **"Qtd. máxima de notas em um lote NFS-e"**, preencha a quantidade máxima de notas (NFS-e) em um único lote; possui a mesma funcionalidade do parâmetro **"Qtd. máxima de notas em um lote NFS-e - NFSEMAXNOTALOTE"**. Caso exista informação no campo Qtd. máxima de notas em um lote NFS-e para alguma cidade, assim como no parâmetro de chave NFSEMAXNOTALOTE, o sistema  irá considerar o campo no Cadastro da cidade em questão.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581319641495)

 Exemplo:**

No parâmetro citado é configurado 50 e no cadastro da cidade de Araxá é configurado 30; para a cidade de Araxá será considerado o valor 30 e, para as demais cidades, o valor 50.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581350514583)

 CAUSA:**

Ocorre por não informar a quantidade de notas suportadas em lote de acordo com a prefeitura no parâmetro **"NFSEMAXNOTALOTE".**