# Erro 1861 - CPF do dependente xxxxxxxxxxx invalido

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/25617498296343-Erro-1861-CPF-do-dependente-xxxxxxxxxxx-invalido](https://ajuda.sankhya.com.br/hc/pt-br/articles/25617498296343-Erro-1861-CPF-do-dependente-xxxxxxxxxxx-invalido)  
> **ID:** `25617498296343` | **Última Atualização:** 2026-07-29T13:18:37Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39579875510039)

** MENSAGEM**

Erro 1861 - CPF do dependente 'xxx.xxx.xxx-xx' inválido Ação sugerida: Deve ser um CPF de dependente cadastrado no RET do eSocial ou no grupo de Informações de Dependentes do próprio evento. Elemento: /eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen/cpfDep

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39579875510679)

** SITUAÇÃO**

Ao tentar enviar o evento **"S-1210 - Pagamentos de Rendimentos do Trabalho"** para o eSocial, o sistema retorna erro informando que o CPF do dependente é inválido, mesmo que o CPF esteja correto no cadastro do sistema e validado na Receita Federal.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39579875512343)

** SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39579875512983)

  Verifique se o CPF do dependente está de acordo com os dados da Receita Federal.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39579883951127)

 Verifique se o dependente está cadastrado no portal do eSocial. Acesse o caminho **"Gestão de Empregados"** (Portal do eSocial). Busque pelo CPF do funcionário, em **"Movimentações Trabalhistas"** clique sobre a última "Alteração Cadastral" e verifique a data de vigência. A data de alteração deve ser igual ou anterior à referência do fechamento (ex: para S-1210 ref 07/2024, a inclusão deve ser consolidada até esta data).

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39579875514903)

 Caso não haja alteração contratual com a data válida no portal do eSocial, gere o evento **"S-2205 - Alteração de Dados Cadastrais do Trabalhador"** com a inclusão do dependente, através da Central do eSocial. 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39579875516183)

  Envie o evento **"S-2205"** para o portal do eSocial e aguarde a confirmação de recebimento com sucesso.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39579875517335)

  Após o envio bem-sucedido do **"S-2205"**, gere novamente o evento **"S-1210"** para o funcionário.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39579883954839)

  Caso o erro persista, verifique se o grau de parentesco do dependente está configurado corretamente. Alguns graus de parentesco podem não gerar as informações necessárias no XML. Nestes casos, ajuste o grau de parentesco para **"Outros"** e inclua a descrição adequada da dependência.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39579875522071)

** CAUSA**

Este erro ocorre porque o dependente não está cadastrado no portal do eSocial ou a data de início de validade da dependência é posterior ao período de referência do evento **"S-1210"**. Outras causas possíveis incluem:
• CPF do dependente inválido perante a Receita Federal;
• Data de início de validade da dependência incompatível com o período de referência do **"S-1210"**;
• Grau de parentesco inadequado que não gera as informações obrigatórias no XML conforme o leiaute do eSocial.