# E0574 Rejeição: O valor monetário do benefício municipal informado na DPS não pode ser superior ao valor do serviço.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226421941143-E0574-Rejei%C3%A7%C3%A3o-O-valor-monet%C3%A1rio-do-benef%C3%ADcio-municipal-informado-na-DPS-n%C3%A3o-pode-ser-superior-ao-valor-do-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226421941143-E0574-Rejei%C3%A7%C3%A3o-O-valor-monet%C3%A1rio-do-benef%C3%ADcio-municipal-informado-na-DPS-n%C3%A3o-pode-ser-superior-ao-valor-do-servi%C3%A7o)  
> **ID:** `37226421941143` | **Última Atualização:** 2026-07-22T14:15:00Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226421923095)

 **MENSAGEM**

E0574 Rejeição: O valor monetário do benefício municipal informado na DPS não pode ser superior ao valor do serviço.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437621399)

 **SITUAÇÃO**

Rejeição apresentada na emissão de uma NFS-e quando a DPS é informada com um benefício fiscal municipal cujo valor monetário é maior que o valor total do serviço declarado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437622167)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437622935)

 Acesse a tela** ''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal que está sendo rejeitada.

- 

Ao selecionar a nota fiscal, ela será aberta automaticamente, direcionando o usuário para a tela **''Central de Vendas''**** **(Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437623703)

 Na grade **''Rodapé''**, na aba **''Totais''**, verifique o campo **''Valor do serviço''** informando o valor total do serviço na nota fiscal.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437624599)

 Verifique o **valor monetário do benefício municipal** que está sendo informado na DPS e certifique-se de que este valor **não seja superior ao valor do serviço**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437626263)

 Caso o valor do benefício esteja incorreto, ajuste-o para um valor **igual ou inferior ao valor do serviço** prestado.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226421932311)

 Revise as **configurações de benefícios fiscais municipais** cadastradas no sistema para garantir que estejam corretas e de acordo com a legislação municipal vigente.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437628823)

 Após realizar os ajustes necessários, tente **emitir novamente a NFS-e**. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226437630231)

 **CAUSA**

A rejeição ocorre porque foi informado um **valor de benefício fiscal municipal** que **excede o valor total do serviço** prestado. A Sefaz possui uma regra de validação que impede que o benefício fiscal seja maior do que a base de cálculo sobre a qual ele incide, garantindo a **consistência tributária** e evitando inconsistências nos valores declarados na DPS.