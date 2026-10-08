# cvc-enumeration-valid: O valor '1' não tem um aspecto válido em relação à enumeração '[2, 3, 4, 5, 6, 7, 9]'

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/12772062614167-cvc-enumeration-valid-O-valor-1-n%C3%A3o-tem-um-aspecto-v%C3%A1lido-em-rela%C3%A7%C3%A3o-%C3%A0-enumera%C3%A7%C3%A3o-2-3-4-5-6-7-9](https://ajuda.sankhya.com.br/hc/pt-br/articles/12772062614167-cvc-enumeration-valid-O-valor-1-n%C3%A3o-tem-um-aspecto-v%C3%A1lido-em-rela%C3%A7%C3%A3o-%C3%A0-enumera%C3%A7%C3%A3o-2-3-4-5-6-7-9)  
> **ID:** `12772062614167` | **Última Atualização:** 2026-07-29T13:17:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365376032023)

 MENSAGEM:**

cvc-enumeration-valid: O valor '1' não tem um aspecto válido em relação à enumeração '[2, 3, 4, 5, 6, 7, 9]'. Deve ser um valor da enumeração.
cvc-type.3.1.3: O valor '1' do elemento 'tpJornada' não é válido.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365407561879)

 CAUSA:**

- Esse erro ocorre quando não foi preenchido o Tipo de Jornada da carga horária; ou

- Preencher o campo "**INDSITREMUNDESLIG**" indevidamente, este campo normalmente só é preenchido em caso de aposentadoria.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365376042007)

 SOLUÇÃO:**

**Para resolução da primeira causa, siga o passo a passo abaixo:**

**MGE**

Para a correção desse erro, verifique no cadastro do funcionário qual é o código da carga horária que ele está vinculado.
 

![cvc-enumeration-valid](https://ajuda.sankhya.com.br/hc/article_attachments/15830437050391)

 
Em seguida, acesse o cadastro da carga horária em Arquivos/Cadastros/Carga Horária e valide o campo Tipo de Jornada.
 

![cvc-enumeration-valid](https://ajuda.sankhya.com.br/hc/article_attachments/15830437053719)

 
 
Selecione o tipo que melhor se enquadrar na carga horária em questão. É obrigatório o preenchimento do tipo de jornada para envio ao eSocial. Após esse ajuste, realize uma nova geração e envie o evento.

**Pessoal +**

Verifique no cadastro do funcionário qual é o código da carga horária que ele está vinculado.

 

![evidencia hoje.png](https://ajuda.sankhya.com.br/hc/article_attachments/18362460414615)

Em seguida, acesse o cadastro da carga horária em Arquivos/Cadastros/Carga Horária e valide o campo Tipo de Jornada.

**

![evidencia 2 hoje.png](https://ajuda.sankhya.com.br/hc/article_attachments/18362460418583)

**

Selecione o tipo que melhor se enquadrar na carga horária em questão.
É obrigatório o preenchimento do tipo de jornada para envio ao eSocial. **
**Após esse ajuste, realize uma nova geração e envie o evento.

 

**P****ara resolução da sua causa siga a orientação abaixo:**

 

Caso o campo "**INDSITREMUNDESLIG**" esteja preenchido indevidamente basta deletar o campo e enviar o evento de rescisão novamente.

Esse campo normalmente só é preenchido em caso de aposentadoria, após deletar o campo o evento de rescisão será finalizado com sucesso.

![evidencia parametro.png](https://ajuda.sankhya.com.br/hc/article_attachments/18362497457303)