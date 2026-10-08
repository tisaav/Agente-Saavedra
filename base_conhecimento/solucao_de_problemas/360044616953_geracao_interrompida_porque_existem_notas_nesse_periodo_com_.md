# Geração interrompida porque existem notas nesse período com situação "ENVIADA", "AGUARDANDO AUTORIZAÇÃO" ou "PENDENTE DE RETORNO". Por exemplo, a nota com número único 'X'

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616953-Gera%C3%A7%C3%A3o-interrompida-porque-existem-notas-nesse-per%C3%ADodo-com-situa%C3%A7%C3%A3o-ENVIADA-AGUARDANDO-AUTORIZA%C3%87%C3%83O-ou-PENDENTE-DE-RETORNO-Por-exemplo-a-nota-com-n%C3%BAmero-%C3%BAnico-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616953-Gera%C3%A7%C3%A3o-interrompida-porque-existem-notas-nesse-per%C3%ADodo-com-situa%C3%A7%C3%A3o-ENVIADA-AGUARDANDO-AUTORIZA%C3%87%C3%83O-ou-PENDENTE-DE-RETORNO-Por-exemplo-a-nota-com-n%C3%BAmero-%C3%BAnico-X)  
> **ID:** `360044616953` | **Última Atualização:** 2026-08-13T15:56:32Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16593052753047)

 MENSAGEM**

Geração interrompida porque existem notas nesse período com situação "ENVIADA", "AGUARDANDO AUTORIZAÇÃO" ou "PENDENTE DE RETORNO". Por exemplo, a nota com número único 'X'.
 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/42695210368663)

 SITUAÇÃO**

Esta mensagem aparece ao tentar realizar a geração do Livro ICMS/IPI ou a geração do ISS em um período que contém notas fiscais com situação indefinida. O sistema interrompe o processo e exibe um aviso informando que existem notas com status **"ENVIADA"**, **"AGUARDANDO AUTORIZAÇÃO"** ou **"PENDENTE DE RETORNO"**, impedindo a conclusão da geração dos livros fiscais.
 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16593028510999)

 SOLUÇÃO**

A mensagem é um bloqueio do sistema, não apenas um aviso simples. Você não conseguirá gerar o livro fiscal enquanto houver notas com esses status, pois o sistema precisa que todas as notas do período estejam com situação definida (aprovadas, canceladas ou rejeitadas) para calcular corretamente os valores fiscais. Para resolver, siga os passos abaixo:
 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593052758807)

 Localize no Portal *(Caminho de acesso: Compras » Vendas » Movimentação Interna)* o número único citado na mensagem de erro;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593052761111)

 Selecione a nota, busque pelo campo **"Status NF-e";**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15238493250199)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593028519703)

 Caso não localize esse campo, o mesmo pode ser inserido através do botão **"Configuração da Grade":**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15238523062807)

 

Busque pelo campo **"Status NF-e"** em **"Colunas disponíveis"** e arraste para **"Colunas selecionadas"**.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/16593028520983)

 De acordo com o **"Status NF-e"** apresentado, proceda com as devidas tratativas:
 

- 

Aguardando Autorização: [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)
 

1. 

Enviada: [Nota Fiscal Eletrônica com status 'Enviada'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044128313)
 

1. 

Pendente de Retorno: [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)
 

1. 

Se a nota apresenta erro na chave NF-e (modelo incorreto), exclua e relance a nota;
 

1. 

Se a nota está travada e não permite ações, contate o suporte para análise de possíveis ajustes via banco de dados.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/16593028522391)

 Realizada a tratativa da respectiva nota, teste a geração dos livros novamente. Caso existam múltiplas notas, repita o processo para cada uma delas.
 

 

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16593028529047)

 CAUSA**

Ao realizar a geração de ICMS/IPI, se detectada a presença no período de notas fiscais com status NF-e 'Aguardando autorização', 'Pendente de retorno' ou 'Enviada', será apresentada a mensagem.


---

### 🔗 Links e Referências Internas:

- [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)
- [Nota Fiscal Eletrônica com status 'Enviada'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044128313)
- [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)