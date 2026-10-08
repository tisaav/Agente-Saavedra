# Não foi encontrada nenhuma conta referencial (J051) cadastrada para esta conta contábil

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33163963437719-N%C3%A3o-foi-encontrada-nenhuma-conta-referencial-J051-cadastrada-para-esta-conta-cont%C3%A1bil](https://ajuda.sankhya.com.br/hc/pt-br/articles/33163963437719-N%C3%A3o-foi-encontrada-nenhuma-conta-referencial-J051-cadastrada-para-esta-conta-cont%C3%A1bil)  
> **ID:** `33163963437719` | **Última Atualização:** 2026-07-22T14:29:17Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33184253525911)

 **MENSAGEM**: 

Não foi encontrada nenhuma conta referencial (J051) cadastrada para esta conta contábil

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33184246141463)

 **SITUAÇÃO**: 

Toda conta contábil que tenha movimentação ou saldo na ECD precisa estar **associada a uma conta do plano referencial** da Receita, definida no** bloco J **(Informações do Plano de Contas e Mapeamento).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33184246142999)

**SOLUÇÃO**: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33184246144791)

 Identifique a conta contábil que está sem vínculo. Para isso, veja no erro ou na pré-validação qual é o código da conta contábil que não está associada.

 

**

![537956de-9501-4cf8-aea3-25fc4f28ef89](https://ajuda.sankhya.com.br/hc/article_attachments/33184246148887)

 **Acesse a tela **''Plano de Contas'' **(Contabilização » Cadastros » Plano de Contas), selecione a conta identificada no passo anterior e, na aba** ''Conta Contábil Referencial'**', preencha o campo **''Tipo'' **e a** ''Conta Referencial Correspondente''. **

 

![image (2).png](https://ajuda.sankhya.com.br/hc/article_attachments/33186067821719)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33184246150423)

**CAUSA**: 

Ocorre durante a validação da ECD (Escrituração Contábil Digital), indicando que a conta contábil usada nos registros **não está vinculada** a uma conta referencial do plano da Receita Federal (Plano Referencial J050/J051).