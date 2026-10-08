# O campo 'Quantidade' deve ser maior que zero

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043147094-O-campo-Quantidade-deve-ser-maior-que-zero](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043147094-O-campo-Quantidade-deve-ser-maior-que-zero)  
> **ID:** `360043147094` | **Última Atualização:** 2026-07-22T16:04:06Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969160855)

 MENSAGEM:**

[CORE_E03234] O campo 'Quantidade' deve ser maior que zero.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969189015)

CAUSA:**

Essa situação é causada pela inserção de itens com o campo 'quantidade' em branco/zero e o parâmetro  **'Aceita quantidade zero em notas de complemento - QTDZEROCPL'** desligado ou sem nenhuma TOP informada no parâmetro '**TOP para aceitar Qtd. igual a zero - TOPQTDZERO'**.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969169687)

 SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143961867031)

 **Ao lançar o item na nota certifique-se de que a 'quantidade' foi informada no campo correto. 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969176599)

 Caso a nota a ser lançada seja uma NF-e complementar, que não tem a obrigatoriedade de informar a quantidade, habilite o parâmetro:  **'Aceita quantidade zero em notas de complemento - QTDZEROCPL'**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969178135)

 Para habilitar o parâmetro acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** *(Caminho de acesso: Configurações » Avançado).*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969178135)

 Busque pela chave **'Aceita quantidade zero em notas de complemento - QTDZEROCPL'** e defina como 'Ligado":

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/9354367930391)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143961879703)

 **Inclua a TOP utilizada no processo dentro do Parâmetro '**TOP para aceitar Qtd. igual a zero - TOPQTDZERO'.** Lembrando que se houver mais de uma TOP inclusa no Parâmetro é necessário separa-las por ; e sem espaçamento entre elas, para que assim o sistema reconheça as TOPs dentro do Parâmetro.

**Por exemplo:** TOP 1116 E TOP 1117, no parâmetro devem estar preenchidas da seguinte forma: 1116, 1117.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969178135)

 Para habilitar o parâmetro acesse a tela **"Preferências"** *(Caminho de acesso: Configurações » Avançado).*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969178135)

 Busque pela chave '**TOP para aceitar Qtd. igual a zero - TOPQTDZERO'** e informe a TOP desejada:

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9354335471639)

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143969187223)

 **ATENÇÃO:**

Parâmetros que poderão interferir nessa rotina:

**"ACEITARVLRZERO":** aceita valor total igual a zero?
**"VLRUNITZERONFE":** Permite valor unitário zero para NF-e?

 

**Observação:** Quando for necessário tornar o campo Valor total dos itens editável, nas operações que envolva conversão de moedas, é crucial que o parâmetro '**TOP para aceitar Qtd. igual a zero - TOPQTDZERO'** não possua um valor informado."


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)