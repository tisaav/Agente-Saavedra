# 904 - Rejeição: Informado indevidamente campo valor de pagamento

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360048487613-904-Rejei%C3%A7%C3%A3o-Informado-indevidamente-campo-valor-de-pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048487613-904-Rejei%C3%A7%C3%A3o-Informado-indevidamente-campo-valor-de-pagamento)  
> **ID:** `360048487613` | **Última Atualização:** 2026-07-22T15:31:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588816917783)

 MENSAGEM:**

904 - Rejeição: Informado indevidamente campo valor de pagamento.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588786108311)

 CAUSA:**

Informado o campo Meio de Pagamento igual a sem pagamento (tag <tPag> =90) e informado campo Valor do Pagamento diferente de zero (tag:vPag<>0).

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588816930839)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588816937751)

 Certifique-se que a UF emissora da nota, não conste no parâmetro abaixo:

- Tela 'Preferências' *(Configurações » Avançado » Preferências) >> *Chave **UFs que omitem o schema NFe 4.0 v1.60B - UFNFEOMITV160B**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18588786128151)

Foi criado o parâmetro UFNFEOMITV160B (UFs que omitem o schema NFe 4.0 v1.60B) com default vazio. Essa criação ocorreu quando algumas UFs ainda estavam com sua SEFAZ sem implementar esse schema.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588816945943)

 Caso utilize os módulos Delph [G1 ou Mitra], certifique-se de estar utilizando versões de executáveis atuais. [4.23.0.11 ou superior].

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588816955543)

 Após avaliar os dois itens acima, refaça o faturamento. Gere um XML em conferência e avalie se a tag <tPag> = 90, e a tag <vPag> = 0,00

*<detPag>*
***<tPag>90</tPag>***
***<vPag>00.00</vPag>***
*</detPag>*

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588786142359)

Gere um novo lote.

**Importante:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588816937751)

 Caso para a emissão realizada, não deva ser gerado <tPag> = 90 [Sem pagamento], será necessário junto ao setor financeiro da empresa, reavaliar as marcações abaixo:

- Acesse o cadastro da TOP, e verifique na aba:Geral, o campo 'Financeiro' = [INCLUIR] 

- Se a TOP já estiver configurada para gerar financeiro, verifique o Tipo de Titulo vinculado ao Tipo de Negociação usado na NFC-e, acesse o cadastro de tipo de titulo *(Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título)*, aba Geral, campo **'Tipo de pgto para NFC-e / NF-e / CF-e**:' e verifique se está configurado com a opção 90-Sem Pagamento. [Ajuste conforme recomendado pelo Financeiro]

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588816945943)

 Nota Técnica 2016.002 - v 1.60:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)