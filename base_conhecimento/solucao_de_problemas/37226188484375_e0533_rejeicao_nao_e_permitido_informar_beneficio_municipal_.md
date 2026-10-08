# E0533 Rejeição: Não é permitido informar Benefício Municipal (BM deve ser nulo) quando o serviço prestado diferente de Tributável (tribISSQN = 1), ou seja, tribISSQN = 2, 3 ou 4.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226188484375-E0533-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-Benef%C3%ADcio-Municipal-BM-deve-ser-nulo-quando-o-servi%C3%A7o-prestado-diferente-de-Tribut%C3%A1vel-tribISSQN-1-ou-seja-tribISSQN-2-3-ou-4](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226188484375-E0533-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-Benef%C3%ADcio-Municipal-BM-deve-ser-nulo-quando-o-servi%C3%A7o-prestado-diferente-de-Tribut%C3%A1vel-tribISSQN-1-ou-seja-tribISSQN-2-3-ou-4)  
> **ID:** `37226188484375` | **Última Atualização:** 2026-07-22T14:15:13Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226188476055)

 **MENSAGEM**

E0533 Rejeição: Não é permitido informar Benefício Municipal (BM deve ser nulo) quando o serviço prestado diferente de Tributável (tribISSQN = 1), ou seja, tribISSQN = 2, 3 ou 4.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205337751)

 **SITUAÇÃO**

A **NFS-e** foi emitida com a informação de um **Benefício Municipal** associada a um serviço cujo r**egime de tributação do ISS** não está definido como tributável no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205338647)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205338775)

 Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa) e localize a empresa emissora da NFS-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205339159)

 Na aba** ''Documentos Fiscais Eletrônicos''**, sub-aba **"NFS-e"**, sub-aba **''Geral''**, verifique o campo **"Regime esp. tributação ISS (NFS-e)''** e identifique qual regime de tributação está configurado:

- 

Se o código for **2, 3 ou 4** (Exigibilidade Suspensa por Decisão Judicial, Exigibilidade Suspensa por Procedimento Administrativo ou Imune), **não é permitido informar benefício municipal**.

- 

Se o serviço realmente deve ser **tributável**, altere o código para **1 (Tributável)**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205340055)

 Caso o regime de tributação esteja correto como **2, 3 ou 4**, acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205340695)

 Localize o TOP utilizado na emissão da NFS-e e acesse a aba **"NFS-e"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205342231)

 Verifique se há algum **código de benefício municipal** preenchido. Caso exista, **remova a informação** deste campo, deixando-o vazio.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226205345431)

 Salve as alterações realizadas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226188480535)

 Emita novamente a NFS-e.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38295864938135)

 OBSERVAÇÃO:** Consulte sempre o **contador responsável** ou a **legislação municipal** para confirmar qual é o regime de tributação correto para o serviço prestado e se há direito a benefício fiscal municipal.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226188481047)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida** que o campo de **Benefício Municipal** só pode ser preenchido quando o serviço está configurado com o **regime de tributação "Tributável" (código 1)**. Quando o serviço possui outros regimes, como **Exigibilidade Suspensa por Decisão Judicial (código 2)**, **Exigibilidade Suspensa por Procedimento Administrativo (código 3)** ou **Imune (código 4)**, o sistema não permite que seja informado benefício municipal, pois **não há tributação efetiva do ISS** nessas situações. A informação indevida do benefício municipal gera inconsistência fiscal e, consequentemente, a rejeição da nota.