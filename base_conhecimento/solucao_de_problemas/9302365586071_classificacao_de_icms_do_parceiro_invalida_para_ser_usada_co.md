# Classificação de ICMS do parceiro inválida para ser usada com esta TOP

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9302365586071-Classifica%C3%A7%C3%A3o-de-ICMS-do-parceiro-inv%C3%A1lida-para-ser-usada-com-esta-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/9302365586071-Classifica%C3%A7%C3%A3o-de-ICMS-do-parceiro-inv%C3%A1lida-para-ser-usada-com-esta-TOP)  
> **ID:** `9302365586071` | **Última Atualização:** 2026-07-22T15:08:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606937775127)

 MENSAGEM:**

[CORE_E04461]  Classificação de ICMS do parceiro inválida para ser usada com esta TOP.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606937782551)

 SITUAÇÃO:**

Ao tentar importar uma nota pelo Portal de Importação de XML a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606937785751)

 CAUSA:**

Quando a classificação de ICMS definida no Tipo de operação está diferente do que foi devido no cadastro do parceiro.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606937787799)

 SOLUÇÃO:**

Verifique os seguintes campos:
No cadastro do** Tipo de operação TOP** *(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)* verifique a configuração do seguinte campo:

TOP -> Aba Impostos -> Classificação Fiscal: 

Se no campo acima estiver com a informação "Usar do Parceiro" , vá até o campo abaixo e verifique se a informação também está como "Usar do Parceiro"

![top impostos.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606937798295)

Acesse a tela **Parceiros*** (Configurações » Cadastros » Parceiros)*

 Aba Grupo ICMS/ISS por Empresa -> Classificação de ICMS:

![parceiros icms.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606997911831)

Os dois campos precisam estar com a mesma informação.
Caso seja necessário realizar algum ajuste, vá até o Portal de Importação de XML e processe novamente o arquivo.