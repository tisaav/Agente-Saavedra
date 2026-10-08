# E0449 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por documento informado.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225524007703-E0449-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-servi%C3%A7o-informado-na-DPS-n%C3%A3o-permite-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-do-ISSQN-por-documento-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225524007703-E0449-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-servi%C3%A7o-informado-na-DPS-n%C3%A3o-permite-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-do-ISSQN-por-documento-informado)  
> **ID:** `37225524007703` | **Última Atualização:** 2026-07-22T14:15:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225540619543)

 **MENSAGEM**

E0449 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por documento informado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225523997591)

 **SITUAÇÃO**

Ao emitir uma **NFS-e**, o sistema apresenta a mensagem de rejeição informando que o código de serviço utilizado **não permite dedução ou redução na base de cálculo do ISSQN**, mesmo que tenha sido configurado algum percentual de dedução ou redução no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225523998231)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225523999127)

 Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225540624151)

 Localize o serviço utilizado no documento fiscal rejeitado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225540624919)

 Verifique o campo **"Cód. Tributação ISS"** e identifique qual código está configurado:

- 

**''07 - Não Tributado''**

- 

**''06 - Isento''**

- 

**''00 - Tributado''**

- 

**''01 - Tributado com ISS Retido''**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225540625815)

 Verifique se o campo **"Perc. de dedução na base do ISS"** está preenchido com algum percentual de dedução ou redução.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225540626711)

 Consulte o **manual da Prefeitura do município** onde o serviço está sendo prestado para verificar se o código de serviço utilizado permite dedução ou redução na base de cálculo do ISSQN.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225524002711)

 Caso o código de serviço **não permita dedução/redução**, realize **um dos seguintes ajustes**:

- 

Remova o percentual informado no campo **"Perc. de dedução na base do ISS"**, deixando-o zerado

- 

Altere o campo **"Tipo de dedução de base do ISS"** para uma opção compatível com a legislação municipal

- 

Utilize um código de serviço diferente que permita a dedução/redução, conforme orientação do seu contador

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225540628503)

 Acesse a tela ****["Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37695925156375)

 Na aba **"NFS-e"**, verifique o campo **"Desconto Condicionado para NFS-e"**, garantindo que esteja configurado adequadamente.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37695911522455)

 Salve as alterações realizadas e emita novamente a **NFS-e**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225524004503)

 **CAUSA**

A rejeição ocorre porque o **código de serviço** informado no documento fiscal possui configurações de **dedução ou redução na base de cálculo do ISSQN**, porém a **legislação municipal** não permite esse tipo de dedução/redução para o serviço específico. Cada município possui regras próprias sobre quais serviços permitem deduções, e o sistema valida essas informações no momento da emissão da NFS-e, rejeitando documentos que não estejam em conformidade com as regras da Prefeitura.


---

### 🔗 Links e Referências Internas:

- ["Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)