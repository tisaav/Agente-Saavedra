# 1030 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Estadual [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096015764759-1030-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Estadual-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096015764759-1030-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Estadual-nItem-999)  
> **ID:** `37096015764759` | **Última Atualização:** 2026-07-22T14:21:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096007005719)

 **MENSAGEM**

1030 Rejeição: CST do IBS/CBS informado obriga informação de diferimento Estadual [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096015721111)

 **SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e, o documento foi rejeitado pela SEFAZ porque o CST do IBS/CBS utilizado exige a informação de diferimento Estadual, porém este grupo de informações não foi preenchido no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096007009303)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096007015831)

 Acesse a tela ****[''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)** **(Comercial » Consultas » Portal de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096007017495)

 Localize a ''**NF-e''** que apresentou a rejeição.

(Ao selecionar o documento, a Central de Vendas será aberta automaticamente) 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096007020311)

  Na ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)** **(Comercial » Rotinas),  **selecione o item **que recebeu a rejeição. Depois clique no botão **''Outras Opções do Item'' **(ícone de três pontos). Em seguida, selecione a opção **''****Consultar/Alterar Dados do Imposto do Item'' **e identifique o código da alíquota utilizada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096015735319)

 Acesse a tela **"Alíquotas IBS e ou CBS"** (Livros Fiscais » Cadastros » Alíquotas IBS e CBS). Pesquise e selecione a alíquota identificada no passo 3. Na alíquota, verifique o **CST do IBS/CBS** que está sendo utilizado na operação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096015739031)

  Caso esteja sendo usado o CST **'510 - Diferimento' **se torna obrigatório o preenchimento do grupo de diferimento Estadual.

 

![1030 Rejeição CST do IBSCBS informado obriga informação de diferimento Estadual.png](https://ajuda.sankhya.com.br/hc/article_attachments/37962663429271)

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096007026967)

 Assim, preencha o campo **"Percentual de Diferimento"** (pDif) com as informações de diferimento Estadual. O sistema calculará automaticamente o **"Valor do Diferimento"** (vDif) com base na fórmula: vDif = vBC x (pIBSUF / 100) x (pDif / 100) 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096015748247)

 Por outro lado, se não for aplicável o diferimento para esta operação, você pode alterar o **CST do IBS/CBS** para um código que não exija diferimento (com ind_gDif = 0).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37962887341079)

 Após realizar as configurações necessárias, gere o lote e envie novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096007033623)

 **CAUSA**

A rejeição ocorre porque o **Código de Situação Tributária (CST)** do IBS/CBS utilizado na nota fiscal possui um indicador que exige a informação de diferimento Estadual (ind_gDif = 1), conforme regra de validação UB22-20. Quando este indicador está ativo, é obrigatório informar o grupo de diferimento (gIBSUF/gDif) com os dados necessários para o cálculo do valor diferido do IBS Estadual. O diferimento é um mecanismo de postergação do pagamento do imposto, transferindo a responsabilidade para outra etapa da cadeia produtiva. Quando um CST com indicador de diferimento é utilizado, o sistema precisa das informações completas sobre o percentual e valor do diferimento para realizar corretamente os cálculos tributários exigidos pela Reforma Tributária.


---

### 🔗 Links e Referências Internas:

- [''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)