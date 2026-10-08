# Grupo de Produto 'X' não pode ser usado com a TOP 'Y'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616113-Grupo-de-Produto-X-n%C3%A3o-pode-ser-usado-com-a-TOP-Y](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616113-Grupo-de-Produto-X-n%C3%A3o-pode-ser-usado-com-a-TOP-Y)  
> **ID:** `360044616113` | **Última Atualização:** 2026-07-22T15:54:23Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617328078487)

 MENSAGEM:**

[CORE_E02936]  Grupo de Produto 'X' não pode ser usado com a TOP 'Y'.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617365001623)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617328085143)

 TOP com restrições/exceções:

Anote o **"****Tipo de Operação (TOP)"** que está sendo utilizado e siga com as orientações abaixo:

- Acesse a tela **"Tipos de Operação" ***(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) *e selecione a TOP em questão, por exemplo *'1407 - Compra - Matéria Prima'*;

- Clique no botão **'Outras Opções**' » '**Restrições/Exceções**'.

 

![Grupo de Produto 'X' não pode ser usado com a TOP 'Y' 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/32694558199063)

 

- Verifique se existem regras vinculadas para '**GRUPO PROD.**

 

![Grupo de Produto 'X' não pode ser usado com a TOP 'Y' 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/32694558205975)

- No exemplo acima, a TOP selecionada (1407 - Compra - Matéria Prima) não poderá ser usada com o grupo de produto '60000 - Produtos Intermediários'.

- Para utilização dessa TOP com esse grupo de produto, ele deveria ser **excluído de exceções**. 

- Caso a marcação fosse para '**Restrições**' (só pode ser usado com), o grupo de produto desejado deveria constar nessa lista.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617365005591)

 Central de Certificações:

Caso a empresa utilize o módulo de **"Central de Certificações"**, realize as análises abaixo:

- Acesse a tela "**Usuários**": (*Caminho de acesso: Configurações » Controle de Acesso*);

- Selecione o usuário logado no sistema, no momento que a validação ocorre;

- Busque a aba '**Validações**'.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14874447888279)

 

- Caso exista alguma regra vinculada, prossiga com as verificações a seguir. Caso não exista, possivelmente essa não é a causa do seu problema/incidente.

- Localizada a regra acima, acesse a tela **"Central de Certificações**" (*Caminho de acesso: **Comercial » Avançado » Certificações*), busque a regra vinculada e faça a análise de sua funcionalidade.

- Se essa regra estiver vinculada a restrições de TOP/Grupo de Produto, sintonize internamente para compreender a necessidade desse no processo da empresa e, assim alterar os dados do seu lançamento ou desativar a regra.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617328090135)

 CAUSA:**

Ocorre quando o lançamento está utilizando 'Grupo de Produto' que tenha restrições e/ou validações em relação a 'TOP' utilizada.