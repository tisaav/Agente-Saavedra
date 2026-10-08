# CNPJ da instituição de pagamento inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16195241533591-CNPJ-da-institui%C3%A7%C3%A3o-de-pagamento-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/16195241533591-CNPJ-da-institui%C3%A7%C3%A3o-de-pagamento-inv%C3%A1lido)  
> **ID:** `16195241533591` | **Última Atualização:** 2026-07-22T14:55:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275901344919)

  MENSAGEM: **

Rejeição 437: CNPJ da instituição de pagamento inválido

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275901347607)

 CAUSA:**

Conforme Regra de Validação da SEFAZ na emissão da NFe(modelo 55) ou NFCe(modelo 65) quando informado no Grupo de Cartões (grupo: <card>) no XML CNPJ com zeros, nulo ou DV inválido será retornado a rejeição "Rejeição 437: CNPJ da instituição de pagamento inválido". 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275910184471)

 SOLUÇÃO:**

- No XML, no grupo <card> verifique a TAG <CNPJ>:

<pag>

<detPag>

<indPag>1</indPag>

<tPag>03</tPag>

<vPag>1.00</vPag>

<card>

<tpIntegra>1</tpIntegra>

<CNPJ>00000000000000</CNPJ>

<tBand>01</tBand>

<cAut>000000000005540</cAut>

</card>

</detPag>

</pag>
 
Neste exemplo o CNPJ do parceiro administradora estava zerado. 
 
**Observação:** Para extrair o XML no Portal de Vendas basta selecionar a nota, clique no botão NFe (ou NFCe) e selecione a opção **"Gerar XML da NF-e/NFC-e em arquivo para conferência"**; 
 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16276036314263)

 Abra a nota na Central de Vendas, e na aba **"Financeiro"** identifique qual tipo de titulo utilizado; 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16276081185431)

 Após identificar o Tipo de Titulo utilizado na operação, acesse a tela **"****Tipos de Título" ***(Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título)*, na aba **"Geral"** localize o campo **"Parc.Administradora"** e verifique qual parceiro foi informado; 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16276081186967)

 Acesse a tela **"Parceiros"** *(Caminho de acesso: Configurações » Cadastros » Parceiros)* e verifique se no campo **"CNPJ / CPF"** foi informado um CNPJ válido, se não, faça a atualização dos dados. 

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16276036325271)

 Após correção do cadastro do parceiro volte novamente no Portal de Vendas e gere o lote da nota; 

 

Regra de validação da SEFAZ:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16195027678103)

 

Referência: Nota Técnica 2020/006 (v 1.40)

https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=