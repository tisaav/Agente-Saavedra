# Certificado não possui cadeia de hierarquia CA

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043005313-Certificado-n%C3%A3o-possui-cadeia-de-hierarquia-CA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043005313-Certificado-n%C3%A3o-possui-cadeia-de-hierarquia-CA)  
> **ID:** `360043005313` | **Última Atualização:** 2026-07-22T16:10:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315146758679)

 MENSAGEM:**

Certificado não possui cadeia de hierarquia CA.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315157034391)

 **SOLUÇÃO:**

A cadeia de certificados é uma lista de certificados utilizada para autenticar uma entidade. A cadeia, ou caminho, começa com o certificado daquela entidade e cada certificado na cadeia é assinado pela entidade identificada pelo próximo certificado na cadeia. A cadeia termina com um certificado de CA raiz. O certificado de autoridade de certificação raiz é sempre assinado pela própria autoridade de certificação (CA). As assinaturas de todos os certificados na cadeia devem ser verificadas até que o certificado de CA raiz seja alcançado.

 

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315157035415)

 Abra o navegador em que o certificado foi previamente instalado. Normalmente, o mesmo
é instalado no Internet Explorer.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315157038231)

 Acesse as opções da internet no caminho *Ferramentas » Opções da Internet » Aba Conteúdo » Certificados*:

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360057726773)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315146769175)

 Selecione o certificado que você quer exportar e clique em “Exportar:

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360056837894)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315157042071)

 Siga os passos a seguir realizando as marcações conforme abaixo:

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360057726933)

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/360057727413)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315157043863)

 OBSERVAÇÃO:** **NÃO** marque a opção “Excluir a chave privada se a exportação tiver êxito”

 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/360056838114)

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/360056838134)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315146778519)

 Insira o nome do arquivo que será gerado na exportação.

 

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/360056838174)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315146779543)

 Clique em concluir e o arquivo será gerado no caminho selecionado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315146781335)

 Após realizada essa operação, importe o arquivo gerado no Console do SanNFe.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315157051543)

 CAUSA:**

Ocorre quando os certificados não foram gerados com a Cadeia de certificação das Autoridades que regulamenta a confiança do certificado, através de um criterioso processo de identificação, tornando-o um documento eletrônico confiável.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458228358423)

 Artigos relacionados:**

**[Não é possível assinar xml a uf (GO) exige a cadeia de certificado.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042866074)**


---

### 🔗 Links e Referências Internas:

- [Não é possível assinar xml a uf (GO) exige a cadeia de certificado.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042866074)