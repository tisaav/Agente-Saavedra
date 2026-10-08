# Pedido de Compra continua pendente após faturado totalmente

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/13976871754647-Pedido-de-Compra-continua-pendente-ap%C3%B3s-faturado-totalmente](https://ajuda.sankhya.com.br/hc/pt-br/articles/13976871754647-Pedido-de-Compra-continua-pendente-ap%C3%B3s-faturado-totalmente)  
> **ID:** `13976871754647` | **Última Atualização:** 2026-07-22T14:59:44Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912115788823)

 SITUAÇÃO:**

Pedido de Compra ao ser faturado integralmente utilizando botão **"Faturar"**, mantém o pedido como Pendente: Sim 

Possibilitando novos faturamentos e geração de novas notas sem a mudança do situação do pedido. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912103397783)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912103400343)

 Acesse a tela  **"DBExplorer" ***(Caminho de acesso: **Configurações » Avançado » DBExplorer* Opção Triggers)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15137074396183)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912103402647)

 Verifique se Trigger TRG_INC_UPD_TGFVAR existe no sistema;

 

![GetImage.png](https://ajuda.sankhya.com.br/hc/article_attachments/13976790559895)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912115796631)

 Na inexistência da trigger, atualize o release, observe se trigger será incluída automaticamente no sistema. 

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912138620183)

 Se a inclusão não for bem sucedida, entre em contato com o suporte para análise.