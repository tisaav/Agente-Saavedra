# Não é possível baixar uma nota ainda não confirmada pela SEFAZ

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110494-N%C3%A3o-%C3%A9-poss%C3%ADvel-baixar-uma-nota-ainda-n%C3%A3o-confirmada-pela-SEFAZ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110494-N%C3%A3o-%C3%A9-poss%C3%ADvel-baixar-uma-nota-ainda-n%C3%A3o-confirmada-pela-SEFAZ)  
> **ID:** `360044110494` | **Última Atualização:** 2026-07-22T15:53:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595121243799)

 MENSAGEM:**

[ORA-20101]: Não é possível baixar uma nota ainda não confirmada pela SEFAZ.
[ORA-06512]: em "SANKHYA.TRG_INC_UPT_TGFLIV_STATUSNFE", line 31
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPT_TGFLIV_STATUSNFE'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595076267927)

 SOLUÇÃO:**

Verifique para o período em que está sendo realizada a 'Geração ICMS/IPI' quais notas estão com o campo STATUS NF-e = 'Aguardando Autorização', 'Aguardando Correção', 'Com erro de Validação' ou 'Pendente de Retorno'. Para tal, siga as instruções abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595121252119)

 Realize filtros nos Portais (*Venda » Compra » Mov.Interna*) para o período de geração dos livros fiscais.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595121255575)

 **Selecione a coluna 'Status NF-e':

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15185354139671)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595076277527)

 Caso não localize esse campo, o mesmo pode ser inserido através do botão **"Configuração da Grade"**:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15185379382551)

 

Busque pelo campo **"Status NF-e"** em **"Colunas disponíveis"** e arraste para **"Colunas selecionadas"**.

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595076285335)

 **Para notas fiscais eletrônicas com Status NF-e diferente de **"Aprovada"**, de acordo com o Status apresentado, proceda com as devidas tratativas:

- Aguardando Autorização: [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)

- Aguardando Correção: [Nota Fiscal Eletrônica com status 'Aguardando Correção'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043231613)

-  Pendente de Retorno: [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595121263127)

 Realizada a tratativa da respectiva nota de acordo com o seu status, teste a geração dos livros novamente. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595121269783)

 CAUSA:**

Ao tentar gerar os livros fiscais de determinado período, se existirem notas com Status NF-e = 'Aguardando Autorização', 'Aguardando Correção', 'Com erro de Validação' ou 'Pendente de Retorno', será apresentada a mensagem.


---

### 🔗 Links e Referências Internas:

- [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)
- [Nota Fiscal Eletrônica com status 'Aguardando Correção'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043231613)
- [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)