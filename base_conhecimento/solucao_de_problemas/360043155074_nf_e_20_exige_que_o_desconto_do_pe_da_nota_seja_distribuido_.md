# NF-e 2.0 exige que o desconto do pé da nota seja distribuído entre os itens

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043155074-NF-e-2-0-exige-que-o-desconto-do-p%C3%A9-da-nota-seja-distribu%C3%ADdo-entre-os-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043155074-NF-e-2-0-exige-que-o-desconto-do-p%C3%A9-da-nota-seja-distribu%C3%ADdo-entre-os-itens)  
> **ID:** `360043155074` | **Última Atualização:** 2026-07-22T16:03:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16144884916247)

 MENSAGEM:**

[CORE_E02337] NF-e 2.0 exige que o desconto do pé da nota seja distribuído entre os itens.

Existe um parâmetro (DISTJDCONF ou DISTDESCNFE) que automatiza esta distribuição.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16144898036759)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16144884922135)

 Se inserido desconto no rodapé da nota, conforme obrigatoriedade da SEFAZ, faz-se necessário que um dos parâmetros abaixo seja ligado, para que ocorra a distribuição do valor de desconto entre os itens, conforme parametrização.

Para tal, acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** *(Caminho de acesso: Configurações » Avançado » Preferências)*

- Chave** "DISTDESCNFE"**

- Quando habilitado, na aprovação de uma NF-e o sistema não irá validar o desconto máximo do produto e vai ratear o desconto lançado no cabeçalho para o(s) produto(s).

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409312548503)

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16144884923927)

 Acesse: Tela** "[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** *(Caminho de acesso: Configurações » Avançado » Preferências)*

- Chave **"DISTJDCONF"**

- Se estiver "Sim", será utilizado para ratear o desconto entre os itens do pedido/nota de acordo com o percentual de desconto máximo definido no cadastro de produtos. Os campos de desconto na área de "totais" da nota aplicarão um desconto apenas sobre os produtos que aceitam desconto. Exemplo: 1 produto - R$ 100,00 não aceita desconto. 2 produto - R$ 20,00 aceita desconto. Se for dado um desconto de 20%, o valor correspondente será de R$4,00, aplicado apenas ao produto 2. Caso todos os produtos permitam descontos porém em percentuais diferentes, o sistema calcula o desconto proporcionalmente. Se o desconto ultrapassar o limite máximo dos itens aparecerá a seguinte mensagem : "Não existem produtos para rateio".

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409312562967)

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16144884926359)

 **Realizado o ajuste de um dos parâmetros acima, conforme processo atual, siga com o lançamento da respectiva NF-e.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16144898048535)

 CAUSA:**

Ocorre quando é informando valor de desconto no rodapé da nota e os parâmetros "**DISTJDCONF"** e "**DISTDESCNFE"** estão desligados.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)