# 468 Rejeição: NF-e com Tipo Emissão = 4, sem EPEC correspondente.(NT2014/001)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101933-468-Rejei%C3%A7%C3%A3o-NF-e-com-Tipo-Emiss%C3%A3o-4-sem-EPEC-correspondente-NT2014-001](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101933-468-Rejei%C3%A7%C3%A3o-NF-e-com-Tipo-Emiss%C3%A3o-4-sem-EPEC-correspondente-NT2014-001)  
> **ID:** `360043101933` | **Última Atualização:** 2026-07-22T16:08:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510064470295)

 MENSAGEM:**

468 Rejeição: NF-e com Tipo Emissão = 4, sem EPEC correspondente. (NT2014/001) 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510050686743)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510064477463)

 Neste caso, aguarde a sincronização entre SEFAZ Nacional e Estadual, normalmente SEFAZ Nacional recepciona a nota, porém na Estadual ainda não houve integração desta nota, ou vice versa, primeiro SEFAZ Estadual recepciona e não sincroniza com SEFAZ Nacional.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510064484375)

 Mesmo que hajam várias tentativas de envio e o erro persista, ainda assim é necessário aguardar. Porém, se passado um prazo considerável e não se conseguir realizar a transmissão, entre em contato com a SEFAZ com um chamado formal para averiguação da situação.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510050699671)

 Vale ressaltar, que desde que a nota seja emitida na Contingência EPEC, se possui o prazo de até 7 dias corridos para a regularização da mesma, ou seja, a geração de lote, saindo do StatusNFe = S - Enviada EPEC e transmissão para StatusNFe = A - Aprovada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510064491543)

 CAUSA:**

Uma NF-e emitida em Contingência EPEC precisa ser transmitida a Sefaz Estadual imediatamente após cessar os problemas técnicos no Ambiente Autorizador da Sefaz Estadual. Nesse tipo de Contingência, primeiro é enviado o Evento EPEC para a Sefaz Nacional, que compartilhará o mesmo com o Ambiente Estadual.

Quando uma NF-e em Contingência EPEC for recebida pela Sefaz Estadual e a Sefaz Nacional ainda não tiver feito o compartilhamento do Evento EPEC com a Sefaz Estadual, será retornado a rejeição.

Essa situação pode ocorrer tanto por uma falha na Sefaz Nacional ao compartilhar o Evento quanto por um falha na Sefaz Estadual ao receber o Evento EPEC.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510050706199)

 OBSERVAÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458167810455)

 ([NT2014/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=1m6MlHgr744=)) - Nota técnica 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458167810455)

 Representação de Status da NF-e no sistema(TGFCAB.STATUSNFE)

'D' - DENEGADA
'A' - Aprovada
'E' - Aguardando Autoriz.
'R' - Aguardando Correção
'V' - Com erro de Validação
'P' - Pendente de Retorno
'N' - Não enviada
'I' - Enviada
'S'- Enviada DPEC