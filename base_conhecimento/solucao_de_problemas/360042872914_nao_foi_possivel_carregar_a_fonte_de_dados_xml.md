# Não foi possível carregar a fonte de dados XML

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042872914-N%C3%A3o-foi-poss%C3%ADvel-carregar-a-fonte-de-dados-XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042872914-N%C3%A3o-foi-poss%C3%ADvel-carregar-a-fonte-de-dados-XML)  
> **ID:** `360042872914` | **Última Atualização:** 2026-07-22T16:05:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001621143)

 MENSAGEM:**

[CORE_E02504] Não foi possível carregar a fonte de dados XML.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001624215)

 SOLUÇÃO:**

Mensagem será retornada quando o modelo configurado na TOP para impressão possui um relatório formatado equivalente ao DANFE e o movimento do qual foi solicitado impressão não é NFE. Visto que o modelo DANFE **busca informações do XML**, sendo assim, para casos onde não trata-se de uma nota fiscal eletrônica, não é possível finalizar a impressão.

Nesse caso, identifique as duas possibilidades:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114992385943)

 Trata-se de emissão de uma nota fiscal eletrônica?

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001629463)

 Certifique-se que foi utilizado o Tipo de Operação correto.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001629463)

Na tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** *(Caminho de acesso: Comercial » Arquivo » Cadastros)* verifique as informações inseridas para os campos abaixo:

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114992415895)

Campo **"NF-e"**, **"Modelo do Documento"** da NF-e/NFC-e

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14597941908503)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001629463)

 Para impressão de um modelo DANFE os campos acima devem respeitar as configurações de nota fiscal eletrônica emissão própria. Dessa forma, sintonize junto ao implantador da empresa, para que os ajustes necessários sejam realizados, de forma que a emissão seja equivalente a um documento fiscal eletrônico. Realizado os ajustes, refaça o lançamento.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001633431)

 Não se trata de uma nota fiscal eletrônica? É uma nota de Terceiros ou Modelo 01, por exemplo.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001629463)

 Será necessário que um modelo de impressão que não seja equivalente do DANFE seja configurado para essa operação. Caso essa impressão nunca tenha sido validada e não exista um modelo previsto/parametrizado, direcione essa demanda para consultores de sua Franquia/Filial.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001629463)

 Na TOP utilizada na nota, o campo **"Modelo de impressão de nota fiscal"** deve estar informado um modelo.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001629463)

 Esse modelo deve estar cadastrado na tela **"[Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-)"** que está no menu: Configurações *» * Avançado.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001635607)

 OBSERVAÇÃO:**

Outra verificação válida no cadastro da respectiva TOP: Verifique na aba **"E-mails da TOP"**, no campo **"Modelo"**, se foi vinculado algum modelo DANFE de forma indevida.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115001641751)

 CAUSA:**

Quando ocorrer a mensagem: "Não foi possível carregar a fonte de dados XML" ao solicitar impressão de notas\pedidos, significa que o modelo configurado na TOP para impressão possui um relatório formatado equivalente ao DANFE e o movimento do qual foi solicitado impressão não é NFE.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-)