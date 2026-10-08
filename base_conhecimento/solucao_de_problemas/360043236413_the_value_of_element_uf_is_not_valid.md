# The value '' of element 'UF' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043236413-The-value-of-element-UF-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043236413-The-value-of-element-UF-is-not-valid)  
> **ID:** `360043236413` | **Última Atualização:** 2026-07-22T16:05:59Z

---

** 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087849909015)

 MENSAGEM:**
cvc-enumeration-valid: Value '' is not facet-valid with respect to enumeration '[AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO, EX]'. It must be a value from the enumeration.
cvc-type.3.1.3: The value '' of element 'UF' is not valid.
 

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087849912471)

 SOLUÇÃO:**
Para correção deste erro, siga os passos abaixo
 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087849914903)

 Identifique os cadastros de cidades envolvidos na operação:

- Parceiro (Cabeçalho da nota)

- Transportadora (Aba Transporte)

- Cidade Emplacamento (Aba Transporte)

- Empresa (Cabeçalho da nota)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087847158295)

 Acesse o cadastro dos parceiros envolvidos *(Caminho de aceso: Configurações » Cadastros » Parceiros*)  e na aba endereço identifique a cidade vinculada. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087847160983)

 Acesse a tela **"[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)"** *(Caminho de aceso: Configurações » Cadastros » Endereços)* e para cada uma das cidades envolvidas no item 2, preencha o campo "**Cód. UF"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087849923479)

 Realizados os ajustes, teste uma nova geração de lote da nota.
 
**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087847168791)

CAUSA:**
Ocorre quando a informação UF estiver em branco para alguma cidade vinculada ao lançamento.


---

### 🔗 Links e Referências Internas:

- [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)