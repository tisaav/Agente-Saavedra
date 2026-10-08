# Operação interestadual e UF de destino igual a UF de origem

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042727474-Opera%C3%A7%C3%A3o-interestadual-e-UF-de-destino-igual-a-UF-de-origem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042727474-Opera%C3%A7%C3%A3o-interestadual-e-UF-de-destino-igual-a-UF-de-origem)  
> **ID:** `360042727474` | **Última Atualização:** 2026-07-22T16:06:37Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513139048087)

 MENSAGEM:**

[772 - Rejeição]: Operação Interestadual e UF de destino igual a UF de origem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513139056279)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513180369303)

 Verifique qual o CFOP apresentado nos Itens:

- CFOP'S iniciados com **1** e **5**: Emissões para **DENTRO** do Estado

- CFOP'S iniciados com **2** e **6**: Emissões para** FORA** do Estado

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513180371479)

 **Verifique se o Endereço do parceiro condiz com a condição de CFOP acima.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458211691031)

 Exemplo:**

- Se sua empresa está cadastrada com Endereço de MG e a nota está sendo emitida para um parceiro com Endereço/CNPJ de MG, não utilize CFOP'S iniciadas com 2 e 6.

- Se sua empresa está cadastrada com Endereço de MG e a nota está sendo emitida para um parceiro com Endereço/CNPJ de MT, não utilize CFOP'S iniciadas com 1 e 5.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513180378647)

Caso o CFOP esteja correto e o endereço incorreto, realize os devidos ajustes no cadastro do parceiro.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513139076247)

 Caso os endereços estejam corretos e o CFOP incorreto, verifique no cadastro do "**[TIPO DE OPERAÇÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" **(Caminho de acesso:* Comercial » Arquivo » Cadastros/Financeiro » Arquivos » Cadastros*) utilizado, aba "**Livros Fiscais"** a configuração atual de CFOP para Dentro/Fora do Estado, realizando os devidos ajustes conforme item 1.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513139078423)

 Realizados os ajustes aconselha-se a inutilização/exclusão da NF-e rejeitada e um novo faturamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513180392599)

 CAUSA:**

Quando for emitida uma NF-e de Saída (tpNF = 1) ou de Entrada (tpNF = 0) para acobertar uma Operação Interestadual (idDest = 2), com a UF do Destinatário igual a UF do Emitente e o CNPJ do Destinatário diferente do CNPJ do Emitente, será retornado a rejeição.


---

### 🔗 Links e Referências Internas:

- [TIPO DE OPERAÇÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)