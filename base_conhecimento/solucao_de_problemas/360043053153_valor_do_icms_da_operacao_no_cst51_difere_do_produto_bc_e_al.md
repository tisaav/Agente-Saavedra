# Valor do ICMS da Operação no CST=51 difere do produto BC e Alíquota

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043053153-Valor-do-ICMS-da-Opera%C3%A7%C3%A3o-no-CST-51-difere-do-produto-BC-e-Al%C3%ADquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043053153-Valor-do-ICMS-da-Opera%C3%A7%C3%A3o-no-CST-51-difere-do-produto-BC-e-Al%C3%ADquota)  
> **ID:** `360043053153` | **Última Atualização:** 2026-07-22T16:09:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474399295127)

 MENSAGEM:**

[351] - Valor do ICMS da Operação no CST=51 difere do produto BC e Alíquota.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474399296407)

 SOLUÇÃO:**

 Identifique a regra de ICMS parametrizadas para o respectivo lançamento (Campo '**'Cód.Alíq.ICMS'**).

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474422304279)

 Acesse: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*, busque a respectiva regra e valide junto ao Contador as configurações abaixo:

- Tributação

- Alíquota

- % de Outorga/Diferimento

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14499770400151)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474422305047)

 Realizada a validação das informações acima, redigite o cabeçalho da nota e gere um novo lote. 

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458198611223)

 Caso essa rejeição ocorra no lançamento de nota de nacionalização verifique as possibilidades abaixo:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474422304279)

 Crie uma alíquota de ICMS UF de Origem 'EX' e UF de destino com o Estado desejado.

- Informe a % de Outorga/Diferimento correspondente ao lançamento.

- No Tipo de Operação utilizado, aba Impostos, configure o campo Cálculo de ICMS, IPI e ISS: como calcula e digita: com essa configuração o sistema fará o cálculo de diferimento corretamente e o usuário poderá realizar o ajuste dos demais impostos manualmente.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474422305047)

 Mantenha a configuração do "****[Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) como "**Cálculo de ICMS, IPI e ISS"** = Não calcula e digita' e faça o lançamento do imposto seguindo as orientações:

- No lançamento dos itens preencha os campos CFOP e Tributação.

- Em 'Itens' » Outras opções » Consultar/Alterar Dados do Imposto do item: faça o lançamento do ICMS preenchendo os seguintes campos:
> Imposto = ICMS
> Incidência = Produto
> Base de cálculo = valor do produto
> Base cálc.reduzida = Base de cálculo
> Alíquota = valor desejado
> Valor = tem que ser o valor devido para que o sistema possa fazer o calculo e % do diferimento.

Usando a segunda opção o sistema não calcula nada de forma automática, sendo necessário informar manualmente todos os impostos pertinentes a operação.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474399303191)

 IMPORTANTE:**

No lançamento manual, vale conferir se o campo 'Tributação' dos itens foi devidamente lançado = 51, além de conferir o campo CFOP (Iniciado em 3);

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474422312471)

 CAUSA:**

Quando for emitida uma NF-e, com CST de ICMS igual a **51 **- "Diferimento" e o Valor do ICMS da Operação (<vICMSOp>) for diferente da multiplicação da 'Base de Cálculo' (<vBC>) * a Alíquota (<pICMS>), será retornado a rejeição.


---

### 🔗 Links e Referências Internas:

- [Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)