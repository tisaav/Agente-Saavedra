# Lentidão na consulta de produtos no SQL Server, veja como proceder

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4404335440663-Lentid%C3%A3o-na-consulta-de-produtos-no-SQL-Server-veja-como-proceder](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404335440663-Lentid%C3%A3o-na-consulta-de-produtos-no-SQL-Server-veja-como-proceder)  
> **ID:** `4404335440663` | **Última Atualização:** 2026-07-22T15:23:21Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347294030871)

 SITUAÇÃO: **

O incidente ocorre na tela de consulta de produtos, na qual pode ocorrer a demora para realizar a consulta de cada item. Quando é feita a consulta de produto e é marcado na consulta algum campo tipo varchar ou text, gera uma sintaxe SQL em que ele faz o **REPLACE** (substituição dos caracteres) e o **UPPER** (conversão para maiúsculo) apresenta o incidente descrito abaixo.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4404335371031)

 

Quando é realizado uma consulta sem o **REPLACE** e o **UPPER**, não passa pelo filtro e esse tempo gasto para consulta é bastante diminuído.

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4404335395607)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347310381975)

 SOLUÇÃO: **

O incidente está ocorrendo na query principal de consulta de Produtos. Nosso padrão de Collation no SQL Server é CI (Case Insensitive, tanto faz maiúscula e minúscula) e AI (Accent Insensitie, tanto faz com ou sem acentuação). A partir da versão 4.7, na subida do Wildfly, se colocarmos a diretiva: -Dskw.consulta.produtos.sql_ci_ai=true, quando a consulta principal de produtos for enviada para o SQL Server, ela já vai sem as tratativas de **UPERCASE** e **REPLACE**.

Para a corrigir tal lentidão, siga os passos abaixo: 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347310383255)

 Clone o DB de Produção para o ambiente de Testes/Treinamento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347310384791)

 Aplique a versão 4.7 ou 4.8 nesse ambiente.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347310386967)

 Coloque a diretiva acima na subida do Wildfly.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347294047895)

 Teste a tela de produtos.

 

Para mais informações referentes a problemas de performance do sistema, acessar o artigo: [Como analisar os problemas de performance (Lentidão) que ocorrem no sistema ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051439534-Como-analisar-os-problemas-de-performance-Lentid%C3%A3o-que-ocorrem-no-sistema-)


---

### 🔗 Links e Referências Internas:

- [Como analisar os problemas de performance (Lentidão) que ocorrem no sistema ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051439534-Como-analisar-os-problemas-de-performance-Lentid%C3%A3o-que-ocorrem-no-sistema-)