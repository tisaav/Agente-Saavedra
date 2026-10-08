# E0612 Rejeição: Não é permitido informar alíquota quando o benefício municipal informado na DPS for do tipo "Isenção" ou "Alíquota Diferenciada".

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226790122007-E0612-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-benef%C3%ADcio-municipal-informado-na-DPS-for-do-tipo-Isen%C3%A7%C3%A3o-ou-Al%C3%ADquota-Diferenciada](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226790122007-E0612-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-benef%C3%ADcio-municipal-informado-na-DPS-for-do-tipo-Isen%C3%A7%C3%A3o-ou-Al%C3%ADquota-Diferenciada)  
> **ID:** `37226790122007` | **Última Atualização:** 2026-07-22T14:14:37Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226790088727)

 **MENSAGEM**

E0612 Rejeição: Não é permitido informar alíquota quando o benefício municipal informado na DPS for do tipo "Isenção" ou "Alíquota Diferenciada".

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226806364183)

 **SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e/NFC-e), o usuário **informou uma alíquota municipal do IBS** para um item que possui um **benefício fiscal municipal** cadastrado na Declaração de Prévia Simplificada (DPS) do tipo **"Isenção"** ou **"Alíquota Diferenciada"**. Esta combinação não é permitida pela Sefaz, resultando na rejeição do documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226790090519)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226806366999)

 Acesse as telas **''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e localize a configuração de alíquota utilizada no documento fiscal rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226806367639)

 Verifique se o campo **"Código de Benefício Fiscal Municipal"** está preenchido com um código do tipo **"Isenção"** ou **"Alíquota Diferenciada".**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226790099095)

 Realize um dos ajustes abaixo, conforme orientação do seu contador:

- 

**Opção 1:** Se o benefício fiscal for do tipo **"Isenção"**, certifique-se de que o campo **"Alíquota Municipal IBS"** esteja **zerado ou em branco**. Quando há isenção, não deve ser informada alíquota.

- 

**Opção 2:** Se o benefício fiscal for do tipo **"Alíquota Diferenciada"**, remova a alíquota do campo **"Alíquota Municipal IBS"**, pois a alíquota diferenciada já está contemplada no próprio benefício fiscal cadastrado na DPS.

- 

**Opção 3:** Se a operação não possui benefício fiscal de isenção ou alíquota diferenciada, remova ou corrija o **"Código de Benefício Fiscal Municipal"** informado incorretamente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226806369559)

 Salve as alterações realizadas na configuração de alíquota.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226806370455)

 Reemita o documento fiscal eletrônico para que as correções sejam aplicadas e o documento seja aceito pela Sefaz.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226790102167)

 **CAUSA**

A rejeição ocorre porque a **Sefaz não permite** que seja informada uma alíquota municipal do IBS quando o benefício fiscal municipal cadastrado na DPS for do tipo **"Isenção"** ou **"Alíquota Diferenciada"**. Isso acontece porque:

- 

No caso de **isenção**, não há incidência de imposto, portanto, a alíquota deve ser zero ou não informada.

- 

No caso de **alíquota diferenciada**, a alíquota específica já está definida no próprio benefício fiscal, não sendo necessário informar uma alíquota adicional no campo de alíquota municipal.

A **inconsistência entre o benefício fiscal e a alíquota informada** gera conflito nas regras de validação da Sefaz, resultando na rejeição E0612.