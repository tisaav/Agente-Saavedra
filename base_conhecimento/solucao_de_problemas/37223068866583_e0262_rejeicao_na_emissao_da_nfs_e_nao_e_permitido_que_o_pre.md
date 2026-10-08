# E0262 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao intermediário do serviço.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223068866583-E0262-Rejei%C3%A7%C3%A3o-Na-emiss%C3%A3o-da-NFS-e-n%C3%A3o-%C3%A9-permitido-que-o-prestador-do-servi%C3%A7o-seja-igual-ao-intermedi%C3%A1rio-do-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223068866583-E0262-Rejei%C3%A7%C3%A3o-Na-emiss%C3%A3o-da-NFS-e-n%C3%A3o-%C3%A9-permitido-que-o-prestador-do-servi%C3%A7o-seja-igual-ao-intermedi%C3%A1rio-do-servi%C3%A7o)  
> **ID:** `37223068866583` | **Última Atualização:** 2026-07-22T14:17:04Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223083967511)

 **MENSAGEM**

E0262 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao intermediário do serviço.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223083967767)

 **SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, o sistema identifica que o **CNPJ/CPF do prestador do serviço** é o mesmo do **intermediário do serviço**, resultando na rejeição da nota pela prefeitura.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223068858263)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223083968535)

 Acesse a tela de **emissão da NFS-e** e verifique se há informações de **intermediário do serviço** preenchidas.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38324250108695)

 Caso o serviço **não possua intermediário**, remova as informações do campo **"Intermediário"** ou deixe-o em branco.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38324250110615)

 Se o serviço **realmente possui um intermediário**, certifique-se de que o **CNPJ/CPF informado** seja diferente do CNPJ/CPF da empresa prestadora do serviço.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223068860695)

 Após realizar os ajustes necessários, emita novamente a **NFS-e**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223068863511)

 **CAUSA**

A rejeição ocorre quando o sistema identifica que o **CNPJ/CPF do prestador do serviço** é idêntico ao **CNPJ/CPF do intermediário** informado na NFS-e. De acordo com as regras da prefeitura, **não é permitido que a mesma empresa seja prestadora e intermediária** do serviço simultaneamente, pois isso caracteriza uma inconsistência fiscal. O intermediário deve ser sempre uma **terceira parte** envolvida na operação.