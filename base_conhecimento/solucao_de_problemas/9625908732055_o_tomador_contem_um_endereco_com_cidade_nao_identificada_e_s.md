# O tomador contém um endereço com Cidade não identificada e sem o país informado, caso esteja emitindo uma nota fiscal para tomador do exterior informe o país do mesmo

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9625908732055-O-tomador-cont%C3%A9m-um-endere%C3%A7o-com-Cidade-n%C3%A3o-identificada-e-sem-o-pa%C3%ADs-informado-caso-esteja-emitindo-uma-nota-fiscal-para-tomador-do-exterior-informe-o-pa%C3%ADs-do-mesmo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9625908732055-O-tomador-cont%C3%A9m-um-endere%C3%A7o-com-Cidade-n%C3%A3o-identificada-e-sem-o-pa%C3%ADs-informado-caso-esteja-emitindo-uma-nota-fiscal-para-tomador-do-exterior-informe-o-pa%C3%ADs-do-mesmo)  
> **ID:** `9625908732055` | **Última Atualização:** 2026-07-22T15:07:11Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667143551383)

**Mensagem**

  [CORE_E06044] O tomador contém um endereço com cidade não identificada e sem o país informado, caso esteja emitindo uma nota fiscal para tomador do exterior informe o país do mesmo. Erro na validação do nome da cidade cadastrada no sistema emissor de nota fiscal, que difere do nome oficial registrado na base de dados do IBGE (Instituto Brasileiro de Geografia e Estatística).

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667165059735)

**Situação**

  Ao tentar faturar a **"Nota Fiscal Eletrônica de Serviços (NFS-e)"**, o sistema apresenta erro relacionado ao cadastro de endereço do cliente ou do prestador de serviços. A mensagem indica que a cidade não está identificada ou que há divergência entre o nome cadastrado e o nome oficial do município na tabela do IBGE. Este erro impede a autorização e transmissão da nota fiscal para a prefeitura.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667165068183)

**Causa**

  O erro ocorre quando o nome da cidade cadastrado no sistema emissor de nota fiscal está diferente do nome oficial registrado na base de dados do IBGE. Esta divergência pode acontecer por:

- Erros de digitação no cadastro do parceiro ou da cidade;

1. Uso de abreviações não oficiais do nome do município;

1. Diferenças de acentuação ou caracteres especiais;

1. Cadastros antigos que não foram atualizados conforme o padrão do IBGE;

1. Ausência de informações obrigatórias como o país no endereço.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667165070103)

**Solução**

  Para resolver o problema, corrija o cadastro da cidade no sistema seguindo os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39742629341591)

  Acesse a tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades) e localize a cidade para a qual está emitindo a nota, ou acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros) caso precise ajustar o endereço específico do cadastro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39742629342487)

  Verifique se o nome da cidade está exatamente igual ao informado no site do IBGE, respeitando acentuação, espaços e caracteres especiais.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39742629343127)

  Consulte o nome oficial do município no site oficial do IBGE: [Brasil | Cidades e Estados | IBGE](https://www.ibge.gov.br/cidades-e-estados).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39742629346583)

  Realize a correção do nome do cadastro da cidade conforme o padrão oficial e salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39742636404119)

  Tente gerar o lote da **"NFS-e"** novamente.

**Exemplos visuais:**

![cidades.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667165073943)

![ibge.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667165085591)

**Observação:** Caso o erro persista, verifique também se o campo **"País"** está devidamente preenchido no endereço do parceiro, pois a ausência desta informação também pode gerar rejeições.