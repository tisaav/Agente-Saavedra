# 1076 Rejeição: Total da BC do IBS e da CBS difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37099331628439-1076-Rejei%C3%A7%C3%A3o-Total-da-BC-do-IBS-e-da-CBS-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37099331628439-1076-Rejei%C3%A7%C3%A3o-Total-da-BC-do-IBS-e-da-CBS-difere-da-soma-dos-itens)  
> **ID:** `37099331628439` | **Última Atualização:** 2026-08-17T15:14:30Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099339137815)

 **MENSAGEM**

1076 Rejeição: Total da BC do IBS e da CBS difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099339138455)

 **SITUAÇÃO**

Ao emitir uma NF-e (modelo 55) ou NFC-e (modelo 65), o sistema está calculando incorretamente o valor total da Base de Cálculo do IBS e da CBS no documento fiscal. O valor total informado no grupo de totais da nota está diferente do somatório das bases de cálculo dos itens que compõem o documento, resultando na rejeição pela SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099331618839)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099339140247)

 Verifique os valores da Base de Cálculo do IBS e da CBS em cada item da nota fiscal. Certifique-se de que todos os itens sujeitos à tributação do IBS e da CBS estejam com os valores corretos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099331620375)

 Confira se há algum item com **redução da base de cálculo** ou com **tratamento tributário diferenciado** que possa estar afetando o cálculo total.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099339141783)

 Acesse as telas** ''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique as configurações aplicadas aos produtos da nota fiscal, garantindo que estejam corretamente parametrizadas conforme a Lei Complementar 214/2025.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099331621655)

 Caso esteja lançando os valores manualmente, recalcule o somatório da Base de Cálculo do IBS e da CBS de todos os itens e certifique-se de que este valor seja exatamente igual ao informado no total da nota.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099331622935)

 Verifique se há **arredondamentos** ou **truncamentos** nos cálculos que possam estar causando diferenças entre o somatório dos itens e o total da nota.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099339143319)

 Após realizar as correções necessárias, tente emitir a nota fiscal novamente. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099331625495)

 **CAUSA**

Esta rejeição ocorre quando o valor total da Base de Cálculo do IBS (Imposto sobre Bens e Serviços) e da CBS (Contribuição sobre Bens e Serviços) informado no grupo de totais da NF-e ou NFC-e é diferente do somatório das bases de cálculo dos itens que compõem o documento fiscal. De acordo com as regras de validação da SEFAZ para a Reforma Tributária (Lei Complementar 214/2025), o sistema verifica se há consistência entre os valores declarados nos itens e o total informado no documento.

Quando essa inconsistência é detectada, a nota fiscal é rejeitada para garantir a correta apuração e recolhimento dos novos tributos. Possíveis causas incluem erros de cálculo, problemas de arredondamento, configurações incorretas nas alíquotas do IBS e CBS, ou lançamentos manuais com valores divergentes.