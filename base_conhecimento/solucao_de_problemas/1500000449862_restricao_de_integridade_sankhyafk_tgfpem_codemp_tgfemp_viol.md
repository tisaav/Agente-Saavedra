# Restrição de integridade (SANKHYA.FK_TGFPEM_CODEMP_TGFEMP) violada - chave mãe não localizada

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000449862-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFPEM-CODEMP-TGFEMP-violada-chave-m%C3%A3e-n%C3%A3o-localizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000449862-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFPEM-CODEMP-TGFEMP-violada-chave-m%C3%A3e-n%C3%A3o-localizada)  
> **ID:** `1500000449862` | **Última Atualização:** 2026-07-22T15:26:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275527925143)

 MENSAGEM**:

[ORA-02291] Restrição de integridade (SANKHYA.FK_TGFPEM_CODEMP_TGFEMP) violada - chave mãe não localizada

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275523495575)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275527935255)

 Acesse o cadastro de Produto que está tentando duplicar em: *Configurações » Cadastros » Produtos » Produtos*

Aba: **"****Impostos/Informações por empresa"**

Identifique o código da empresa, vinculado ao produto, e certifique-se se esta empresa está ativa no sistema em: Comercial » Preferências » Empresa.

Considere primeiramente dar a devida manutenção no código da empresa vinculada, para posterior duplicação do produto.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275527938199)

 Após os ajustes, tente duplicar novamente o produto.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275527942807)

 CAUSA:**

Ocorre quando o código da empresa vinculado ao produto está inativo ou foi excluído do sistema e, ao tentar duplicar o produto, o sistema copia as informações para o novo produto e como não existe mais a empresa, apresenta o erro.