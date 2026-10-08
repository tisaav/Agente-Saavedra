# 1046 Rejeição: Percentual de redução de alíquota do Município não é válido para este cClassTrib [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141414273687-1046-Rejei%C3%A7%C3%A3o-Percentual-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-do-Munic%C3%ADpio-n%C3%A3o-%C3%A9-v%C3%A1lido-para-este-cClassTrib-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141414273687-1046-Rejei%C3%A7%C3%A3o-Percentual-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-do-Munic%C3%ADpio-n%C3%A3o-%C3%A9-v%C3%A1lido-para-este-cClassTrib-nItem-999)  
> **ID:** `37141414273687` | **Última Atualização:** 2026-07-22T14:19:23Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141414258327)

 **MENSAGEM**

1046 Rejeição: Percentual de redução de alíquota do Município não é válido para este cClassTrib [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141414259095)

 **SITUAÇÃO**

Esta rejeição é apresentada durante a emissão do documento fiscal quando é informado um percentual de redução de alíquota municipal (pRedAliq) juntamente com a Classificação Tributária (cClassTrib) no IBS Municipal, e o sistema impede o processamento do documento devido à inconsistência entre essas informações.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141397877399)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141397877911)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas  de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o indicador de redução de alíquota (ind_gRed) associado ao CST utilizado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141397879575)

 Caso o CST utilizado não permita redução de alíquota (ind_gRed = 0), remova o percentual de redução de alíquota municipal ou altere para um CST compatível com a redução desejada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141397880343)

 Se o CST permitir redução de alíquota (ind_gRed = 1), na aba **''Tributação''**, seção **''Dados de Tributação'',** no campo **''Cód''**, verifique se o percentual informado é válido para a Classificação Tributária (cClassTrib) utilizada na operação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38126772090135)

 Ajuste o documento fiscal com o percentual de redução de alíquota municipal correto para o CST e cClassTrib utilizados.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141397882775)

 Em caso de compra governamental, certifique-se de que o percentual de redução de alíquota está corretamente informado conforme a legislação aplicável.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141414269975)

 **CAUSA**

A rejeição ocorre devido a uma das seguintes situações:

- 

O CST informado no documento possui um indicador que **exige o uso de Redução de Alíquota** (ind_gRed = 1), mas o percentual de redução informado (pRedAliq) não é válido para a Classificação Tributária (cClassTrib) utilizada.

- 

O CST informado possui um indicador que **veda o uso de Redução de Alíquota** (ind_gRed = 0), mas foi informado um percentual de redução de alíquota municipal maior que zero.

- 

Em operações de compra governamental, o percentual de redução de alíquota municipal não foi informado corretamente conforme as regras específicas para este tipo de operação.

Esta validação faz parte das regras implementadas pela Reforma Tributária (Lei Complementar nº 214/2025) para garantir a correta aplicação das alíquotas do IBS Municipal de acordo com a classificação tributária e o CST utilizados na operação.