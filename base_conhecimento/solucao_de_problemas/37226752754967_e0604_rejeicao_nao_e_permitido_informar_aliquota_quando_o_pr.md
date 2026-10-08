# E0604 Rejeição: Não é permitido informar alíquota quando o prestador de serviço possui algum regime especial de tributação.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226752754967-E0604-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-prestador-de-servi%C3%A7o-possui-algum-regime-especial-de-tributa%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226752754967-E0604-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-prestador-de-servi%C3%A7o-possui-algum-regime-especial-de-tributa%C3%A7%C3%A3o)  
> **ID:** `37226752754967` | **Última Atualização:** 2026-07-22T14:14:39Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226752747415)

 **MENSAGEM**

E0604 Rejeição: Não é permitido informar alíquota quando o prestador de serviço possui algum regime especial de tributação.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226752748567)

 **SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviço Eletrônica), o sistema rejeitou o documento com a mensagem E0604.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226752748695)

 **SOLUÇÃO**

Para resolver esta rejeição, verifique as configurações da empresa e ajuste conforme necessário:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226752748823)

 Acesse a tela ****["Empresa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Configurações » Cadastros » Empresa) e localize a empresa emitente da NFS-e. 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37619567600791)

 Navegue até a aba **"Documentos Fiscais Eletrônicos"**, depois acesse a sub-aba **"NFS-e"** e em seguida a seção **"Geral"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37619567602839)

 Verifique o campo **“Regime esp. tributação ISS (NFS-e)”** e, caso esteja preenchido com alguma das opções abaixo, a empresa estará configurada com **regime especial de tributação**.

- 

**''Microempresa municipal''**

- 

**''Estimativa''**

- 

**''Sociedade de profissionais''**

- 

**''Cooperativa''**

- 

**''Microempresário Individual (MEI)''**

- 

**''Microempresário e Empresa de Pequeno Porte (ME EPP)''**

- 

**''Optante pelo Simples Nacional''**

- 

**''Normal / Nenhum''**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226736438295)

 Escolha uma das alternativas abaixo conforme a situação da empresa: 

**Se a empresa realmente possui regime especial de tributação:**

- 

Remova a alíquota de ISS informada na NFS-e.

- 

Acesse a tela **"Alíquota de ISS"** (Contratos e Serviços » Arquivos » Cadastros » Alíquotas de ISS), desabilite ou ajuste a configuração que está enviando a alíquota no documento fiscal.

**Se a empresa não possui regime especial de tributação:**

- 

Após acessar a aba indicada no passo 2, deixe o campo **“Regime esp. tributação ISS (NFS-e)”** sem seleção, para que o sistema envie normalmente a alíquota de ISS na NFS-e.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226736438551)

 Salve as alterações realizadas.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37619597495959)

 Emita novamente a NFS-e. O documento deverá ser aceito pela Sefaz sem a rejeição E0604.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226736439447)

 **CAUSA**

A rejeição E0604 ocorre porque a **legislação fiscal não permite** que uma NFS-e contenha simultaneamente a informação de **regime especial de tributação de ISS** e a **alíquota de ISS**. Quando a empresa possui regime especial, a tributação segue regras diferenciadas, tornando incompatível o envio da alíquota padrão. O sistema rejeitou o documento para garantir a conformidade com as regras estabelecidas pela Secretaria da Fazenda Municipal.


---

### 🔗 Links e Referências Internas:

- ["Empresa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa)