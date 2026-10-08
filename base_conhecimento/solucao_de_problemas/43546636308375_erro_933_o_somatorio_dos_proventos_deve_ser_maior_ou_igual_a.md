# Erro 933 - O somatório dos Proventos deve ser maior ou igual ao somatório dos Descontos no Demonstrativo de Pagamento

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43546636308375-Erro-933-O-somat%C3%B3rio-dos-Proventos-deve-ser-maior-ou-igual-ao-somat%C3%B3rio-dos-Descontos-no-Demonstrativo-de-Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/43546636308375-Erro-933-O-somat%C3%B3rio-dos-Proventos-deve-ser-maior-ou-igual-ao-somat%C3%B3rio-dos-Descontos-no-Demonstrativo-de-Pagamento)  
> **ID:** `43546636308375` | **Última Atualização:** 2026-09-18T11:30:07Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546666555287)

 **MENSAGEM**

[933] O somatório dos Proventos deve ser maior ou igual ao somatório dos Descontos no Demonstrativo de Pagamento 

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546666555927)

 **SITUAÇÃO**

O erro 933 ocorre quando, ao processar a folha de pagamento ou enviar informações ao eSocial, o sistema identifica que o total dos proventos (valores a receber, como salários, adicionais, etc.) é menor do que o total dos descontos (valores a pagar, como INSS, IRRF, pensão, etc.) no demonstrativo de pagamento do colaborador. Isso faz com que a remuneração líquida fique negativa, o que não é permitido pelas regras do eSocial e da legislação trabalhista.

 

**Por que isso acontece?**

- Algum evento de provento não está sendo considerado corretamente no eSocial.

- Algum evento de desconto está sendo considerado indevidamente.

- A soma de dois ou mais eventos resulta em diferença negativa.

- Eventos de provento não estão marcados para compor o eSocial.

 

 

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546666557463)

 Acesse o movimento do mês do colaborador na tela Pessoal+ » Rotinas Folha » Gerenciador de Folhas **"**  e confira se existe algum evento com valor que justifique a diferença entre proventos e descontos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546666558615)

 Verifique se a soma de dois ou mais eventos resulta no valor da diferença apresentada, caso não localize a divergência em um único item.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546636300567)

 Analise evento por evento, conferindo valores, incidências e se estão corretamente classificados como provento ou desconto. Pessoal+ » Cadastros » Eventos

- Localize cada evento utilizado no movimento do colaborador.

- Na aba **Propriedades**, confira se a opção **"Compõe eSocial"** está marcada para todos os eventos de provento que devem ser considerados.

- Se algum evento de provento não estiver marcado, marque a opção e salve.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546666560535)

 Recalcule a folha

1. Após ajustar os eventos, recalcule a folha de pagamento do colaborador.

1. Verifique se o erro persiste.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546636301975)

 Ajuste a configuração do tipo de rubrica para **"Informativa dedutora"** caso identifique que algum evento de desconto está classificado incorretamente no eSocial e realize nova geração do evento S-1200.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546636303255)

 Gere novamente o evento S-1200 e envie ao eSocial. Caso o erro persista, revise a tabela de rubricas no portal do eSocial e, se necessário, envie uma retificação do evento S-1010 para corrigir a natureza da rubrica.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546636304151)

 **Resumo dos Pontos de Atenção**

1. O total de proventos deve ser sempre maior ou igual ao total de descontos.

1. Todos os eventos de provento relevantes precisam estar configurados para compor o eSocial.

1. Analise evento por evento para identificar possíveis inconsistências.

1. Manter a integridade dos dados evita rejeições e problemas legais.