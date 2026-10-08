# Configurações - Gerar registro 0220 utilizando UND enviada pelo Fornecedor

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/21631135942679-Configura%C3%A7%C3%B5es-Gerar-registro-0220-utilizando-UND-enviada-pelo-Fornecedor](https://ajuda.sankhya.com.br/hc/pt-br/articles/21631135942679-Configura%C3%A7%C3%B5es-Gerar-registro-0220-utilizando-UND-enviada-pelo-Fornecedor)  
> **ID:** `21631135942679` | **Última Atualização:** 2026-07-22T14:49:59Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027847959)

 **SITUAÇÃO:**

Melhores Praticas para gerar registro 0220 utilizando UND enviada pelo Fornecedor.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21631098150679)

SOLUÇÃO:**

Para que esse processo funcione, temos um passo a passo a verificar:
 
Vimos que na Nota, o Produto foi feito a entrada como CX (CAIXA), que é a Unidade Alternativa que foi configurada no Produto.
 
Para que na Geração do 0220 o mesmo recebe a Unidade do Parceiro, no caso a Unidade configurada na tela Produtos, aba Produtos Equivalentes. É preciso validar as seguintes configurações.
 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027857815)

 Acesse tela Preferencias > Empresa >> Aba EFD - Escrituração Fiscal Digital
 
Verifique se o Campo "Gerar registro 0220 utilizando UND enviada pelo Fornecedor" está marcado. Caso não esteja, para que a configuração do Registro 0220 levar a UND do Parceiro, o campo deve-se estar marcado.
 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027873303)

 Tela Produtos, aba Unidade Alternativa >> Sub aba 0220 UND Conversão - EFD
 

![SAIS 27-02.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027888407)

 

Nessa tela é preciso configurar a devida opção para gerar o Registro 0220, onde temos 3 opções.
 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027857815)

 Opção Utiliza a Unidade Alternativa, sendo assim NÂO irá levar para o EFD a UNIDADE do Parceiro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027873303)

 Opção utiliza a UND do Produto Equivalente, sendo assim essa opção irá levar a UNIDADE configurada na Aba Produtos Equivalentes, e assim levando ao registro 0220 a UNIDADE do Parceiro.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657071922711)

 Opção "A Partir da Função", essa terceira opção seria utilizada na necessidade de criar um processo personalizado, liberado o acesso a uma Function, criada na implementação para uma função personalizada no Banco de Dados.
 
Após verificar a tela Unidade Alternativa, vamos para a segunda configuração.
 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657071922711)

 Tela Produtos, aba Produtos Equivalentes.

 

![Central de compras 27-02.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657071942423)

 
Nessa tela, se deve configurar o seguinte:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027857815)

 Código do Parceiro a fazer essa Utilização

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657027873303)

 O Campo "UNIDADE" deve-se configurar com a Unidade que foi utilizada na Nota. Por exemplo (Caso na Nota tenha sido utilizada a Unidade Alternativa CX (CAIXA), deve-se configurar o campo Unidade na tela Produtos Equivalentes como CX (CAIXA).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21657071922711)

 O Campo "UNIDADE DO PARCEIRO" deve-se configurar conforme a Unidade do Parceiro, sendo esse o campo que irá para o Registro 0220 conforme a Unidade que preencher.
 
Após fazer as configurações basta gerar o EFD - Fiscal e será levado ao Registro 0220 a UND configurada do Parceiro.