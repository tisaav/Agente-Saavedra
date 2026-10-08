# (VALIDAR GEOVANA - Ticket 528992/489690/489690) - Erro ao realizar integração contábil - (Erro no método 'criarResumo' Motivo: null)

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35913861133079--VALIDAR-GEOVANA-Ticket-528992-489690-489690-Erro-ao-realizar-integra%C3%A7%C3%A3o-cont%C3%A1bil-Erro-no-m%C3%A9todo-criarResumo-Motivo-null](https://ajuda.sankhya.com.br/hc/pt-br/articles/35913861133079--VALIDAR-GEOVANA-Ticket-528992-489690-489690-Erro-ao-realizar-integra%C3%A7%C3%A3o-cont%C3%A1bil-Erro-no-m%C3%A9todo-criarResumo-Motivo-null)  
> **ID:** `35913861133079` | **Última Atualização:** 2026-07-29T13:21:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913881164439)

 **MENSAGEM: **

Ao tentar gerar a integração contábil é exibida a seguinte mensagem de erro:  

Falha 
Erro no método 'criarResumo' Motivo: null

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913861121687)

 SOLUÇÃO:**

Para resolver o problema, realize os seguintes procedimentos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913881167639)

 Identifique os tipos de folhas que está ocorrendo o erro para filtrar os funcionários.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913861127831)

 Em seguida acesse a tela ****[''Configuração Funcionários''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios)** **(Pessoal+  » Cadastros).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36342415515159)

 Confira **''HORASSEM'' **(Qtd Horas Semanais) e **CODCARGAHOR** (Carga horária). 

Esses campos devem estar **preenchidos** para que **não apresente erro na ******[''Integração Contábil''](https://ajuda.sankhya.com.br/hc/pt-br/articles/7080867168151-Integra%C3%A7%C3%A3o-Cont%C3%A1bil-da-Folha-de-Pagamento). 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913881169047)

 Por fim, clique e execute a rotina da integração contábil.

 

**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/35913881171351)

 IMPORTANTE:**

Caso a **Carga Horária** esteja preenchida na tela, mas o campo **CODCARGAHOR** não apareça gravado na **TFPUNF**, exclua a carga horária do funcionário, cadastre novamente e confirme se o registro foi salvo corretamente na tabela.

Para funcionários **intermitentes**, que não possuem horas fixas, utilize o valor **0** no campo de carga horária.


---

### 🔗 Links e Referências Internas:

- [''Configuração Funcionários''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios)
- [''Integração Contábil''](https://ajuda.sankhya.com.br/hc/pt-br/articles/7080867168151-Integra%C3%A7%C3%A3o-Cont%C3%A1bil-da-Folha-de-Pagamento)