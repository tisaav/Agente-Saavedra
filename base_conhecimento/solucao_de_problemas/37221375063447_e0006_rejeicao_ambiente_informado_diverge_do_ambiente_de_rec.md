# E0006 Rejeição: Ambiente informado diverge do ambiente de recebimento para o qual o emitente enviou a DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221375063447-E0006-Rejei%C3%A7%C3%A3o-Ambiente-informado-diverge-do-ambiente-de-recebimento-para-o-qual-o-emitente-enviou-a-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221375063447-E0006-Rejei%C3%A7%C3%A3o-Ambiente-informado-diverge-do-ambiente-de-recebimento-para-o-qual-o-emitente-enviou-a-DPS)  
> **ID:** `37221375063447` | **Última Atualização:** 2026-07-22T14:18:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221360525719)

 **MENSAGEM**

E0006 Rejeição: Ambiente informado diverge do ambiente de recebimento para o qual o emitente enviou a DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221375016215)

 **SITUAÇÃO**

A DPS foi emitida com indicação de ambiente diferente daquele para o qual o documento foi transmitido.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221375020823)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38354559496087)

 Acesse a tela **"Empresas"** (Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221375024535)

 Na aba** ''Documentos Fiscais Eletrônicos''**, sub-aba** ''NFS-e''**, sub-aba** ''Geral''**, confira o campo **''Ambiente''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221360538775)

 Confirme se o ambiente selecionado está correto:

- 

**Ambiente de Produção:** utilizado para emissão de documentos fiscais com validade jurídica.

- 

**Ambiente de Homologação:** utilizado apenas para testes, sem validade fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221360543255)

 Caso o ambiente esteja **incorreto**, ajuste a configuração para o ambiente adequado e salve as alterações.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221375034135)

 Certifique-se de que o **certificado digital** utilizado está vinculado ao ambiente correto (produção ou homologação).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221375036567)

 Após realizar os ajustes, **gere novamente a DPS** e transmita para o ambiente correto.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38354559498135)

 Valide no **XML da DPS** se a tag referente ao ambiente (tpAmb) está preenchida corretamente:

- 

**tpAmb = 1:** Produção

- 

**tpAmb = 2:** Homologação

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221360556311)

 **CAUSA**

A rejeição **E0006** ocorre quando há **divergência entre o ambiente informado** no documento fiscal (campo tpAmb no XML) e o **ambiente de recebimento** para o qual a DPS foi efetivamente transmitida. Isso pode acontecer quando o sistema está configurado para um ambiente, mas o documento é enviado para outro, gerando inconsistência na validação da Sefaz.