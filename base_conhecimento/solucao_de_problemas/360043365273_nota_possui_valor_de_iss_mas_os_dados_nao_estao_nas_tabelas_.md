# Nota possui valor de ISS mas os dados não estão nas tabelas de impostos

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365273-Nota-possui-valor-de-ISS-mas-os-dados-n%C3%A3o-est%C3%A3o-nas-tabelas-de-impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365273-Nota-possui-valor-de-ISS-mas-os-dados-n%C3%A3o-est%C3%A3o-nas-tabelas-de-impostos)  
> **ID:** `360043365273` | **Última Atualização:** 2026-07-22T16:05:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113707677079)

 MENSAGEM:**

[CORE_E03910] Nota possui valor de ISS mas os dados não estão nas tabelas de impostos.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113722796695)

 CAUSA:**

Mensagem apresentada, quando na emissão de NFS-e não são localizadas informações de ISS na tabela de impostos (TGFDIN). 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113707679767)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113722779415)

 Abra a nota através da **"Central de Vendas/Compras"**, selecione na grade Itens o primeiro produto.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113722783511)

 **No botão **"Outras Opções [...]"** »** "Consultar/alterar dados dos impostos do Item"** verifique se foi gerada uma linha para o Imposto ISS. Realize essa análise para todos os itens.

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14556973722263)

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14556996460311)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113722786199)

 Em caso negativo, revise as configurações relacionadas ao cálculo desse imposto detalhadas no artigo: **"[Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014)"**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113707698455)

 Alíquotas de ISS

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113707698455)

 Cadastro de **"Serviços"** » Aba **"Impostos"** » Campo **"ISS"**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113707698455)

 **"[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** » Aba **"Propriedades"** » Campo ISS

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113707698455)

 Cadastro de **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** » Aba **"Fiscal"** » **"Retém ISS"**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113707698455)

 Cadastro de **"[Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** » Aba **"Livro Fiscal"** (Atualização livros de ISS / Modelo Documento ISS / Código CFPS).

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113722791703)

 Revisado os cadastros acima, caso exista algum ajuste, ou comprove estarem de acordo com o cálculo previsto, redigite o cabeçalho da nota, forçando a atualização das informações. Em seguida, gere um novo lote da NFS-e.


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)