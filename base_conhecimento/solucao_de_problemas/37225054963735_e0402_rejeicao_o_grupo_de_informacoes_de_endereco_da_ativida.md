# E0402 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior deve ser informado quando o país do local da prestação for informado na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225054963735-E0402-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-da-atividade-de-evento-ocorrido-no-exterior-deve-ser-informado-quando-o-pa%C3%ADs-do-local-da-presta%C3%A7%C3%A3o-for-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225054963735-E0402-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-da-atividade-de-evento-ocorrido-no-exterior-deve-ser-informado-quando-o-pa%C3%ADs-do-local-da-presta%C3%A7%C3%A3o-for-informado-na-DPS)  
> **ID:** `37225054963735` | **Última Atualização:** 2026-07-22T14:16:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071081495)

 **MENSAGEM**

E0402 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior deve ser informado quando o país do local da prestação for informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225054951319)

 **SITUAÇÃO**

Ao tentar emitir uma **Declaração de Prestação de Serviços (DPS)** para um tomador localizado no exterior, o sistema apresenta a rejeição E0402, indicando que **faltam informações obrigatórias do endereço** da atividade realizada fora do Brasil.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071085335)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071086103)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **tomador do serviço** que está no exterior.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071086615)

 Verifique se o campo **"País"** está preenchido corretamente no cadastro do endereço do parceiro.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225054955159)

 Acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços » Cidades) e valide se o **nome da cidade** está cadastrado corretamente:

- 

Caso a prestação seja no exterior, certifique-se de que a cidade esteja vinculada ao **país correto**;

- 

Verifique se o **nome da cidade** está de acordo com o padrão internacional ou conforme exigido pela legislação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071091479)

 Na emissão da **DPS**, certifique-se de que o campo **"Local de Tributação"** esteja configurado como **"Exterior"**:

- 

Esta opção deve ser selecionada quando a **prestação de serviço e/ou o tomador** encontrar-se no exterior;

- 

No XML, a tag **<Tributacao>** será preenchida com o valor **"E"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071091863)

  Preencha o **grupo de informações de endereço da atividade** no documento fiscal, informando:

- 

**Endereço completo** do local onde o serviço foi prestado no exterior;

- 

**País** onde ocorreu a prestação do serviço;

- 

Demais informações exigidas pela legislação para eventos ocorridos fora do Brasil.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071092887)

 Após realizar os ajustes necessários, **redigite algum item** no cabeçalho da nota fiscal para que o sistema atualize as informações.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225071093783)

 Gere o **lote da DPS** novamente e transmita o documento para a Sefaz.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225054959127)

 **CAUSA**

A rejeição ocorre quando a **Declaração de Prestação de Serviços (DPS)** é emitida para um tomador localizado no exterior e o **grupo de informações de endereço da atividade** não foi preenchido corretamente. Conforme a legislação da **Reforma Tributária (Lei Complementar nº 214/2025)**, quando o **país do local da prestação** for informado na DPS, é obrigatório detalhar o **endereço completo** onde o evento ocorreu no exterior, incluindo país, cidade e demais dados do local da prestação do serviço.