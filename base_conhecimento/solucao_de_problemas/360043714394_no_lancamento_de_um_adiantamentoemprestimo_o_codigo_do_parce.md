# No lançamento de um Adiantamento/Empréstimo, o código do parceiro é alterado ao Concluir

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043714394-No-lan%C3%A7amento-de-um-Adiantamento-Empr%C3%A9stimo-o-c%C3%B3digo-do-parceiro-%C3%A9-alterado-ao-Concluir](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043714394-No-lan%C3%A7amento-de-um-Adiantamento-Empr%C3%A9stimo-o-c%C3%B3digo-do-parceiro-%C3%A9-alterado-ao-Concluir)  
> **ID:** `360043714394` | **Última Atualização:** 2026-07-22T16:00:32Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17285691809943)

 SITUAÇÃO:**

No lançamento de um Adiantamento/Empréstimo, o código do parceiro é alterado ao Concluir.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17285649014679)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17285649020439)

 Acesse: Configurações » Avançado » Preferências

**"CODPARCFUNCS-Parceiro p/empréstimo p/Funcionários": **altere para 0 (zero)

Esse comportamento ocorre sempre que o parâmetro: CODPARCFUNCS - Parceiro p/empréstimo p/Funcionários estiver configurado com um valor diferente de 0 (zero).

Pois, no momento da inclusão do Adiantamento/Empréstimo será mantido o Código do Parceiro que estiver informado no parâmetro mencionado acima.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17285649027863)

 Acesse: Configurações » Rotinas » Adiantamento/Empréstimo

Após o ajuste no parâmetro, acesse novamente a rotina e efetue o lançamento do Adiantamento/Empréstimo.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17285649035799)

 NOTA:** 

Fica a critério da empresa a alteração do parâmetro. Pois, caso o Departamento Pessoal utilize um Parceiro **'coringa'** para Adiantamento/Empréstimo para Funcionário, o parâmetro precisa estar com o código do Parceiro coringa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17285649045143)

 CAUSA:**

Ocorre quando há um valor diferente de 0 (zero) no parâmetro CODPARCFUNCS.