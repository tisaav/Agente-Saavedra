# 1104 Rejeição: Valor da Base de cálculo do IBS e CBS difere do somatório dos valores que a compõem [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095955639831-1104-Rejei%C3%A7%C3%A3o-Valor-da-Base-de-c%C3%A1lculo-do-IBS-e-CBS-difere-do-somat%C3%B3rio-dos-valores-que-a-comp%C3%B5em-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095955639831-1104-Rejei%C3%A7%C3%A3o-Valor-da-Base-de-c%C3%A1lculo-do-IBS-e-CBS-difere-do-somat%C3%B3rio-dos-valores-que-a-comp%C3%B5em-nItem-999)  
> **ID:** `37095955639831` | **Última Atualização:** 2026-07-22T14:21:30Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095941078167)

 **MENSAGEM**

1104 Rejeição: Valor da Base de cálculo do IBS e CBS difere do somatório dos valores que a compõem [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095941079959)

 **SITUAÇÃO**

Ao emitir uma **NF-e (modelo 55) **ou **NFC-e (modelo 65) **com a **tributação do IBS e CBS**, o sistema está calculando incorretamente o valor da base de cálculo desses impostos, resultando em uma divergência entre o valor informado no campo vBC (Base de Cálculo) e o somatório dos componentes que deveriam formar essa base.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095941080727)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095941081879)

 Verifique se os valores que compõem a base de cálculo do IBS e CBS estão corretos no documento fiscal.

A base de cálculo deve ser igual ao somatório de:

- 

(+) vProd (Valor do Produto)

- 

(+) vServ (Valor do Serviço) 

- 

(+) vFrete (Valor do Frete) 

- 

(+) vSeg (Valor do Seguro) 

- 

(+) vOutro (Outros Valores) 

- 

(+) vII (Valor do Imposto de Importação) 

- 

(-) vDesc (Valor do Desconto) 

- 

(-) vPIS (Valor do PIS) 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095941082903)

 Acesse a tela de **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a configuração da operação está correta para o cálculo do IBS e CBS.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095955624087)

 Na aba **"Impostos"**, verifique se os parâmetros relacionados à Reforma Tributária estão configurados corretamente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095955626647)

 Acesse a tela **"****Assistente de Configuração Integral da Reforma Tributária****"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se as configurações de tributação estão corretas.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095955628055)

 Verifique o **CST do IBS/CBS **utilizado no documento fiscal. Certifique-se de que o código está correto e compatível com a operação realizada. 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095941086871)

 Recalcule os impostos do documento fiscal para garantir que a base de cálculo do IBS e CBS seja atualizada corretamente. 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095955631255)

 Após realizar as correções necessárias, tente emitir o documento fiscal novamente. 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095955635607)

 **CAUSA**

Esta rejeição ocorre quando o valor informado no campo vBC (Base de Cálculo do IBS e CBS) não corresponde ao somatório dos componentes que devem formar essa base, conforme estabelecido no Art. 346 da LC 214/2025. A base de cálculo do IBS e CBS deve seguir uma fórmula específica, somando valores como o valor do produto, serviço, frete, seguro e outros valores, e subtraindo valores como descontos e PIS.

Quando há divergência nesse cálculo, a SEFAZ rejeita o documento fiscal com a mensagem 1104. É importante ressaltar que esta regra de validação está marcada como **"Implementação Futura, aguardando orientação normativa"**, o que significa que pode haver atualizações ou ajustes na forma como essa validação é aplicada pela SEFAZ no futuro.