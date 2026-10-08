# E0172 Rejeição: O Regime Especial de Tributação deve ser "Nenhum" (regEspTrib = 0) quando o serviço prestado for diferente de Tributável (tribISSQN = 1), ou seja, tribISSQN = 2, 3 ou 4.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222494570263-E0172-Rejei%C3%A7%C3%A3o-O-Regime-Especial-de-Tributa%C3%A7%C3%A3o-deve-ser-Nenhum-regEspTrib-0-quando-o-servi%C3%A7o-prestado-for-diferente-de-Tribut%C3%A1vel-tribISSQN-1-ou-seja-tribISSQN-2-3-ou-4](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222494570263-E0172-Rejei%C3%A7%C3%A3o-O-Regime-Especial-de-Tributa%C3%A7%C3%A3o-deve-ser-Nenhum-regEspTrib-0-quando-o-servi%C3%A7o-prestado-for-diferente-de-Tribut%C3%A1vel-tribISSQN-1-ou-seja-tribISSQN-2-3-ou-4)  
> **ID:** `37222494570263` | **Última Atualização:** 2026-07-22T14:17:45Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222494562327)

 **MENSAGEM**

E0172 Rejeição: O Regime Especial de Tributação deve ser "Nenhum" (regEspTrib = 0) quando o serviço prestado for diferente de Tributável (tribISSQN = 1), ou seja, tribISSQN = 2, 3 ou 4.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222459213719)

 **SITUAÇÃO**

Ao emitir uma NFS-e, o usuário configurou um **Regime Especial de Tributação ISS** diferente de **"Nenhum"** no cadastro da empresa, porém o **Código de Tributação ISS** utilizado na operação indica que o serviço **não é tributável** (Isento, Imune, Exigibilidade Suspensa ou Não Incidência). Esta combinação de configurações é **incompatível** e resulta na rejeição da nota fiscal pela prefeitura.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222494563991)

 **SOLUÇÃO**

Para corrigir esta rejeição, ajuste o **Regime Especial de Tributação ISS** conforme o tipo de tributação do serviço:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222494564887)

 Acesse a tela **"Empresa"** Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222459216151)

 Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba **"Geral"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222459216791)

 Localize o campo **"Regime esp. tributação ISS (NFS-e)''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222494566935)

 Verifique qual **Código de Tributação do ISS** está sendo utilizado na operação e ajuste o regime especial conforme o enquadramento:

- 

**Para serviços Isentos (cód. 06), Imunes (cód. 09), com Exigibilidade Suspensa (cód. 02 ou 03) ou de Não Incidência (cód. 07): **Configure o campo “Regime esp. trib. ISS (NFS-e)” como “Nenhum” ou deixe-o **em branco**, pois não se aplica regime especial nesses casos.

- 

**Para serviços Tributáveis (cód. 00 ou 01): **Configure o ''Regime esp. trib ISS (NFS-e)'' de acordo com o enquadramento correto da empresa, como **Microempresa Municipal, Estimativa, Sociedade de Profissionais, Cooperativa, MEI, ME/EPP, Simples Nacional**, entre outros aplicáveis.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222459218839)

 Salve as alterações realizadas no cadastro da empresa.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222459219991)

 Emita novamente a NFS-e com as configurações corrigidas.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222459221015)

 **CAUSA**

Esta rejeição ocorre porque a **prefeitura valida a consistência** entre o **Regime Especial de Tributação ISS** e o **Código de Tributação ISS** do serviço. Quando o serviço **não é tributável** (Isento, Imune, Exigibilidade Suspensa ou Não Incidência no Município), o sistema não deve informar nenhum regime especial de tributação, pois **não há incidência de ISS** sobre a operação. O regime especial só deve ser informado quando o serviço for efetivamente **tributável**, ou seja, quando houver **recolhimento de ISS**.