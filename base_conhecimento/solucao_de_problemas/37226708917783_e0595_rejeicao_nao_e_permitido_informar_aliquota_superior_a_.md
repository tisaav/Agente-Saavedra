# E0595 Rejeição: Não é permitido informar alíquota superior a 5%.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226708917783-E0595-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-superior-a-5](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226708917783-E0595-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-superior-a-5)  
> **ID:** `37226708917783` | **Última Atualização:** 2026-07-22T14:14:43Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226708905879)

 **MENSAGEM**

E0595 Rejeição: Não é permitido informar alíquota superior a 5%.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226708909335)

 **SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e com operações sujeitas à **tributação do IBS e CBS**, o documento fiscal foi rejeitado pela SEFAZ apresentando a mensagem de erro informando que **não é permitido informar alíquota superior a 5%**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226692536599)

 **SOLUÇÃO**

Para resolver esta rejeição, é necessário **ajustar as alíquotas cadastradas** no sistema, garantindo que estejam em conformidade com os limites estabelecidos pela legislação. Siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226692536983)

 Acesse a tela **"Alíquota IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota CBS" **(Livros Fiscais » Cadastros » Aliquotas de CBS). ** **

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226692537623)

 Localize o cadastro de alíquota que está sendo utilizado na operação fiscal que gerou a rejeição.

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37622263878167)

 **Verifique os campos **"Alíquota IBS (%)"** e **"Alíquota CBS (%)"** cadastrados para a operação:

- 

Certifique-se de que **nenhuma das alíquotas informadas seja superior a 5%**;

- 

Caso identifique alíquota acima do limite permitido, ajuste o percentual para um valor **igual ou inferior a 5%.**

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226692540183)

 **Na aba **''Tributação''**, seção **''Dados de tributação''**, verifique também o **"Código de situação tributária - CST"** associado à operação, pois determinados CSTs possuem **restrições específicas quanto ao percentual de alíquota** que pode ser informado.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226708914071)

 Após realizar os ajustes, **salve as alterações** no cadastro de alíquota.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38293990081047)

 Retorne ao documento fiscal e **reemita a NF-e ou NFC-e** com as alíquotas corrigidas.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226708914711)

 **CAUSA**

A rejeição ocorre porque a **SEFAZ identificou que a alíquota informada no documento fiscal excede o limite máximo de 5%** estabelecido pela legislação para determinadas operações ou situações tributárias específicas relacionadas ao **IBS e CBS**. Esta validação visa garantir que as operações fiscais estejam em conformidade com as **regras da Reforma Tributária** previstas na Lei Complementar nº 214/2025, que estabelece limites e condições para a aplicação das alíquotas dos novos tributos.