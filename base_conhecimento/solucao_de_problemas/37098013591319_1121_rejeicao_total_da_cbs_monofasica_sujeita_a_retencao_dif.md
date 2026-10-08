# 1121 Rejeição: Total da CBS monofásica sujeita a retenção difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098013591319-1121-Rejei%C3%A7%C3%A3o-Total-da-CBS-monof%C3%A1sica-sujeita-a-reten%C3%A7%C3%A3o-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098013591319-1121-Rejei%C3%A7%C3%A3o-Total-da-CBS-monof%C3%A1sica-sujeita-a-reten%C3%A7%C3%A3o-difere-da-soma-dos-itens)  
> **ID:** `37098013591319` | **Última Atualização:** 2026-07-22T14:20:23Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098013570455)

 **MENSAGEM**

1121 Rejeição: Total da CBS monofásica sujeita a retenção difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098013573655)

 **SITUAÇÃO**

A nota fiscal foi emitida com divergência entre o valor total da CBS monofásica sujeita à retenção informado no rodapé do documento e os valores de CBS monofásica sujeita à retenção registrados nos itens da nota.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098026512663)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098026513431)

 Acesse a tela** ''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e verifique os valores da CBS monofásica sujeita a retenção em cada item da nota fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098013577751)

 Na grade **''Itens''**, clique em **''Outras Opções''** (ícone com três pontos) e selecione **''Consultar/Alterar Dados do Imposto do Item...''**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098026514839)

 Para cada item, verifique o valor da CBS monofásica sujeita a retenção (campo **"vCBSMonoReten"**) na aba **"Tributação"** ou **"IBS/CBS"** de cada item.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098026517911)

 Certifique-se de que o valor total da CBS monofásica sujeita a retenção no rodapé da nota (campo **"vCBSMonoReten"** no grupo **"IBSCBSTot"**) corresponde à soma dos valores de **"vCBSMonoReten"** de todos os itens.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098013584151)

 Caso haja divergência, verifique a configuração das alíquotas da CBS monofásica na tela **''Produtos'' **(Configurações » Cadastros » Produtos » Produtos) e nas telas **''Alíquotas IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38044118841495)

 Corrija os valores da CBS monofásica sujeita a retenção nos itens ou no total da nota, conforme necessário, para que o somatório dos valores dos itens seja igual ao valor total informado no rodapé da nota.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098013586583)

 Após as correções, reenvie a nota fiscal para processamento. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098013587735)

 **CAUSA**

A rejeição ocorre devido a uma inconsistência no cálculo da CBS monofásica sujeita a retenção. De acordo com as regras de validação da Sefaz, o valor total da CBS monofásica sujeita a retenção informado no rodapé da nota fiscal (campo **vCBSMonoReten** no grupo **IBSCBSTot**) deve ser exatamente igual à soma dos valores da CBS monofásica sujeita a retenção de cada item da nota (campo **vCBSMonoReten** de cada item).

Esta validação é parte das regras implementadas pela Lei Complementar 214/2025 para a Reforma Tributária, que estabelece a correta apuração e retenção da CBS monofásica. A divergência pode ocorrer devido a erros de arredondamento, configurações incorretas nas alíquotas ou problemas no cálculo automático dos valores.