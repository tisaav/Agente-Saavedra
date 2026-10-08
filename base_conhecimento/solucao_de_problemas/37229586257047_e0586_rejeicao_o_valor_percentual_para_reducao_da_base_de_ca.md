# E0586 Rejeição: O valor percentual para redução da base de cálculo deve ser maior que 0 e menor ou igual ao percentual parametrizado pelo município de incidência do ISSQN.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37229586257047-E0586-Rejei%C3%A7%C3%A3o-O-valor-percentual-para-redu%C3%A7%C3%A3o-da-base-de-c%C3%A1lculo-deve-ser-maior-que-0-e-menor-ou-igual-ao-percentual-parametrizado-pelo-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/37229586257047-E0586-Rejei%C3%A7%C3%A3o-O-valor-percentual-para-redu%C3%A7%C3%A3o-da-base-de-c%C3%A1lculo-deve-ser-maior-que-0-e-menor-ou-igual-ao-percentual-parametrizado-pelo-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN)  
> **ID:** `37229586257047` | **Última Atualização:** 2026-07-22T14:13:50Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229634089495)

 **MENSAGEM:**

E0586 Rejeição: O valor percentual para redução da base de cálculo deve ser maior que 0 e menor ou igual ao percentual parametrizado pelo município de incidência do ISSQN.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229586241943)

 **SITUAÇÃO:**

Ao emitir uma NFS-e com redução da base de cálculo do ISSQN, a nota foi rejeitada. O sistema indicou que o percentual de redução informado está inválido.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229634091287)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37562380627223)

 Acesse as telas **''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Aliquotas de CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229634096151)

 Localize a alíquota utilizada no documento fiscal rejeitado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229634096535)

 Verifique a seção **''Redução e Deferimentos''** está configurado para o ISSQN, e certifique-se de que:

- 

O valor seja **maior que zero (0)**;

- 

O valor seja **menor ou igual ao percentual máximo** permitido pelo município de incidência do ISSQN.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229634096535)

 Verifique a legislação municipal ou entre em contato com a prefeitura do município de incidência para confirmar o **percentual máximo de redução da base de cálculo** permitido para o serviço prestado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229586246935)

 Ajuste o campo **''% Redução Alíquota (Gov.)''**, informando um valor **válido conforme os limites estabelecidos pelo município**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229586247703)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229634100759)

 Retorne ao documento fiscal rejeitado e tente emitir novamente, garantindo que o percentual de redução esteja correto.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229634101399)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida se o percentual de redução da base de cálculo do ISSQN** informado no documento fiscal está dentro dos **limites estabelecidos pelo município** de incidência do serviço. Quando o percentual configurado é **igual a zero ou ultrapassa o limite máximo** permitido pela legislação municipal, o documento é rejeitado para garantir a conformidade fiscal e evitar inconsistências no recolhimento do imposto.