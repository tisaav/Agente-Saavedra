# O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é valido.

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37086525701399-O-valor-do-campo-CNPJ-CNPJ-do-emitente-do-documento-fiscal-referenciado-informado-n%C3%A3o-%C3%A9-valido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37086525701399-O-valor-do-campo-CNPJ-CNPJ-do-emitente-do-documento-fiscal-referenciado-informado-n%C3%A3o-%C3%A9-valido)  
> **ID:** `37086525701399` | **Última Atualização:** 2026-07-22T14:21:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122050062743)

 MENSAGEM:**

“Erro
O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é valido.
Código: CORE_E04895.”

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122050065303)

** SITUAÇÃO**:

Ao tentar emitir ou confirmar um documento fiscal, o sistema apresenta a mensagem acima.

Esse erro indica que o CNPJ informado no documento fiscal referenciado não atende às validações exigidas pela SEFAZ.

 

##### **

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122050066199)

 SOLUÇÃO:**

Siga os passos abaixo para correção:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122058474007)

 Verifique o CNPJ do emitente**

- 

Confirme se o CNPJ informado no documento fiscal referenciado está correto.

- 

Utilize apenas números, sem pontos, barras ou traços.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122058478615)

 Valide o cadastro da empresa**

- 

Acesse o cadastro da empresa no sistema.

- 

Certifique-se de que o CNPJ está correto e ativo.

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122050072855)

 Revise o documento fiscal referenciado**

Confira:

- 

Chave de acesso.

- 

CNPJ do emitente.

- 

Modelo e série da nota.

Se necessário, refaça o vínculo do documento referenciado.

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122058481815)

 Verifique o ambiente de emissão**

- 

Confirme se a nota referenciada pertence ao mesmo ambiente (Produção ou Homologação).

#####  

##### **

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37122050076695)

 CAUSA:**

A inconsistência ocorre devido a divergências nos dados do documento fiscal referenciado, geralmente relacionadas a:

- 

CNPJ inválido, incorreto ou incompleto.

- 

CNPJ com dígito verificador inválido ou com caracteres indevidos.

- 

CNPJ diferente do cadastrado para a empresa emissora.

- 

Documento fiscal referenciado cadastrado incorretamente.

- 

Nota fiscal referenciada com dados divergentes (modelo, série ou chave de acesso). 

- 

Chave de acesso informada manualmente com erro.

- 

Utilização de ambiente incorreto (Produção x Homologação), como referência a uma nota de homologação em ambiente de produção ou vice-versa.