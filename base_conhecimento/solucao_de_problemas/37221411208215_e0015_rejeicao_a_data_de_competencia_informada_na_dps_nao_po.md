# E0015 Rejeição: A data de competência informada na DPS não pode ser posterior à data de emissão (dhEmi) da DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221411208215-E0015-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-informada-na-DPS-n%C3%A3o-pode-ser-posterior-%C3%A0-data-de-emiss%C3%A3o-dhEmi-da-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221411208215-E0015-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-informada-na-DPS-n%C3%A3o-pode-ser-posterior-%C3%A0-data-de-emiss%C3%A3o-dhEmi-da-DPS)  
> **ID:** `37221411208215` | **Última Atualização:** 2026-07-22T14:18:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411184535)

 **MENSAGEM**

E0015 Rejeição: A data de competência informada na DPS não pode ser posterior à data de emissão (dhEmi) da DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221427087255)

 **SITUAÇÃO**

Durante a emissão de uma **DPS (Documento de Prestação de Serviços)**, o usuário informou uma **data de competência posterior à data de emissão** do documento. Ao tentar transmitir a DPS para a Sefaz, o documento foi rejeitado com a mensagem de erro acima, pois a validação da Sefaz não permite que a data de competência seja futura em relação à data de emissão.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411191063)

 **SOLUÇÃO**

Para resolver esta rejeição, ajuste a **data de competência** da DPS para que seja **igual ou anterior à data de emissão** do documento. Siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221427095959)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411194519)

 Na grade **''Cabeçalho''**, verifique o campo **"Dt. Neg."**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221427097879)

 Verifique a **data de Emissão (dhEmi) **da DPS no XML de conferência ou na tela de emissão do documento.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221427098263)

 Ajuste a data da competência para que seja **igual ou anterior à data de emissão**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221411199767)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38353205184023)

 Gere um novo lote e reenvie a DPS para autorização na Sefaz.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221427100055)

 **CAUSA**

A rejeição ocorre quando a **data de competência informada na DPS é posterior à data de emissão** do documento. A Sefaz valida que a competência do serviço prestado não pode ser futura em relação ao momento em que o documento está sendo emitido, garantindo a **consistência temporal das informações fiscais**.