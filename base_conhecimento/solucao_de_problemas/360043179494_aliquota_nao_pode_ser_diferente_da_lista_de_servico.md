# Alíquota não pode ser diferente da lista de serviço

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179494-Al%C3%ADquota-n%C3%A3o-pode-ser-diferente-da-lista-de-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179494-Al%C3%ADquota-n%C3%A3o-pode-ser-diferente-da-lista-de-servi%C3%A7o)  
> **ID:** `360043179494` | **Última Atualização:** 2026-07-22T16:02:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148149832343)

 MENSAGEM:**

Alíquota não pode ser diferente da lista de serviço.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148149839127)

 SITUAÇÃO:**

Ao tentar transmitir uma NFS-e, ocorre a seguinte mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148173464471)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148149846423)

 Acesse: tela **"Serviços"** (*Caminho de acesso: Configurações » Cadastros » Produtos » Serviço*).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148173470615)

 Para os 'serviços' inseridos na NFS-e rejeitada, acesse a aba **Alíquota de ISS**  e verifique o "**Percentual de ISS"** cadastrado para a cidade do parceiro destinatário dos respectivos serviços:

 

![Percentual_ISS.png](https://ajuda.sankhya.com.br/hc/article_attachments/12611769814039)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148149852567)

 De acordo com o percentual de ISS acima, verifique junto a Prefeitura e/ou Contador, se esse está de acordo com o esperado.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148173476887)

 Caso o percentual esteja incorreto, realize os devidos ajustes e realize uma nova emissão da NFS-e.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148149866775)

 Caso o percentual **esteja correto**, verifique se a respectiva Prefeitura se enquadra na necessidade de envio do ISS com alíquota em percentual. Em caso positivo, inserir o** "Código IBGE"** no parâmetro abaixo:

- Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Configurações » Avançado » Preferências);

- Chave **"MUNALIQPERCNFSE"** - Cód.IBGE municípios c/ alíquota NFSe em percentual;

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148173486487)

 Após ajustes, gere um novo lote da nota de serviço.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148173489303)

 CAUSA:**

Ocorre quando a respectiva prefeitura não aceita o percentual de alíquota de ISS, fazendo com o que o sistema divida o % (percentual) por 100.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)