# Informar o local de saída do País somente no caso da exportação (NT2013/005)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042577174-Informar-o-local-de-sa%C3%ADda-do-Pa%C3%ADs-somente-no-caso-da-exporta%C3%A7%C3%A3o-NT2013-005](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042577174-Informar-o-local-de-sa%C3%ADda-do-Pa%C3%ADs-somente-no-caso-da-exporta%C3%A7%C3%A3o-NT2013-005)  
> **ID:** `360042577174` | **Última Atualização:** 2026-07-22T16:09:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473835749783)

 MENSAGEM:**

[356 - Rejeição]: Informar o local de saída do País somente no caso da exportação(NT2013/005). 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473835751959)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473835752599)

 Acesse a NF-e, verifique onde estão disponíveis os campos "**Local do Embarque"** ,"**UF Local Embarque"**, geralmente os campos estão dispostos na aba: "**Transporte"** do Rodapé da Nota.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14475123720855)

- 
Caso não esteja disponível para preenchimento, acesse com um usuário que tenha permissão a rotina: *'Comercial » Configuração » Configurador de Layout da Nota*, verifique qual é o Layout Utilizado na nota e disponibilize os 2(dois) campos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473835753367)

 Após o procedimento, volte a acessar a NF-e novamente e faça o devido preenchimento do Local e UF do Embarque, salve o cabeçalho da NF-e.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473851380503)

 Gere um novo Lote ou busque autorização, conforme status NF-e atual.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473835754775)

 CAUSA:**

Quando for emitida uma NF-e e o Grupo de Exportação for informado, mas o Tipo de Operação da NF-e for "0 - Entrada" e o Identificador de destino da operação for igual a "1 - Operação interna" ou "2 - Operação interestadual", será retornado a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473835756311)

 OBSERVAÇÃO:**

([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=jLEf0c3bSBI=)) - Nota Técnica.