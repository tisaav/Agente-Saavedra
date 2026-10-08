# O valor do campo cProd informado não é valido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/25370872910359-O-valor-do-campo-cProd-informado-n%C3%A3o-%C3%A9-valido](https://ajuda.sankhya.com.br/hc/pt-br/articles/25370872910359-O-valor-do-campo-cProd-informado-n%C3%A3o-%C3%A9-valido)  
> **ID:** `25370872910359` | **Última Atualização:** 2026-07-22T14:45:54Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25370872898839)

 **MENSAGEM:**

O valor do campo cProd (Código do produto ou serviço. Preencher com CFOP caso se trate de itens não relacionados com mercadorias/produto e que o contribuinte não possua codificação própria
Formato ”CFOP9999”.) informado não é valido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25370879765911)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25479204022167)

 Como essa mensagem não traz o item com erro, habilite o parâmetro "**Imprimir os XMLs processados pelo SanNFe no log?-DEBUGXML"** e analise o trecho DEBUG_XML_REQUEST do server log, que pode ser extraído da tela** administração do Servidor** *(Configurações » Avançado » Administração do Servidor)* , como mostrado na imagem abaixo.

 

![O valor do campo cProd informado não é valido 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/27904479869847)

 

![O valor do campo cProd informado não é valido 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/27904473941015)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25479204029079)

 Localizando o trecho que menciona o Cprod, verifique se a informação listada após a palavra Value existe no cadastro de produtos do sistema.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30091859652247)

 Abra o cadastro do produto e verifique no campo referência (mostrado abaixo com um exemplo de erro), se existe espaço em branco ou caracteres especiais a frente do código. Caso exista estes itens, faça a exclusão dos mesmos.

 

![O valor do campo cProd informado não é valido 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/27904473947543)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25481771178519)

 Após o ajuste, redigite o item na Central e faça a geração do lote novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25370879771415)

CAUSA:**

Acontece quando é gerado no XML um valor inválido para o campo cProd, espaços em branco indevidos também podem causar essa rejeição.  Alguns exemplos de caracteres especiais que pode ajudar na análise.

Conforme Gif abaixo, se vê como que através do Notepad++ é possível fazer essa análise.  Utilize o filtro **[^0-9A-Za-z\t\n\r\<\>\|\$\?\ \"\=\:\/\-\+\%\@\*\#\(\)\;_,.]** dentro da opção 'Localizar', mencionando modo de pesquisa **'expressão regular'**:

![CaracteresCentral.gif](https://ajuda.sankhya.com.br/hc/article_attachments/25370872908183)

 
Outros caracteres que podem ser identificados.

Todo conteúdo de um XML passa por uma análise do “parser” específico da linguagem. Alguns caracteres afetam o funcionamento deste “parser”, não podendo aparecer no texto de uma forma não controlada.
 
Os caracteres que afetam o “parser” são:
• > (sinal de maior),
• < (sinal de menor),
• & (e-comercial),
• “ (aspas),
• ‘ (sinal de apóstrofo).
 

**Observação: **importante verificar se o cliente não usa nenhum campo com referência personalizada para geração no XML, podendo gerar o erro também.