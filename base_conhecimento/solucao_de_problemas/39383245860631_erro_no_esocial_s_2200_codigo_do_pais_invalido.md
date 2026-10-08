# Erro no eSocial S-2200: Código do País Inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39383245860631-Erro-no-eSocial-S-2200-C%C3%B3digo-do-Pa%C3%ADs-Inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/39383245860631-Erro-no-eSocial-S-2200-C%C3%B3digo-do-Pa%C3%ADs-Inv%C3%A1lido)  
> **ID:** `39383245860631` | **Última Atualização:** 2026-07-29T13:23:29Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39383245856791)

 **Mensagem**

[240] - Código do país inválido

Elemento: /eSocial/evtAdmissao/trabalhador/paisNac

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39383245857687)

 **Situação**

Ao enviar o **"evento S-2200"** (Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador) para o eSocial, o sistema retorna a mensagem de erro informando que o código do país está inválido. O usuário verifica o cadastro de países no sistema e confirma que o código está presente tanto na **"Tabela BACEN"** quanto no cadastro interno de **"País"** (como **"Código Fiscal"**), porém o evento continua sendo rejeitado pelo eSocial.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39383264912023)

 **Solução**

Para corrigir o erro, ajuste o código do país no cadastro do sistema conforme a **"Tabela 06 - Países"** do eSocial:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39383245858071)

 Acesse a tela **"Países"** (Configurações » Cadastros » Endereços » Países) no sistema.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39383245858199)

 Localize o país que está gerando o erro no envio do **"evento S-2200"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39383245858455)

 Verifique o código preenchido no campo **"****País Domicílio Fiscal****"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39383245858583)

 Consulte a **"Tabela 06 - Países"** disponível no manual do eSocial para identificar o código correto que deve ser utilizado.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39383245858967)

 Altere/cadastre o código no cadastro do país para o código correspondente na **"Tabela 06"** do eSocial. 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39383264913431)

 Salve as alterações realizadas no cadastro.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39383245859223)

 Retorne a Central do e-social e gere novamente o **"evento S-2200"**.

 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39383264915223)

 **Causa**

O erro ocorre devido à divergência entre o código do país cadastrado no sistema e o código exigido pelo eSocial. O cadastro de países no ERP pode estar preenchido com o **"código BACEN"**, enquanto o eSocial utiliza a **"Tabela 06 - Países"**, que possui codificação própria e diferente em alguns casos.

Por exemplo, um país pode estar cadastrado com o código **"639"** conforme padrão BACEN, mas na **"Tabela 06"** do eSocial o código correto é **"063"**. Essa inconsistência na validação do código do país impede o envio do **"evento S-2200"**, gerando a rejeição com o erro 240.