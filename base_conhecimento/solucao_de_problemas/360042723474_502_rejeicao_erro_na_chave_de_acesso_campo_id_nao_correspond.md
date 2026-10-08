# 502 Rejeição: Erro na Chave de Acesso - Campo Id não corresponde à concatenação dos campos correspondentes

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042723474-502-Rejei%C3%A7%C3%A3o-Erro-na-Chave-de-Acesso-Campo-Id-n%C3%A3o-corresponde-%C3%A0-concatena%C3%A7%C3%A3o-dos-campos-correspondentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042723474-502-Rejei%C3%A7%C3%A3o-Erro-na-Chave-de-Acesso-Campo-Id-n%C3%A3o-corresponde-%C3%A0-concatena%C3%A7%C3%A3o-dos-campos-correspondentes)  
> **ID:** `360042723474` | **Última Atualização:** 2026-07-22T16:06:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513844145303)

 MENSAGEM:**

502 Rejeição: Erro na Chave de Acesso - Campo Id não corresponde à concatenação dos campos correspondentes.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513885280407)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513885294615)

 Realize a consulta da chave NF-e gerada nos Portais Nacional e Estadual da SEFAZ, certificando-se que essa não foi recebida/autorizada.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513844169623)

 SEFAZ NACIONAL:

-  Acesse [Sefaz nacional](https://www.nfe.fazenda.gov.br/portal/principal.aspx)

-  Selecione a opção Serviços >> [Consultar NF-e](https://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=resumo&tipoConteudo=d09fwabTnLk=) 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513844169623)

 SEFAZ ESTADUAL

-  Acesse [Sefaz estadual](https://www.nfe.fazenda.gov.br/portal/principal.aspx)

-  Selecione ao lado direito a opção 'Portais Estaduais da NF-e'

- Selecione o Estado da empresa emissora 4- No Portal da empresa emissora busque pelo serviço de Consulta de notas/chave.

![Erro_na_Chave_de_Acesso_-_Campo_Id_n_o_corresponde___concatena__o_dos_campos_correspondentes.png](https://ajuda.sankhya.com.br/hc/article_attachments/14639236774039)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513885306391)

 Caso a consulta acima retorne a chave como Inexistente em ambas [SEFAZ Nacional e Estadual] e o Status dessa NF-e esteja como 'Aguardando Correção', proceda com a inutilização e exclusão da nota rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513885310103)

 Emita uma nova nota, onde a chave será gerada conforme dados atuais.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513885313687)

 IMPORTANTE:**

Atualmente a chave de acesso de um documento fiscal eletrônico é formado pelas seguintes informações:

********

| Campo | Quantidade de caracteres |
| --- | --- |
| Código da UF do emitente | 02 |
| Ano e mês de emissão da NF-e | 04 |
| CNPJ do emitente | 14 |
| Modelo do documento fiscal | 02 |
| Série do documento fiscal | 03 |
| Número do Documento Fiscal | 09 |
| Forma de emissão da NF-e | 01 |
| Código numérico que compõe a chave de acesso | 08 |
| Dígito verificador da chave de acesso | 01 |

 

Caso consiga compreender qual campo causou a divergência, realize os devidos ajustes, de forma que a informação original seja contemplada.

**Exemplo: 
**

- Lançada NF-e com data de entrada e saída igual a  30/11, gerada chave com mês 11, porém a nota não foi aprovada de imediato. Após virada do mês atualiza-se a data da nota para 02/12 e é realizada uma tentativa de geração de lote com mês 12, causando a rejeição. 

![Erro_na_Chave_de_Acesso_-_Campo_Id_n_o_corresponde___concatena__o_dos_campos_correspondentes_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14639276310039)

Como vemos no XML, as tags do XML foram geradas com data atual, mas a chave é composta pelo ano de 2019, mês 11. O que gera erro.

- Nesse cenário as datas poderão ser atualizadas para mês 11, conforme chave de acesso, sendo possível a aprovação.

- Caberá a SEFAZ de cada estado recepcionar essa nota em mês subsequente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513885317271)

CAUSA:**

Realizada emissão de NF-e onde os dados concatenados em sua chave NF-e não corresponderem as informações atuais da nota, será apresentada a rejeição.