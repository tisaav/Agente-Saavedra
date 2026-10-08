# Centro de Resultado XXXXXXXXX não está ativo ou não é analítico. Financeiro de Nro Único: XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360054958694-Centro-de-Resultado-XXXXXXXXX-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico-Financeiro-de-Nro-%C3%9Anico-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360054958694-Centro-de-Resultado-XXXXXXXXX-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico-Financeiro-de-Nro-%C3%9Anico-XXXX)  
> **ID:** `360054958694` | **Última Atualização:** 2026-07-22T15:27:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16939450587543)

 MENSAGEM:**

Centro de Resultado XXXXXXXXX não está ativa ou não é analítico. Financeiro de Nro Único: XXXX.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16939450588567)

 SOLUÇÃO:**

Acesse primeiro o cadastro do produto utilizado no lançamento, aba **"Venda"** e verifique se o campo Centro de Resultado está preenchido.  

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14817006284567)

 

Caso o campo esteja preenchido, verifique no cadastro do centro de resultado se o mesmo é sintético e se está ativo, pois é necessário que os campos **"Analítico"** e **"Ativo"** estejam flegados.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14817114985879)

 

Caso não tenha a configuração acima, realize os seguintes passos:

Identifique qual Centro de Resultado será utilizado para o lançamento do respectivo financeiro, considerando o comportamento do sistema, conforme abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16939450590999)

 Se o parâmetro **"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"** estiver habilitado, será utilizado o mesmo Centro de Resultado inserido no cabeçalho do lançamento;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13737341752471)

 

Nesse caso, altere o Centro de Resultado do lançamento ou certifique-se que esse esteja **ativo** e seja analítico, através de seu cadastro na tela **"Centros de Resultado"*** (Caminho de acesso: Configurações » Cadastros » Gerencial » Centros de Resultado)*; Feito isso, teste o faturamento novamente.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16939450592791)

 Se o parâmetro citado no item 1 estiver desabilitado, o sistema segue a seguinte hierarquia para preenchimento do Centro de Resultado do Financeiro:

"Em específico para o Centro de Resultado, caso este não esteja informado no **Tipo de Negociação**, ele será preenchido no Financeiro da Nota, com o valor informado no **cadastro de "Vendedores/Compradores"**; não sendo este informado, será pega a informação da aba **"Identificação no cadastro de "Usuários"**; caso este também não esteja informado, o Centro de Resultado do Financeiro da Nota irá seguir ao preenchimento realizado no** "Cabeçalho da Nota**."

- Identificado o Centro de Resultado a ser utilizado, certifique-se que esse esteja **ativo** e seja analítico, através de seu cadastro na tela Centros de Resultado* (Caminho de acesso: Configurações » Cadastros » Gerencial » Centros de Resultado).* Feito isso, teste o faturamento novamente.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14817274128535)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16939450593303)

 CAUSA:**

Ao tentar faturar o pedido com uma TOP que gera financeiro o sistema tentou inserir um Centro de Resultado que não é analítico ou não esta ativo, ou informar um centro de resultado no cadastro do produto que não é analítico.