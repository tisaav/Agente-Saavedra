# E0684 Rejeição: A alíquota do PIS deve ser informada quando a base de cálculo deste imposto for informada.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37227168610839-E0684-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-PIS-deve-ser-informada-quando-a-base-de-c%C3%A1lculo-deste-imposto-for-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/37227168610839-E0684-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-PIS-deve-ser-informada-quando-a-base-de-c%C3%A1lculo-deste-imposto-for-informada)  
> **ID:** `37227168610839` | **Última Atualização:** 2026-07-22T14:14:29Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227185222551)

 **MENSAGEM**

E0684 Rejeição: A alíquota do PIS deve ser informada quando a base de cálculo deste imposto for informada.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227185222807)

 **SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e, o sistema calculou a **base de cálculo do PIS** para um ou mais itens do documento fiscal, porém a **alíquota do PIS não foi informada** no cadastro de alíquotas. Como resultado, a nota foi rejeitada pela Sefaz com a mensagem E0684, indicando que é obrigatório informar a alíquota quando há base de cálculo do imposto.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227168604055)

 **SOLUÇÃO**

Para resolver esta rejeição, configure corretamente a alíquota de PIS no cadastro de alíquotas:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227185224215)

 Acesse a tela **"Alíquota de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227185225623)

 Localize o registro de alíquota correspondente ao **produto** e ao **"Código de situação tributária - CST"** utilizado na nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227185226391)

 Verifique se o campo **"Alíquota"** está preenchido com o percentual correto do PIS:

- 

Se o campo estiver **vazio ou zerado**, informe a alíquota adequada conforme a legislação vigente e o regime tributário da empresa.

- 

Certifique-se de que o campo **"Tipo"** da alíquota está configurado corretamente como **"Entrada"** ou **"Saída"**, de acordo com o CST informado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227168606487)

 Confirme que a marcação **"Produto sem tributação"** não está ativada, pois ela zera automaticamente os campos de alíquota.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227185227031)

 Salve as alterações realizadas no cadastro de alíquotas.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227168607895)

 Retorne ao documento fiscal rejeitado e realize uma nova tentativa de transmissão da nota. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227168608535)

 **CAUSA**

A rejeição ocorreu porque o sistema identificou que existe uma **base de cálculo do PIS** informada no documento fiscal, mas a **alíquota correspondente não foi preenchida** no cadastro de **"Alíquota de PIS"**. Segundo a legislação tributária e as regras de validação da Sefaz, sempre que houver base de cálculo para o imposto, é obrigatório informar a alíquota aplicável. A ausência dessa informação impede a correta apuração do tributo e, consequentemente, a autorização do documento fiscal.