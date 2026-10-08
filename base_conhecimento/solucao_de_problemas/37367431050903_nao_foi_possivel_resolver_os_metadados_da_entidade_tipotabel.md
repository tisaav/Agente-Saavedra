# Não foi possível resolver os metadados da entidade 'TipoTabela-pt_BR'

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37367431050903-N%C3%A3o-foi-poss%C3%ADvel-resolver-os-metadados-da-entidade-TipoTabela-pt-BR](https://ajuda.sankhya.com.br/hc/pt-br/articles/37367431050903-N%C3%A3o-foi-poss%C3%ADvel-resolver-os-metadados-da-entidade-TipoTabela-pt-BR)  
> **ID:** `37367431050903` | **Última Atualização:** 2026-07-29T13:22:23Z

---

##### **

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309954672791)

 MENSAGEM:**

Erro interno  

Não foi possível resolver os metadados da entidade 'TipoTabela-pt_BR'.  

Erro ao carregar os metadados da entidade TipoTabela:  

Erro interno: Metadados do campo 'TFPEVE->DTATUALIZACAO' não inicializados.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37367461032471)

#####  

##### **

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309954675991)

 SOLUÇÃO:**

Para corrigir o problema, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479201759895)

 Acesse a tela ****[''Plano de Saúde''](https://ajuda.sankhya.com.br/hc/pt-br/articles/14865357667223-Plano-de-Sa%C3%BAde) (Pessoal+ » Cadastros » Plano de Saúde).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479201764631)

 Pesquise a **tabela de faixas** utilizada no cálculo da folha.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479201767575)

 Localize o campo onde é informado o ''**C****ódigo do evento''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479189132951)

 Verifique se o campo possui apenas **números**.

- 

Remova letras, espaços ou descrições do evento.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479189134103)

 Ajuste o campo para conter **somente o código numérico**:

##### **Exemplo correto:**

```text
1005
```

#####  

##### **Exemplo incorreto:**

```text
1005 PLANO DE SAÚDE
```

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479189134103)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479189135511)

 Volte para a folha de pagamento e tente **confirmar novamente**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37478246851223)

 CAUSA:**

O erro ocorre quando, na **tabela de faixas**, o campo que referencia o código do evento é** preenchido com informações que não são numéricas**, como letras, espaços ou descrições do evento (por exemplo: “1005 PLANO DE SAÚDE”).

 

![{09AE2C20-581C-4417-B769-E36B3546B169}.png](https://ajuda.sankhya.com.br/hc/article_attachments/37479189137431)

 

Como o sistema aceita apenas valores numéricos nesse campo, a inclusão de qualquer caractere adicional gera falhas de validação, impedindo a confirmação da folha de pagamento ou a execução correta dos cálculos.


---

### 🔗 Links e Referências Internas:

- [''Plano de Saúde''](https://ajuda.sankhya.com.br/hc/pt-br/articles/14865357667223-Plano-de-Sa%C3%BAde)