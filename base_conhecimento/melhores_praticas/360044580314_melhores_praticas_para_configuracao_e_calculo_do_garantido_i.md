# Melhores Práticas para Configuração e Cálculo do Garantido Integral (GNRE - Compra)

> **Módulo:** Melhores Praticas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580314-Melhores-Pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-Garantido-Integral-GNRE-Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580314-Melhores-Pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-Garantido-Integral-GNRE-Compra)  
> **ID:** `360044580314` | **Última Atualização:** 2026-07-22T15:51:07Z

---

Este Programa foi instituído pelo Decreto nº 512/2007. O **Icms Garantido Integral** é um regime especial de apuração do imposto, que consiste na cobrança antecipada do imposto relativo às operações tributadas a serem realizadas no Estado, pelos estabelecimentos inscritos no Cadastro de Contribuintes do Estado.

Veja Como configurar o Garantido Integral - Processo válido para Movimentação de **COMPRA**

- 1º - Comercial » Arquivo » Cadastros » Observações para Notas

Crie uma observação.Os campos: 'Num. Processo', 'Origem Processo', 'Vincular DAE/GNRE' e restantes, não são obrigatórios o preenchimento.

- 2º - Configurações » Cadastros » Impostos

Crie um Imposto. Preencha: Nome, Descrição.
Ativo = [SIM]
Tipo Imposto = [Marcar, conforme o critério desejado]

Os demais campos do cabeçalho e das subs-abas(Parceiro, TOP, Empresa, Grupo de Produto, Produto e Serviço), não precisam ser configurados.

- 3º- Configurações » Avançado » Preferências

- 
**Tipo de Título p/indicar GNRE p/S.T. - TIPTITGNREST':** Configure esse parâmetro com o tipo de título que será usado para gerar a GNRE.

- 4º-  Comercial » Preferências » Empresa » Aba Propriedade

![Ambiente GNRE 15-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20582632881687)

**Após o lançamento e a aprovação da nota que resulte no cálculo do DIFAL, é necessário gerar o lote na tela a seguir. É importante observar que, caso alguma das configurações mencionadas acima esteja ausente, as informações financeiras relacionadas a essa nota não serão exibidas na tela para a geração do lote.**

 

**Parâmetros:**

1. CODOBSGARANTIDO = [Preencher com o código da Observação, do 1º item]

1. CODIMPGARANTIDO = [Preencher com o código do Imposto, do 2º item]

1. TIPTITGNREST = [Não poderá conter o mesmo título do 'Garantido Integral'] - No caso da compra o parâmetro TIPTITGNREST não pode ser igual ao tipo de titulo informando na aba parcelas do Tipo de Negociação criado para parcela que contenha a fórmula;

- 4º- Comercial » Arquivo » Cadastros » Tipos de Negociação

Crie um Tipo de Negociação, na aba Parcelas, faça a seguinte configuração:

2(Duas) Parcelas ou mais, sendo:
1ª Parcela, informar Prazo, Banco, Tipo de Titulo(qualquer um), Percentual 100%.

No campo: 'Formula', use a seguinte expressão:
**VALORIMPOSTO(XX,'V')**

Onde XX é o código do Imposto criado no 2º item.
**V** de Valor do Imposto
**B** de Base do Imposto
**A** de Alíquota do Imposto

As demais parcelas, podem ser criados sem Formula e rateado o percentual de acordo com a quantidade de parcelas, que sera considerado para formar o Valor total da Nota.

- 5º - Configurações » Cadastros » Produtos » Produtos

Aba: Imposto

Campos: 

1. Tipo de substituição:[Subst. na compra e na venda]

1. Calcular ICMS:[Marcado]

- 6º - Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Crie uma Regra de ICMS Interestadual, seguindo a Exceção desejada para a Nota de Compra.

Aba: **Geral**
Tributação: 10-Tributada e c/ cobrança por substituição
Alíquota= [Informe o Percentual]
Modalidade BC ICMS = [Valor da Operação]
Observação= [**Preencher com o código da Observação, do 1º item**]

Aba: **Substituição Tributaria**
Margem Lucro (MVA) = [Informe o percentual]
Aliq. Subst. Tributária = [Informe o percentual]
Modalidade BC ICMS ST= [Margem Valor Agregado(%)]

Os demais campos não são obrigatórios e não interferem no processo.

 

**Vejamos o Lançamento de uma Nota de COMPRA:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196429699607)

 No Rodapé, haverá a incidência do ICMS em campos próprios, e Base e Valor de ICMS-ST, será zerado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196429702039)

 Haverá a incidência do calculo do ICMS-ST via 'Outros Impostos', destacando os valores.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196429702679)

 No Lançamento da Nota de Compra, haverá destacado 'em separado' no Financeiro da nota o valor da Guia da GNRE, referente ao ICMS-ST.

 

**-Veja também:**

[Melhores Práticas para Configuração e Cálculo do ICMS-ST Extra Nota (GNRE - Venda).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094153)


---

### 🔗 Links e Referências Internas:

- [Melhores Práticas para Configuração e Cálculo do ICMS-ST Extra Nota (GNRE - Venda).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094153)