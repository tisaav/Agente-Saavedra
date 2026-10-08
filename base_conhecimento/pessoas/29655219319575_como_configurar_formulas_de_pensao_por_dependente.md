# Como configurar fórmulas de pensão por dependente?

> **Módulo:** Pessoas+ | **Subseção:** Eventos e Regras de Cálculo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/29655219319575-Como-configurar-f%C3%B3rmulas-de-pens%C3%A3o-por-dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/29655219319575-Como-configurar-f%C3%B3rmulas-de-pens%C3%A3o-por-dependente)  
> **ID:** `29655219319575` | **Última Atualização:** 2026-09-27T14:18:34Z

---

### **Eventos**

Os eventos de pensão devem ter sequência de cálculo 4 (menor que do evento de IRRF da respectiva folha), ser do **Tipo Desconto** e ter a **Unidade** igual a **Quantidade**.

### **Fórmulas**

Essas **fórmulas representam uma sugestão de regra específica para cálculo de pensão alimentícia** com base na [Solução de Consulta COSIT nº 354/2014](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/59828), que trata dos casos em que a decisão judicial determina que o valor da pensão seja definido como um percentual da remuneração após a dedução do Imposto de Renda Retido na Fonte (IRRF).

Nessa situação, considerando que a própria pensão pode ser deduzida da base de cálculo do imposto, cria-se uma relação de interdependência entre os valores. Para resolver essa dependência, a fonte pagadora deve utilizar uma fórmula matemática que permita calcular corretamente ambos os valores de forma simultânea.

Ressalta-se que a utilização dessas fórmulas depende da determinação expressa na decisão judicial. Caso a decisão estabeleça critérios diferentes, a regra de cálculo deverá ser personalizada para atender ao que foi definido judicialmente.

⚠️ As fórmulas auxiliares devem ser criadas antes das fórmulas principais.

#### **1 - Pensão Normal/Rescisão**

Considere a legenda:

- 

**@E_INSS **- Característica do evento de INSS calculado na folha;

Caso seja MGEPessoal, ou o evento não possua característica, usar &E+código do evento (Exemplo &E9010).

- 

**@E_DEPENDENTESIRRF** - Característica do evento de dedução de dependente calculado na folha;

Caso seja MGEPessoal, ou o evento não possua característica, usar "&E+código do evento" (Exemplo &E999). 

- 
**&FXXXX** - Código da fórmula auxiliar de pensão nas férias (Exemplo &F9570).

**XXXX - Auxiliar 1 Folha Normal****

| ((FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'M', QueMovimento.SEQUENCIA) - ((IF(MemSetVar('BIrPen', (FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'M', QueMovimento.SEQUENCIA) - IF(isBaseSimplificadaMP1171(12), &VLRSIMPLIRRF + @E_INSS, @E_DEPENDENTESIRRFFER))) > 0, MemGetVar('BIrPen'), 0) * (FTF(2, 1, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB)/100)) - FTF(2, 2, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB))) * (QueMovimento.INDICE/100)) / (1 - ((QueMovimento.INDICE/100)* (FTF(2, 1, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB)/100))) |
| --- |

**YYYY - Pensão Folha Normal/Rescisão **(essa fórmula deverá ser associada ao evento de desconto de pensão)**

| IF((&TIPFOL='N') OR (&TIPFOL='R'), ((FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'M', QueMovimento.SEQUENCIA) - ((IF(MemSetVar('BIrPen', (FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'M', QueMovimento.SEQUENCIA) - IF(isBaseSimplificadaMP1171(12), &VLRSIMPLIRRF + @E_INSS, @E_DEPENDENTESIRRFFER))) > 0, MemGetVar('BIrPen'), 0) * (FTF(2, 1,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB)/100)) - FTF(2, 2,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB))) * (QueMovimento.INDICE/100)) / (1 - ((QueMovimento.INDICE/100)* (FTF(2, 1,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB)/100))),0) |
| --- |

**Fórmula Indice**

**

| QueMovimento.INDICE |
| --- |

 

#### **2- Pensão Folha de Férias**

Considere a legenda:

- 

**@E_PROVISAODEDESCONTOINSS** - Característica do evento de INSS calculado na folha;

Caso seja MGEPessoal, ou o evento não possua característica, usar &E+código do evento (Exemplo &E9330).

- 

**@E_DEPENDENTESIRRFFER** - Característica do evento de dedução de dependente calculado nas férias;

Caso seja MGEPessoal, ou o evento não possua característica, usar "&E+código do evento" (Exemplo &E998). 

- 
**&FXXXX **- Código da fórmula auxiliar de pensão nas férias (exemplo &F9570).

**XXXX - Auxiliar 1 Férias****

| ((FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'F', QueMovimento.SEQUENCIA) - ((IF(MemSetVar('BIrPen', (FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'F', QueMovimento.SEQUENCIA) - IF(isBaseSimplificadaMP1171(22), &VLRSIMPLIRRF + @E_PROVISAODEDESCONTOINSS, @E_DEPENDENTESIRRFFER))) > 0, MemGetVar('BIrPen'), 0) * (FTF(2, 1, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB)/100)) - FTF(2, 2, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB))) * (quemovimento.INDICE/100) / (1 - (quemovimento.INDICE/100)* (FTF(2, 1, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB)/100))) |
| --- |

**YYYY - Pensão Folha Férias **(essa fórmula deverá ser associada ao evento de desconto de pensão)**

| IF((&TIPFOL='F') , ((FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'F', QueMovimento.SEQUENCIA) - ((IF(MemSetVar('BIrPen', (FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'F', QueMovimento.SEQUENCIA) - IF(isBaseSimplificadaMP1171(22), &VLRSIMPLIRRF + @E_PROVISAODEDESCONTOINSS, @E_DEPENDENTESIRRFFER))) > 0, MemGetVar('BIrPen'), 0) * (FTF(2, 1,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB)/100)) - FTF(2, 2,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB))) * (quemovimento.INDICE/100)) / (1 - ((quemovimento.INDICE/100)* (FTF(2, 1,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB)/100))),0) |
| --- |

**Fórmula Indice**

**

| QueMovimento.INDICE |
| --- |

 

#### **3 - Pensão Décimo Terceiro**

Considere a legenda:

- 

**@E_INSS13SALARIO** - Característica do evento de INSS calculado na folha;

Caso seja MGEPessoal, ou o evento não possua característica, usar &E+código do evento (Exemplo &E9330). 

- 

**@E_DEPENDENTESIRRF13SAL** - Característica do evento de dedução de dependente calculado nas férias;

Caso seja MGEPessoal, ou o evento não possua característica, usar "&E+código do evento" (Exemplo &E998). 

- 
**&FXXXX** - Código da fórmula auxiliar de pensão nas férias (exemplo &F9570).

**XXXX - Auxiliar 1 Décimo Terceiro****

| ((FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'D', QueMovimento.SEQUENCIA) - ((IF(MemSetVar('BIrPen', (FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'D', QueMovimento.SEQUENCIA) - IF(isBaseSimplificadaMP1171(13), &VLRSIMPLIRRF + @E_INSS13SALARIO, @E_DEPENDENTESIRRF13SAL))) > 0, MemGetVar('BIrPen'), 0) * (FTF(2, 1, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB)/100)) - FTF(2, 2, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB))) * (quemovimento.INDICE/100) / (1 - (quemovimento.INDICE/100)* (FTF(2, 1, MemGetVar('BIrPen'), &REFEREPAGTO, QueFuncionario.TIPTAB)/100))) |
| --- |

**YYYY - Pensão Décimo Terceiro **(essa fórmula deverá ser associada ao evento de desconto de pensão)**

| IF((&TIPFOL='D') OR (&TIPFOL='R'), (FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC,'D',QueMovimento.SEQUENCIA) - ((IF(MemSetVar('BIrPen', (FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC,'D',QueMovimento.SEQUENCIA) - IF(isBaseSimplificadaMP1171(13), &VLRSIMPLIRRF + @E_INSS13SALARIO, @E_DEPENDENTESIRRF13SAL))) > 0, MemGetVar('BIrPen'), 0) * (FTF(2, 1,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB)/100)) - FTF(2, 2,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB))) * (quemovimento.INDICE/100) / (1 - ((quemovimento.INDICE/100)* (FTF(2, 1,(MemGetVar('BIrPen') - &FXXXX), &REFEREPAGTO, QueFuncionario.TIPTAB)/100))),0) |
| --- |

**Fórmula Indice**

**

| QueMovimento.INDICE |
| --- |

 

**Planilha Conferência dos 7 cálculos**

[https://docs.google.com/spreadsheets/d/1IM2GOBjFBiWWMdtKEPBjOVntn6WdSi5B/editusp=sharing&ouid=115559160932353771197&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1IM2GOBjFBiWWMdtKEPBjOVntn6WdSi5B/edit)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29655752612887)

 Acesse também:

[Cadastro de Dependente com Pensão Alimentícia](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Cadastro-de-Dependente-com-Pens%C3%A3o-Aliment%C3%ADcia)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Dependente com Pensão Alimentícia](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Cadastro-de-Dependente-com-Pens%C3%A3o-Aliment%C3%ADcia)