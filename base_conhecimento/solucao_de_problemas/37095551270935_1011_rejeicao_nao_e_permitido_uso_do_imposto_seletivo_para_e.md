# 1011 Rejeição: Não é permitido uso do Imposto Seletivo para esta classificação da operação [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095551270935-1011-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-uso-do-Imposto-Seletivo-para-esta-classifica%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095551270935-1011-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-uso-do-Imposto-Seletivo-para-esta-classifica%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-nItem-999)  
> **ID:** `37095551270935` | **Última Atualização:** 2026-07-22T14:21:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095536427159)

 **MENSAGEM**

1011 Rejeição: Não é permitido uso do Imposto Seletivo para esta classificação da operação [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095551240983)

 **SITUAÇÃO**

Esta rejeição ocorre quando o usuário tenta emitir uma NF-e ou NFC-e incluindo o grupo de Imposto Seletivo (IS) para um item cuja classificação tributária não permite a aplicação deste imposto. O sistema da Sefaz identifica uma incompatibilidade entre a classificação tributária do Imposto Seletivo (cClassTribIS) informada no documento fiscal e a utilização do grupo IS.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095536430231)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095551243415)

 Verifique a classificação tributária do Imposto Seletivo (cClassTribIS) utilizada no item rejeitado e confirme se este produto realmente deve ser tributado pelo Imposto Seletivo.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095536432279)

 Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e localize o produto que gerou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095536434583)

 Na aba **''Impostos''**, verifique se o campo **''NCM''** está informado corretamente conforme o produto, e se este NCM está sujeito á tributação do Imposto Seletivo conforme a legislação vigente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095551247127)

 Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária), e verifique as configurações de tributação do **Imposto Seletivo** para o produto em questão.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095551249431)

 Caso o produto não deva ser tributado pelo Imposto Seletivo, remova o grupo IS da nota fiscal, ajustando a configuração tributária do item.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095551256343)

 Se o produto deve ser tributado pelo Imposto Seletivo, verifique se a classificação tributária (cClassTribIS) está corretamente configurada de acordo com a operação realizada.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095551259159)

 Após realizar os ajustes necessários, tente emitir a nota fiscal novamente.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095551263127)

 **CAUSA**

Esta rejeição ocorre devido à implementação das regras de validação da Reforma Tributária (Lei Complementar nº 214/2025), especificamente a regra **UB01-10**, que verifica a compatibilidade entre a classificação tributária do Imposto Seletivo (cClassTribIS) e a aplicação deste imposto no documento fiscal.

O Imposto Seletivo (IS) é aplicável apenas a produtos específicos, conforme determinado pela legislação. Quando o sistema identifica que o grupo IS foi informado para um item cuja classificação tributária não permite a aplicação deste imposto, a nota é rejeitada.

A causa específica é a tentativa de utilizar o grupo de Imposto Seletivo (IS) para uma classificação tributária (cClassTribIS) que não está habilitada para receber este tipo de tributação, gerando incompatibilidade entre a classificação informada e a aplicação do imposto.