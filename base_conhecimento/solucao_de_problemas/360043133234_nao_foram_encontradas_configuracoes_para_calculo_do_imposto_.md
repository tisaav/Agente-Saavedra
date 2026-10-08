# Não foram encontradas configurações para cálculo do imposto 'COFINS'

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133234-N%C3%A3o-foram-encontradas-configura%C3%A7%C3%B5es-para-c%C3%A1lculo-do-imposto-COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133234-N%C3%A3o-foram-encontradas-configura%C3%A7%C3%B5es-para-c%C3%A1lculo-do-imposto-COFINS)  
> **ID:** `360043133234` | **Última Atualização:** 2026-07-22T16:04:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137672818199)

 MENSAGEM:**

Não foram encontradas configurações para cálculo do imposto 'COFINS'.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137665701527)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137665703319)

 Verifique nos cadastros abaixo se as marcações referente ao Cálculo de COFINS encontram-se adequadas ao seu lançamento:

- Tela **"[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)"** *(Comercial » Preferências) - *Aba **"Propriedades"**: '**Calcula COFINS?**'

- Tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** *(Comercial » Arquivo » Cadastros)*/ Aba **"Impostos":** '**Tem COFINS**'

- Tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** *(Configurações » Cadastros)*/ Aba **"Impostos"**: "**Grupo COFINS"**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137672825623)

 Na Tela **"Alíquotas de COFINS"** *(Comercial >> Arquivo >> Cadastros >> Alíquotas)* realize um filtro com as informações referente ao seu lançamento, considerando os campos abaixo:

- Deve existir uma configuração nessa tela com o mesmo GRUPO informado no cadastro do produto, com os campos TIPO (Entrada/Saída) e EMPRESA correspondentes.

- Se os campos PARCEIRO/TOP encontrarem-se como 0, significa que essa alíquota será utilizada para todos os parceiros/TOP'S referente aquele TIPO/GRUPO.

- Necessário compreender que tratando-se de nota fiscal eletrônica, mesmo que não exista incidência desse imposto, as configurações citadas acima deverão existir, mesmo que para uma alíquota = 0 (zero).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137665709335)

 Caso não exista o cadastro acima que atenda ao seu lançamento, realize esse com apoio do seu Contador. Existindo dúvidas pontuais acione o Service Desk Sankhya, ressaltando que a configuração não é realizada por essa equipe, se evidenciado essa necessidade um consultor de sua Franquia deverá ser acionado.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137665710871)

 CAUSA:**

Mensagem será apresentada quando não existir uma exceção de COFINS configurada para o respectivo lançamento.


---

### 🔗 Links e Referências Internas:

- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)