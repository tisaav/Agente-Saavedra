# Um número da faixa já foi utilizado

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043117433-Um-n%C3%BAmero-da-faixa-j%C3%A1-foi-utilizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043117433-Um-n%C3%BAmero-da-faixa-j%C3%A1-foi-utilizado)  
> **ID:** `360043117433` | **Última Atualização:** 2026-07-22T16:07:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505063379351)

 MENSAGEM:**

[241 - Rejeição]: Um número da faixa já foi utilizado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505063382935)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505077032599)

 Identifique se a numeração referente a tentativa de inutilização já foi recebida pela SEFAZ:

- Selecione a nota no respectivo portal  » Botão "**NF-e"**  » "**Consulta situação atual da nota**". Caso seja retornada uma solicitação de atualização do status dessa nota conforme SEFAZ, execute o mesmo. Nesse cenário, a nota não deverá ser inutilizada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505077035031)

 Também é possível através da Chave NF-e do lançamento a ser utilizado realizar a consulta nos Portais Nacional/Estadual da SEFAZ.

Consulta: [SEFAZ Nacional](http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505077037207)

 Realizada a identificação, reavalie a necessidade de inutilização, visto que não é permitido inutilizar numerações de NF-e quando já foram Autorizadas, Canceladas, Denegadas ou quando há um Evento EPEC vinculado a numeração, mesmo que a NF-e ainda não tenha sido autorizada.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505063394071)

 IMPORTANTE:**

A SEFAZ não valida o ambiente, ou seja, se esta numeração já foi emitida em ambiente de Homologação, contendo o mesmo CNPJ, Modelo, Série, Número este erro será apresentado. Pois, a chave da nota não é composta por 'Ambiente' de envio.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16505063398807)

CAUSA:**

Quando for realizada a inutilização de uma numeração já utilizada, será retornada a rejeição.

Não se pode inutilizar numerações de NF-e quando já foram Autorizadas, Canceladas, Denegadas ou quando há um Evento EPEC vinculado a numeração, mesmo que a NF-e ainda não tenha sido autorizada.