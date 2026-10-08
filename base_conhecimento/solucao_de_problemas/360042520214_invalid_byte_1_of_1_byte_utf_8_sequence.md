# Invalid byte 1 of 1-byte UTF-8 sequence

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042520214-Invalid-byte-1-of-1-byte-UTF-8-sequence](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042520214-Invalid-byte-1-of-1-byte-UTF-8-sequence)  
> **ID:** `360042520214` | **Última Atualização:** 2026-07-22T16:10:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457895731863)

 MENSAGEM:**

Invalid byte 1 of 1-byte UTF-8 sequence.
Caractere inválido na nota (ex.: ^, ~, ?). Verifique os cadastros relacionados (ex.: parceiros, produtos, empresa)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457879573399)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457879575703)

 Revise todos os cadastros relacionados a emissão da respectiva NF-e, buscando por possíveis caracteres especiais e/ou espaços em branco.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457895736599)

 Atente-se a novos cadastros, informações que normalmente não são utilizadas em outras emissões.

- 
**Ex:** (Campo "**Observação"**, Cadastro do 'Parceiro Principal', Cadastro do 'Parceiro Transportador', Cadastro do produto, etc)

Caso não identifique tais caracteres visualmente no sistema, recomendamos a análise do XML através do recurso 'Notepad++', conforme detalhado abaixo:

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457879582999)

 Acesse a tela "**[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)"** (Caminho de acesso: *Comercial » Consulta):*

- Botão "**NF-e"** » Gerar XML da NF-e em arquivo para conferência.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457895740823)

 Com o XML gerado, será possível identificar o caractere inválido com maior facilidade através do aplicativo Notepad ++. Para isso, acesse o conteúdo e compreenda de que forma essa análise será realizada:  [Como identificar caracteres inválidos em um XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616473)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457879585815)

 IMPORTANTE: **Espaços em branco indevidos também podem causar essa rejeição.  Conforme .gif abaixo, através do Notepad++ é possível fazer essa análise.  Utilize o filtro **[^0-9A-Za-z\t\n\r\<\>\|\$\?\ \"\=\:\/\-\+\%\@\*\#\(\)\;_,.],** dentro da opção 'Localizar',  mencionando o modo de pesquisa **'expressão regular'**:

 

![CaracteresCentral.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360083953474)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457879586839)

 Identificado o registro, acesse o sistema e faça o ajuste.

- Por exemplo: Se o caractere especial estava no campo de "**Número"** do endereço do parceiro, acesse o cadastro do parceiro e faça o ajuste na aba "**Endereço", **Campo "**Número"**.

**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457879588119)

 **Após os ajustes, redigite os campos empresa e parceiro da nota e gere um novo lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457879588887)

 CAUSA:**

Quando uma NF-e é gerada e existe algum carácter especial no cadastro de Empresa, Parceiro, Produto, Transportadora, Observação, Informações Complementares e outros da NF-e, ao gerar o XML e enviar para a SEFAZ, ocorre a Rejeição.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17857553697687)

 **OBSERVAÇÃO:**

- Uma opção para verificar quebra de linha em alguma tag do XML da NF-e, é acessar o site abaixo, copiar e colar todo o xml da nota e clicar em 'Validar'

         [https://www.sefaz.rs.gov.br/NFE/NFE-VAL.aspx](https://www.sefaz.rs.gov.br/NFE/NFE-VAL.aspx)

- Exemplo**:** quebra de linha na tag de Nome do Emitente da Nota

**         Errado:**<xNome>NOME FANTASIA DA EMPRESA NOVA
                    </xNome>

**        Correto:** <xNome>NOME FANTASIA DA EMPRESA NOVA</xNome>

Apresentará o erro Schema do XML, ao validar no site acima:

 *The 'http://www.portalfiscal.inf.br/nfe:xNome' element is invalid - The value 'NOME FANTASIA DA EMPRESA NOVA ' is invalid according to its datatype 'String' - The Pattern constraint failed.*
*Caminho: NFe[1]/infNFe/emit/xNome*


---

### 🔗 Links e Referências Internas:

- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)
- [Como identificar caracteres inválidos em um XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616473)