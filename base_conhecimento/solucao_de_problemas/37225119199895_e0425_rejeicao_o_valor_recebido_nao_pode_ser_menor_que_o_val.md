# E0425 Rejeição: O valor recebido não pode ser menor que o valor do serviço informado na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225119199895-E0425-Rejei%C3%A7%C3%A3o-O-valor-recebido-n%C3%A3o-pode-ser-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225119199895-E0425-Rejei%C3%A7%C3%A3o-O-valor-recebido-n%C3%A3o-pode-ser-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS)  
> **ID:** `37225119199895` | **Última Atualização:** 2026-07-22T14:16:10Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225101546647)

 **MENSAGEM**

E0425 Rejeição: O valor recebido não pode ser menor que o valor do serviço informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225101547031)

 **SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)**, o usuário informou um **valor recebido inferior ao valor total do serviço** prestado. Esta inconsistência entre os valores fez com que o documento fosse **rejeitado pela Sefaz** com a mensagem de erro E0425.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225119192471)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225119193495)

 Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize o documento que foi rejeitado.

- 

Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas''**** **(Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225101549335)

 Na grade **''Rodapé''** verifique o campo **''****Valor do Serviço''** informando o **valor total do serviço **no documento.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225101549975)

 Na aba **''Financeiro''**, verifique o campo **''Vlr. do Desdobramento'' **e confira o **valor recebido** informado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225101550871)

 Ajuste o **valor recebido** para que seja **igual ou maior** que o valor total do serviço prestado, considerando: 

- 

Se o pagamento foi realizado integralmente, informe o **valor total do serviço**;

- 

Se houver **troco**, certifique-se de que o valor recebido seja maior que o valor do serviço e informe corretamente o valor do troco;

- 

Se o pagamento for **parcial**, verifique se este tipo de operação está permitido para DPS.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225101551127)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225119195287)

 Realize novamente a **transmissão do documento** para a Sefaz.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225119195799)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida** que o valor recebido pelo serviço prestado **não pode ser inferior** ao valor total do serviço informado no Documento de Prestação de Serviços. Esta validação garante a **consistência fiscal** e evita que sejam emitidos documentos com valores de recebimento incompatíveis com o valor da prestação do serviço, o que poderia caracterizar **inconsistência tributária**.