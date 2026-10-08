# Geração registro C177, itens não incentivado no EFD ICMS 

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20837711747735-Gera%C3%A7%C3%A3o-registro-C177-itens-n%C3%A3o-incentivado-no-EFD-ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/20837711747735-Gera%C3%A7%C3%A3o-registro-C177-itens-n%C3%A3o-incentivado-no-EFD-ICMS)  
> **ID:** `20837711747735` | **Última Atualização:** 2026-07-24T12:43:44Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20837714537111)

SOLUÇÃO:**

Para que o sistema gere no campo **COD_INF_ITEM** do **C177**, o código informado no campo **"Cód. do Produto Sem Incentivo"** da tela **Cadastros Incentivos Fiscais/Financeiros:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20881436892311)

 Na tela **Empresa*** (Comercial » Preferências » Empresa)*, aba "EFD - Escrituração Fiscal digital", sub aba "Bloco e Registro" configure e marque para gerar.

![Empresas 26-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20881436907799)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20881421700887)

 Na tela **Produtos** *(Configurações » Cadastros » Produtos)* configure os campos **"Cód. Apur. Inc. PRODEPE/FUNCRESCE"** e **"Indicador Esp. Inc. PRODEPE/FUNCRESCE"** com a opção 'Sem Incentivos';

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20881421712407)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20881436943895)

 Na tela **Cadastros Incentivos Fiscais/Financeiros ***(Livros Fiscais » Arquivos » Cadastro Incentivos Fiscais/Financeiros)*,  será possível configurar os diversos incentivos que por ventura a empresa tenha, e neste caso temos o campo Cód. do Produto Sem Incentivo que deverá ser preenchido.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20881421719063)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20881436960919)

 No cadastro de **CFOP** *(Comercial » Arquivo » Cadastros » CFOP)*, marque o campo "Tipo de Operação PRODEPE" igual a "Operação Incentivada".

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20881421728407)