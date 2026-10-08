# 1019 Rejeição: Valor do Imposto Seletivo difere do calculado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095694855959-1019-Rejei%C3%A7%C3%A3o-Valor-do-Imposto-Seletivo-difere-do-calculado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095694855959-1019-Rejei%C3%A7%C3%A3o-Valor-do-Imposto-Seletivo-difere-do-calculado-nItem-999)  
> **ID:** `37095694855959` | **Última Atualização:** 2026-08-24T16:48:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095680312215)

 **MENSAGEM**

1019 Rejeição: Valor do Imposto Seletivo difere do calculado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095680312855)

 **SITUAÇÃO**

A nota fiscal foi emitida com divergência no valor do Imposto Seletivo informado no documento, em relação ao valor esperado para o enquadramento aplicado, resultando na rejeição pelo sistema.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095680313879)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095680314391)

 Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se o NCM está cadastrado corretamente, especialmente se o produto pertencer aos grupos sujeitos ao Imposto Seletivo (códigos 2401, 2402, 2403, 2404, 2203, 2204, 2205, 2206, 2208).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095694845975)

 Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique as configurações do Imposto Seletivo para o produto em questão.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095694846871)

 Confira se o **"Código de situação tributária - CST"** do Imposto Seletivo está corretamente configurado para o produto e operação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095694847767)

 Verifique se a **"Base de Cálculo"** (vBCIS) e a **"Alíquota"** (pIS) do Imposto Seletivo estão corretamente informadas.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095694849303)

 Certifique-se de que o cálculo do valor do Imposto Seletivo está seguindo a fórmula: **vIS = vBCIS * (pIS / 100)**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095694850071)

 Após realizar as correções necessárias, tente emitir a nota fiscal novamente.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095694850583)

 **CAUSA**

A causa desta rejeição está relacionada à **inconsistência no cálculo do Imposto Seletivo**. De acordo com a regra de validação UB11-10 para os modelos 55/65, o valor do Imposto Seletivo (vIS) deve ser igual à Base de Cálculo (vBCIS) multiplicada pela Alíquota (pIS) dividida por 100.

Esta inconsistência pode ocorrer devido a:

- 

Erro na configuração da alíquota do Imposto Seletivo

- 

Erro no cálculo da base de cálculo do Imposto Seletivo

- 

Arredondamento incorreto dos valores

- 

Configuração inadequada do CST do Imposto Seletivo

- 

Falha na aplicação da fórmula de cálculo do Imposto Seletivo

A Lei Complementar 214 de 16 de janeiro de 2025, que implementa a Reforma Tributária, estabelece novas regras para o Imposto Seletivo, e o sistema precisa estar corretamente configurado para calcular este imposto de acordo com as normas vigentes.