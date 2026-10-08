# Como realizar o cálculo proporcional de PIS/COFINS para Frete

> **Módulo:** Fiscal e Contábil | **Subseção:** Apuração de ICMS, IPI e ISS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26556855929495-Como-realizar-o-c%C3%A1lculo-proporcional-de-PIS-COFINS-para-Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/26556855929495-Como-realizar-o-c%C3%A1lculo-proporcional-de-PIS-COFINS-para-Frete)  
> **ID:** `26556855929495` | **Última Atualização:** 2026-09-15T14:21:31Z

---

```text

![versão FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312522356375)

 Esta funcionalidade está disponível a partir da versão 4.29.
```

Conheça nesse artigo como gerar os Registros D101 e D105 no SPED Contribuições, considerando a base de cálculo proporcional aos itens tributados da NF-e.

### **Configurações iniciais**

#### **Preferências da Empresa**

Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), acesse a aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) e ative a marcação **"Calcula PIS e Cofins na confirmação do financeiro"**.

![Marcação Calcula PIS e Cofins na confirmação do financeiro acionada.png](https://ajuda.sankhya.com.br/hc/article_attachments/26558821888535)

Ainda na mesma tela, acesse a aba [EFD-Escrituração Fiscal Digital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaefdescrituraofiscaldigital). No campo **"Tipo de Escrituração"**, selecione **"EFD Contribuições"**. Na sub-aba **"Blocos e Registros"**, certifique-se de que as seguintes opções estão marcadas como** "Gerar Registro"**:

- Registro D100 - AQUISIÇÃO DE SERVICOS DE TRANSPORTES (CODIGOS 07, 08, 8B, 09, 10, 11, 26, 27 E 57);

- Registro D101 - COMPLEMENTO DO DOCUMENTO DE TRANSPORTE - PIS/PASEP;

- Registro D105 - COMPLEMENTO DO DOCUMENTO DE TRANSPORTE - COFINS.

![Blocos e Registros.png](https://ajuda.sankhya.com.br/hc/article_attachments/26558837577367)

#### **Cadastro da TOP**

Acesse o cadastro do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) com o** "Tipo de Movimento"** = **"I-Financeiro"**. Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), marque a opção **"Calcula PIS/COFINS por percentual das notas"**.

![Cadastro da TOP.png](https://ajuda.sankhya.com.br/hc/article_attachments/26558925209239)

#### **Cadastro da Natureza de Receitas e Despesas**

Acesse o cadastro da [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas) do frete. Na aba [PIS/COFINS Todas Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#Abapis/cofinstodasempresas) ou na aba [Natureza x PIS/COFINS X Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#abanaturezapiscofinsempresa), configure o CST e as alíquotas de PIS/COFINS.

![Cadastro da Natureza de Receitas e Despesas.png](https://ajuda.sankhya.com.br/hc/article_attachments/26559125647383)

### **Geração do Registro D101 e D105**

O cálculo proporcional de PIS/COFINS sobre o frete pode ser realizado de duas maneiras:

#### **1) Importação de CT-e em TOP Financeira**

Acesse o [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) e, nas [Preferências para Importar CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e), realize as configurações abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26559549251991)

 No campo **"Tipo de Operação"** da seção **"Movimentação Financeira"**, selecione a TOP com o **"Tipo de Movimento"** = **"I-Financeiro"**.

![Tipo de Operação.png](https://ajuda.sankhya.com.br/hc/article_attachments/26559549262999)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26559645735447)

 Na seção **"Exigência de Vínculos"**, defina o campo **"Exige vínculo com notas"** com a opção **"Exige"**.

![Exigência de Vínculos.png](https://ajuda.sankhya.com.br/hc/article_attachments/26561835888407)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26559629333783)

 Realize a importação do CT-e vinculando-o a uma NF-e já existente no sistema. 

**Exemplo:** NF-e de Compra com dois produtos, sendo um tributado pelo PIS/COFINS e outro não.

![NF-e de Compra com dois produtos.png](https://ajuda.sankhya.com.br/hc/article_attachments/26564373426839)

Na tela Portal de Importação de XML, o CT-e será importado na TOP Financeira e vinculado à NF-e.

![CT-e importado.png](https://ajuda.sankhya.com.br/hc/article_attachments/26565077968919)

A consulta dos impostos de PIS/COFINS pode ser realizada através da opção [Consultar/Alterar Dados do Imposto Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es#Consultar/AlterarDadosdoImpostoFinanceiro), presente no botão [Mais Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Maisop%C3%A7%C3%B5es) da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). 

**

![ConsultarAlterar Dados do Imposto Financeiro.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584005253655)

**

Ao gerar o EFD Contribuições, na tela [EFD - Contribuições PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4407916885271-EFD-Contribui%C3%A7%C3%B5es-PIS-COFINS), a base de cálculo do PIS/COFINS sobre o frete será proporcional conforme o cálculo no sistema.

![EFD Contribuições.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584005254423)

Na aba **"D001"**, sub-aba **"D105"**, pode-se conferir o **"Vlr. base cálc. da COFINS"**.

![Vlr. base cálc. de COFINS.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584005254935)

#### 
**2) ****Lançamento de Frete Extra Nota pela Central de Compras**

![Lançamento de Frete Extra Nota pela Central de Compras.png](https://ajuda.sankhya.com.br/hc/article_attachments/26583973438871)

Ao confirmar a nota, será exibida a tela para lançar o financeiro do frete.

![lançamento do financeiro do frete.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584400629399)

Certifique-se de que os campos** "Tipo Operação"**, **"Tipo de Título"** e **"Natureza"**, estão devidamente preenchidos.

![lançamento do financeiro do frete 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584390264599)

Realize a baixa do título para que o cálculo proporcional seja realizado. Depois pode-se realizar a consulta dos impostos de PIS/COFINS através da opção [Consultar/Alterar Dados do Imposto Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es#Consultar/AlterarDadosdoImpostoFinanceiro), presente no botão [Mais Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Maisop%C3%A7%C3%B5es), da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). 

![Consultar-Alterar Dados do Imposto Financeiro2.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584400637463)

Ao gerar o EFD Contribuições, na tela [EFD - Contribuições PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4407916885271-EFD-Contribui%C3%A7%C3%B5es-PIS-COFINS), o valor de base para PIS/COFINS desse frete será proporcional conforme o cálculo no sistema.

![PIS-PASEP.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584400638999)

Na aba **"D001"**, sub-aba **"D105"**, pode-se conferir o **"Vlr. base cálc. da COFINS"**.

![COFINS.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584400639767)

### **Memória de cálculo**

Realize o cálculo do PIS conforme a memória de cálculo abaixo. Pode-se aplicar o mesmo procedimento ao COFINS, ajustando apenas os valores e a alíquota correspondente.

![Memória de cálculo.png](https://ajuda.sankhya.com.br/hc/article_attachments/26584459905815)

Para mais detalhes, acesse a planilha [Cálculo Proporcional de PIS/COFINS para Frete](https://docs.google.com/spreadsheets/d/1ZzgmFPRGPeFxUHrQ9hA_4gZBKonyQYd9JSEx69522r8/edit?gid=0#gid=0).

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)
- [EFD-Escrituração Fiscal Digital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaefdescrituraofiscaldigital)
- [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)
- [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas)
- [PIS/COFINS Todas Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#Abapis/cofinstodasempresas)
- [Natureza x PIS/COFINS X Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#abanaturezapiscofinsempresa)
- [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)
- [Preferências para Importar CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e)
- [Consultar/Alterar Dados do Imposto Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es#Consultar/AlterarDadosdoImpostoFinanceiro)
- [Mais Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Maisop%C3%A7%C3%B5es)
- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)
- [EFD - Contribuições PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4407916885271-EFD-Contribui%C3%A7%C3%B5es-PIS-COFINS)