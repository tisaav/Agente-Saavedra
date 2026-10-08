# Erro no cálculo do 13º salário para estagiários

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39292501554071-Erro-no-c%C3%A1lculo-do-13%C2%BA-sal%C3%A1rio-para-estagi%C3%A1rios](https://ajuda.sankhya.com.br/hc/pt-br/articles/39292501554071-Erro-no-c%C3%A1lculo-do-13%C2%BA-sal%C3%A1rio-para-estagi%C3%A1rios)  
> **ID:** `39292501554071` | **Última Atualização:** 2026-07-29T13:22:33Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39292509508375)

 **MENSAGEM**

O sistema está calculando 13º salário para funcionários cadastrados como estagiários.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39292509509143)

 **SITUAÇÃO**

Ao processar a folha de pagamento, o sistema calcula indevidamente o 13º salário para colaboradores que possuem contrato de estágio. Esse cálculo aparece na folha mesmo que os funcionários estejam cadastrados com vínculo de estagiário.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39292509510551)

 **CAUSA**

O erro ocorre porque os estagiários estavam cadastrados com vínculo incorreto, como **"60 - Prazo Determinado"**. Funcionários com contrato de estágio não possuem direito ao 13º salário e não devem ter período de experiência configurado. Quando o vínculo está incorreto, o sistema interpreta que o colaborador tem direito ao benefício e realiza o cálculo indevidamente. Ao ajustar o cadastro para o vínculo correto de estagiário, o sistema deixa de calcular o 13º salário automaticamente.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39292501525271)

 **SOLUÇÃO**

Para corrigir o cálculo do 13º salário para estagiários, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39292501527447)

 Acesse a tela **"Cadastro de Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize os colaboradores estagiários que estão com o cálculo incorreto.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39292509519383)

 Verifique o campo **"Tipo de Vínculo"** no cadastro do funcionário.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41082044299799)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39292509520279)

 Caso o vínculo esteja configurado como **"60 - Prazo Determinado"** ou outro vínculo incorreto, altere para o vínculo específico de **"Estagiário"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39292509521431)

 Clique no **"Botão Salvar"** para gravar as alterações realizadas no cadastro do funcionário.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39292509527063)

 Recalcule a folha de pagamento para que o sistema processe corretamente, sem incluir o 13º salário para os estagiários.
 

 

**Observações importantes:**

- 

Estagiários não têm direito ao 13º salário conforme a legislação brasileira.
 

1. 

O vínculo correto deve ser sempre o específico para estagiários.
 

1. 

Após o ajuste do vínculo, não é necessário realizar configurações adicionais.
 

1. 

O sistema automaticamente deixará de calcular o 13º salário para esses colaboradores.