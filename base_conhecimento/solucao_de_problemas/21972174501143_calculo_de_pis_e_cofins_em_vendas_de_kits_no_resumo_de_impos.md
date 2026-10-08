# Cálculo de PIS e COFINS em Vendas de (KITS) no Resumo de Impostos

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/21972174501143-C%C3%A1lculo-de-PIS-e-COFINS-em-Vendas-de-KITS-no-Resumo-de-Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/21972174501143-C%C3%A1lculo-de-PIS-e-COFINS-em-Vendas-de-KITS-no-Resumo-de-Impostos)  
> **ID:** `21972174501143` | **Última Atualização:** 2026-07-22T14:49:40Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21976562809239)

 **SITUAÇÃO:**

Ao analisar os impostos de uma nota, percebe se que os valores dos impostos PIS/COFINS estão com base de cálculo "Duplicada" ou seja aparentemente sendo uma falha.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21972169864215)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21976529893399)

  No caso da venda de kits é que os impostos sejam calculados apenas para os componentes do kit, e não para ele em si. 

A rotina **"Resumo de Impostos"** nas outras opções da Nota, apresentará o valor das bases  e valores dos impostos, se houver o cálculo dos impostos tanto para o KIT, quanto para o COMPONENTE, ficará duplicada conforme comportamento do sistema, visto que lá estará sendo realizada a "Soma de todas as sequências da tabela".

Entretanto, ao verificar os de impostos na TGFDIN ''Consultar alterar dados dos impostos" será trago a base corretamente do itens, de forma separadas, e também será levado ao XML corretamente. 

![Cabeçalho 11-03.png](https://ajuda.sankhya.com.br/hc/article_attachments/21976839348375)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21976839354903)

 Sobre o parâmetro** "****Calcular Impostos para Matéria Prima ****- CALCIMPMP"** voltado para (ICMS/ST/IPI), o mesmo não faz impacto neste processo pois aqui estará sendo utilizado o parâmetro  **"Configuração para Kit Independente - CONFKITIND"**, e com isso as outras parametrizações deixarão de ser consideradas pelo sistema. 
 
Para mais informações desta rotina: [Configuração de Kit](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit)


---

### 🔗 Links e Referências Internas:

- [Configuração de Kit](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit)