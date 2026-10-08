# E0352 Rejeição: O preenchimento do campo nDI (Número da Declaração de Importação) é obrigatório quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 2.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224574847767-E0352-Rejei%C3%A7%C3%A3o-O-preenchimento-do-campo-nDI-N%C3%BAmero-da-Declara%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-2](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224574847767-E0352-Rejei%C3%A7%C3%A3o-O-preenchimento-do-campo-nDI-N%C3%BAmero-da-Declara%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-2)  
> **ID:** `37224574847767` | **Última Atualização:** 2026-07-22T14:16:29Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574807447)

 **MENSAGEM**

E0352 Rejeição: O preenchimento do campo nDI (Número da Declaração de Importação) é obrigatório quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 2.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574810135)

 **SITUAÇÃO**

Ao tentar processar uma **Nota Fiscal Eletrônica de importação** vinculada a uma **movimentação temporária de bens com retorno**, o sistema apresenta a rejeição informando que o **número da Declaração de Importação (DI)** não foi informado. O usuário estava lançando produtos importados em uma operação de **retorno de movimentação temporária** e não preencheu o campo obrigatório referente à **Declaração de Importação**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574811543)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224590719511)

 Acesse a tela ****[''Portal de Compras''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras) (Comercial » Consulta » Portal de Compras).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574816407)

 Localize e abra a nota que está apresentando a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574822807)

 Para cada item da nota, clique no botão **"Outras Opções" **(ícone com três pontos), e selecione **"Declaração de Importação e Adições"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224590732823)

 No pop-up da **"Declaração de Importação"**, preencha corretamente os seguintes campos obrigatórios:

- 

**"Número da DI/DSI/DA"**: informe o número da Declaração de Importação.

- 

**"Data de Registro"**: informe a data de registro da DI.

- 

**"Local de Desembaraço"**: informe o local onde ocorreu o desembaraço aduaneiro.

- 

**"UF de Desembaraço"**: selecione a Unidade Federativa correspondente.

- 

**"Data de Desembaraço"**: informe a data do desembaraço aduaneiro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224590734487)

 Repita o procedimento para **todos os produtos da NFe** que estejam vinculados à **movimentação temporária de bens com retorno**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574833687)

 Para conferência, gere o **XML da NFe** e pesquise pela tag **"<nDI>"** para certificar que foi gerada corretamente em todos os produtos.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574836631)

 Após os ajustes, gere novamente o lote da nota fiscal.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224574839191)

 **CAUSA**

A rejeição ocorre quando o campo **"Vínculo da Operação à Movimentação Temporária de Bens" (movTempBens)** está preenchido com o valor **"2 - Retorno de movimentação temporária"** e o campo **"Número da Declaração de Importação (nDI)"** não foi informado na **Declaração de Importação** dos produtos. Conforme a regra de validação da Sefaz, quando há **retorno de movimentação temporária de bens importados**, é obrigatório informar os dados da DI para que a nota seja aceita.


---

### 🔗 Links e Referências Internas:

- [''Portal de Compras''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)