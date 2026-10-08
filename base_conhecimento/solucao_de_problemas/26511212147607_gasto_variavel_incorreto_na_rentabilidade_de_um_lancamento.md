# Gasto Variável incorreto na rentabilidade de um lançamento

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26511212147607-Gasto-Vari%C3%A1vel-incorreto-na-rentabilidade-de-um-lan%C3%A7amento](https://ajuda.sankhya.com.br/hc/pt-br/articles/26511212147607-Gasto-Vari%C3%A1vel-incorreto-na-rentabilidade-de-um-lan%C3%A7amento)  
> **ID:** `26511212147607` | **Última Atualização:** 2026-07-22T14:41:46Z

---

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 Ao analisar a rentabilidade de um lançamento e se deparar com o gasto variável calculando de forma incorreta, analise algum dos pontos abaixo para entender o cálculo.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26511212133015)

 Para realizar o cálculo será necessário uma nota de exemplo, para que seja substituído na fórmula do Gasto Variável abaixo:

 

```text
GASTO VARIÁVEL = IMPOSTO - ST A RECUPERAR + OUTROS GASTOS + COMISSÃO
```

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **Impostos:** ICMS + PIS + COFINS + CSLL (da Nota)

**Observação:** para que o sistema considere o ICMS no cálculo, é necessário que no cadastro do produto, aba **"Impostos"**, esteja marcado o campo **"Considerar débito ICMS nas consultas gerenciais?"**.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **ST a recuperar:** objeto customizável pela função no banco de dados SNK_GET_ST_RECUPERAR(), por padrão traz **zero **como resultado.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **Outros gastos: **Embalagem + Frete + Juro + Destaque - Desconto

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **Comissão:** é preenchida de acordo com as preferências do GOL - Gerente Online. Acesse as **"Preferências"**, aba **"Margem de Contribuição"** e verifique o quadrante Comissão. 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26511212136727)

 Se mesmo realizando o cálculo com a fórmula acima o valor não bater, analise os parâmetros abaixo:

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **CALGAVARCENPORT - Funo p/ Calculo Gasto Variavel Central/Portal**

Caso esteja preenchido com alguma informação, significa que o cálculo do gasto variável não está sendo realizado de forma nativa, mas sim por um objeto personalizado criado no banco de dados. Neste caso, para manutenção, verifique com quem criou ou com a unidade responsável.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

** EXTRAGASTVAR - Gasto variável **

O parâmetro afeta a forma de uso das despesas acessórias para compor os **outros gastos** citado na fórmula do passo 1.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26511212138007)

 **Se ligado:**

Embalagem = Valor da Embalagem + IPI da Embalagem - ICMS da Embalagem

(O ICMS da embalagem só é descontado se o tipo de IPI da embalagem for INCLUSO)

Frete = Se o frete for incluso é usado o (valor do frete bruto),

Se o frete for CIF é usado o (valor do frete - ICMS do frete)

**Observações: **Juro, Destaque e desconto não são considerados com este parâmetro ligado.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26511212138007)

Se desligado:**

Embalagem = Se IPI da Embalagem = INCLUSO, então Valor da Embalagem + IPI da Embalagem + ICMS da Embalagem.

Frete = Se Tipo do Frete = INCLUSO ou CIF, então usamos o Valor do Frete, se não usamos ZERO.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **CALCDINRENT - Calcular impostos para Análise de Rentabilidade?**

Quando estiver habilitado, o cálculo de "PIS/COFINS/CSLL" (quando existir) na nota, será considerado na análise de rentabilidade. O parâmetro habilitado/desabilitado não define o cálculo dos impostos, mas define a participação destes na Análise de Rentabilidade.

Outro detalhe do parâmetro é que quando ligado ao abrir a tela de **"Análise de Rentabilidade na Central"**, serão calculados os impostos da nota. Impostos como PIS e COFINS são calculados apenas na confirmação da nota, mas com este parâmetro ligado serão calculados quando abrir a Análise de Rentabilidade.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **HABALIQESPICMS - Habilita config. de alíquota de ICMS gerencial**

Caso seja habilitado, o sistema desconsidera o ICMS de item isento (Suframa), do cálculo.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

 **ATUALCOMITE - Atualizar Comissão por item?**

Caso este parâmetro esteja ativado, o sistema considera a comissão registrada na grade de itens para compor o Gasto Variável. Se estiver desativado, será considerada a comissão inserida no cabeçalho da nota para estruturar o gasto. Para as notas antigas (lançadas antes da ativação do parâmetro), o sistema não considera a comissão na formação do Gasto Variável. Além disso, como a ativação do parâmetro não dispara o recálculo de comissão, a rentabilidade do item só observará o percentual do item para as notas com comissão calculada ou recalculada após a ativação do mesmo.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450249616279)

** LANCCOMMULT - Lançar Comissão p/Múltiplos Vendedores?**

Se trabalha com comissão ultima o sistema não busca mais a comissão da grade de itens conforme citado no parâmetro acima, mas sim a comissão dos múltiplos vendedores informados na nota (TGFCCM).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29601372639511)

 Ao analisar todas as configurações, use uma nota e um item de exemplo substituindo todos os valores no fórmula para realizar o cálculo.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26570919769751)

**CAUSA:**

É necessário analisar as configurações acima para que os valores sejam substituídos na formula, chegando ao correto cálculo.