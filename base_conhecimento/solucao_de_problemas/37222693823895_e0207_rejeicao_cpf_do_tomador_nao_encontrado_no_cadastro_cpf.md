# E0207 Rejeição: CPF do tomador não encontrado no cadastro CPF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222693823895-E0207-Rejei%C3%A7%C3%A3o-CPF-do-tomador-n%C3%A3o-encontrado-no-cadastro-CPF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222693823895-E0207-Rejei%C3%A7%C3%A3o-CPF-do-tomador-n%C3%A3o-encontrado-no-cadastro-CPF)  
> **ID:** `37222693823895` | **Última Atualização:** 2026-07-22T14:17:33Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222693810327)

 **MENSAGEM**

E0207 Rejeição: CPF do tomador não encontrado no cadastro CPF.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222693810967)

 **SITUAÇÃO**

Ao emitir um **documento fiscal eletrônico** (NF-e, NFS-e ou NFC-e), o sistema retorna a rejeição informando que o **CPF do tomador/destinatário** não foi encontrado no cadastro da Receita Federal. A rejeição ocorre no momento da **transmissão do documento** para a SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222677926423)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222677927319)

 Acesse o site da ****[''Receita Federal''](https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp) e consulte a situação cadastral do CPF do tomador/destinatário.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222677928087)

 Verifique se o **CPF está ativo e regular** na base da Receita Federal.

- 

Caso o CPF esteja **inativo, suspenso ou cancelado**, solicite ao cliente que regularize sua situação cadastral junto à Receita Federal.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222677928855)

 Confirme se o **CPF informado no cadastro** está correto e sem erros de digitação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37807247282967)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do tomador/destinatário.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222677936407)

 Corrija o **número do CPF** no campo **"CNPJ / CPF"** do cadastro do parceiro, caso identifique alguma inconsistência.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37807247284119)

 Salve as alterações realizadas no cadastro.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37807224292631)

 Reemita o **documento fiscal eletrônico** para o tomador/destinatário com os dados corrigidos. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222677939479)

 **CAUSA**

A rejeição é retornada pela **SEFAZ** quando o **CPF do tomador/destinatário** informado no documento fiscal não consta na base de dados da **Receita Federal**, está **inativo, cancelado ou digitado incorretamente** no cadastro do parceiro. A validação é realizada para garantir a **autenticidade e regularidade fiscal** das partes envolvidas na operação.