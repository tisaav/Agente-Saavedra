# Fer Motivo: Falha ao persistir requisição Falha ao persistir funcionário

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35789163898903-Fer-Motivo-Falha-ao-persistir-requisi%C3%A7%C3%A3o-Falha-ao-persistir-funcion%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/35789163898903-Fer-Motivo-Falha-ao-persistir-requisi%C3%A7%C3%A3o-Falha-ao-persistir-funcion%C3%A1rio)  
> **ID:** `35789163898903` | **Última Atualização:** 2026-07-29T13:21:06Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315771137815)

 **MENSAGEM:** 

Falha
Não foi possível confirmar requisição pendente.
Motivo: Falha ao persistir requisição.
Falha ao persistir funcionário.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35789163895319)

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315802451735)

 SITUAÇÃO:**

Ao tentar aprovar uma requisição pendente, o sistema apresenta a mensagem de falha. 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315802454167)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315771146135)

 Acesse o **''Pessoal+''** (Rotinas Folha» Requisições); 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315802461207)

 Localize o campo ''**Vínculo''** e altere temporariamente para '**'Prazo Indeterminado**''**; **

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315771153047)

 Retorne à tela da requisição e tente aprovar novamente, o processo será concluído com sucesso; 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315771155223)

 Após a aprovação, volte ao cadastro do funcionário; 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315802466199)

 Restaure o vínculo para **“Prazo Determinado”; **

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315802468887)

 Preencha o campo **“Objeto determinante da contratação por prazo determinado”** (campo obrigatório para este tipo de vínculo).

![7 (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/36315802470551)

 Salve o cadastro para que o erro não volte a ocorrer.

**Observações importantes: ** 

- 

O campo Objeto determinante da contratação por prazo determinado é exigido pela legislação trabalhista e deve estar sempre preenchido quando o vínculo for Prazo Determinado.

- 

Caso o funcionário esteja realmente dispensado do período de experiência, avalie se o vínculo por prazo determinado é o mais adequado para o caso.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36315771164951)

 CAUSA:**

O erro ocorre quando o vínculo do funcionário está definido como Prazo Determinado e, ao mesmo tempo, a opção ''**Dispensado da experiência''** está habilitada.

Essa combinação de configurações impede o sistema de registrar corretamente os dados do funcionário, ocasionando falha na gravação da requisição.

![image (59).png](https://ajuda.sankhya.com.br/hc/article_attachments/36315771166871)