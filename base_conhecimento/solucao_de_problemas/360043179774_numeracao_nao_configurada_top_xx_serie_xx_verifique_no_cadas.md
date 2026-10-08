# Numeração não configurada TOP XX série XX. Verifique no cadastro de TOP de Operação/Impressão/Controle de Numeração

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179774-Numera%C3%A7%C3%A3o-n%C3%A3o-configurada-TOP-XX-s%C3%A9rie-XX-Verifique-no-cadastro-de-TOP-de-Opera%C3%A7%C3%A3o-Impress%C3%A3o-Controle-de-Numera%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179774-Numera%C3%A7%C3%A3o-n%C3%A3o-configurada-TOP-XX-s%C3%A9rie-XX-Verifique-no-cadastro-de-TOP-de-Opera%C3%A7%C3%A3o-Impress%C3%A3o-Controle-de-Numera%C3%A7%C3%A3o)  
> **ID:** `360043179774` | **Última Atualização:** 2026-08-21T02:19:31Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165965504407)

 MENSAGEM:**

[CORE_E02247] Numeração não configurada TOP XX série XX. Verifique no cadastro de TOP de Operação/Impressão/Controle de Numeração.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165917261079)

 SITUAÇÃO:**

Ao tentar emitir um pedido ou nota a seguinte mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165965554071)

 CAUSA:**

Mensagem apresentada ao realizar lançamentos no sistema com número/série nota não cadastrados no controle de numeração da respectiva TOP.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165917264023)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165965513623)

 Acesse a tela** "[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial »> Arquivos » Cadastros » Tipos de Operação - TOP)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165965516567)

 Campo **"Outras Opções"** » "**Controle de Numeração":**

 

![top13.png](https://ajuda.sankhya.com.br/hc/article_attachments/14707938360983)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165965533207)

 Deverá existir uma linha para a 'Empresa', 'Série' e 'Modelo de Documento' referente ao lançamento realizado.

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/12235796078871)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458156206743)

 EXEMPLO¹:**

Numeração não configurada.
Top: 1018
Empresa: 2
Série: 1
CodModDoc = 0 ou 1
Verifique no Cadastro de Tipo de Operação/Impressão/Controle de Numeração.

 

Conforme mensagem de erro, o sistema está solicitando o cadastro de uma linha de numeração na TOP 1018, para empresa 2, série 1, Modelo do documento 0 ou 1.

Dessa forma, teríamos:

 

![top14.png](https://ajuda.sankhya.com.br/hc/article_attachments/14708000718999)

 

O** "Tipo de Numeração" **serve para identificar qual será a opção de numeração da top, conjuntamente ao campo Base de Numeração e **"Outras Opções – Controle de Numeração"**. Exemplo: Base de Numeração é Venda e o Tipo de Numeração é Empresa e nas Outras Opções – Controle de Numeração cadastra-se a empresa 1.

- 
**Única:** Todas as notas criadas com este tipo de Numeração respeitarão a mesma sequência para uma empresa, sem série, etc.

- 
**Empresa/Série:** Todas as notas criadas com este tipo de Numeração terão para cada empresa/série terá uma sequência a ser seguida.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458156206743)

 **EXEMPLO²:** 

Caso a empresa trabalhe com cupom fiscal, necessariamente deverá configurar a TOP por Empresa/Série.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165917273111)

 IMPORTANTE:**

- Lembre-se de verificar se o campo **"Série"** informado no cabeçalho da nota, corresponde a série necessária para o respectivo lançamento. 

- 
Caso não visualize esse campo no lançamento, faça a inserção do mesmo através do** "****[Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)"**, para mais detalhes acesse: [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)
- [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)