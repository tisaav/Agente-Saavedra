# Configurações de Ajustes de Apuração, Filtro UF na geração de Ajuste de documento Devolução de Venda

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16005178315671-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o-Filtro-UF-na-gera%C3%A7%C3%A3o-de-Ajuste-de-documento-Devolu%C3%A7%C3%A3o-de-Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/16005178315671-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o-Filtro-UF-na-gera%C3%A7%C3%A3o-de-Ajuste-de-documento-Devolu%C3%A7%C3%A3o-de-Venda)  
> **ID:** `16005178315671` | **Última Atualização:** 2026-07-22T14:55:39Z

---

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16861888031767)

 SOLUÇÃO:**

Sobre a geração na tela **Configurações de Ajustes de Apuração** *(Livros Fiscais » Arquivos » Configurações de Ajustes de Apuração)*, para devolução de emissão própria, ao gerar no livro o sistema faz um tratamento identificando que a mercadoria entrou no estoque e inverte Origem e Destino da UF. Diante disso, segue abaixo uma sugestão de filtro que atende a demanda.

 

EXISTS(
SELECT 1
FROM TGFPAEM M
WHERE CAB.CODPARC = M.CODPARC
AND CAB.CODEMP = M.CODEMP
AND CAB.NUNOTA = ITE.NUNOTA
AND LIV.NUNOTA= CAB.NUNOTA
AND LIV.SEQUENCIA = ITE.SEQUENCIA
AND ITE.CODPROD = PRO.CODPROD
**AND LIV.UFORIGEM <> 'SC'**
AND ITE.ALIQICMS = X
AND PRO.GRUPOICMS = XXXXX
AND CAB.CODTIPOPER IN (XX, XX, XX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX))

Em seguida basta rodar a geração do Livro. Lembrando que o sistema apresenta a nota no livro primeiro, e depois gera os ajustes, o intervalo entre um acontecimento e outro pode demorar, então para consultar o ajuste na nota, certifique que a geração no livro encerrou.