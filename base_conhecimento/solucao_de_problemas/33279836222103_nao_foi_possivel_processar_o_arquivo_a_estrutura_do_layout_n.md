# Não foi possível processar o arquivo. A estrutura do layout não é adequada a estrutura do arquivo ou não foram encontrados os identificadores correspondentes

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33279836222103-N%C3%A3o-foi-poss%C3%ADvel-processar-o-arquivo-A-estrutura-do-layout-n%C3%A3o-%C3%A9-adequada-a-estrutura-do-arquivo-ou-n%C3%A3o-foram-encontrados-os-identificadores-correspondentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/33279836222103-N%C3%A3o-foi-poss%C3%ADvel-processar-o-arquivo-A-estrutura-do-layout-n%C3%A3o-%C3%A9-adequada-a-estrutura-do-arquivo-ou-n%C3%A3o-foram-encontrados-os-identificadores-correspondentes)  
> **ID:** `33279836222103` | **Última Atualização:** 2026-07-22T14:29:09Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/33279825390743)

**Mensagem**

Não foi possível processar o arquivo. A estrutura do layout não é adequada à estrutura do arquivo ou não foram encontrados os identificadores correspondentes.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/33279836214679)

**Solução**

Para que o processamento funcione bem, configure corretamente os campos essenciais no layout (Configurações >> Cadastros >> Layouts de Processamento de Arquivo). Eles são:

- 
**TIP_MOVTO** – Tipo de movimento;

- 
**NSU_TEF_POS** – NSU gerado pelo TEF (Auttar, SiTef, PayGo etc.);

- 
**NSU_ADQUIRENTE** – NSU gerado pela adquirente (autorizadora);

- 
**COD_AUTORIZACAO** – Código de autorização da transação gerado pela autorizadora;

- 
**DT_MOVTO** – Data da transação;

- 
**QTD_PARCELAS** – Quantidade de parcelas da venda, quando parcelada;

- 
**NRO_PARCELA** – Número da parcela que está sendo paga;

- 
**VLR_PARCELA_LIQ** – Valor líquido da parcela (sem taxa);

- 
**VLR_PARCELA** – Valor bruto da parcela (com taxa);

- 
**VLR_TAXA_AUTORIZACAO** – Valor total da taxa cobrada do cliente pela autorizadora;

- 
**VLR_TRANSACAO** – Valor total da transação;

- 
**DT_PAGTO** – Necessário quando a opção **"Baixar títulos na data do arquivo"** estiver ativa;

- 
**NUM_CONTA_CORRENTE** – Utilizado quando a opção **"Priorizar Conta e Empresa do arquivo na baixa"** estiver marcada, sendo necessário informar também o campo **DIGITO_CONTA**;

- 
**DIGITO_CONTA** – Dígito da conta corrente.

**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/33334733755543)

Importante:** a posição de cada campo no layout precisa corresponder exatamente à ordem das colunas no arquivo de retorno. Isso significa que o campo com sequência 1 deve estar na primeira posição do arquivo, o de sequência 2 na segunda posição e assim por diante. Por isso, ao configurar o layout, é importante prestar atenção na ordem dos campos conforme a estrutura do arquivo recebido. 

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33334722811799)

Se esse erro continuar acontecendo durante o processamento, veja também os artigos abaixo e consulte o manual da operadora para verificar se o arquivo está dentro do padrão esperado: 

- [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334-Concilia%C3%A7%C3%A3o-de-Cart%C3%A3o)

- [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054-Layout-de-Processamento-de-Arquivo)

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/33279825391511)

**Causa**

Esse erro acontece quando o Layout de Processamento do Arquivo não combina com a estrutura do arquivo que está sendo processado.


---

### 🔗 Links e Referências Internas:

- [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334-Concilia%C3%A7%C3%A3o-de-Cart%C3%A3o)
- [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054-Layout-de-Processamento-de-Arquivo)