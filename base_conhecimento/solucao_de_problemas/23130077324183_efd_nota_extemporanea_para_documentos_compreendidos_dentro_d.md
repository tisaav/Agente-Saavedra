# EFD - Nota Extemporânea: ''Para documentos compreendidos dentro do período da escrituração deverá ser utilizada uma situação para documentos regular códigos ''00'' ou ''02'' ou ''06''. ''

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/23130077324183-EFD-Nota-Extempor%C3%A2nea-Para-documentos-compreendidos-dentro-do-per%C3%ADodo-da-escritura%C3%A7%C3%A3o-dever%C3%A1-ser-utilizada-uma-situa%C3%A7%C3%A3o-para-documentos-regular-c%C3%B3digos-00-ou-02-ou-06](https://ajuda.sankhya.com.br/hc/pt-br/articles/23130077324183-EFD-Nota-Extempor%C3%A2nea-Para-documentos-compreendidos-dentro-do-per%C3%ADodo-da-escritura%C3%A7%C3%A3o-dever%C3%A1-ser-utilizada-uma-situa%C3%A7%C3%A3o-para-documentos-regular-c%C3%B3digos-00-ou-02-ou-06)  
> **ID:** `23130077324183` | **Última Atualização:** 2026-07-22T14:48:35Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23130039322903)

 **MENSAGEM:**

''Para documentos compreendidos dentro do período da escrituração deverá ser utilizada uma situação para documentos regular códigos ''00'' ou ''02'' ou ''06''. ''

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23130039326103)

SOLUÇÃO:**

Quando se trata de devolução extemporânea, no lançamento da nota no portal tem as seguintes configurações. 
Habilite o parâmetro **"Permite informar data extemporâneos na CAF? - DOCEXTEMP"**; assim, será utilizada a data extemporânea do lançamento para definição, a data do movimento do livro fiscal e será gerada a informação do campo COD_SIT do registro C100 igual a 01 (Escrituração extemporânea de documento regular).

**Observação:** quando o parâmetro acima estiver habilitado, você conseguirá alterar a NF-e de emissão própria que está com o status de aprovada.

Ao ativá-lo, será possível incluir no cabeçalho do layout da nota o campo 'dados extemporâneos'. 
Nesse campo, você deve inserir os dados de que o documento está sendo lançado no sistema.
E nos demais campos de data, informar a data original do arquivo.
Pois assim na geração do livro e SPED o sistema vai validar a informação do campo "Data extemporânea" e não ocorrerá erro no PVA.