# Erro no cálculo do IR: dedução simplificada e INSS somados incorretamente

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39324144057623-Erro-no-c%C3%A1lculo-do-IR-dedu%C3%A7%C3%A3o-simplificada-e-INSS-somados-incorretamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39324144057623-Erro-no-c%C3%A1lculo-do-IR-dedu%C3%A7%C3%A3o-simplificada-e-INSS-somados-incorretamente)  
> **ID:** `39324144057623` | **Última Atualização:** 2026-07-29T13:22:38Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39324144037783)

 **MENSAGEM**

Durante a conferência da folha de pagamento, nota-se que o sistema calcula o IRRF de forma incorreta. A dedução simplificada de R$ 607,20 é aplicada juntamente ao valor do INSS, resultando em uma base de cálculo incorreta e em um desconto de IRRF diferente do devido.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39324127500695)

 **SITUAÇÃO**

Ao processar o **Cálculo da Folha de Pagamento** (Pessoal+ > Cálculo > Individual/Coletivo ), o sistema apresenta divergência no valor do IRRF descontado do colaborador. A base de cálculo é formada incorretamente, pois, após aplicar a dedução simplificada, o sistema soma o valor do INSS às deduções, gerando uma base de cálculo do IRRF incorreta e, consequentemente, um valor de desconto divergente do esperado.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39324144039063)

 **SOLUÇÃO**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39324144040087)

 Verifique se o evento de desconto de IRRF está configurado corretamente. Na tela **Eventos**, confirme se ele está ativo na aba **Padrões** e possui a característica **IRRF**..

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39324144040855)

 Atualize o **Módulo Pessoal +** para a versão mais recente, caso haja atualização disponível.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39324127503383)

 Verifique se as **Tabelas de IRRF** estão cadastradas corretamente no sistema, com os valores vigentes para o período de competência.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39324127507991)

 Confira se as **Fórmulas de Cálculo** estão parametrizadas de acordo com o padrão Sankhya, especialmente aquelas que tratam das características **DESCONTOSIMPLIFICADO** e **INSS**.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39324144045719)

 Confirme se os eventos de INSS (101), Desconto Simplificado (202) e Dependentes - IRRF (176) possuem as identificações corretas.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39324127510039)

 Caso esses eventos não estejam configurados para impressão nos documentos, marque-os para imprimir em todos os documentos. Para isso, acesse cada um dos eventos (INSS, Desconto Simplificado e Dependentes - IRRF) e, na parte superior da tela, configure o campo **"Imprime em:"** conforme necessário.
 

Por fim, recalcule as folhas que realizam recomposição para que os ajustes sejam considerados e, em seguida, confira novamente a folha de pagamento, validando principalmente a base de cálculo do IRRF e as deduções aplicadas.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39324144047255)

 **CAUSA**

A divergência pode ocorrer devido a uma inconsistência na fórmula de cálculo do IRRF em versões anteriores do **Módulo Pessoal +** ou por identificações incorretas dos eventos, impedindo que os valores sejam processados conforme o padrão esperado. Como consequência, a fórmula pode considerar indevidamente valores que deveriam apenas ser comparados para deduzi-los durante a composição da base de cálculo do IRRF.

Adicionalmente, parametrizações incorretas nas **Tabelas de Faixa do INSS** ou nas fórmulas de eventos relacionados à recomposição do cálculo do IRRF também podem resultar em valores incorretos para as variáveis utilizadas no processamento.