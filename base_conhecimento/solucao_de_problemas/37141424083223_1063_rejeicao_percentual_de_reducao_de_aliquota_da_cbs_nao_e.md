# 1063 Rejeição: Percentual de redução de alíquota da CBS não é válido para este cClassTrib [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141424083223-1063-Rejei%C3%A7%C3%A3o-Percentual-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-CBS-n%C3%A3o-%C3%A9-v%C3%A1lido-para-este-cClassTrib-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141424083223-1063-Rejei%C3%A7%C3%A3o-Percentual-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-CBS-n%C3%A3o-%C3%A9-v%C3%A1lido-para-este-cClassTrib-nItem-999)  
> **ID:** `37141424083223` | **Última Atualização:** 2026-07-22T14:19:18Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141424073751)

 **MENSAGEM**

1063 Rejeição: Percentual de redução de alíquota da CBS não é válido para este cClassTrib [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141424074263)

 **SITUAÇÃO**

Ao emitir uma nota fiscal, o sistema retorna uma rejeição relacionada ao **percentual de redução da alíquota da CBS** informado no documento fiscal, em conjunto com a **Classificação Tributária (cClassTrib)** utilizada. A rejeição é apresentada no momento da validação e transmissão da nota fiscal eletrônica.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141424075927)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141424076567)

 Acesse a tela **''Central de Vendas'' **(Comercial » Rotinas » Central de Vendas) e localize e abra a nota fiscal que apresentou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141424076951)

 Na aba **''Outras opções'' **(ícone com três pontos), selecione a opção **''Consultar/Alterar Dados do Imposto do Item''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141431972887)

 Verifique o campo** ''Código de Classificação Tributária''** (cClassTrib) utilizada no item da nota fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141431973399)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141424078743)

 Verifique se o **CST** utilizado permite a aplicação de redução de alíquota para a CBS.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141431976983)

 Verifique no CST informado se o indicador de **Redução de Alíquota** está configurado corretamente:

- 

**Exige o uso de Redução de Alíquota (ind_gRed = 1): **Certifique-se de que o percentual de redução esteja preenchido e seja compatível com a classificação tributária utilizada.

- 

**Veda o uso de Redução de Alíquota (ind_gRed = 0): **Não informe percentual de redução para a alíquota, **exceto** nos casos de **compra governamental**, quando a legislação permitir.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37867563008407)

 Ajuste o campo **"% da Redução CBS"** (pRedAliq) para que seja comaptível com a Classificação Tributária utilizada.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38195488374679)

 Em caso de compra governamental, verifique se o percentual de redução está corretamente informado no grupo de redução de alíquota da CBS (gCBS/gRed).

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38195483297815)

 Após realizar os ajustes necessários, tente emitir a nota fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141431978903)

 **CAUSA**

A rejeição ocorre devido a uma incompatibilidade entre o percentual de redução de alíquota da CBS informado e a Classificação Tributária (cClassTrib) utilizada no documento fiscal.

Conforme a regra de validação UB65-10, quando informado o grupo de Redução de Alíquota (gCBS/gRed), o sistema verifica:

- 

**Se o CST possui indicador que exige o uso de Redução de Alíquota (ind_gRed = 1)**: neste caso, o Percentual de Redução de Alíquota (pRedAliq) deve ser válido para a Classificação Tributária informada.

- 

**Se o CST possui indicador que veda o uso de Redução de Alíquota (ind_gRed = 0)**: neste caso, não deve ser informado percentual de redução de alíquota, exceto em casos específicos de compra governamental.

A validação é realizada para garantir que a aplicação de reduções de alíquota da CBS esteja em conformidade com as regras tributárias estabelecidas pela Lei Complementar 214/2025, que implementa a Reforma Tributária.