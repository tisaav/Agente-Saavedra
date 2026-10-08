# NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042725654-NF-e-com-identifica%C3%A7%C3%A3o-de-estrangeiro-e-inscri%C3%A7%C3%A3o-estadual-informada-para-destinat%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042725654-NF-e-com-identifica%C3%A7%C3%A3o-de-estrangeiro-e-inscri%C3%A7%C3%A3o-estadual-informada-para-destinat%C3%A1rio)  
> **ID:** `360042725654` | **Última Atualização:** 2026-07-22T16:06:41Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512065472919)

 MENSAGEM:**

[925 - Rejeição]: NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512078254487)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512078257559)

 O erro será retornado quando haver 'Identificação de Estrangeiro' e  'Insc. Estadual / Identidade' e se trabalhar com CFOP's iniciados em 3 ou 7.

Desta forma, informe apenas a 'Identificação de Estrangeiro', **deixando em branco a 'Insc. Estadual / Identidade'.**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512065483287)

 Acesse a tela "**[Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)** (Caminho de acesso:* Configurações » Cadastros*)

- Aba: **"Identificação"**

- Campo** "Identificação de Estrangeiro":** utilize o campo "**Identificação de Estrangeiro**" para Parceiros do exterior, em vendas com geração de NF-e ou NFC-e. Informe aqui o número do passaporte ou outro documento legal para identificar a pessoa estrangeira. A informação deste campo deve ter entre 5 e 20 caracteres/números.

![NF-e_com_identifica__o_de_estrangeiro_e_inscri__o_estadual_informada_para_destinat_rio.png](https://ajuda.sankhya.com.br/hc/article_attachments/14612294635543)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512078262167)

 Após os ajustes, gere o lote novamente.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512078265367)

 IMPORTANTE:**

O parâmetro **"ACEITAIEBRANCO - Aceita Insc. Est. de Parceiro em branco?"** deve estar habilitado para que a I.E. fique vazia no cadastro do Parceiro. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512065493783)

CAUSA:**

Quando for realizada uma operação estrangeira, tag <idEstrangeiro>, e CFOP com iniciais 3 ou 7, mas em conjunto está sendo informada 'Inscrição Estadual', tag <IE>, do Parceiro.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16512065495703)

 OBSERVAÇÃO:**

([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota técnica


---

### 🔗 Links e Referências Internas:

- [Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)