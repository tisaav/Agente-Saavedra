# E0490 Rejeição: Valor 0 para o motivo da não informação do NIF do fornecedor não é permitido na Sefin do Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225856947735-E0490-Rejei%C3%A7%C3%A3o-Valor-0-para-o-motivo-da-n%C3%A3o-informa%C3%A7%C3%A3o-do-NIF-do-fornecedor-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225856947735-E0490-Rejei%C3%A7%C3%A3o-Valor-0-para-o-motivo-da-n%C3%A3o-informa%C3%A7%C3%A3o-do-NIF-do-fornecedor-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e)  
> **ID:** `37225856947735` | **Última Atualização:** 2026-07-22T14:15:32Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225872778775)

 **MENSAGEM**

E0490 Rejeição: Valor 0 para o motivo da não informação do NIF do fornecedor não é permitido na Sefin do Sistema Nacional NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225872779415)

 **SITUAÇÃO**

Ao emitir uma **NFS-e pelo Padrão Nacional**, o sistema rejeitou o documento fiscal porque o **fornecedor estrangeiro** não possui o **NIF (Número de Identificação Fiscal)** informado no cadastro, e o motivo da não informação foi preenchido com o valor **"0" (zero)**, que não é aceito pela Sefin do Sistema Nacional.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225856933911)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225872781079)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do fornecedor estrangeiro** que está vinculado à NFS-e rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225856935703)

 Na aba **"Identificação"**, verifique o campo **"Identificação de Estrangeiro"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225856937239)

 Caso o fornecedor possua o **NIF**, preencha o campo **"Identificação de Estrangeiro"** com o número correto do NIF do fornecedor.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225872784535)

 Caso o fornecedor **não possua o NIF**, será necessário informar um **motivo válido** para a não informação do NIF, diferente de **"0" (zero)**. Consulte a documentação da Sefin do Sistema Nacional de NFS-e para identificar os códigos de motivo aceitos.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225856943511)

 Salve as alterações realizadas no cadastro do parceiro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225872787863)

 Retorne à tela de emissão da **NFS-e** e gere novamente o documento fiscal para transmissão.
 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225872791575)

 **CAUSA**

A rejeição ocorre quando uma **NFS-e é emitida pelo Padrão Nacional** e o **fornecedor estrangeiro** não possui o campo **"Identificação de Estrangeiro"** preenchido no cadastro de parceiros, ou quando o **motivo da não informação do NIF** é preenchido com o valor **"0" (zero)**, que não é permitido pela **Sefin do Sistema Nacional de NFS-e**. A tag **<nifTomador>** é gerada no XML da nota, mas sem informação válida ou com motivo inválido, resultando na rejeição do documento fiscal.