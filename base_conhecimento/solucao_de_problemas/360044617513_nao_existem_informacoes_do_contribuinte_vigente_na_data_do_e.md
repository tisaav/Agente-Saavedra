# Não existem Informações do Contribuinte vigente na data do evento

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617513-N%C3%A3o-existem-Informa%C3%A7%C3%B5es-do-Contribuinte-vigente-na-data-do-evento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617513-N%C3%A3o-existem-Informa%C3%A7%C3%B5es-do-Contribuinte-vigente-na-data-do-evento)  
> **ID:** `360044617513` | **Última Atualização:** 2026-07-22T15:52:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981810079767)

 MENSAGEM:**

[MS1009]: Não existem Informações do Contribuinte vigente na data do evento. Localização:Registro: evtServTom - XPATH: /Reinf/evtServTom

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981810081303)

 SITUAÇÃO:**

Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981810083351)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981810088215)

 Consulte na referência atual, ou em referências anteriores da empresa, o último registro do evento R1000 finalizado;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981810089239)

 Verifique o intervalo entre a Dt. Inicial da Vigência e Dt. Final da Vigência. Caso esteja fora da referência atual é necessário o envio de um evento de alteração do registro R1000;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981810089879)

 Este evento de alteração do registro R1000 pode ser gerado a partir da alteração das datas de início e fim da validade;

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981818869399)

 Para correção, siga os passos abaixo:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458112644375)

 Acesse: Comercial » Preferências » Empresa
Aba:** "EFD-Escrituração Fiscal Digital"**
Tipo de Escrituração: EFD Reinf

Campo **"Data Validade Inicial Reinf":** informe data posterior a registrada no Dt. Final da Vigência o último evento R1000 com status finalizado.

 

**Exemplo:**

Caso o ultimo evento R1000 com status finalizado para a empresa esteja com o Dt. Final da Vigência igual a '31/07/2018', informar no campo Data Validade Inicial Reinf das preferências da empresa a data '01/08/2018'.

Campo **"Data Validade Final Reinf":** deixar vazio

Isso fará com que o sistema gere um registro de alteração para o evento R1000, fazendo com que a Dt. Inicial de Vigência e Dt. Final da Vigência fiquem compatíveis com referência atual.

 

Transmita novamente o R1000.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981818871831)

 CAUSA:**

O evento R1000 é enviado apenas uma vez, quando ocorrer alguma alteração nos registros o R1000 é enviado novamente com o Tipo de Envio Alteração.
Pode ocorrer de ter enviado as informações do período anterior e estar preenchido Data Inicial da Vigência e Data Final da Vigência, com isso os dados constará na Receita(R1000) fechado.