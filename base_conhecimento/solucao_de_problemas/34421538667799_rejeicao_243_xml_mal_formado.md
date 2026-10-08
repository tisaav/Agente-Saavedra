# Rejeição 243: XML Mal Formado

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34421538667799-Rejei%C3%A7%C3%A3o-243-XML-Mal-Formado](https://ajuda.sankhya.com.br/hc/pt-br/articles/34421538667799-Rejei%C3%A7%C3%A3o-243-XML-Mal-Formado)  
> **ID:** `34421538667799` | **Última Atualização:** 2026-07-22T14:27:09Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003851500055)

 **MENSAGEM:**

[243] XML Mal Formado

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003851501463)

 **SITUAÇÃO:**

A rejeição ocorre ao tentar transmitir uma Nota Fiscal Eletrônica (NF-e) quando o arquivo XML gerado **não segue a estrutura exigida pelo Schema da SEFAZ**. 

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003851503895)

 **SOLUÇÃO:**

Siga o passo a passo para corrigir a rejeição:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003851505175)

 Valide o arquivo XML antes de enviar: 
Utilize um validador de XML (online ou integrado ao sistema) para verificar se a estrutura está conforme o Schema da SEFAZ.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003838849175)

 Revise a codificação do arquivo:
Confirme que o XML está salvo em **"UTF-8 sem BOM"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003838851095)

 Evite que certos caracteres especiais estejam em sua forma pura:
Certifique-se de que caracteres como **"&"**, **"<"**, **">"** e **"aspas"** estejam **escapados corretamente, conforme a tabela abaixo:**

 

````

````

````

````

````

| Caractere | Uso no XML | Como deve ser representado no conteúdo |
| --- | --- | --- |
| & | Marca início de entidades XML | & |
| < | Indica abertura de tag | < |
| > | Indica fechamento de tag | > |
| " (aspas duplas) | Delimita valor de atributo | " |
| ' (aspas simples) | Também pode delimitar atributo | ' |

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003851512727)

 Corrija tags mal estruturadas:
Verifique se todas as **tags abertas foram devidamente fechadas** e se estão na **ordem correta**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003838856343)

 Utilize um editor de texto ou XML adequado: 
Ferramentas como **"VS Code"**, **"Notepad++"**, **"XML Notepad"** ou sistemas de ERP confiáveis ajudam a detectar erros automaticamente. 

Para saber mais como fazer essa detecção automática dos erros, acesse o artigo: [Como identificar caracteres inválidos em um XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616473)
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35003851516695)

 **CAUSA:**

A rejeição é causada por **erros de estruturação no arquivo XML**, como tags abertas sem fechamento, caracteres inválidos, espaços em branco indevidos, sequência incorreta de elementos ou codificação errada do arquivo.


---

### 🔗 Links e Referências Internas:

- [Como identificar caracteres inválidos em um XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616473)