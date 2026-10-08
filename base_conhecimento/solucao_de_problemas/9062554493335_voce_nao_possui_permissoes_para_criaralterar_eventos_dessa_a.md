# Você não possui permissões para criar/alterar eventos dessa agenda

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9062554493335-Voc%C3%AA-n%C3%A3o-possui-permiss%C3%B5es-para-criar-alterar-eventos-dessa-agenda](https://ajuda.sankhya.com.br/hc/pt-br/articles/9062554493335-Voc%C3%AA-n%C3%A3o-possui-permiss%C3%B5es-para-criar-alterar-eventos-dessa-agenda)  
> **ID:** `9062554493335` | **Última Atualização:** 2026-07-22T15:11:07Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791234588311)

 MENSAGEM:**

 [CORE_E05425]: Você não possui permissões para criar/alterar eventos dessa agenda.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791234592023)

 SITUAÇÃO:**

Ao tentar alterar o executante que foi informado em uma OS ou tentar lançar um evento dentro da Tela de agenda de recursos a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791256642839)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791256645271)

 Acesse: *Módulos » Contratos e Serviços » Ordem de Serviço e marque a opção "Permite criar evento R & S".*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791234608791)

 Somente poderá incluir/alterar/excluir os eventos de executantes subordinados ou o próprio usuário logado na sua agenda propriamente dita. Caso o usuário logado tente incluir/alterar/excluir eventos para um executante que não seja um subordinado sistema emitirá a mensagem: *"você não possui permissões para criar/alterar eventos dessa agenda."*

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791234610839)

 Para que haja essa hierarquia de gerência, acesse a tela 'Relacionamento entre usuários' *(acesse à tela: Configurações » Controle de Acesso » Relacionamento entre Usuários)*, filtre o usuário (Gerente) e acrescente na aba 'Subordinados', o(s) usuário(s) subordinado(s).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791256660887)

 A tela 'Relacionamento entre usuário' também é utilizada para cadastrar os usuários em suas respectivas Filas, além de possibilitar a definição de Gerentes e Subordinados. Esses cadastros são realizados a partir de três abas presentes na tela, que são: membros da fila, gerentes e subordinados. Para saber mais sobre as abas, leia o artigo ['Relacionamento entre Usuários'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598154).

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791234628247)

 Ainda sobre essa tela, inicialmente ela possui dois campos de filtro, que são por "Nome" e/ou "Grupo" (de usuários), estes podem ser utilizados para localização de um ou vários usuários pertencentes a um mesmo grupo. E na parte superior da tela, tem-se a possibilidade de criação de um filtro através do "Assistente de Filtro", onde pode-se buscar os dados da melhor forma desejada. Depois de criado o filtro, clica-se em "Aplicar" para que a filtragem seja feita, ou seja, para X conseguir alterar a Agenda de Y, para isso ele tem que ser subordinado de X.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18791256669975)

CAUSA: **

Tentar criar/alterar eventos de agenda de usuários que não são seus subordinados.


---

### 🔗 Links e Referências Internas:

- ['Relacionamento entre Usuários'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598154)