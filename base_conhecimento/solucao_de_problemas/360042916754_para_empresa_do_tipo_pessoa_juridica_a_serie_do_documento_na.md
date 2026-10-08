# Para empresa do tipo "Pessoa Jurídica", a série "" do documento não é válida

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042916754-Para-empresa-do-tipo-Pessoa-Jur%C3%ADdica-a-s%C3%A9rie-do-documento-n%C3%A3o-%C3%A9-v%C3%A1lida](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042916754-Para-empresa-do-tipo-Pessoa-Jur%C3%ADdica-a-s%C3%A9rie-do-documento-n%C3%A3o-%C3%A9-v%C3%A1lida)  
> **ID:** `360042916754` | **Última Atualização:** 2026-07-22T16:05:06Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117295632279)

 MENSAGEM:**

[CORE_E03060] Para empresa do tipo "Pessoa Jurídica", a série "" do documento não é válida. Deve ser de 0 a 889, não pode ter zeros a esquerda e não pode ter espaços em branco.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117295635863)

 SITUAÇÃO:**

Ao tentar emitir uma NF-e ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117265552279)

 SOLUÇÃO:**

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458169669911)

 Para verificar a série da nota e se ela está correta, siga os passos:**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117265570839)

 **Na **"Central (Vendas/Compras/Mov.Interna)"** localize o campo **"Série";**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117295646999)

 Certifique-se que de que o campo não esteja em branco e de que não há espaços em branco entre os números, deve haver um dado válido;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117265579543)

 Caso não haja um valor válido, insira a série cadastrada para aquela empresa na TOP em uso. 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117295656343)

 Teste uma nova emissão da nota.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458169669911)

 **Para observar a raiz da série que está sendo usada e ou criar uma série, siga as orientações abaixo:**

Para verificar a série que está sendo considerada, abra a tela **"[Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"**, selecione a TOP que está sendo utilizada no lançamento e procure pelo **"Controle de Numeração"** dentro do botão **"Outras Opções (..)"**, conforme o print:

![Para empresa do tipo Pessoa Jurídica a série  do documento 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/24268693982359)

 

Ao abrir o controle de numeração, busque pela empresa da nota e veja se a série ligada a ela é a mesma que está sendo usada na nota que apresentou o erro. Caso não seja, informe a série correta na Central (Vendas/Compras/Mov.Interna). Já, se não existir uma série para a empresa da nota, será necessário cria-la e informá-la novamente na nota (conforme descrito nos 4 passos acima).

 

Para criar uma série:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117265570839)

 Ainda dentro do Controle de numeração, clique no botão "+"

 

![Para empresa do tipo Pessoa Jurídica a série  do documento 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/24285740274583)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117295646999)

 Cadastre as informações solicitadas e salve. Vale lembrar que o número cadastrado deverá respeitar as regras estabelecidas, são elas: a numeração deve ser de 0 a 889, não pode ter zeros a esquerda e não pode ter espaços em branco.

 

![Para empresa do tipo Pessoa Jurídica a série  do documento 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/24285758663575)

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117295659671)

** OBSERVAÇÃO:**

Verifique se no "**[Configurador de Layout  de nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota)**" o campo Série está marcado como obrigatório e editável, pois caso não esteja como editável o campo ficará indisponível na central e com valor padrão vazio.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117265592087)

 CAUSA:**

Ocorre ao tentar emitir a NF-e, informando no campo Série um valor diferente da faixa  0 a 889, ou que contenha zeros à esquerda, ou espaços em branco.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Configurador de Layout  de nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota)