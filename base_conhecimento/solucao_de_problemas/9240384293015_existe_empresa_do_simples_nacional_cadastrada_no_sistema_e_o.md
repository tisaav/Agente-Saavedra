# Existe empresa do Simples Nacional cadastrada no sistema e o campo CSOSN não foi configurado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9240384293015-Existe-empresa-do-Simples-Nacional-cadastrada-no-sistema-e-o-campo-CSOSN-n%C3%A3o-foi-configurado](https://ajuda.sankhya.com.br/hc/pt-br/articles/9240384293015-Existe-empresa-do-Simples-Nacional-cadastrada-no-sistema-e-o-campo-CSOSN-n%C3%A3o-foi-configurado)  
> **ID:** `9240384293015` | **Última Atualização:** 2026-07-22T15:09:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611523713943)

 MENSAGEM:**

[CORE_E06608] Existe empresa do Simples Nacional cadastrada no sistema e o campo CSOSN não foi configurado.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611549541655)

 SITUAÇÃO:**

Ao tentar configurar uma alíquota de ICMS que não é Simples Nacional a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611549552535)

 CAUSA:**

Quando existe alguma empresa cadastrada como Simples Nacional e o campo CSOSN não estiver preenchido.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611523735319)

 SOLUÇÃO:**

A mensagem de alerta é apresentada, a partir das versões mais recentes da 4.11.

Foi feito o processo de melhoria no sistema para que seja feita a validação do CSOSN quando possuir alguma empresa optante do Simples Nacional cadastrada no Sistema.

Portanto as regras de alíquota que foram cadastradas anteriormente precisam ser ajustadas com o preenchimento do campo conforme imagem abaixo:

*(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS)*

![Simples nacional.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611549561111)