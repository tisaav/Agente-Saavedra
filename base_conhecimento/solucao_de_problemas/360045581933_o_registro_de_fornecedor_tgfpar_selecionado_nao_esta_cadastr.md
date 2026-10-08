# O registro de fornecedor TGFPAR selecionado não está cadastro ou não está ativo ou não é analítico

> **Módulo:** Solucao de Problemas | **Subseção:** Prestação de Serviços  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045581933-O-registro-de-fornecedor-TGFPAR-selecionado-n%C3%A3o-est%C3%A1-cadastro-ou-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045581933-O-registro-de-fornecedor-TGFPAR-selecionado-n%C3%A3o-est%C3%A1-cadastro-ou-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico)  
> **ID:** `360045581933` | **Última Atualização:** 2026-07-22T15:33:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311269889431)

 MENSAGEM:**

[SQL 50001]: o registro de fornecedor TGFPAR selecionado não está cadastro ou não está ativo ou não é analítico.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311277226135)

 SOLUÇÃO:**

Ao executar a rotina de 'Reajuste de Contratos Ativos', caso seja localizado algum contrato com o campo ATIVO=NÃO, porém com produtos/serviços que tenham ocorrências de ativação vigentes, será apresentada a mensagem.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311277228823)

 Identifique na tela **"[Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos)"** *(Caminho de acesso: Contratos e Serviços » Arquivos)* os que estão com o campo **"ATIVO"** = 'NÃO'.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311269903767)

 Dentre esses, localize aqueles que ainda possuem produtos/serviços com ocorrência de ativação vigentes. Ou seja, que não possuem ocorrências de cancelamento ou suspensão vinculadas.

Localizado o(s) contrato(s) causador(es) da mensagem de validação, alinhe internamente qual o processo adequado:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311269908375)

 Ative o respectivo contrato ou lance as devidas ocorrências de cancelamento ou suspensão para seus produtos/serviços.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311277242519)

 Feito isso, será possível executar a rotina de** "[Reajuste de Contratos Ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos)".**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311277247511)

 CAUSA:**

Ao executar a rotina de Reajuste de Contratos Ativos, caso seja localizado algum contrato com o campo ATIVO=NÃO, porém com produtos/serviços que tenham ocorrências de ativação vigentes, será apresentada a mensagem.


---

### 🔗 Links e Referências Internas:

- [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos)
- [Reajuste de Contratos Ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos)