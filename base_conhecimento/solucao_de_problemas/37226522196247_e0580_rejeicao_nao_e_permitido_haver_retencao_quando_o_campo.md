# E0580 Rejeição: Não é permitido haver retenção quando o campo referente à tributação do ISSQN indicar imunidade, exportação ou não incidência.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226522196247-E0580-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-haver-reten%C3%A7%C3%A3o-quando-o-campo-referente-%C3%A0-tributa%C3%A7%C3%A3o-do-ISSQN-indicar-imunidade-exporta%C3%A7%C3%A3o-ou-n%C3%A3o-incid%C3%AAncia](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226522196247-E0580-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-haver-reten%C3%A7%C3%A3o-quando-o-campo-referente-%C3%A0-tributa%C3%A7%C3%A3o-do-ISSQN-indicar-imunidade-exporta%C3%A7%C3%A3o-ou-n%C3%A3o-incid%C3%AAncia)  
> **ID:** `37226522196247` | **Última Atualização:** 2026-07-22T14:14:56Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522177559)

 **MENSAGEM**

E0580 Rejeição: Não é permitido haver retenção quando o campo referente à tributação do ISSQN indicar imunidade, exportação ou não incidência.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226538204823)

 **SITUAÇÃO**

Ao emitir uma NFS-e, o sistema apresenta a mensagem de rejeição informando que **não é permitido haver retenção de ISSQN** quando a natureza de operação configurada indica **imunidade, exportação ou não incidência** do imposto.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226538205335)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522179479)

 Acesse o cadastro de **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP utilizada na emissão da NFS-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522180503)

 Acesse a aba **"NFS-e"** e verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522182423)

 Confirme se a natureza de operação está configurada com uma das seguintes opções:

- 

**''2 - Tributação fora do município''**

- 

**''2 - Não incidência''**

- 

**''4 - Imune''**

- 

**''4 - Exportação''**

- 

**''5 - Imunidade''**

- 

**''9 - Imune/Isenta de ISSQN''**

- 

**''C - Imune/Isenta ISSQN''**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522184087)

 Acesse a tela** ''Parceiros''** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço utilizado na nota fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522187927)

 Na aba** ''Fiscal'',** confirme se o campo** ''Retém ISS''** está desabilitado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226538210711)

 Salve as alterações.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522189463)

 Retorne à nota fiscal e realize novamente a emissão da NFS-e. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226522193303)

 **CAUSA**

A rejeição ocorre porque o sistema identificou uma **incompatibilidade entre a natureza de operação do ISSQN e a configuração de retenção** do imposto. Quando a natureza de operação indica **imunidade, exportação ou não incidência**, não pode haver retenção de ISSQN, pois nesses casos o imposto não é devido ou não incide sobre a operação. A prefeitura não permite que seja informada retenção de ISS quando a tributação está configurada com essas características específicas.