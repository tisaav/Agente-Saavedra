# Imprimir a tag <placa> no XML/DANFE 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/12228255422743-Imprimir-a-tag-placa-no-XML-DANFE](https://ajuda.sankhya.com.br/hc/pt-br/articles/12228255422743-Imprimir-a-tag-placa-no-XML-DANFE)  
> **ID:** `12228255422743` | **Última Atualização:** 2026-07-22T15:01:13Z

---

Para que a tag <placa> seja destacada no XML e DANFE, preencha devidamente o campo **"Gerar as informações do Grupos Veículo Transporte e Grupo Reboque",** nas Preferências da Empresa.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14684961203479)

 

#### **Veja as Opções:**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450715908887)

 Dentro do Município:** A tag <placa> será destacada apenas para notas emitidas para o mesmo município da empresa emissora.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450715908887)

 Todas as Operações:** A tag <placa> será destacada para todas as notas emitidas.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450715908887)

 Dentro do Estado:** A tag <placa> será destacada apenas para notas emitidas para a mesma UF da empresa emissora. Porém, irá depender da validação da Sefaz de cada estado, pois algumas retornam a Rejeição: 868-Rejeição: Grupos Transportador, Veiculo Transporte e Reboque não devem ser informados.

Caso apresente a rejeição mencionada acima, verifique com a Contabilidade da Empresa a melhor opção a ser utilizada.

 
**Observação:**
 
Caso as informações acima estiverem preenchidas e a tag <placa> ainda não esteja sendo gerada é necessário verificar também o parâmetro abaixo:
 
Tela:** Preferências-** *Configurações » Avançado » Preferências*

**CONOCTRANSPXML : Considerar OC para gerar tag veicTransp XML**
 

**Ligado:** O sistema irá considerar uma Ordem de Carga para gerar a tag <placa> , caso não possua a ordem de carga o sistema não irá gerar a tag.

**Desligado:** O sistema irá buscar as informações cadastradas na central na aba transporte.