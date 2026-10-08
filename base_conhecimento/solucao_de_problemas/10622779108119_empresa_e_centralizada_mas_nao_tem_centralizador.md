# Empresa é centralizada, mas não tem centralizador

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10622779108119-Empresa-%C3%A9-centralizada-mas-n%C3%A3o-tem-centralizador](https://ajuda.sankhya.com.br/hc/pt-br/articles/10622779108119-Empresa-%C3%A9-centralizada-mas-n%C3%A3o-tem-centralizador)  
> **ID:** `10622779108119` | **Última Atualização:** 2026-07-29T13:16:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19029652949271)

 MENSAGEM:**

Empresa é centralizada, mas não tem centralizador.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19029667810455)

 SITUAÇÃO:**

Ao importar arquivo gerado da sefip 650 a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19029667813783)

 CAUSA:**

Ocorre quando as empresas filiais estão como centralizadoras.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19029652969239)

 SOLUÇÃO:**

Só serão utilizadas as opções de centralizadora e centralizadas quando as empresas filiais forem centralizadas na Matriz e a Matriz centralizadora. Ou seja, todo recolhimento de INSS e FGTS na SEFIP será pelo CNPJ da matriz, mas quando as filiais têm CNPJ próprio e funcionários vinculados a eles, o recolhimento de INSS e FGTS é realizado no respectivo CNPJ e não na matriz.

Nesse caso, acesse o cadastro das **Empresas** *(Caminho de acesso à tela: Configurações » Cadastros » Pessoal » Empresas), *vá até a aba Informações Gerais e no campo 'Centralizadora', nas empresas que estiverem como centralizadora, altere para 'Não Centraliza'.

![empresas 13-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19029652974103)

No MGE Pessoal, essa configuração estará em Arquivos > Empresas, aba informações gerais:

![MGE 13-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19029667831319)

Após isto, o arquivo será gerado e importado na SEFIP conforme esperado.

**Importante:** Ressaltamos que só utiliza a configuração de Centralizadora e Centralizadas se o recolhimento for todo pelo CNPJ da matriz. Mas se tiver certificado digital de CNPJ das empresas filiais no CNS, o recolhimento segue esses CNPJ's, dispensando assim a configuração de centralizadas e centralizadora.