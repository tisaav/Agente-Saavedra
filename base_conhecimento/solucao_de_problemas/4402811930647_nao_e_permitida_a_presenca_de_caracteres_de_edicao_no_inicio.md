# Não e permitida a presença de caracteres de edição no início/fim da mensagem ou entre as tags da mensagem

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4402811930647-N%C3%A3o-e-permitida-a-presen%C3%A7a-de-caracteres-de-edi%C3%A7%C3%A3o-no-in%C3%ADcio-fim-da-mensagem-ou-entre-as-tags-da-mensagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/4402811930647-N%C3%A3o-e-permitida-a-presen%C3%A7a-de-caracteres-de-edi%C3%A7%C3%A3o-no-in%C3%ADcio-fim-da-mensagem-ou-entre-as-tags-da-mensagem)  
> **ID:** `4402811930647` | **Última Atualização:** 2026-07-22T15:24:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661672471)

 MENSAGEM:**

[588 - Rejeição]: Não é permitida a presença de caracteres de edição no inicio/fim da mensagem ou entre as tags da mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661677591)

 SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo: 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342658410903)

 Acesse DBExplorer e realize a consulta

***SELECT XML FROM TGFNFE WHERE NUNOTA = ?***

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342658414103)

 Substitua o '?' pelo Nro único da nota.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661691415)

 Copie a informação do campo XML e cole em um editor de texto, no qual a descrição imediatamente antes da 'quebra de linha' será a configuração com o caractere oculto.

**Exemplo:**

| <outros dados do xml>........<cProdANP>888888888</cProdANP><descANP>TESTE DESCRICAO </descANP> <UFCons>MT</UFCons>..............<continuação do xml até o final> |
| --- |

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342658424855)

 ATENÇÃO:**

Ocorreu o problema na tag descANP. Observe que ocorreu ali a 'quebra de linha' onde o correto é todo o XML constar em uma única linha. Neste exemplo, na configuração do produto no campo **"Descrição ANP"** está com o texto e + caractere oculto no final.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661699607)

 Apague totalmente a informação (utilize o comando CTRL+A ou equivalente para selecionar tudo) e salve o cadastro.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661705751)

 Digite manualmente o texto necessário para o campo divergente e salve novamente com a informação atualizada.

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661710231)

 Após correção gere nova nota.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661716119)

 OBSERVAÇÃO:**

Em cadastros evite utilizar CTRL+V e equivalentes.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342661718039)

 CAUSA:**

Ao realizar a emissão de uma NF-e (mod. 55) ou NFC-e (mod. 65) com caracteres dentro da mensagem que não são permitidos pela SEFAZ segundo o projeto da nota fiscal eletrônica, como “espaço”, “tab”, “line-feed”, e/ou “carriage return”, o órgão autorizador retorna a rejeição 588.