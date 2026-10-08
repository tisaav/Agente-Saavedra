# Valor do campo "Cód. Tipo de Assinante" deve estar entre 1 e 6

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110694-Valor-do-campo-C%C3%B3d-Tipo-de-Assinante-deve-estar-entre-1-e-6](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110694-Valor-do-campo-C%C3%B3d-Tipo-de-Assinante-deve-estar-entre-1-e-6)  
> **ID:** `360044110694` | **Última Atualização:** 2026-07-22T15:53:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16647259453591)

 MENSAGEM:**

[CORE_E00913]:  Valor do campo "Cód.Tipo de Assinante" deve estar entre 1 e 6.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16647281489047)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16647281500439)

 Verifique na tela **"Empresa"** *(Caminho de acesso: Comercial » Preferências), aba 'Livros Fiscais' » Nota Fiscal de Comunicação/Telecomunicação" » **Cód.Tipo de Assinante:***

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14765535470743)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16647259466647)

 Defina esse campo de acordo com a necessidade da empresa, com uma das opções abaixo:

1 - Comercial/Industrial
2 - Poder Público
3 - Residencial/Pessoa física
4 - Público
5 - Semi-Público
6 - Outros

Quando a opção** "Permite informar Assinante na Central?"** estiver desmarcada, o sistema pegará o número informado no campo **"Cód.Tipo de Assinante" **do tipo de assinante e o informará em seu correspondente no Pedido/Nota.

Se a opção Permite informar Assinante na Central? estiver marcada, o sistema trará o campo para Central de Compras e Central de Vendas sem preenchimento para o usuário informá-lo. Estes campos serão visualizado em conformidade ao que for disposto no[Configurador de Layout da Nota.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)

**Nota:** Estes dados são de responsabilidade do usuário/empresa.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16647281506839)

 IMPORTANTE: **

Para as notas lançadas antes da configuração feita na empresa, será necessário ajuste via banco de dados, setando a informação na tabela. Ou, relançar as notas, setando a marcação "Permite informar Assinante na Central" e preencher o campo ao efetuar o lançamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16647281511575)

CAUSA:**

Mensagem retornada quando realizada a emissão/lançamentos de notas com Modelo de Documento 20 ou 21 e não informado o Cód.Tipo de Assinante.


---

### 🔗 Links e Referências Internas:

- [Configurador de Layout da Nota.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)