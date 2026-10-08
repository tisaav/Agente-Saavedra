# EFD Contribuições - Conta Contábil nos registros D101 e D105

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35904027129239-EFD-Contribui%C3%A7%C3%B5es-Conta-Cont%C3%A1bil-nos-registros-D101-e-D105](https://ajuda.sankhya.com.br/hc/pt-br/articles/35904027129239-EFD-Contribui%C3%A7%C3%B5es-Conta-Cont%C3%A1bil-nos-registros-D101-e-D105)  
> **ID:** `35904027129239` | **Última Atualização:** 2026-07-22T14:24:26Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36098305347991)

 SITUAÇÃO:**

Ao contabilizar documentos fiscais que compõem os registros D101 e D105, foi identificado que as contas contábeis não são geradas quando o documento é emitido ou lançado em uma empresa e a contabilização ocorre em outra, mesmo que as configurações contábeis estejam aparentemente corretas.  

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36098305350807)

 SOLUÇÃO:**

Para que a geração das contas contábeis ocorra normalmente, existem duas alternativas:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36098305353751)

 Realize a contabilização na própria empresa do documento, garantindo que a empresa da conta analítica corresponda à do documento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36098305360535)

 Na tela **“Empresa”** (Comercial» Preferências» Empresa), acesse a aba “**EFD – Escrituração Fiscal Digital”** e, na seção **“EFD Contribuições**”, desmarque a opção** “Contas contábeis analíticas para geração dos registros de apuração de PIS/COFINS”**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36098288709271)

 **CAUSA:**

Quando a empresa está configurada para utilizar a rotina Contas contábeis analíticas para geração dos registros de apuração de PIS/COFINS, o sistema realiza a validação entre a empresa vinculada à conta contábil e a empresa do documento fiscal.
Dessa forma, caso a contabilização ocorra em uma empresa diferente daquela onde o documento foi lançado, o sistema não localiza a conta analítica correspondente, e, consequentemente, não gera as contas contábeis nos registros D101 e D105.