# Nota com Diferimento de ICMS, e proporcionalização de ICMS Para o Frete

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36500284707223-Nota-com-Diferimento-de-ICMS-e-proporcionaliza%C3%A7%C3%A3o-de-ICMS-Para-o-Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/36500284707223-Nota-com-Diferimento-de-ICMS-e-proporcionaliza%C3%A7%C3%A3o-de-ICMS-Para-o-Frete)  
> **ID:** `36500284707223` | **Última Atualização:** 2026-07-22T14:22:53Z

---

##### **

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570922197399)

 SITUAÇÃO:**

Ao emitir uma Nota de Venda sujeita à **Tributação 51 – Diferimento,** o é esperado é que o **ICMS do Frete (ICMSFRETE)** siga o mesmo critério aplicado ao **ICMS do item**, garantindo consistência entre os valores calculados na **TGFITE (itens)** e na **TGFCAB (cabeçalho)**.

No entanto, em alguns cenários, o ICMSFRETE **não considera o deferimento**, mesmo que o ICMS do item esteja correto.

Esse comportamento gera **divergência entre os valores exibidos na grade de itens e na totalização da nota (TGFDIN X TGFCAB)**, dificultando a confirmação do documento.

 

##### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570931702551)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570931703191)

 Acesse a tela ****[''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570931703703)

 No campo **''Chave ou Descrição'' **pesquise** **pelo parâmetro **''****GALQICMSFRTPROP''.**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570922199703)

 Abra a configuração e altere o campo **''Ligado/Desligado'' **para** ''Desligado''**.

 

![ICMS.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570922200471)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570922201111)

 Recalcule o item da nota.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570922202007)

 O ICMS do Frete será ajustado e ficará coerente com os valores da TGFITE.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36570922205335)

 **CAUSA: **

O comportamento está relacionado ao parâmetro** **''GALQICMSFRTPROP''** – “Garantir alíq. de ICMS de Frete proporcional ao IPI?”**.

Quando esse parâmetro está **ligado (valor padrão)**, o sistema prioriza a proporcionalização do ICMS do frete **com base no IPI**, e não com base no diferimento do ICMS aplicado do item.

Por isso, mesmo que o item esteja com diferimento configurado corretamente, o frete continua sendo calculado **integralmente**, sem considerar o percentual de diferimento.


---

### 🔗 Links e Referências Internas:

- [''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)