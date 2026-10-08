# Erro na Emissão do TCRT: Falha. Não foi possível gerar o relatório solicitado.

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37365334730647-Erro-na-Emiss%C3%A3o-do-TCRT-Falha-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-relat%C3%B3rio-solicitado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37365334730647-Erro-na-Emiss%C3%A3o-do-TCRT-Falha-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-relat%C3%B3rio-solicitado)  
> **ID:** `37365334730647` | **Última Atualização:** 2026-07-29T13:22:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37470765287063)

 MENSAGEM:**

Falha. Não foi possível gerar o relatório solicitado.

**Motivo: **Error evaluating expression: Source text:

String format (“%s %s %s %s”, SF(PIS).substring(0,3), SF(PIS).substring(3,8), SF(PIS).substring(8,10), SF(PIS).substring(10,11))

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37365318747415)

 

##### **

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309941624599)

 SITUAÇÃO:**

Ao tentar emitir o **TRCT (Termo de Rescisão do Contrato de Trabalho)**, o sistema apresentou um erro que impediu a geração do relatório. A falha está relacionada à validação de expressão e à formatação do campo **PIS**, que não atende aos critérios esperados pelo sistema.

 

##### **

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309954470807)

 SOLUÇÃO:**

Para resolver o problema, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37470765297431)

 Acesse a tela ****[''Configuração Funcionários''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios)** **(Pessoal+ » Cadastros » Configuração Funcionários)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37470757951767)

 Localize o campo **''PIS/PASEP''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37470765298455)

 Verifique se o número:

- 

Possui **11 dígitos**.

- 

Está preenchido **sem espaços, pontos ou caracteres especiais**.

- 

Corresponde ao número correto do colaborador.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37470757954327)

 Caso identifique inconsistências:

- Corrija o PIS.

- Salve o cadastro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37470765299991)

 Após o ajuste, **realize novamente a emissão do TRCT**.

 

##### **

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309954471447)

 CAUSA:**

O erro ocorre quando o número do **PIS/PASEP** do colaborador está **incompleto, inválido ou fora do padrão exigido pelo sistema**.

Durante a emissão do **TRCT**, o sistema realiza a quebra e formatação do número do PIS por meio de validações internas (substring). Quando o cadastro apresenta inconsistências, esse processo falha, impedindo a geração do relatório.

Isso pode acontecer quando o **PIS/PASEP** possui quantidade de dígitos inferior ao padrão de **11 dígitos**, está cadastrado com **caracteres inválidos**, como pontos, espaços ou símbolos, ou ainda quando se encontra **nulo, incompleto ou inconsistente** no cadastro do colaborador.


---

### 🔗 Links e Referências Internas:

- [''Configuração Funcionários''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios)