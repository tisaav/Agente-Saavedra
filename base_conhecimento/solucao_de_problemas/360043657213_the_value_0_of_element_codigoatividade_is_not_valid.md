# The value '0' of element 'CodigoAtividade' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657213-The-value-0-of-element-CodigoAtividade-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657213-The-value-0-of-element-CodigoAtividade-is-not-valid)  
> **ID:** `360043657213` | **Última Atualização:** 2026-07-22T16:04:31Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134930584471)

 MENSAGEM:**

cvc-pattern-valid: Value '0' is not facet-valid with respect to pattern '[0-9]{9}' for type 'tpCodigoAtividade'.cvc-type.3.1.3: The value '0' of element 'CodigoAtividade' is not valid.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134936681623)

 SITUAÇÃO:**

Ao realizar emissão de NFS-e pelo **"[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)"**, no Sankhya W, acessando a opção **"(...)"** » **"Ver Acompanhamento"**, é possível consultar o detalhe da rejeição a seguir.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134930587159)

 SOLUÇÃO:**

Algumas Prefeituras utilizam o **Cód. Natureza Oper. ISS (NFS-e)** ao invés do **CNAE**. Para saber qual o CNAE ou Código da natureza de Oper. correto, consulte a Prefeitura local.

Após esta verificação configure o sistema conforme orientação abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134936684567)

 Acesse: Configurações » Cadastros » Produtos » Serviço

- Aba: **Impostos**, campo **"CNAE"** - O código é composto por 7 dígitos e pode ser consultado no site da Prefeitura.

 

![servicos4.png](https://ajuda.sankhya.com.br/hc/article_attachments/14637262934039)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134930592535)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Campo: **"Cód. Natureza Oper. ISS (NFS-e)"**

 

![top5.png](https://ajuda.sankhya.com.br/hc/article_attachments/14637255030039)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134936687255)

 Após os ajustes, redigite o item na nota, caso o ajuste seja no cadastro do serviço.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134936688663)

 CAUSA:**

Ocorre quando o CNAE esta informado incorretamente no cadastro do serviço ou não preenchido.


---

### 🔗 Links e Referências Internas:

- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)