# E0121 Rejeição: O nome ou razão social do prestador não deve ser informado quando o emitente da DPS for o próprio prestador.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222173264407-E0121-Rejei%C3%A7%C3%A3o-O-nome-ou-raz%C3%A3o-social-do-prestador-n%C3%A3o-deve-ser-informado-quando-o-emitente-da-DPS-for-o-pr%C3%B3prio-prestador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222173264407-E0121-Rejei%C3%A7%C3%A3o-O-nome-ou-raz%C3%A3o-social-do-prestador-n%C3%A3o-deve-ser-informado-quando-o-emitente-da-DPS-for-o-pr%C3%B3prio-prestador)  
> **ID:** `37222173264407` | **Última Atualização:** 2026-07-22T14:18:03Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222173251735)

 **MENSAGEM**

E0121 Rejeição: O nome ou razão social do prestador não deve ser informado quando o emitente da DPS for o próprio prestador.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222157287959)

 **SITUAÇÃO**

Mensagem apresentada ao emitir uma **DPS-e (Declaração de Prestação de Serviços eletrônica)** em que o **emitente do documento é o próprio prestador do serviço**, mas foram informados dados do prestador no grupo de informações específico, gerando inconsistência na validação da Sefaz.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222157289879)

 **SOLUÇÃO**

Para resolver esta rejeição, **não informe o nome ou razão social do prestador** quando o emitente da DPS-e for o próprio prestador do serviço. Siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222173254039)

 Acesse a tela **''Central de Vendas'' **(Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222173254935)

 Verifique se o **emitente do documento é o próprio prestador** do serviço.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222157294359)

 Certifique-se de que o campo **"Empresa" **esteja **vazio ou não preenchido** no grupo de informações do prestador.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222157295511)

 Caso o campo esteja preenchido, **remova as informações** do nome ou razão social do prestador.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222157296407)

 Salve as alterações e **emita novamente a DPS-e**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222157297431)

 **CAUSA**

A rejeição ocorre quando, na emissão da **DPS-e**, o sistema identifica que o **emitente do documento é o próprio prestador do serviço**, mas o campo de **nome ou razão social do prestador foi preenchido** no grupo de informações específico. Conforme as **regras de validação da Sefaz** estabelecidas pela **Lei Complementar nº 214/2025**, quando o emitente é o próprio prestador, **não deve haver duplicidade de informações**, e os dados do prestador não devem ser informados separadamente, evitando inconsistências no documento fiscal eletrônico.