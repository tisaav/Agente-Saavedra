# Configurações para geração dos eventos R-2050 e R-2055 EFD REINF Alterações decorrem da Medida Provisória nº 1.166/2023

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14651356449943-Configura%C3%A7%C3%B5es-para-gera%C3%A7%C3%A3o-dos-eventos-R-2050-e-R-2055-EFD-REINF-Altera%C3%A7%C3%B5es-decorrem-da-Medida-Provis%C3%B3ria-n%C2%BA-1-166-2023](https://ajuda.sankhya.com.br/hc/pt-br/articles/14651356449943-Configura%C3%A7%C3%B5es-para-gera%C3%A7%C3%A3o-dos-eventos-R-2050-e-R-2055-EFD-REINF-Altera%C3%A7%C3%B5es-decorrem-da-Medida-Provis%C3%B3ria-n%C2%BA-1-166-2023)  
> **ID:** `14651356449943` | **Última Atualização:** 2026-07-22T14:58:18Z

---

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450660505495)

 R-2050 ****– Comercialização de produção:** receitas informadas com o indicativo de comercialização {indCom} igual a “8 - Comercialização da produção para entidade executora do PAA” não mais geraram o código de receita “1213” a recolher no totalizador R-9001.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969625235991)

 O sistema busca a informação no campo **"****Indicador de Comercialização":** 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14651232381335)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450660505495)

 R-2055** **- Aquisição de produção rural:** aquisições informadas por contribuinte pessoa jurídica com os indicativos {indAquis} igual a “3 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA” ou “6 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA - Produção isenta (Lei 13.606/2018)” gerarão o código de receita “1213” a recolher no totalizador R-9001. 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969625235991)

  O sistema busca a informação no campo **"I****ndicador de aquisição":**

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14651175835799)

**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912762376983)

 Se não tiver escolhido nenhuma opção acima, o sistema valida o CNPJ da empresa com 14 caracteres, se tiver, o sistema vai lançar 1 na tag.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912749714839)

 Se o CNPJ não tiver 14 caracteres, o sistema vai validar o seguinte campo nas preferências da **"****Empresa"  ***(Caminho de acesso: **Comercial » Preferências » Empresa):*

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14651179900951)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912749716631)

 Se ele estiver desmarcado, o sistema vai lançar o valor 2 na tag, caso nenhuma configuração acima for verdadeira, o sistema vai lançar o valor 3 na tag.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969719491991)

 **OBSERVAÇÃO:**

[Alterações decorrentes da Medida Provisória nº 1.166/2023](http://sped.rfb.gov.br/pagina/show/7191)