# Não foi possível recuperar o Certificado Digital! CNPJ do detentor do Certificado Digital XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10415596663063-N%C3%A3o-foi-poss%C3%ADvel-recuperar-o-Certificado-Digital-CNPJ-do-detentor-do-Certificado-Digital-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/10415596663063-N%C3%A3o-foi-poss%C3%ADvel-recuperar-o-Certificado-Digital-CNPJ-do-detentor-do-Certificado-Digital-XXXX)  
> **ID:** `10415596663063` | **Última Atualização:** 2026-07-22T15:03:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606035507991)

 MENSAGEM:**

[CORE_E06974] Não foi possível recuperar o Certificado Digital! CNPJ do detentor do Certificado Digital XXXXXX.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606035518871)

 SITUAÇÃO:**

Ao tentar gerar o EFD REINF a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606044395543)

 CAUSA: **

Ocorre quando algum cadastro não está correto.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606044403735)

 SOLUÇÃO:**

- Necessário verificar se no cadastro da empresa possui procurador;

- Caso se trate de filial verificar se esta está devidamente cadastrada no sistema.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606035540247)

 Acesse a tela **Preferências** *(Configurações » Avançado » Preferências)* e desligue o parâmetro **Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - FPSANREINFEXE**;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606044414743)

 Ligue os parâmetros **Ativa o Reinf embarcardo? - ATVREINFSKW** e **Ativa os logs do Reinf embarcardo? - DEBUGREINFSKW** ( a ativação desses parâmetros é para o sistema deixar de usar o San-Esocial e passar a usar o San-NFe para comunicar os dados do Reinf com a receita).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606035551383)

 Assim que ligar esses parâmetros será necessário reiniciar o SankhyaOm. Isso é necessário, pois nesta versão 1.05.01 o Reinf não usará mais o San-Esocial, somente o San-NFe.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606044437527)

 O certificado digital **com o CNPJ do procurador**, deverá ser cadastrado na tela 'Console NF-e' dentro do SankhyaOm, para que o sistema consiga assinar os arquivos XML.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606035567639)

 Na tela de geração do Reinf foi criado o campo 'Versão do layout' onde ao cadastrar a referência 01/05/2021 deverá estar selecionado com a versão '1.05.01-Após Junho/2021'.