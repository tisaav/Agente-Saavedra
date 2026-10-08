# ORA-31603: objeto 'X' do tipo procedure não encontrado no esquema 'Y'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33884091184279-ORA-31603-objeto-X-do-tipo-procedure-n%C3%A3o-encontrado-no-esquema-Y](https://ajuda.sankhya.com.br/hc/pt-br/articles/33884091184279-ORA-31603-objeto-X-do-tipo-procedure-n%C3%A3o-encontrado-no-esquema-Y)  
> **ID:** `33884091184279` | **Última Atualização:** 2026-07-22T14:28:05Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884067768727)

 MENSAGEM:**

ORA-31603: objeto 'X' do tipo procedure não encontrado no esquema 'Y'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884091172631)

 SITUAÇÃO:**

Ao exportar um processo de negócio na rotina Flow, a mensagem de erro é apresentada.  

 

**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/34049563561495)

 Atenção:** Para avançar com a correção, é necessário conhecimento técnico em **banco de dados**, pois a investigação e a resolução envolvem consultas SQL e a identificação de elementos estruturais do sistema.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884091173527)

SOLUÇÃO:**

Ao exportar um processo no Flow, o sistema automaticamente inicia a exportação dos metadados das instâncias envolvidas, incluindo botões de ação, eventos personalizados, triggers e outros elementos vinculados ao processo.

Assim, se algum botão de ação estiver associado a um objeto (como uma procedure) que não existe mais no banco de dados, um erro será gerado.

Para identificar onde esse objeto está sendo referenciado, execute a consulta SQL abaixo, substituindo **''NO_DO_OBJETO''** pelo nome exato do objeto mencionado na mensagem de erro:

```text
SELECT * FROM TSIBTA WHERE CONFIG LIKE '%NO_DO_OBJETO%'
```

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884067771799)

 **A consulta retornará os registros onde o objeto está sendo citado. Assim, será possível identificar **qual instância o botão de ação** está com essa referência obsoleta;
 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884091175831)

 **Após localizar o componente, acesse a tela correspondente no sistema a instância, podendo ser o ''**Dicionário de Dados'', ''Construtor de Telas'' **ou ''**Formulários Formatados''; **
 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884091176599)

 **Localize a tabela identificada, vá até a **aba Ações**, e verifique qual botão de ação está referenciando o objeto ausente citado na mensagem de erro;
 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884091181847)

 **Após isso, será necessário realizar uma análise:

- 

Se o objeto (procedure) foi excluído propositalmente, é recomendável remover o botão de ação; 

- 

Se o objeto foi removido por engano, é possível recriá-lo no banco (desde que a lógica da procedure esteja disponível e seja válida). 
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33884067788183)

 CAUSA:**

O erro ocorre porque botões de ação no Flow ainda referenciam objetos removidos do banco de dados.

Durante a exportação, o sistema busca todos os componentes associados, incluindo procedures citadas nos botões. Se o objeto não for encontrado, é gerado o erro **ORA-31603**.

Esse problema geralmente surge após manutenções no banco, como exclusão de procedures obsoletas, sem atualização das configurações, comprometendo a consistência da exportação.