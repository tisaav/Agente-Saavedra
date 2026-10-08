# Ajuste de Estoque por Série

> **Módulo:** Suprimentos e Estoque | **Subseção:** Inventário  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117673-Ajuste-de-Estoque-por-S%C3%A9rie](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117673-Ajuste-de-Estoque-por-S%C3%A9rie)  
> **ID:** `360045117673` | **Última Atualização:** 2026-07-29T14:49:50Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312634539671)

 Módulo: **Inventário > Arquivo          
```

Esta rotina, realiza o ajuste de estoque por série, ou seja, é uma opção que será utilizada por empresas que controlam seu estoque através do controle adicional de estoque por Série.

[Configurações](#configura%C3%A7%C3%B5es)                                            [Processo](#processo)                                            [Regras](#regras)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084366753)

O controle por série, no controle adicional de estoque, é uma ferramenta muito útil para empresas que têm controle do Item e não do Produto.

Após a cópia e contagem, alguns produtos podem apresentar diferenças, sendo necessário ajustar o estoque no sistema. Estas diferenças demandam recontagens. 

Dependendo do volume, pode ser necessária uma sindicância, a fim de descobrir as causas das diferenças, que podem ser:

- Notas sem registro no sistema;

- Algum local sem contagem;

- Erro de digitação;

- Erro de anotação;

- Erro na inadimplência de produto;

- Roubo;  

Para utilizar a funcionalidade de Ajuste de Estoque por Série, você deve selecionar a **"Empresa"**, a data de **"Cópia"** e **"Contagem"** e ajustar, podendo gerar uma nota de entrada e/ou saída.

## 
Configurações

Antes de efetuar o Ajuste de Estoque por Série, é necessário que você configure as Empresas com os modelos das notas em [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos), e indique o campo **"Tipo Operação" **que será utilizada na geração da nota.

O [Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado para o ajuste, deve estar configurado na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), campo **"Tipo de Emissão"** como "de Ajuste", para que o status vá corretamente para o Histórico da Série.

Depois de configurados os modelos, você deverá acessar a tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba** **[Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo) e indicar os modelos de nota de entrada e saída:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084366833)

Após configuração dos modelos e gerada a cópia e a contagem dos produtos por série, você pode efetuar o ajuste.

Outra opção para configurar os modelos, é através dos parâmetros abaixo:

- Nota Modelo Ajuste Estoque (Entrada) - NOTAENTAJUSTEST;

- Nota Modelo Ajuste Estoque (Saída) - NOTASAIAJUSTEST.

[[voltar ao topo]](#top)

## 
Processo

Uma vez posicionado na tela Ajuste de Estoque Por Série, informe a **"Empresa"** em que será feito o ajuste; você pode filtrar por **"Produto"** ou **"Local"**, ou ainda fazer filtros personalizados conforme desejar.

Informe a opção que o sistema buscará para compor o **"Preço Unitário" **do produto na nota de ajuste que for gerada, de acordo com as seguintes opções:

- Usar o preço informado na TOP;

- Preço de Venda;

- Último Custo de Reposição;

- Último Custo Variável.

 

**Seção Datas**

Informe no campo **"Cópia"**, a data da Cópia do Estoque.

Insira no campo** "Contagem"**, a data da Contagem do Estoque.

**Observação:** Se não houver Cópia ou Contagem nas datas informadas, o sistema exibirá uma mensagem; ao clicar na lupa 

![lupa.png](https://ajuda.sankhya.com.br/hc/article_attachments/8757140333463)

, é possível visualizar quais são as datas em que foram realizadas as cópias/contagens.

[[voltar ao topo]](#top)

## 
Regras

- Se o produto com série estiver na cópia e não estiver na contagem, será gerada uma nota de Saída;

- Se o produto com série estiver na contagem e não estiver na cópia, será gerada uma nota de Entrada.

Informe as datas da Contagem e da Cópia; defina o Preço Unitário a ser utilizado nas notas de ajuste, e pressione o botão **"Ajustar"**, para que sejam lançados na Nota de Ajuste, os produtos que precisam ser ajustados.

Nesta opção, o sistema fará automaticamente a funcionalidade do botão **"Gerar zero para produtos inexistentes na Contagem ou na Cópia"**. Desta forma, para cada Série que existir na Cópia e não existir na Contagem, será criada uma linha na Contagem com estoque zero para referenciar a linha existente na Cópia e, da mesma forma, para Séries que existirem na Contagem e não existirem na Cópia. As Séries existentes na Cópia e não existentes na Contagem, serão lançadas na Nota de Saída; Séries existentes na Contagem e não existentes na Cópia, serão lançadas na Nota de Entrada.

Depois de informados os dados necessários para a geração do ajuste, a tela com os números únicos da nota de saída e entrada que forem gerados, se apresentará. Com o duplo clique na linha desejada, é possível abrir a nota selecionada.

[[voltar ao topo]](#top)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251274647447)

 Acesse também:

[Contagem de Estoque por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609614)

[Cópia de Estoque por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609674)


---

### 🔗 Links e Referências Internas:

- [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)
- [Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa)
- [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo)
- [Contagem de Estoque por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609614)
- [Cópia de Estoque por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609674)