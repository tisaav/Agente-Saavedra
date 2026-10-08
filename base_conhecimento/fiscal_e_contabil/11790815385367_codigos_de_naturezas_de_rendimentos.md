# Códigos de Naturezas de Rendimentos

> **Módulo:** Fiscal e Contábil | **Subseção:** Cadastros e Configurações Fiscais  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/11790815385367-C%C3%B3digos-de-Naturezas-de-Rendimentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/11790815385367-C%C3%B3digos-de-Naturezas-de-Rendimentos)  
> **ID:** `11790815385367` | **Última Atualização:** 2026-09-15T14:03:20Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312895576215)

 Módulo: **Livros Fiscais > Arquivos          

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312912192535)

 **Versão disponível:** a partir da 4.17
```

A partir de Abril/2023 será obrigatório transmitir os eventos do Grupo 4000 da [EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553) de acordo com os códigos de Naturezas de Rendimentos. 

Desse modo, nesta tela se encontram todos os Códigos de Naturezas de Rendimentos disponibilizados pela RFB que serão utilizados para geração dos eventos do Grupo 4000 da EFD Reinf e nela será possível alterar e incluir, caso tenha novos códigos que serão associados aos cadastros de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) e [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553).

![Códigos-de-naturezas-de-rendimentos.png](https://ajuda.sankhya.com.br/hc/article_attachments/18299151012887)

Para cadastrar os Códigos de Naturezas de Rendimentos, acione o botão 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16284241263383)

** "Inserir novo código"** e preencha o **"****Código Natureza Rendimento"** e a **"****Descrição Natureza Rendimento"**. 

### **Aba Geral**

Efetue as marcações quando houver, **"****Fundo ou Clube de Investimento"**, **"Décimo Terceiro"** e **"****Rendimento Recebido Acumuladamente"**.

Caso haja algum tipo de dedução ou rendimento isento, informe o código nos campos **"Tipo de Dedução" **e **"Tipo Rendimento Isento"**, respectivamente. Havendo mais de um código, utilize o ponto e vírgula (;) para separá-los. 

No campo **"Tipo Tributo"** informe os tipos de impostos referentes aos Tipos Rendimento Isento separados por ponto e vírgula (;).  Sendo eles: IR, CSLL, COFINS, PP, Agreg.

O campo **"Bloco de aplicação"** indicará qual o evento de aplicação correspondente conforme o código de natureza inserido no campo, sendo esses:

- 4010;

- 4020;

- 4040; 

- 4080.

Determine o** "Local de Aplicação" **dentre as opções** "Ambos"**, **"****Financeiro"** ou **"****Serviço"**.

Indique as **"****Datas"** de início e fim da validade desses códigos.

Habilite a marcação **"****Ativo"** para validar o código cadastrado.

Efetue a marcação **"Gerar sem tributação?"** quando o campo Tipo Tributo estiver vazio, conforme determinação da Receita Federal, assim, poderá ser enviado tanto nota sem retenção de impostos, considerando apenas o valor bruto da nota, como financeiro, considerando apenas valor do desdobramento do título, no [EFD - Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553-EFD-Reinf). Nesse caso, os demais campos de valores da sub-aba Documentos, aba Rendimentos, do grupo de eventos 4000 na tela EFD REINF, serão gerados zerados. Porém, quando a marcação estiver desligada, indicando que o rendimento sofre tributação normalmente, o sistema irá validar se há retenções nas tabelas de impostos para gerar os dados no arquivo.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18299418263063)

 A fim de evitar retorno de erro da Receita Federal, utilize a marcação acima apenas nas condições citadas.

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)
- [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553)
- [EFD - Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553-EFD-Reinf)