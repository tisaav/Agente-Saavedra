# 1151 Rejeição: Grupo IBS/CBS Monofásico informado indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095779024151-1151-Rejei%C3%A7%C3%A3o-Grupo-IBS-CBS-Monof%C3%A1sico-informado-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095779024151-1151-Rejei%C3%A7%C3%A3o-Grupo-IBS-CBS-Monof%C3%A1sico-informado-indevidamente-nItem-999)  
> **ID:** `37095779024151` | **Última Atualização:** 2026-07-22T14:21:34Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095793506455)

 **MENSAGEM**

1151 Rejeição: Grupo IBS/CBS Monofásico informado indevidamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095779011479)

 **SITUAÇÃO**

Esta rejeição ocorre quando o contribuinte tenta emitir uma NF-e ou NFC-e informando o grupo **IBS/CBS Monofásico** em um item cujo CST (Código de Situação Tributária) **não permite essa informação** (`ind_gIBSCBSMono = 0`).

Mesmo que o CST não autorize, se o grupo Monofásico for informado, o documento fiscal será rejeitado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095779011991)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095779014295)

 Acesse a tela **''Aliquotas Monofásicas''** (Livros Fiscais » Cadastros » Aliquotas Monofásicas) e verifique o CST do item rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095793509911)

 Em seguida, consulte a **“Tabela de Indicadores de CST do IBS e da CBS”**, disponibilizada no site do governo.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37247549590039)

 Verifique se o CST utilizado permite a informação do grupo IBS/CBS Monofásico (`ind_gIBSCBSMono = 1`).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095793516567)

 Caso o CST não permita o uso do grupo IBS/CBS Monofásico:

- 

Altere o CST do IBS/CBS para um que permita a tributação monofásica, se a operação realmente exigir este regime.

- 

Remova as informações do grupo IBS/CBS Monofásico do item, se a operação não utilizar tributação monofásica.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095779018135)

 Acesse a tela ****[''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e altere o CST e selecione a operação utilizada na nota fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095793517847)

 Na aba **''NF-e/NFC-e/CF-e''**, localize a seção de configuração do IBS/CBS e ajuste o CST conforme necessário para a operação.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095793518103)

 Se for necessário remover o grupo IBS/CBS Monofásico, acesse o ****[“Assistente de Configuração Integral da Reforma Tributária”](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria) (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e **ajuste as configurações do item** conforme necessário.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37247547849879)

 Após realizar todas as alterações, emita novamente a nota fiscal.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095779021079)

 **CAUSA**

A rejeição é causada pela regra de validação **UB13-39 da SEFAZ**, que verifica se o CST do IBS/CBS informado possui o indicador `ind_gIBSCBSMono = 0`. Quando este indicador é zero, o grupo **gIBSCBSMono** (id: UB84, grupo: imposto/IBSCBS/gIBSCBSMono) **não deve ser informado** no documento fiscal.

Essa validação faz parte da **Lei Complementar nº 214/2025 (Reforma Tributária)**. A tributação monofásica é um regime especial aplicável apenas a determinados produtos e operações, podendo ser usada somente quando o CST permitir expressamente.

Cada CST possui indicadores específicos que determinam quais grupos podem ser informados. Se o documento fiscal contém informações incompatíveis com o CST utilizado, a SEFAZ rejeita o envio.


---

### 🔗 Links e Referências Internas:

- [''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [“Assistente de Configuração Integral da Reforma Tributária”](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria)