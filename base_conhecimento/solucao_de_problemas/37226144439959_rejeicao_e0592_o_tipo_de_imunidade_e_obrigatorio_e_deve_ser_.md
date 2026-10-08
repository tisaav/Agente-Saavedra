# REJEIÇÃO E0592: O tipo de imunidade é obrigatório e deve ser informado somente quando o campo referente à tributação do ISSQN for igual a "2 - Imunidade"

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226144439959-REJEI%C3%87%C3%83O-E0592-O-tipo-de-imunidade-%C3%A9-obrigat%C3%B3rio-e-deve-ser-informado-somente-quando-o-campo-referente-%C3%A0-tributa%C3%A7%C3%A3o-do-ISSQN-for-igual-a-2-Imunidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226144439959-REJEI%C3%87%C3%83O-E0592-O-tipo-de-imunidade-%C3%A9-obrigat%C3%B3rio-e-deve-ser-informado-somente-quando-o-campo-referente-%C3%A0-tributa%C3%A7%C3%A3o-do-ISSQN-for-igual-a-2-Imunidade)  
> **ID:** `37226144439959` | **Última Atualização:** 2026-07-22T14:15:17Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226127821591)

 **MENSAGEM**

E0592 Rejeição: O tipo de imunidade é obrigatório e deve ser informado somente quando o campo referente à tributação do ISSQN for igual a "2 - Imunidade".

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226127823767)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)**, o usuário configurou o campo de **tributação do ISSQN** com o valor **"2 - Imunidade"**, porém **não informou o tipo de imunidade** correspondente. Alternativamente, o usuário pode ter preenchido o **tipo de imunidade** em uma situação onde a **tributação do ISSQN não está configurada como imunidade**, gerando inconsistência na validação da Sefaz.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226127824663)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226144434071)

 Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa) e localize a aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba ''Geral''.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226127826839)

 Verifique a configuração do campo **"Regime esp. Tributação ISS (NFS-e)"**:

- 

Se a tributação estiver configurada como **"2 - Imunidade"**, certifique-se de que o campo **"Tipo de Imunidade"** esteja devidamente preenchido com uma das opções disponíveis.

- 

Se a tributação **não for imunidade**, remova qualquer informação preenchida no campo **"Tipo de Imunidade"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226144434711)

 Caso a empresa seja **imune ou isenta**, acesse a tela **"Empresa"** (Contabilidade » Preferências), aba **"ECF - Escrituração Contábil Fiscal"** e sub-aba **"Parâmetros de tributação"**, e verifique se o campo **"Tipo de Pessoa Jurídica Imune ou Isenta"** está corretamente configurado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226127827735)

 Após realizar os ajustes necessários, **gere novamente a NFS-e** e verifique se a rejeição foi solucionada. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226127828375)

 **CAUSA**

A rejeição ocorre porque a **Sefaz exige que o tipo de imunidade seja informado obrigatoriamente** quando a **tributação do ISSQN estiver configurada como "2 - Imunidade"**. Da mesma forma, o **tipo de imunidade não deve ser preenchido** se a tributação do ISSQN estiver configurada com **qualquer outro valor diferente de imunidade**. A inconsistência entre esses campos gera a rejeição E0592.