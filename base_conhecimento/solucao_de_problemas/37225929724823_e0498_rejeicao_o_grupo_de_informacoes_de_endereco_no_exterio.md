# E0498 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o fornecedor for identificado pelo NIF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225929724823-E0498-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-fornecedor-for-identificado-pelo-NIF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225929724823-E0498-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-fornecedor-for-identificado-pelo-NIF)  
> **ID:** `37225929724823` | **Última Atualização:** 2026-07-22T14:15:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225946112791)

 **MENSAGEM**

E0498 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o fornecedor for identificado pelo NIF.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929708695)

 **SITUAÇÃO**

Ao emitir um documento fiscal (NF-e ou NFC-e) para um **fornecedor estrangeiro** que foi identificado pelo **NIF (Número de Identificação Fiscal)**, o sistema rejeitou a nota porque **as informações de endereço no exterior não foram preenchidas** no cadastro do parceiro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929710231)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225946118807)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **fornecedor estrangeiro** que está sendo utilizado no documento fiscal rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929713175)

 Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o número do NIF ou documento equivalente.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929713559)

 Na aba **''Fiscal''**, seção** ''Informações para REINF''**, verifique se o campo **''Indicativo do NIF''** está configurado com a opção **''Beneficiário com NIF''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929714455)

 Preencha obrigatoriamente o campo **"Nro. do NIF – Número de Identificação Fiscal"** com o número fornecido pelo órgão de administração tributária do país de origem do fornecedor.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225946120599)

 Na aba** ''Endereço''**, preencha as **informações completas do endereço no exterior**, incluindo: 

- 

Logradouro

- 

Número

- 

Complemento (se houver)

- 

Bairro

- 

Cidade

- 

País

- 

Código Postal

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929716375)

  Certifique-se de que o campo **"UF"** do endereço esteja configurado como **"EX"** (Exterior).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929716759)

  Salve as alterações realizadas no cadastro do parceiro.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225946122007)

 Retorne ao documento fiscal rejeitado e realize uma **nova tentativa de transmissão** para a SEFAZ. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225929719447)

 **CAUSA**

A rejeição ocorre porque a **SEFAZ exige que, quando um fornecedor estrangeiro for identificado pelo NIF** (Número de Identificação Fiscal), o **grupo de informações de endereço no exterior seja obrigatoriamente preenchido** no documento fiscal.

Esta é uma **regra de validação da SEFAZ** para garantir a correta identificação e rastreabilidade de operações com parceiros internacionais. Sem o endereço completo no exterior, o documento não pode ser validado e é rejeitado automaticamente.