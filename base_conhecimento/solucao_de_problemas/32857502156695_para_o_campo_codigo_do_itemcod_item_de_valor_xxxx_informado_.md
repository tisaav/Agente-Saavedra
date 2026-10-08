# Para o campo código do item(COD_ITEM), de valor xxxx, informado no registro C185 deve existir pelo menos um registro H010 com o mesmo valor para o campo 02 - COD_ITEM

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32857502156695-Para-o-campo-c%C3%B3digo-do-item-COD-ITEM-de-valor-xxxx-informado-no-registro-C185-deve-existir-pelo-menos-um-registro-H010-com-o-mesmo-valor-para-o-campo-02-COD-ITEM](https://ajuda.sankhya.com.br/hc/pt-br/articles/32857502156695-Para-o-campo-c%C3%B3digo-do-item-COD-ITEM-de-valor-xxxx-informado-no-registro-C185-deve-existir-pelo-menos-um-registro-H010-com-o-mesmo-valor-para-o-campo-02-COD-ITEM)  
> **ID:** `32857502156695` | **Última Atualização:** 2026-07-22T14:30:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33145465995159)

 MENSAGEM **

Para o campo código do item(COD_ITEM), de valor xxxx, informado no registro C185 deve existir pelo menos um registro H010 com o mesmo valor para o campo 02 - COD_ITEM cujo Registro pai H005 tenha o campo 04 - MOT_INV igual a 06 e o campo DT_INV igual ao

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33145504383895)

 **SITUAÇÃO **

Essa mensagem indica uma **inconsistência entre o registro C185 e o bloco H (inventário)** na sua EFD (Escrituração Fiscal Digital).

**Exemplo:** há um **registro C185** com o `COD_ITEM = xxxx`. E a validação está dizendo que:

**"Esse mesmo código de item (xxxx) precisa estar presente no bloco H010**, que representa itens do inventário."

 

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33147385420823)

 **Acesse também:** Para entender a geração do** C185** e demais veja o artigo [Manual configuração para geração dos registros restituição do ICMS ST - MG](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057819854-Manual-configura%C3%A7%C3%A3o-para-gera%C3%A7%C3%A3o-dos-registros-restitui%C3%A7%C3%A3o-do-ICMS-ST-MG)

 

#### **

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33147372860695)

Pré-requisitos:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33147385425175)

 Um **registro H010** com o campo `COD_ITEM = 31857`;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33147385425175)

O **H010** deve estar **vinculado a um registro H005** onde: 

- Campo 04 – `MOT_INV` (motivo do inventário) seja **"06"** → Inventário na mudança de período de apuração do ICMS;

- Campo `DT_INV` (data do inventário) seja o **dia anterior ao **`**DT_INI**`** do registro 0000** (início do período da EFD).

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33147372866839)

SOLUÇÃO**

Há duas formas de resolver essa questão no Sankhya, sendo elas: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33147372870295)

 Garantir que o produto xxxx tenha cópia/contagem na data do inventário na tela ''**Geração EFD - Fiscal ICMS/IPI Restituição/Complementação de ST'**', no campo ''**data do Inventário**''. 

É possível verificar se o produto em questão foi gerado ou não na cópia/contagem por meio de uma consulta **TGFCTE. **

**Exemplo:**  > SELECT * FROM TGFCTE WHERE CODPROD=XXXX AND REFERENCIA='XX/XX/XXXX' 

Substitua o 'XXXXX' pelo código do produto e pela data respectivamente

- Se o produto não existir na** TGFCTE,** na data de inventário usada para gerar o **C185**, é necessário fazer uma cópia/contagem que inclua esse produto.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33147372874135)

 Se o produto existir na **TGFCTE**, porém a quantidade for zero, verifique na tela ''**Gerência de Produtos''** em quanto o saldo desse item finalizou na data do inventário usado para geração do C185 (pela tela Geração EFD - Fiscal ICMS/IPI Restituição/Complementação de ST, no campo data do Inventário). Se existir a linha com valor zero, é necessário ligar o parâmetro **GERH30EST0**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32857502155031)

 

Ao ligar este parâmetro, o sistema irá gerar os registros H010 e H030 mesmo com quantidade 0 para fins de amparo do C185.


---

### 🔗 Links e Referências Internas:

- [Manual configuração para geração dos registros restituição do ICMS ST - MG](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057819854-Manual-configura%C3%A7%C3%A3o-para-gera%C3%A7%C3%A3o-dos-registros-restitui%C3%A7%C3%A3o-do-ICMS-ST-MG)