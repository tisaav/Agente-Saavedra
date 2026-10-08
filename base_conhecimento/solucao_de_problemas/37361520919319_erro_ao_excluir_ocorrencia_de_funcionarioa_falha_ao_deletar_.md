# Erro ao Excluir Ocorrência de Funcionário(a): “Falha ao deletar a ocorrência. Motivo: null”

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37361520919319-Erro-ao-Excluir-Ocorr%C3%AAncia-de-Funcion%C3%A1rio-a-Falha-ao-deletar-a-ocorr%C3%AAncia-Motivo-null](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361520919319-Erro-ao-Excluir-Ocorr%C3%AAncia-de-Funcion%C3%A1rio-a-Falha-ao-deletar-a-ocorr%C3%AAncia-Motivo-null)  
> **ID:** `37361520919319` | **Última Atualização:** 2026-07-29T13:22:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445207462039)

 MENSAGEM:**

“Falha ao deletar a ocorrência. Motivo: null”

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37361520918679)

 

##### **

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309927186583)

 SITUAÇÃO: **

##### Ao tentar **excluir o último lançamento de ocorrência da funcionário(a)**, o sistema apresentou a mensagem de erro acima. A exclusão não foi concluída, mesmo tratando-se do último registro lançado.

#####  

##### **

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309927188887)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445207470871)

 Acesse a tela ****[''Ocorrências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494-Ocorr%C3%AAncias) (Pessoal+ » Rotinas Folha » Ocorrências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445207472791)

 Localize a ocorrência que precisa ser excluída.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445271548311)

 Verifique se existem **ocorrências recorrentes ativas** para o colaborador(a).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445207474967)

 Confirme que todas as ocorrências recorrentes que exigem **anexo de atestado** possuam o documento vinculado.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445207476503)

 Ajuste qualquer configuração inconsistente da ocorrência recorrente.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445437160983)

 Após realizar as correções, **exclua novamente o lançamento de ocorrência**.

 

##### **

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309927190295)

 CAUSA:**

O erro ocorre quando existe uma ocorrência configurada como ''**Recorrente''** que não possui um **anexo de atestado** vinculado.

Essa configuração inconsistente faz com que o sistema acione um **gatilho de validação**, bloqueando a exclusão da ocorrência e exibindo a mensagem de erro sem detalhar o motivo (“null”).

 

##### **

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309938164759)

 OBSERVAÇÃO:**

- 

Ocorrências marcadas como ''Recorrentes'' exigem validações adicionais no sistema.

- 

A ausência de **anexo obrigatório (atestado)** em ocorrências desse tipo pode gerar inconsistências e bloqueios operacionais.

- 

O erro não está relacionado à tentativa de exclusão em si, mas sim à **configuração incorreta da ocorrência recorrente existente**.


---

### 🔗 Links e Referências Internas:

- [''Ocorrências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494-Ocorr%C3%AAncias)