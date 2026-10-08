# E0065 Rejeição: Não é possível substituição da NFS-e que tenha sido gerada em ambientes geradores diferentes.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37229452867095-E0065-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-substitui%C3%A7%C3%A3o-da-NFS-e-que-tenha-sido-gerada-em-ambientes-geradores-diferentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/37229452867095-E0065-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-substitui%C3%A7%C3%A3o-da-NFS-e-que-tenha-sido-gerada-em-ambientes-geradores-diferentes)  
> **ID:** `37229452867095` | **Última Atualização:** 2026-07-22T14:13:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229452861847)

 **MENSAGEM**

E0065 Rejeição: Não é possível substituição da NFS-e que tenha sido gerada em ambientes geradores diferentes.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229396560279)

 **SITUAÇÃO**

Ao realizar a tentativa de substituição de uma NFS-e, o sistema apresenta a rejeição acima relacionada à divergência entre o ambiente de geração da nota fiscal de serviço original e o ambiente em que a substituição está sendo solicitada.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229396560663)

 **SOLUÇÃO**

Para resolver esta rejeição, siga as orientações abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229452863895)

 Identifique em qual **ambiente gerador a NFS-e original foi emitida** (exemplo: sistema próprio, portal da prefeitura, webservice, etc.).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229452864279)

 Acesse o **mesmo ambiente gerador** onde a nota fiscal original foi criada para realizar a substituição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229396561943)

 Caso a nota original tenha sido emitida pelo **portal da prefeitura**, realize a substituição diretamente no portal municipal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229452865047)

 Caso a nota original tenha sido emitida pelo **sistema ERP via webservice**, realize a substituição através do próprio sistema.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229396562327)

 **CAUSA**

A rejeição ocorre porque a **prefeitura não permite a substituição de NFS-e entre ambientes geradores diferentes**. Isso significa que se a nota fiscal original foi emitida em um determinado sistema ou portal, a substituição deve ser realizada obrigatoriamente no mesmo ambiente. Esta é uma **regra de validação da Secretaria de Fazenda Municipal** para garantir a integridade e rastreabilidade das operações fiscais.