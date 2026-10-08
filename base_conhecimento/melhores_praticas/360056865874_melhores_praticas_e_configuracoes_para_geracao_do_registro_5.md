# Melhores Práticas e Configurações para Geração do Registro 53 - Sintegra - MGE/Mitra

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360056865874-Melhores-Pr%C3%A1ticas-e-Configura%C3%A7%C3%B5es-para-Gera%C3%A7%C3%A3o-do-Registro-53-Sintegra-MGE-Mitra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056865874-Melhores-Pr%C3%A1ticas-e-Configura%C3%A7%C3%B5es-para-Gera%C3%A7%C3%A3o-do-Registro-53-Sintegra-MGE-Mitra)  
> **ID:** `360056865874` | **Última Atualização:** 2026-07-22T15:27:02Z

---

**Caso de Uso:**
 
A empresa possui uma 'Nota Fiscal de Compra', na qual o fornecedor não somou o ST no total, neste caso é preciso gerar um documento 'GNRE' e também uma despesa no financeiro referente ao ST. Para isto deve-se configurar no sistema.
 
**Outros artigos relacionados:**

- [Melhores Práticas para Configuração e Cálculo do Garantido Integral (GNRE - Compra).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580314)

- [Associar autenticação do DAE e GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014)

**Vejamos as configurações que envolvem o processo:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16250296934423)

 Acesse o MGE Configurações*, Menu>>Arquivos>>Endereços>>UFs*
Campo: **Parceiro Secretaria da Receita Estadual** = [Preencher este com o código do parceiro, devidamente já cadastrado]

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360096534054)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16250296936983)

 Acesse o MGE Financeiro*, Menu>>Avançado>>Preferencias>>Empresa*
Aba: Fiscal
Campo: Gerar GNRE p/ ST [marcado]

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360098849453)

Aba: Inscrição Estadual de Contribuinte Substituto Tributário no Estado Destinatário
Campo: Gerar GNRE p/ ST [marcado]

Preencher  Código e Descrição da UF e Inscrição Estadual.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360096535454)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16250276435095)

 MGE Configurações, Financeiro ou Estoque, acesse a tela de Parâmetros em *Avançado>>Preferencias>>Todas as Preferências*

Parâmetro TIPTITGNREST (TIPO DE TÍTULO da GNRE p/ST) - Informar neste parâmetro o código do '*Tipo de Título', que será usado para a GNRE.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/360096535694)

**O cadastro de Tipo de Título é acessado em **MGE Financeiro>>Arquivos>>Cadastros>>Tipos de Titulo>>Tipos de Titulo***

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16250296945303)

 Acesse o MGE Financeiro, *Menu>>Rotinas>>Associar Autenticação do Documento de Arrecadação*

Nesta tela apresentará os títulos que possuem o 'Tipo de Título' igual ao valor do parâmetro TIPTITGNREST e que tenham o campo 'Histórico' vazio.

Na parte superior, pode ser utilizado o filtro rápido por Empresa e/ou Parceiro.
Ao 'Aplicar', os títulos serão apresentados, para que seja digitado no histórico as informações da GNRE. Após as atualizações do histórico, ao aplicar, os títulos não serão apresentados novamente.
 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16250276441495)

 Acesse o MGE Estoque, *Menu>>Arquivos>>Produtos*
Aba: Impostos
Campo: Produto constante no apêndice I do RCTE/GO = [marcado]

 
 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16250296950039)

 Acesse o MGE Estoque, *Menu>>Arquivos>>Cadastros>>Tipos de Operação*
Aba: Validações
Gerar GNRE p/ ST = [marcado]

**Nota**: Esta opção estará habilitada somente para 'Pedido de Compra' e de 'Venda', 'Nota de Compra' e de 'Venda'.
 
A geração do financeiro da nota pegará a 'Parcela' do 'Tipo de Negociação', que esteja com o 'Tipo de Título' igual ao parâmetro TIPTITGNREST. Se a 'Empresa' e a TOP estiverem marcadas para "Gerar GNRE p/ ST?", se a Nota possuir valor de ST, o sistema gerará um financeiro de despesa, para o 'Parceiro da Secretária da Receita Estadual' da UF de destino, e com o valor da ST.
 
Caso não seja possível, o sistema encontrar o 'Parceiro da Secretária da Receita Estadual', a parcela não será gerada.
 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16250296954135)

 Acesse o MGE Livros, *Menu>>Conexão>>Sintegra*
Registros Opcionais>>Marcar a opção 55-GNRE

 
Funcionalidade:  Gerar o registro 55, para os títulos de despesas baixados, com a data da baixa dentro do período informado, com o 'Tipo de Título' igual ao do parâmetro TIPTITGNREST, que não seja uma provisão.
 

**Condição**: Não será gerado o registro 53 - Substituição Tributária "Sintegra" se: O campo "Produto constante no apêndice I do RCTE/GO" for igual a 'SIM'; a movimentação for de 'Entrada', onde a UF da empresa seja GO e a UF do Parceiro também seja GO; e o 'Valor de ST', não somar ao total da nota.


---

### 🔗 Links e Referências Internas:

- [Melhores Práticas para Configuração e Cálculo do Garantido Integral (GNRE - Compra).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580314)
- [Associar autenticação do DAE e GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014)