# 1170 Rejeição: Grupo de Ajuste de Competência não informado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096950124951-1170-Rejei%C3%A7%C3%A3o-Grupo-de-Ajuste-de-Compet%C3%AAncia-n%C3%A3o-informado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096950124951-1170-Rejei%C3%A7%C3%A3o-Grupo-de-Ajuste-de-Compet%C3%AAncia-n%C3%A3o-informado-nItem-999)  
> **ID:** `37096950124951` | **Última Atualização:** 2026-07-22T14:21:02Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096947414679)

 **MENSAGEM**

1170 Rejeição: Grupo de Ajuste de Competência não informado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096947416087)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) com um CST que exige o preenchimento do grupo de ajuste de competência, o documento foi rejeitado pela SEFAZ porque este grupo obrigatório não foi informado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096950104471)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096950105751)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a operação utilizada na nota fiscal rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096950107543)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se os campos **"Tipo de Nota Fiscal de Crédito"** e/ou **"Tipo de Nota Fiscal de Débito"** estão configurados corretamente para a operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096947420055)

 Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária" **(Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096947421847)

 Verifique se o **Código de Situação Tributária (CST) **do item realmente exige o Ajuste de Competência.

- O sistema só permite esse grupo se o indicador do código for igual a 1 (`ind_gAjusteCompet = 1`)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37962783770135)

 Na seção **''Impostos''**, inclua as informações do grupo de ajuste de competência, preenchendo os valores de IBS e/ou CBS conforme necessário.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096947424663)

 Certifique-se de que pelo menos um dos valores (IBS ou CBS) seja maior que zero, conforme exigido pela regra de validação UB112-30.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096947425687)

 Após realizar as correções, emita a nota fiscal novamente.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096947426327)

 **CAUSA**

Esta rejeição ocorre quando um **CST do IBS/CBS** que possui indicador que obriga o preenchimento do grupo de ajuste de competência (ind_gAjusteCompet = 1) é utilizado na nota fiscal, mas o grupo **"gAjusteCompet"** não foi informado. De acordo com a regra de validação UB112-20, quando o CST possui este indicador, é obrigatório informar o grupo de ajuste de competência. Além disso, conforme a regra UB112-30, quando este grupo é informado, pelo menos um dos valores (IBS ou CBS) deve ser maior que zero. Esta validação faz parte das novas regras implementadas pela Reforma Tributária (Lei Complementar nº 214/2025), que introduziu os novos tributos IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços).


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)