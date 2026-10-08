# Base de Cálculo de Valor de Imposto na Importação de XML utilizando rateio de despesas acessórias por item.

> **Módulo:** Fiscal e Contábil | **Subseção:** Apuração de ICMS, IPI e ISS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360047495333-Base-de-C%C3%A1lculo-de-Valor-de-Imposto-na-Importa%C3%A7%C3%A3o-de-XML-utilizando-rateio-de-despesas-acess%C3%B3rias-por-item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047495333-Base-de-C%C3%A1lculo-de-Valor-de-Imposto-na-Importa%C3%A7%C3%A3o-de-XML-utilizando-rateio-de-despesas-acess%C3%B3rias-por-item)  
> **ID:** `360047495333` | **Última Atualização:** 2026-09-15T14:20:58Z

---

Para que a Base de Cálculo e o Valor do ICMS entre nosso sistema e o valor do XML não apresentem divergências ao realizar a importação do XML pelo [Portal de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354), você deverá realizar as configurações abaixo:

- No [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), o campo **"Cálculo de ICMS, IPI e ISS"** deverá estar com a opção **"Não calcula e digita"** selecionada;

- Ainda na TOP, na aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias), você deverá habilitar a marcação **"Importar o XML mantendo as despesas acessórias com os valores do XML"**, bem como selecionar todas as marcações de proporcionalização.

Com as configurações acima realizadas, as rotinas Portal de importação de XML, Confirmação da Nota e [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953) estarão aptas a efetuarem a Base de Cálculo e Valor do ICMS sem divergências.


---

### 🔗 Links e Referências Internas:

- [Portal de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354)
- [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias)
- [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953)