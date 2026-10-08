# Divergência nos valores de IR enviados ao eSocial/DCTFWeb

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39360917385879-Diverg%C3%AAncia-nos-valores-de-IR-enviados-ao-eSocial-DCTFWeb](https://ajuda.sankhya.com.br/hc/pt-br/articles/39360917385879-Diverg%C3%AAncia-nos-valores-de-IR-enviados-ao-eSocial-DCTFWeb)  
> **ID:** `39360917385879` | **Última Atualização:** 2026-09-26T00:42:14Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39360931432087)

 **Mensagem**

Valores de Imposto de Renda (IR) calculados no sistema não foram enviados corretamente para o eSocial, resultando em diferenças na guia DCTFWeb.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39360931433751)

 **Situação**

Ao conferir a **"Guia da DCTFWeb"**, foram identificadas divergências nos valores de IR de alguns colaboradores. Os valores calculados no sistema Sankhya não correspondem aos valores enviados ao eSocial, impedindo a correta emissão da guia de recolhimento. Esta inconsistência gera problemas na apuração fiscal e pode resultar em pendências junto à Receita Federal.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39360917377303)

 **Solução**

Para corrigir as divergências nos valores de IR enviados ao eSocial, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39360917377943)

 Identifique os colaboradores com divergência nos valores de IR comparando os dados do sistema com a **"Guia DCTFWeb"**. A tela: **''S-5002 - Conferência de IRRF'' (**Pessoal+ » Consultas » S-5002 - Conferência IRRF) poderá ser considerada uma ferramenta auxiliar neste processo. 

**Para auxilio em sua utilização, veja o link:**

[https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda-Retido-na-Fonte-por-Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda-Retido-na-Fonte-por-Trabalhador)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39360917378327)

 Acesse o **"Evento S-1210" na tela: ''central eSocial'' **(Pessoal+ » Rotinas Folha » Central do eSocial) do colaborador identificado no eSocial.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39360931436823)

 Realize a exclusão do **"Evento S-1210"** enviado anteriormente com os valores incorretos.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41274871057047)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41274871058071)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41274871058455)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41274840613911)

Após selecionar o ícone de lixeira, o evento será transferido para a aba; pendentes e estará preparado para envio como 'exclusão'

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41274871058839)

 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39360931438231)

 Verifique se os cálculos de IR estão corretos no sistema Sankhya, conferindo a folha de pagamento do colaborador.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39360917381911)

 Realize o reenvio do **"Evento S-1210"** com os valores corretos ao eSocial.

Para suporte com este processo, veja o link:

[https://ajuda.sankhya.com.br/hc/pt-br/articles/37960826085271-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1210-para-o-eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/37960826085271-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1210-para-o-eSocial)

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39360931439255)

 Aguarde o processamento do evento pelo eSocial e verifique se foi aceito sem erros.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39360917383319)

 Consulte novamente a **"Guia DCTFWeb"** para confirmar que os valores foram atualizados corretamente.

![8](https://ajuda.sankhya.com.br/hc/article_attachments/39360931440791)

 Caso persistam divergências em outros colaboradores, repita o processo para cada um deles ou solicite apoio da unidade de suporte para realizar uma conferência completa.
 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39360917384343)

 **Causa**

As divergências nos valores de IR enviados ao eSocial podem ocorrer devido a:

- 

Inconsistências no cálculo da folha de pagamento que não foram identificadas antes do envio;
 

1. 

Eventos **"S-1210"** enviados com dados desatualizados ou incorretos;
 

1. 

Alterações retroativas na folha de pagamento que não foram refletidas no eSocial;
 

1. 

Problemas na integração entre o sistema Sankhya e o eSocial durante o envio dos eventos;
 

1. 

Deduções ou bases de cálculo despadronizadas/configuradas incorretamente no sistema.


---

### 🔗 Links e Referências Internas:

- [https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda-Retido-na-Fonte-por-Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda-Retido-na-Fonte-por-Trabalhador)
- [https://ajuda.sankhya.com.br/hc/pt-br/articles/37960826085271-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1210-para-o-eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/37960826085271-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1210-para-o-eSocial)