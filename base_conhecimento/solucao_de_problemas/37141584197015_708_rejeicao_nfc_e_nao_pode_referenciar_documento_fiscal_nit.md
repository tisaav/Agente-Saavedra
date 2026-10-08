# 708 Rejeição: NFC-e não pode referenciar documento fiscal [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141584197015-708-Rejei%C3%A7%C3%A3o-NFC-e-n%C3%A3o-pode-referenciar-documento-fiscal-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141584197015-708-Rejei%C3%A7%C3%A3o-NFC-e-n%C3%A3o-pode-referenciar-documento-fiscal-nItem-999)  
> **ID:** `37141584197015` | **Última Atualização:** 2026-07-22T14:19:01Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141584178711)

 **MENSAGEM**

708 Rejeição: NFC-e não pode referenciar documento fiscal [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141575552151)

 **SITUAÇÃO**

Ao tentar transmitir uma NFC-e (Nota Fiscal de Consumidor Eletrônica – modelo 65), o sistema retorna uma rejeição durante o processo de autorização, impedindo a conclusão da emissão do documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141575553047)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141575554327)

 Acesse a tela ****[''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141584183191)

 Localize a TOP utilizada para emissão da NFC-e.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141584184215)

 Na aba **“NF-e/NFC-e/CF-e”**, verifique o campo **“Buscar NF de origem p/ referenciar na NFe”**:

- 

Se a opção estiver **marcada**, **desmarque-a** para emissões de **NFC-e**;

- 

Essa configuração deve permanecer **desativada** para evitar referência indevida de NF-e na emissão da NFC-e.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141584185367)

 Caso esteja tentando emitir uma **NFC-e complementar ou de ajuste**, altere o **modelo do documento** para **NF-e (modelo 55)**, pois somente esse modelo permite a **referência a outros documentos fiscais**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141584187671)

 Se for necessário manter o **modelo NFC-e**, remova da nota fiscal **qualquer referência a outros documentos**, como **chaves de acesso**, **números de notas** ou **documentos fiscais vinculados**, garantindo que a emissão esteja de acordo com as regras desse modelo.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38186313760663)

 Acesse a tela ****[“Central de Vendas”](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Faturamento » Central de Vendas) e verifique se existe algum campo de **referência a documentos fiscais** preenchido.

- 

Caso haja, **limpe essas informações** antes de gerar a **NFC-e**, garantindo que não haja vínculos indevidos com outros documentos.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141584188311)

 **CAUSA**

A rejeição ocorre porque, de acordo com as regras da SEFAZ, o modelo de NFC-e (65) **não permite referenciar outros documentos fiscais** em sua estrutura. Diferentemente da NF-e (modelo 55), a NFC-e é destinada exclusivamente a operações de venda ao consumidor final, não sendo permitido seu uso para complementos, ajustes ou qualquer operação que exija referência a documentos anteriores.

Esta limitação está alinhada com a finalidade da NFC-e, que é simplificar as operações de varejo. Quando há necessidade de referenciar documentos fiscais, o modelo adequado a ser utilizado é a NF-e (modelo 55).


---

### 🔗 Links e Referências Internas:

- [''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [“Central de Vendas”](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)