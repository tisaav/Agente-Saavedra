# Erro for input string: "F"

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36859518583831-Erro-for-input-string-F](https://ajuda.sankhya.com.br/hc/pt-br/articles/36859518583831-Erro-for-input-string-F)  
> **ID:** `36859518583831` | **Última Atualização:** 2026-07-22T14:22:21Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36859518570135)

 **MENSAGEM:**

for input string: "F"

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36859518571415)

 **SITUAÇÃO: **

Ao tentar confirmar o MDF-e pela tela **Viagens de Transporte (MDF-e)**, o sistema exibe a mensagem:

```text
for input string: "F"
```

O caractere exibido entre aspas na mensagem pode variar conforme o valor configurado na **série do documento**. Dependendo da configuração, o sistema pode mostrar **"F"**, **"U"**, **"B"**, entre outros.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36859518573719)

SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881814960663)

 **Acesse a tela ****[''Viagens de Transporte (MDF-e)''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e)** **(Comercial » Rotinas » Viagens de Transporte (MDF-e)).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881814964631)

 Clique no botão **“Outras Opções” **(ícone da engrenagem no canto superior direito).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881847237783)

 Selecione a opção **''****Controle de Numeração''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881847238551)

 No campo **''****Série''**, substitua o valor atual (exemplo: `MDf`) por uma **série numérica válida**, como **1** ou **2**, conforme o padrão utilizado pela empresa e aceito pela SEFAZ.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881814971415)

 Salve as alterações.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881847240087)

 OBSERVAÇÃO:**

Após ajustar a série no ''Controle de Númeração'', é necessário gerar uma nova **Ordem de Carga** ou um **novo MDF-e** para que a numeração correta seja aplicada. 

O MDF-e que já foi emitido com a série inválida **não será atualizado retroativamente**. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36859502116247)

CAUSA:**

O erro ocorre devido à configuração incorreta** **do** Controle de Numeração do MDF-e**, especificamente ao campo ''Série''.

No caso analisado, a série configurada com **letras**, por exemplo:

- 

Série configurada: `MDf`

Quando o sistema tenta interpretar a série como número, ocorre erro de conversão, gerando a exceção:

```text
for input string: "F"
```

O comportamento segue um padrão: o erro aponta para o **último caractere inválido da série**:

- 

Se a série for **MDF** → erro **"F"**

- 

Se a série for **MDu **→ erro **"U"**

- 

Se for **A1B**→ erro **"B"**

Ou seja, **qualquer série que contenha ****letras ou caracteres não numéricos**** causará o problema**.

A série do MDF-e **deve obrigatoriamente ser numérica **(recomenda-se a utilização da série 1), conforme o padrão da SEFAZ.


---

### 🔗 Links e Referências Internas:

- [''Viagens de Transporte (MDF-e)''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e)