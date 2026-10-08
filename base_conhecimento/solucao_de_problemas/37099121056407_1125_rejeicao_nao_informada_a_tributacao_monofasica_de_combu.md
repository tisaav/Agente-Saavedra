# 1125 Rejeição: Não informada a Tributação Monofásica de Combustível [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37099121056407-1125-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37099121056407-1125-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-nItem-999)  
> **ID:** `37099121056407` | **Última Atualização:** 2026-07-22T14:20:00Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099121044631)

 **MENSAGEM**

1125 Rejeição: Não informada a Tributação Monofásica de Combustível [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099150469271)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida para produto classificado como combustível sujeito à Tributação Monofásica, porém o grupo de Tributação Monofásica de Combustível não foi informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099121046551)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099121047447)

 Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se a Classificação ICMS está configurado para um código que exige tributação monofásica de combustível.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099121048599)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a TOP utilizada está configurada corretamente para operações com combustíveis.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38364654915991)

 Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099150476823)

 Configure corretamente as alíquotas para tributação monofásica de combustíveis, verificando se o indicador **"ind_gMonoPadrao"** está configurado como 1 (exige tributação monofásica).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38364649853719)

 Ao emitir a nota fiscal, certifique-se de que o grupo de tributação monofásica (id: UB84a) esteja sendo informado corretamente para os itens de combustível, conforme exigido pelo Art. 172 da LC 214/2025.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099121051159)

 **CAUSA**

A rejeição 1125 ocorre devido à **ausência do grupo de tributação monofásica** (id: UB84a) em um documento fiscal que contém itens classificados como combustíveis. De acordo com a regra de validação UB84a-10, quando o indicador **ind_gMonoPadrao** está configurado como 1 na classificação tributária do produto, é **obrigatória** a informação da tributação monofásica, conforme estabelecido no Art. 172 da LC 214/2025. Esta validação é aplicada tanto para NF-e (modelo 55) quanto para NFC-e (modelo 65).