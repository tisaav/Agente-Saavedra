# E0333 Rejeição: Valor 0 para o modo de prestação não é permitido na Sefin do Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224478876951-E0333-Rejei%C3%A7%C3%A3o-Valor-0-para-o-modo-de-presta%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224478876951-E0333-Rejei%C3%A7%C3%A3o-Valor-0-para-o-modo-de-presta%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e)  
> **ID:** `37224478876951` | **Última Atualização:** 2026-07-22T14:16:34Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224494764055)

 **MENSAGEM**

E0333 Rejeição: Valor 0 para o modo de prestação não é permitido na Sefin do Sistema Nacional NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224478863895)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)** através do Sistema Nacional NFS-e, o usuário recebe a rejeição E0333 informando que o **valor da nota está zerado** e não é permitido pela Sefin (Secretaria de Finanças) para o modo de prestação configurado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224478865175)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224478866711)

 Acesse a nota fiscal rejeitada e verifique o valor total da nota no cabeçalho do documento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224478868631)

 Confira o lançamento dos itens de serviço. Certifique-se de que:

- 

Os serviços estejam cadastrados na tela **“Serviço” **(Configurações » Cadastros » Produtos » Serviço), e não na tela de **''Produtos''** (Configurações » Cadastros » Produtos » Produtos).

- 

Os **valores unitários** e as **quantidades** estejam preenchidos corretamente.

- 

Não exista **desconto ou abatimento** aplicado que esteja zerando o valor total da nota.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224494771223)

 Caso o valor da nota esteja zerado devido a **descontos ou abatimentos**, ajuste os valores para que o **total da nota seja superior a zero**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224494771863)

 Acesse a tela ****["Empresa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa), na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba** ''Geral''** se as configurações de **emissão de NFS-e** estão corretas para o município.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224494773655)

 Após realizar os ajustes necessários, **salve as alterações** e tente transmitir novamente a NFS-e para a Prefeitura.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224494774167)

 **CAUSA**

A rejeição ocorre quando uma **NFS-e é transmitida** através do Sistema Nacional NFS-e com **valor total igual a zero**. A Sefin não permite a emissão de notas fiscais de serviço sem valor para o modo de prestação configurado, pois isso viola as regras de validação estabelecidas pela Secretaria de Finanças do município. O valor zerado pode ser resultado de **itens não preenchidos corretamente**, **descontos totais aplicados** ou **cadastros inadequados dos serviços** no sistema.


---

### 🔗 Links e Referências Internas:

- ["Empresa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa)