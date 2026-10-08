# 1074 Rejeição: Não informado o grupo de redução de alíquota Municipal [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37100489930903-1074-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Municipal-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37100489930903-1074-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Municipal-nItem-999)  
> **ID:** `37100489930903` | **Última Atualização:** 2026-07-22T14:19:43Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100489901079)

 **MENSAGEM**

1074 Rejeição: Não informado o grupo de redução de alíquota Municipal [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100489901975)

 **SITUAÇÃO**

A rejeição acima ocorreu quando usuário tentou emitir uma NF-e ou NFC-e sem informar o grupo de Redução de Alíquota Municipal obrigatório para o CST utilizado, conforme a validação UB45-20.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100489903383)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100475067159)

 Acesse as telas **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100475068311)

 Verifique se o CST utilizado exige a informação de redução de alíquota (ind_gRed = 1) ou se está sendo utilizado em uma operação de compra governamental. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100475069079)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100489909015)

 Selecione o TOP utilizado na operação. 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100489912087)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se a configuração do TOP está correta para a operação que está sendo realizada. 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100475075095)

 Em seguida, acesse a tela ************["Assistente de Configuração Integral da Reforma Tributária"](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria) (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária). 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100475076631)

 Configure corretamente o **"Percentual de Redução de Alíquota Municipal"** para o CST utilizado, informando o valor adequado conforme a legislação vigente. 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100489917207)

 Caso esteja **realizando uma operação de compra governamental**, certifique-se de que o grupo de compras governamentais está devidamente preenchido e que o grupo de redução de alíquota municipal também está informado. 

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37528425061783)

 Após realizar as configurações necessárias, emita o documento fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100475081623)

 **CAUSA**

A rejeição 1074 ocorre quando o grupo de **Redução de Alíquota Municipal não é informado**, **mesmo sendo obrigatório**. Segundo a regra de validação UB45-20, o grupo deve ser preenchido em duas situações:

- 

Quando o CST utilizado possui o indicador de Redução de Alíquota (ind_gRed = 1).

- 

Quando o documento fiscal inclui o grupo de compras governamentais (gCompraGov).

A falta dessa informação impede o cálculo correto do IBS municipal e gera a rejeição do documento fiscal pela Sefaz.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- ["Assistente de Configuração Integral da Reforma Tributária"](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria)