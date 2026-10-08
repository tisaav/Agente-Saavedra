# O Tamanho do Registro xxxxxxxx, é diferente do especificado para o arquivo

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9291198908183-O-Tamanho-do-Registro-xxxxxxxx-%C3%A9-diferente-do-especificado-para-o-arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9291198908183-O-Tamanho-do-Registro-xxxxxxxx-%C3%A9-diferente-do-especificado-para-o-arquivo)  
> **ID:** `9291198908183` | **Última Atualização:** 2026-07-22T15:09:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699251187863)

 MENSAGEM:**

[CORE_E00732]: O Tamanho do Registro xxxxxxxx, é diferente do especificado para o arquivo.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699298321431)

 SITUAÇÃO:**

Ao tentar gerar uma remessa a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699251201687)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699251207063)

 Acesse o layout selecionado na tela **"Configuração Arquivo de Remessa"** *(Caminho de acesso: Financeiro » EDI Bancário » Configuração Arquivo de Remessa),* confira o campo **"Tamanho"** e compare com o Tamanho atual do registro que é apresentado ao lado conforme imagem abaixo:

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699298333463)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699298339607)

 Identifique o registro que está com o tamanho incorreto, poderá ser no detalhe, header, ou trailer de acordo com o manual do banco. Veja:

 

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699251218583)

 

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699251233175)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699251236247)

 O Tamanho atual do registro precisa ser igual ao campo Tamanho, que seguirá a definição do manual do banco. Caso** 'Tamanho atual do registro'** esteja diferente, identifique nesse registro qual campo está com tamanho incompatível ao definido para o mesmo no manual do banco e redefina seu **'Tamanho'** no registro identificado, podendo ser header, detalhe ou trailer.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16699298349335)

 CAUSA: **

Ocorre quando o layout está com o tamanho diferente do manual do banco.