# 1176 Rejeição: Total do IBS estornado difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141617558807-1176-Rejei%C3%A7%C3%A3o-Total-do-IBS-estornado-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141617558807-1176-Rejei%C3%A7%C3%A3o-Total-do-IBS-estornado-difere-da-soma-dos-itens)  
> **ID:** `37141617558807` | **Última Atualização:** 2026-07-22T14:18:57Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141617550487)

 **MENSAGEM**

1176 Rejeição: Total do IBS estornado difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141617550999)

 **SITUAÇÃO**

Ao emitir uma NF-e (modelo 55) ou NFC-e (modelo 65) com estorno de IBS, o sistema identificou que o valor total do IBS estornado informado no grupo de totais da nota fiscal é diferente do somatório dos valores de IBS estornados em cada item da nota.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141617551511)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141601019671)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize a nota rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141617554711)

 Na grade** ''Itens''**, aperte em** ''Outras Opções'' (ícone de três pontos)**, e selecione **''Consultar/Alterar Dados do Imposto do Item''.**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141601022359)

 Na seção **''IBS''**, confira os valores de estornados para cada item. Certifique-se de que os valores estão corretos conforme a legislação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141601022615)

 Verifique se o "**Tipo de Operação - TOP**" (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) está configurado corretamente para calcular o IBS estornado.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141617556247)

 Na aba** ''Impostos''**, seção "**Reforma Tributária**", verifique se o campo **''Tem IBS''** está habilitado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38160524395927)

 Caso esteja realizando o cálculo manual do IBS estornado, some corretamente os valores de IBS estornados de cada item e informe o total exato no rodapé da nota fiscal.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38164004142999)

 Após realizar as correções, inutilize a NF-e rejeitada, exclua-a e emita uma nova nota fiscal com os valores corretos. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141601023767)

 **CAUSA**

Esta rejeição ocorre quando, ao emitir uma **NF-e (modelo 55)** ou NFC-e (modelo 65), o valor total do IBS estornado informado no grupo de totais da nota fiscal é diferente do somatório dos valores de IBS estornados em cada item da nota.

De acordo com as regras de validação da Sefaz, o valor total do IBS estornado deve corresponder exatamente à soma dos valores de IBS estornados de todos os itens da nota fiscal, conforme estabelecido pela Lei Complementar nº 214/2025 que implementa a Reforma Tributária.