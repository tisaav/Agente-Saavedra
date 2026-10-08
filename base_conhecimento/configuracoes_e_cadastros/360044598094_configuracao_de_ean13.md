# Configuração de EAN13

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598094-Configura%C3%A7%C3%A3o-de-EAN13](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598094-Configura%C3%A7%C3%A3o-de-EAN13)  
> **ID:** `360044598094` | **Última Atualização:** 2026-07-29T13:47:05Z

---

```text

![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310634203031)

 **Módulo:** Configurações > Avançado
```

EAN-13 é um código de barras no padrão EAN - European Article Number definido pela [GS1 Brasil - Associação Brasileira de Automação](https://www.gs1br.org/), adaptado em mais de cem organizações membros GS1, para a identificação dos itens, principalmente nos pontos de venda a varejo. No EAN-13 o símbolo codifica treze números que estão divididos em quatro partes; dos treze dígitos, doze são dos dados referentes ao produto e um é o dígito verificador.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360081654473)

**Código EAN:** Este código corresponde a um valor inteiro que pode ser composto por um máximo de 9 dígitos. Esse código é fornecido pela EAN Brasil; geralmente quando a empresa não o possui, informa-se 12345678.

**Sequencial:** Tem-se aqui, um campo inteiro que é utilizado para a geração do código no [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-). Possui característica de ser negativo; neste caso, o código do produto é utilizado para compor o EAN13. Caso seja informado algum número maior ou igual a zero, será utilizado de forma sequencial para compor o código.

![](https://ajuda.sankhya.com.br/hc/article_attachments/360061915233)

As quatro partes que compõem o código são:

- País de origem do produto;

- Empresa fabricante;

- Produto por ela produzido;

- Dígito verificador.

A configuração dos campos Código EAN e Sequencial, corresponde aos campos NUMDEC e INTEIRO, quando na utilização do parâmetro **"Base de Cálculo do Cód. de Barras EAN13 - EAN13" **(tabela TSIPAR). 

Veja mais detalhes sobre o uso de código de barras na documentação do [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-)