# Propriedade 'ArquivoRelatorio.NOME' com largura acima do limite: (XX > XX)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34108786627607-Propriedade-ArquivoRelatorio-NOME-com-largura-acima-do-limite-XX-XX](https://ajuda.sankhya.com.br/hc/pt-br/articles/34108786627607-Propriedade-ArquivoRelatorio-NOME-com-largura-acima-do-limite-XX-XX)  
> **ID:** `34108786627607` | **Última Atualização:** 2026-07-22T14:27:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34108786623767)

 **MENSAGEM**

Propriedade 'ArquivoRelatorio.NOME' com largura acima do limite: (XX XX)

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34323985722519)

 **SITUAÇÃO**

O erro ocorre ao tentar inserir ou atualizar um relatório no **"Sankhya"** utilizando um arquivo **".jrxml"** cujo nome ultrapassa o limite de caracteres permitido pelo sistema.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34108756414487)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34323985730711)

  Localize o arquivo **".jrxml"** que está sendo utilizado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324005377943)

  Renomeie o arquivo para que o nome completo (incluindo **".jrxml"**) não ultrapasse o limite informado na mensagem de erro (o sistema exibe **XX > XX**, onde o segundo valor é o tamanho máximo permitido).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34323985733527)

  Salve o arquivo com o novo nome.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34323985735703)

  Faça o upload novamente na tela de **"Gerenciamento de Relatórios".**

 

### 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324005387799)

 ****Dicas:**

- 

Utilize nomes curtos, objetivos e sem espaços desnecessários.

- 

Caso queira manter uma identificação, use abreviações.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34108756418071)

 **CAUSA**

O campo **"NOME"** do arquivo de relatório possui um tamanho máximo definido internamente.
Quando o nome do arquivo (incluindo a extensão **".jrxml"**) excede esse limite, o sistema bloqueia a operação e exibe a mensagem de erro.

**Exemplo:**
Nome permitido: **relatorio_vendas_2025.jrxml** (29 caracteres)
Nome inválido: **relatorio_vendas_detalhado_por_regiao_setor_financeiro.jrxml** (63 caracteres)

**Causas do erro:**
Nome original do arquivo muito extenso.
Inclusão de informações desnecessárias no nome, como datas, descrições longas ou caracteres redundantes.