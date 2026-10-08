# Nenhuma página a apresentar. Verifique o filtro e tente novamente

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/25169472211095-Nenhuma-p%C3%A1gina-a-apresentar-Verifique-o-filtro-e-tente-novamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/25169472211095-Nenhuma-p%C3%A1gina-a-apresentar-Verifique-o-filtro-e-tente-novamente)  
> **ID:** `25169472211095` | **Última Atualização:** 2026-08-18T20:02:13Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169472191767)

 **MENSAGEM:**

[CORE_E02500] Nenhuma página a apresentar. Verifique o filtro e tente novamente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169510485783)

SOLUÇÃO:**

Acesse a tela  **"Configuração de funcionários"** e verifique principalmente a falta dos dados como CTPS, Série, UF CTPS e outros que contém o * (asterisco) que são obrigatórios.

Após ajustar os dados no cadastro do funcionário, emita novamente o relatório para validar se a emissão será concluída com sucesso.

 

![451454614_872578971565271_6101682681129542641_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169472200855)

 

![Nenhuma página a apresentar. Verifique o filtro e tente novamente 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/25343871591703)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169472209047)

CAUSA:**

O problema ocorre porque faltam informações no cadastro do funcionário. Visto que a query do relatório valida estes campos, caso falte algum ele não é gerado apresentando a mensagem acima.