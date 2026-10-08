# Total do COFINS difere do somatório dos itens sujeitos ao ICMS

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042643294-Total-do-COFINS-difere-do-somat%C3%B3rio-dos-itens-sujeitos-ao-ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042643294-Total-do-COFINS-difere-do-somat%C3%B3rio-dos-itens-sujeitos-ao-ICMS)  
> **ID:** `360042643294` | **Última Atualização:** 2026-07-22T16:07:23Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443873590551)

 ****MENSAGEM:**

[603 - Rejeição]: Total do COFINS difere do somatório dos itens sujeitos ao ICMS.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889846807)

 **SOLUÇÃO:**

Para correção siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889847447)

 Acesse o "****[Cadastro de Produtos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113):

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889848983)

 Aba: "**Impostos**", campo "**Grupo COFINS"** = Verificar o valor informado neste campo.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889849879)

 Vá até o Cadastro de **"**********[Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813)" e identifique através de um filtro por empresa, TOP, Parceiro e Tipo(Saída/Entrada), se existe uma regra devidamente cadastrada para o mesmo GRUPO que está informado no cadastro do(s) produto(s).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443873593111)

 Após os ajustes, fature novamente a nota ou redigite o item na nota e gere lote novamente.

 

** 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443873594519)

OBSERVAÇÕES:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889848983)

 Procure orientações do contador, quanto ao % de 'Alíquota de COFINS' e o 'Cód. sit. tributária:';

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889848983)

 Recomenda-se sempre criar regras específicas para o respectivo tipo de movimento;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889848983)

 O cálculo de PIS e COFINS é obrigatório para todas as movimentações de VENDA, mesmo que a incidência seja zero. Revisar a marcação de COFINS no Cadastro das Preferências da Empresa (*Comercial » Preferências » Empresa*) e no Cadastro de Tipos de Operação -TOP (*Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*) 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443889852439)

 **CAUSA:**

Quando for emitida uma NF-e com o total do COFINS da NF-e diferente do somatório do valor do COFINS de cada item, será retornado a rejeição

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443873594519)

OBSERVAÇÕES:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Produtos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)
- [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813)