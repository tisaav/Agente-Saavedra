# O valor 'XXXX' do elemento 'NCM' não é válido

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507654-O-valor-XXXX-do-elemento-NCM-n%C3%A3o-%C3%A9-v%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507654-O-valor-XXXX-do-elemento-NCM-n%C3%A3o-%C3%A9-v%C3%A1lido)  
> **ID:** `360042507654` | **Última Atualização:** 2026-07-22T16:10:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057492631)

 MENSAGEM:**

ERRO NA VALIDAÇÃO. Número Único: 'X'
Validação básica Sefaz: Erros encontrados:
cvc-pattern-valid: O valor 'XXXX' não tem um aspecto válido em relação ao padrão '[0-9]{2}|[0-9]{8}' do tipo '#AnonType_NCMproddetinfNFeTNFe'.
cvc-type.3.1.3: O valor 'XXXX' do elemento 'NCM' não é válido. erro.handshake=true

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057495191)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057497751)

 Acesse a tela** "[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** (*Arquivos » Produtos*),  Aba **"Propriedades"** - Campo **'Cód.NCM': **informe um NCM válido.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315047061783)

 Na mensagem de erro é retornado o NCM rejeitado. Caso não saiba a qual produto esse NCM está vinculado, gere o XML em conferência conforme abaixo para análises detalhadas:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057504407)

 Selecione a nota rejeitada » Lançamento » Botão direito » **"Gerar XML da NF-e em arquivo para Conferência"**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057504407)

 Abra o XML gerado pelo Internet Explorer e/ou Bloco de Notas.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057504407)

 Aperte ctrl+f do teclado, será aberto um campo de busca, faça a busca pelo código do NCM apresentado na mensagem de erro, até que seja localizado o código do produto (<cProd>) referenciado na rejeição apresentada.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057505559)

 CASO DE USO:**

Validação básica Sefaz: Erros encontrados:
cvc-pattern-valid: O valor** '33043000'** não tem um aspecto válido em relação ao padrão '[0-9]{2}|[0-9]{8}' do tipo '#AnonType_NCMproddetinfNFeTNFe'.
cvc-type.3.1.3: 
O valor **'33043000'** do elemento 'NCM' não é válido. erro.handshake=true

Identificado o item rejeitado, realize os ajustes no campo citado, conforme item 1 desse artigo.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315057507991)

 ATENÇÃO:** É possível realizar a consulta de NCM por Descrição ou Código, através do seguinte link:

**[Consulta NCM](https://efisco.sefaz.pe.gov.br/sfi_com_tge/PRConsultarNCM)**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315047068567)

 CAUSA:**

Ocorre quando uma NF-e for transmitida,  onde o NCM de um ou mais itens, não existir na Tabela de NCM publicado pelo MDIC²-Ministério do Desenvolvimento, Indústria e Comércio Exterior.


---

### 🔗 Links e Referências Internas:

- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)