# O parceiro 'X' não está habilitado na SEFAZ

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615413-O-parceiro-X-n%C3%A3o-est%C3%A1-habilitado-na-SEFAZ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615413-O-parceiro-X-n%C3%A3o-est%C3%A1-habilitado-na-SEFAZ)  
> **ID:** `360044615413` | **Última Atualização:** 2026-07-31T02:48:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609557072279)

 MENSAGEM:**

[CORE_E04217]:  O parceiro 'X' não está habilitado na SEFAZ.

[CORE_E04216] O parceiro 'X' não está habilitado na Receita Federal.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609603797015)

SOLUÇÃO:**

Para correção seguir os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609603799319)

 **Verifique a configuração da TOP** Acesse **Comercial » Arquivo » Cadastros » Tipos de Operação – TOP**, aba **Geral**, opção **"Valida situação cadastro na SEFAZ"**.

Quando marcada, o sistema valida a situação cadastral na confirmação de **Pedidos/Notas**, **Formação de Carga** e **Faturamento**.

A consulta é feita por um WebService da própria SEFAZ. Como essa informação é de responsabilidade do órgão, pode haver casos em que o retorno esteja desatualizado.

A validação de SEFAZ vale para qualquer tipo de parceiro (física ou jurídica). Já a validação de **Receita Federal** (CORE_E04216) só se aplica a parceiros **pessoa jurídica**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609603800855)

 **Verifique a situação cadastral do parceiro** Acesse **Configurações » Cadastros » Parceiros**, aba **Fiscal**, campo **"Situação Cadastral SEFAZ"**. Se estiver **"Não Habilitado"**, o sistema bloqueia a confirmação mesmo para não contribuintes.

**Observação:**** **caso o parceiro esteja como **"Não Habilitado",** **a validação será efetuada mesmo sendo um parceiro não contribuinte.**

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42359898870423)

  Se a restrição não se aplicar, use "Suspender validação SEFAZ"** A SEFAZ pode retornar "Não Habilitado" sem que isso impeça de fato o parceiro de comprar ou realizar operações com ICMS. Nesse caso, no cadastro do Parceiro, aba Fiscal → **Outras Opções » Suspender validação SEFAZ**, informe no pop-up **"Data para nova Consulta"** a partir de quando o retorno da SEFAZ deve voltar a ser considerado. O sistema libera a confirmação imediatamente e só consulta a SEFAZ novamente na data informada.

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42359898870935)

 **No parâmetro **"QTDDIACONSSEFAZ - Qtde de dias para realizar nova consulta na SEFAZ"**, deverá ser informado a quantidade de dias em que será realizado nova consulta, para verificar a situação do Parceiro junto a SEFAZ:

- 

Se o número de dias desde a última consulta for menor que o valor definido no parâmetro, a validação será feita pelo campo 'Situação Cadastral SEFAZ' do Cadastro do Parceiro, sem nova consulta à SEFAZ.

- 

Se ao tenta confirmar o Pedido/Nota o campo "Sit. Cad. SEFAZ", retornar zero, o sistema não confirmará o Pedido.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15021605550999)

 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16609603802647)

CAUSA:**

A TOP usada no pedido/nota está configurada para validar a situação cadastral do parceiro. Ao confirmar o documento, o sistema consulta a SEFAZ (e, se aplicável, a Receita Federal) e identifica alguma restrição/suspensão/irregularidade que impede a emissão do documento eletrônico para esse parceiro.