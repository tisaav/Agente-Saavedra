# 486 Rejeição: Não informado o Grupo de Autorização para UF que exige a identificação do Escritório de Contabilidade na Nota Fiscal

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043120633-486-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-Grupo-de-Autoriza%C3%A7%C3%A3o-para-UF-que-exige-a-identifica%C3%A7%C3%A3o-do-Escrit%C3%B3rio-de-Contabilidade-na-Nota-Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043120633-486-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-Grupo-de-Autoriza%C3%A7%C3%A3o-para-UF-que-exige-a-identifica%C3%A7%C3%A3o-do-Escrit%C3%B3rio-de-Contabilidade-na-Nota-Fiscal)  
> **ID:** `360043120633` | **Última Atualização:** 2026-07-22T16:07:20Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486334106519)

 **MENSAGEM:**

486 Rejeição: Não informado o Grupo de Autorização para UF que exige a identificação do Escritório de Contabilidade na Nota Fiscal

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486322693911)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486322700695)

 Acesse: *Comercial » Preferências » Empresa*

- 

Aba: **"Contador"**

- 

Campo** "Enviar responsável contábil na NFE?": **marque 

**Nota:** *Esta informação dependerá de cada SEFAZ Estadual exigi-la. Verifique com o contador da Empresa se a Sefaz do seu estado exige esta informação e, caso positivo, marque esta opção e preencha os dados desta aba. Caso negativo, desmarque a opção.*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486334114327)

 Após os ajustes, gere o lote da nota novamente.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486334119959)

 Configure a aba "**Acesso ao XML da NF-e/CTe", **na tela **"******[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**"** (Caminho de acesso:* Comercial » Preferências » Empresa*)com o nome SEFAZ e o CNPJ informada na mensagem de erro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486334126359)

 CAUSA:**

Quando for emitida uma NF-e e a Sefaz exigir que seja informado no Grupo de Autorização para obter o XML (autXML) a identificação (CNPJ ou CPF) do Escritório de Contabilidade e o grupo em questão não for informado, será retornada a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16486334129303)

 OBSERVAÇÃO:**
 

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=v9JbkEY7evI=)) - Nota Técnica.


---

### 🔗 Links e Referências Internas:

- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)