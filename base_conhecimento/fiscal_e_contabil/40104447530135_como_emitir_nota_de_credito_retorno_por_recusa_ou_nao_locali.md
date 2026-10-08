# Como emitir Nota de Crédito — Retorno por recusa ou não localização (Tipo 03)

> **Módulo:** Fiscal e Contábil | **Subseção:** Nota fiscal de crédito  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/40104447530135-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-recusa-ou-n%C3%A3o-localiza%C3%A7%C3%A3o-Tipo-03](https://ajuda.sankhya.com.br/hc/pt-br/articles/40104447530135-Como-emitir-Nota-de-Cr%C3%A9dito-Retorno-por-recusa-ou-n%C3%A3o-localiza%C3%A7%C3%A3o-Tipo-03)  
> **ID:** `40104447530135` | **Última Atualização:** 2026-09-09T11:43:53Z

---

**Módulo:** Comercial › Rotinas

**Caminho de acesso:** `Menu Principal › Comercial › Rotinas › Portal de Vendas`

## O que é e para que serve

Use a Nota Fiscal de Crédito (Tipo 03) quando a entrega de um bem material não se concretizar por recusa total do cliente ou por não localização do destinatário. Neste processo, você (fornecedor) emite a nota para realizar o desfazimento automático do débito destacado na nota original, resolvendo a falta de sincronia entre o fato gerador da circulação e o da entrega efetiva. 

**Não use este processo para mercadorias efetivamente recebidas pelo cliente (nestes casos, use a nota de devolução padrão - Finalidade 4).**

## Antes de começar

Localize o documento fiscal original de fornecimento para o devido referenciamento. Em seguida, configure o [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e a tributação.

### Configuração do Tipo de Operação (TOP)

Acesse o Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e configure:

- 
**Tipo de Movimento:** selecione D (Devolução de Venda).

- 
****[Aba Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)**:** selecione Despesas (para estornar/compensar a venda original no contas a receber).

- 
****[Aba Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)**:** no campo **Atualização do Estoque**, selecione Entrar (essencial para registrar a entrada física do bem que retornou).

- 
****[Aba Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)**:** no campo **Atualização de Livro ICMS**, selecione Livro de Entrada. Utilize o CFOP contrário à operação que será retornada.

- 
****[Aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)**:** marque as opções **Tem CBS** e **Tem IBS** na seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF).

- 
****[Aba NF-e / NFC-e / CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)**:** em **NF-e**, selecione 5 - Nota de Crédito. Em **Tipo de Nota de Crédito**, selecione 03 - Retorno por recusa total na entrega ou por não localização do destinatário.  Marque a opção **Buscar NF de origem p/referenciar na NFe** para que os documentos relacionados sejam gerados corretamente no XML do DFe.

### Configuração da Tributação (IBS e CBS)

Acesse as telas de [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria) e [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria) e configure a exceção com:

- 
**CST e Classificação Tributária (cClassTrib):** utilize os mesmos aplicados no documento de fornecimento original.

- 
**Alíquotas:** informe as alíquotas vigentes, garantindo que sejam idênticas às da nota de fornecimento.

## Como emitir a nota

1. Acesse o ****[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas).

1. Localize o documento fiscal referente à venda que está retornando.

1. Selecione a nota e clique em ****[Dev/Est](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Tela-Portal-de-Vendas#devolucao-venda).

1. No pop-up, selecione a TOP configurada.

1. Selecione os itens que não foram entregues.

1. Confirme que você consta como emitente e mantenha o cliente como destinatário.

1. Finalize a emissão e salve a nota.

****

| Nota É obrigatório referenciar a chave de acesso da nota original. O valor do crédito apropriado é limitado ao valor total de IBS destacado na nota referenciada. O cliente deve realizar o evento de "Operação não Realizada” ou “Desconhecimento da Operação”, e o transportador o evento de "Insucesso de entrega". |
| --- |

## Pontos de atenção

### Estrutura do XML

Para validação correta, o XML conterá obrigatoriamente a tag de referência (`NFref`) e o destaque no grupo (`gIBSCBS`), sinalizando à apuração assistida o cancelamento total do débito de um fornecimento não ocorrido legalmente:

```text

<ide>
    <finNFe>5</finNFe>
    <tpNFCredito>03</tpNFCredito>
    <NFref>
        <refNFe>44-CHAVE-DA-NOTA-DE-VENDA-ORIGINAL-44</refNFe>
    </NFref>
</ide>
<det nItem="1">
    <imposto>
        <IBSCBS>
            <CST>xxx</CST>
            <cClassTrib>xxxxxx</cClassTrib>
            <gIBSCBS>
                <vBC>xx.xx</vBC>
                <vIBS>x.xx</vIBS>
                <vCBS>x.xx</vCBS>
            </gIBSCBS>
        </IBSCBS>
    </imposto>
</det>

```


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Aba Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)
- [Aba Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)
- [Aba Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)
- [Aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF)
- [Aba NF-e / NFC-e / CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)
- [Alíquotas de IBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria)
- [Alíquotas CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895-Cadastro-de-Al%C3%ADquotas-CBS-Reforma-Tribut%C3%A1ria)
- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
- [Dev/Est](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Tela-Portal-de-Vendas#devolucao-venda)