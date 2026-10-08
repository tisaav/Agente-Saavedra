# E0016 Rejeição: A data de competência deve ser igual ou posterior à data de ativação do convênio do município emissor informado na DPS, exceto quando o emitente for MEI na data de competência informada.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221447527191-E0016-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-deve-ser-igual-ou-posterior-%C3%A0-data-de-ativa%C3%A7%C3%A3o-do-conv%C3%AAnio-do-munic%C3%ADpio-emissor-informado-na-DPS-exceto-quando-o-emitente-for-MEI-na-data-de-compet%C3%AAncia-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221447527191-E0016-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-deve-ser-igual-ou-posterior-%C3%A0-data-de-ativa%C3%A7%C3%A3o-do-conv%C3%AAnio-do-munic%C3%ADpio-emissor-informado-na-DPS-exceto-quando-o-emitente-for-MEI-na-data-de-compet%C3%AAncia-informada)  
> **ID:** `37221447527191` | **Última Atualização:** 2026-07-22T14:18:41Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221447507735)

 **MENSAGEM**

E0016 Rejeição: A data de competência deve ser igual ou posterior à data de ativação do convênio do município emissor informado na DPS, exceto quando o emitente for MEI na data de competência informada.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221447508631)

 **SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o usuário informou uma **data de competência anterior à data de ativação do convênio** do município emissor. Como resultado, o documento foi rejeitado pela Sefaz com a mensagem de erro acima.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221447509271)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221447509783)

 Verifique a **data de ativação do convênio** do município emissor junto à prefeitura ou no portal da Secretaria da Fazenda municipal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221447510935)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221463294743)

 Na grade **''Cabeçalho''**, localize o campo **''Dt. Neg.''** e ajuste a data da competência para que seja **igual ou posterior á data de ativação do convênio** do município emissor.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221463296791)

 Caso o emitente seja **MEI (Microempreendedor Individual)** na data de competência informada, esta validação não se aplica e a DPS poderá ser emitida normalmente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221463297815)

 Salve as alterações e tente emitir novamente a DPS
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221463299095)

 **CAUSA**

A rejeição E0016 ocorre quando a **data de competência informada na DPS é anterior à data de ativação do convênio** do município emissor. Esta validação garante que apenas documentos fiscais com competência válida sejam processados, respeitando o período em que o município está habilitado para receber declarações eletrônicas. A exceção aplica-se quando o emitente possui a **condição de MEI** na data de competência, situação na qual esta regra de validação não é aplicada.