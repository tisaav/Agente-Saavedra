# 301 Rejeição: O NCM do produto predominante da carga lotação deve ser informado - MDF-e

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35299279582615-301-Rejei%C3%A7%C3%A3o-O-NCM-do-produto-predominante-da-carga-lota%C3%A7%C3%A3o-deve-ser-informado-MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/35299279582615-301-Rejei%C3%A7%C3%A3o-O-NCM-do-produto-predominante-da-carga-lota%C3%A7%C3%A3o-deve-ser-informado-MDF-e)  
> **ID:** `35299279582615` | **Última Atualização:** 2026-07-22T14:25:35Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35299279573527)

 **MENSAGEM:**

301 Rejeição: O NCM do produto predominante da carga lotação deve ser informado

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35299279574551)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35308206107799)

 Acesse a tela de **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)), em seguida, abra a viagem que está sendo apresentada a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35308206111383)

 Depois, na viagem em questão, vá até a aba** "MDF-e",** sub aba **"Produto Predominante" **e preencha as informações referente ao produto predominante que está sendo transportado. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35299257550615)

 

**Após o preenchimento dessas informações, será gerado o grupo de TAGs <prodPred> no arquivo XML do MDF-e. **

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35299257551895)

CAUSA:**

A rejeição acontece se o campo NCM do grupo "produto predominante" (prodPred) não for informado nos casos em que: 

- 
**Modal for rodoviário e o Tipo de Emitente (tpEmit) for:**

  - Prestador de Serviço de Transporte (tpEmit=1) ou

  - Transportador com CT-e Globalizado (tpEmit=3) ou

  - Transportador Próprio (tpEmit=2) que informou o tipo de transportador (tpTransp)

- E o **MDF-e tiver apenas um documento fiscal (DF-e) no grupo infDoc**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35333255407127)

 Para **mais informações sobre os ajustes necessários para adequação à Nota Técnica 2025.001 v1.02** acesse o artigo: ****[Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência.](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503)


---

### 🔗 Links e Referências Internas:

- [Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência.](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503)