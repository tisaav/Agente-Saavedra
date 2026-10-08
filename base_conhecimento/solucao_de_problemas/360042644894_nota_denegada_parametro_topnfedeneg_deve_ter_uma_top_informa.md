# Nota Denegada - parâmetro TOPNFEDENEG deve ter uma TOP informada

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042644894-Nota-Denegada-par%C3%A2metro-TOPNFEDENEG-deve-ter-uma-TOP-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042644894-Nota-Denegada-par%C3%A2metro-TOPNFEDENEG-deve-ter-uma-TOP-informada)  
> **ID:** `360042644894` | **Última Atualização:** 2026-07-22T16:07:18Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400033943)

 MENSAGEM:**

[CORE_E01230] Nota Denegada. Parâmetro TOPNFEDENEG deve ter uma TOP informada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400035607)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400039319)

 Vincule no cadastro da TOP utilizada na emissão da respectiva NF-e um Tipo de Operação NF-e DENEGADA, conforme detalhado abaixo:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334385375511)

 Tela **"[Tipos de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"*** (Caminho de acesso: Comercial » Arquivo » Cadastros), aba*** "[NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)"**: 

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334385375895)

 Tipo Operação NF-e Denegada**: A TOP informada aqui irá sobrepor as TOPS informadas no parâmetro **"TOPNFEDENEG"**. Isto será necessário quando a operação da NF-e for diferente das operações das TOPS informadas neste parâmetro (normalmente TOPS de Venda, Compra, Devoluções etc.).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400040471)

 Após criação da TOP Denegada e inserção em seu devido campo, consulte a situação atual da nota no botão NF-e.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400038679)

**** OBSERVAÇÕES:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400039319)

 Usualmente, a configuração da TOP Denegada é uma 'duplicação' da TOP utilizada na operação, porém com ressalvas:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334385375511)

 Financeiro: Não atualiza

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334385375511)

 Estoque: Não atualiza

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334385375511)

 Livro: Não atualiza

As atualizações são retiradas para que seja desfeito o processo realizado na TOP anterior, realizando a "anulação" desta nota.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400040471)

 Caso a nota de origem é advinda de pedidos, é necessário que o parâmetro **"DENEGDEIXAPEND"** esteja habilitado. Pois, somente com tal parâmetro habilitado, é possível refaturar o pedido após os ajustes da IE, seja do emitente ou destinatário.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334385379607)

 A TOP Denegada a ser vinculada no campo mencionado acima, deve ter o mesmo** Tipo de Movimento** da TOP utilizada no lançamento. Exemplo: Se emitida uma NF-e de Devolução de Compra, e essa for denegada pela SEFAZ, será necessário cadastrar uma **Top Denegada** com o Tipo de movimento DEVOLUÇÃO DE COMPRA.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400041367)

 Caso não possua essa TOP configurada, valide se existe uma "padrão" com tipo de movimento 'Venda' devidamente cadastrada, duplicando a mesma e ajustando o tipo de movimento conforme desejado. Certifique que esse cadastro padrão foi realizado e validado junto a um consultor e encontra-se de acordo com o esperado. Caso contrário o direcionamento para criação dessa TOP será realizado para sua Filial.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334400042647)

 CAUSA:**

Ocorre quando o parâmetro não esta configurado com o código da TOP de Denegada.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)