# The value ' ' of element 'cEANTrib' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625194-The-value-of-element-cEANTrib-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625194-The-value-of-element-cEANTrib-is-not-valid)  
> **ID:** `360042625194` | **Última Atualização:** 2026-07-22T16:08:33Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509856804631)

 MENSAGEM:**
cvc-pattern-valid: Value ' ' is not facet-valid with respect to pattern '[0-9]{0}|[0-9]{8}|[0-9]{12,14}' for type '#AnonType_cEANTribproddetinfNFeTNFe'.
cvc-type.3.1.3: The value ' ' of element 'cEANTrib' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509880454551)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509856814487)

 Acesse o cadastro do respectivo produto : Tela **"Produtos"** (Caminho de acesso:* Configurações » Cadastros » Produtos*)

- Aba: **"Impostos"**

- Campo **"EAN/GTIN produto p/ NF-e"**

**

![The_value_____of_element__cEANTrib__is_not_valid.png](https://ajuda.sankhya.com.br/hc/article_attachments/14606199117079)

**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509880463511)

 Avalie juntos aos responsáveis na sua empresa, **se esse produto possui um controle efetivo de Código EAN/GTIN. **Em caso negativo, o campo "EAN/GTIN Produto p/ NF-e" deve ser alterado para "**Não Informar**". Realizado esse ajuste, inutilize a numeração da respectiva NF-e, realize sua exclusão e uma nova emissão.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509880465687)

 Caso esse controle seja necessário, avalie as opções abaixo:

- 
**Código de Barras Estoque:** Caso esteja esta opção, informe um EAN/GTIN válido no campo "**Cód. de Barras"** da aba: "**ESTOQUE"**

- 
**Cód. Barras da Unid.Alternativa ou a Referencia:** Caso esteja esta opção, informe um EAN/GTIN válido no campo Código de Barras da aba: "**Unidades Alternativa"**

- 
**Referência:** Caso esteja esta opção, informe um EAN/GTIN válido no campo 'Referencia da aba: Geral'

- 
**Código do Produto:** Caso esteja esta opção, nada a fazer.

Realizado os devidos ajustes, inutilize a numeração da respectiva NF-e, realize sua exclusão e uma nova emissão.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509856823575)

 CAUSA:**

Quando for emitida uma NF-e e dentre os teus itens for informado na tag <cEANTrib> um código GTIN ( identificador para itens comerciais) inválido, a rejeição será apresentada. Visto que o Código de Barras (GTIN ou EAN) somente deve ser informado se tratar-se de um código válido e aceito.