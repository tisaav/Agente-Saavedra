# 1123 Rejeição: Total da CBS monofásica retida anteriormente difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098046485143-1123-Rejei%C3%A7%C3%A3o-Total-da-CBS-monof%C3%A1sica-retida-anteriormente-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098046485143-1123-Rejei%C3%A7%C3%A3o-Total-da-CBS-monof%C3%A1sica-retida-anteriormente-difere-da-soma-dos-itens)  
> **ID:** `37098046485143` | **Última Atualização:** 2026-07-22T14:20:22Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098046474007)

 **MENSAGEM**

1123 Rejeição: Total da CBS monofásica retida anteriormente difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098038421783)

 **SITUAÇÃO**

A nota fiscal foi emitida com divergência entre o valor total da CBS monofásica retida anteriormente informado no rodapé do documento e os valores de CBS monofásica retida anteriormente registrados nos itens da nota.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098038422423)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098046476695)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e verifique os valores da CBS monofásica retida anteriormente em cada item da nota fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098038423831)

 Selecione a nota fiscal rejeitada e clique na aba **"Itens"** para visualizar todos os itens da nota.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098038426775)

 Para cada item que possui tributação monofásica, verifique o valor informado no campo **"vCBSMonoRet"** (valor da CBS monofásica retida anteriormente).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098046478615)

 Calcule manualmente a soma de todos os valores de **"vCBSMonoRet"** de cada item e compare com o valor total informado no rodapé da nota (campo **"vCBSMonoRet"** do grupo **"IBSCBSTot"**).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098038428567)

 Caso identifique divergências, corrija os valores da CBS monofásica retida anteriormente em cada item ou ajuste o valor total no rodapé da nota, garantindo que o somatório dos itens seja igual ao valor total informado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37991223837847)

 Acesse a tela **''Alíquota de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se a configuração do ''Código de Situação Tributária'' (CST) está correto para cada item.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098038429847)

 Certifique-se de que os itens que possuem tributação monofásica retida anteriormente estejam utilizando um CST que permita essa informação (verifique o indicador **"ind_gMonoRet"** associado ao CST).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098046481815)

 Após realizar as correções necessárias, recalcule os impostos da nota fiscal e tente emitir novamente o documento. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098046482583)

 **CAUSA**

A rejeição 1123 ocorre devido a uma inconsistência no cálculo da CBS monofásica retida anteriormente. Conforme a regra de validação UB105-10 da SEFAZ, o valor total da CBS monofásica do item (vTotCBSMonoItem) deve ser resultante da fórmula: vTotCBSMonoItem = vCBSMono + vCBSMonoReten - vCBSMonoDif.

Esta inconsistência pode ocorrer por diversos motivos:

• Erro no cálculo automático dos valores da CBS monofásica retida anteriormente;

• Alteração manual incorreta dos valores em algum item da nota;

• Utilização de CST inadequado para a operação, que não permite a informação de tributação monofásica retida anteriormente (conforme regras UB94-10 e UB94-20);

• Falha na totalização dos valores no rodapé da nota fiscal.

A validação é exigida pela Lei Complementar 214/2025, que estabelece as regras para a tributação monofásica no âmbito da Reforma Tributária, garantindo a correta apuração e recolhimento da CBS.