# Armazenando Produtos Recebidos em Endereço Flutuante

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112233-Armazenando-Produtos-Recebidos-em-Endere%C3%A7o-Flutuante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112233-Armazenando-Produtos-Recebidos-em-Endere%C3%A7o-Flutuante)  
> **ID:** `360045112233` | **Última Atualização:** 2026-07-29T14:15:25Z

---

A partir das configurações descritas abaixo, você poderá cadastrar e configurar um endereço especial flutuante, de modo que quando as quantidades forem fracionadas durante a geração das tarefas de armazenamento, estas sejam enviadas para o endereço flutuante, permitindo assim que somente as unidades fechadas sejam armazenadas nos endereços de picking e pulmões.

**Observação:** durante a geração das tarefas de armazenamento, será utilizada a maior unidade alternativa configurada para o produto para calcular a quantidade que será armazenada no endereço flutuante.

Primeiramente, ative o parâmetro **"Utilizar endereço flutuante no recebimento? - WMSUTILENDFLUT"** na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

Com o parâmetro ativado, na tela **"Preferências da Empresa"**, aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), informe no campo **"Cód. End. Flutuante"** o endereço flutuante, que previamente deve ser cadastrado na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento).

![empresa.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896084349847)

Na tela **"Cadastro de Produtos"**, aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abawms), realize a marcação do campo **"Utiliza endereço flutuante"**.

![produtos.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896123831063)

Além disso, na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaunidadesalternativas), configure a **"Unidade alternativa"** para o produto.

![unidade_alternativa.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896180524695)

Feitas as configurações acima citadas, sendo gerada uma Nota de Compra para o produto com uma quantidade que fracione a quantidade no volume alternativo, esta nota deve ser enviada para o Recebimento do WMS.

Realize a conferência e acesse a rotina [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento) para pré-visualizar as tarefas para este recebimento.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458063665815)

 Considere o seguinte exemplo:

Suponhamos que para um produto que possui a unidade alternativa LT (Lote) e unidade principal ML (Milheiro), foi solicitada na nota a quantidade de 10,4 ML; sabendo que, uma unidade do volume LT corresponde a 0,5 de ML, tem-se na conversão 20,8 LT.

Como o armazenamento é feito apenas de unidades fechadas no pulmão ou no picking, a diferença da quantidade fechada (0,8) é armazenada no endereço flutuante em unidade padrão (0,4 ML). O restante, 20 LT é armazenado no endereço de picking/pulmão.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)
- [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms)
- [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento)
- [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abawms)
- [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaunidadesalternativas)
- [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento)