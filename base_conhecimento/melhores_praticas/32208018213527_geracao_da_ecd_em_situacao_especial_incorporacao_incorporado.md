# Geração da ECD em situação especial - Incorporação/ Incorporadora

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32208018213527-Gera%C3%A7%C3%A3o-da-ECD-em-situa%C3%A7%C3%A3o-especial-Incorpora%C3%A7%C3%A3o-Incorporadora](https://ajuda.sankhya.com.br/hc/pt-br/articles/32208018213527-Gera%C3%A7%C3%A3o-da-ECD-em-situa%C3%A7%C3%A3o-especial-Incorpora%C3%A7%C3%A3o-Incorporadora)  
> **ID:** `32208018213527` | **Última Atualização:** 2026-07-22T14:31:53Z

---

Em situações especiais, como **incorporação, cisão, fusão ou extinção**, **deverá ser transmitido mais de uma ECD para o mesmo CNPJ no mesmo ano-calendário. No entanto,**** cada uma deve ter naturezas diferentes de escrituração** e obedecer regras específicas.

 

![Geração da ECD em situação especial - Incorporação 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/32481121676055)

 

![Geração da ECD em situação especial - Incorporação 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/32481121676951)

 

### **Exemplo prático: Incorporação em 15/07/2024**

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32480838879639)

 Arquivo 1**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32480831657367)

Os **campos de situação especial e data do evento** no registro 0000 devem estar preenchidos corretamente na empresa incorporadora. Para isso, acesse a tela **"Empresa" ***(Contabilidade » Preferências » Empresa), *vá até a aba **"ECD - Escrituração Contábil Digital"**, em seguida, sub-aba **"Situação Especial" **e informe a data e a situação especial. 

 

![Geração da ECD em situação especial - Incorporação 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/32481121678103)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32480831657367)

Depois, vá até a tela **"Geração de arquivo - ECD" ***(Contabilidade » Conexão » ECD » Geração de Arquivo - ECD) *e informe a data. **Importante destacar que a data limite deve ser a data em que aconteceu a situação especial. **

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32480831657367)

Em seguida, no campo **"Indicador de sit. início do período" **informe opção **"0 - Normal ( Início do primeiro dia do ano)".**

 

![Geração da ECD em situação especial - Incorporação 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/32481114536215)

 

|0000|LECD|01012023|15072023|EMPRESA TESTE|11111111000199|AM||3534401|99999|3|0|0|0||0|0||N|N|0|0|1|

Campo 11 – Situação Especial: 3 (corresponde a incorporação no período)

Campo 12 – Indicador de Situação no Início do Período: 0 (Normal) 

 

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32480838879639)

 Arquivo 2**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32480831657367)

 Para geração do arquivo 2, não se informa a situação especial nas preferências da empresa. Informe somente na tela Geração de arquivo - ECD. **Atente-se para que a data inicial do arquivo 2 seja o primeiro dia posterior ao final da geração do arquivo 1** (por exemplo, como o arquivo 1 tinha data final 15/07/2024, a data inicial do arquivo 2 será 16/07/2024).

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32480831657367)

E no campo Indicador de sit. início do períodos selecione a opção **"2 - Resultante de cisão/ fusão ou remanescente de cisão, ou realizou incorporação"**

 

![Geração da ECD em situação especial - Incorporação 5.png](https://ajuda.sankhya.com.br/hc/article_attachments/32481121680663)

 

Campo 11 – Não há situação especial no período. 

Campo 12 – Indicador de Situação no Início do Período: 2 (Resultante de cisão)

|0000|LECD|16072023|31122023|EMPRESA TESTE|11111111000199|AM||3534401|99999||2|0|0||0|0||N|N|0|0|1|