# Código de incidência tributária da rubrica para o IRRF inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10651946021527-C%C3%B3digo-de-incid%C3%AAncia-tribut%C3%A1ria-da-rubrica-para-o-IRRF-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/10651946021527-C%C3%B3digo-de-incid%C3%AAncia-tribut%C3%A1ria-da-rubrica-para-o-IRRF-inv%C3%A1lido)  
> **ID:** `10651946021527` | **Última Atualização:** 2026-07-29T13:16:35Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976283830167)

 MENSAGEM:**

Erro 1352 - Código de incidência tributária da rubrica para o IRRF inválido. Ação Sugerida: O valor informado no campo deverá existir na Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF.'

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976283844503)

 SITUAÇÃO:**

Ao realizar o envio da rescisão, evento  S-2299 a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976283857175)

 CAUSA:**

Ocorre quando o cadastro do evento está incorreto.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976281059863)

 SOLUÇÃO:**

Conforme [Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-html/tabelas.html#21) do e-Social, a incidência de IRRF '00 - Não é base do IRRF', **não é mais válida**, sendo assim, caso a rubrica esteja com essa informação, deve ser alterada: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976281069335)

 Acesse o cadastro do evento que apresentou o erro;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976281074199)

 Na guia ESOCIAL, no quadro INCIDÊNCIAS, no campo  "Incidência para IRRF", altere o código para um que seja válido, de acordo a Tabela 21 do eSocial.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976283879319)

 Clique em Salvar;

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976283887639)

 Após, gere novamente o evento S-1010;

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18976283894935)

 Acompanhe a validação do evento no eSocial.