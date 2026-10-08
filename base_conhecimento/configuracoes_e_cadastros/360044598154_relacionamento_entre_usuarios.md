# Relacionamento entre Usuários

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598154-Relacionamento-entre-Usu%C3%A1rios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598154-Relacionamento-entre-Usu%C3%A1rios)  
> **ID:** `360044598154` | **Última Atualização:** 2026-08-25T23:43:21Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310664234903)

 **Módulo:** Configurações > Controle de Acesso
```

Essa tela é utilizada para cadastrar os usuários em suas respectivas Filas; além de possibilitar a definição de Gerentes e Subordinados. Esses cadastros são realizados a partir de três abas presentes na tela, por meio dos links a seguir, você pode conferir sobre cada uma delas:

[Filtros](#filtros)[Aba Membros da Fila](#abamembrosdafila)

[Aba Gerentes](#abagerentes)[Aba Subordinados](#abasubordinados)

[Botão Outras Opções...](#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

![membros_da_fila.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/1500011746761)

## 
Filtros

Você utilizará os campos **"Nome"** e **"Grupo"** para localizar um, ou vários usuários que pertencem ao mesmo grupo.

Também é possível criar um filtro através do **"Assistente de Filtro"**, onde pode-se buscar os dados da melhor forma desejada. Após sua criação, clique em **"Aplicar"** para que a filtragem seja feita.

No campo **"Usuário"** do Painel Principal, informe o usuário que terão seus relacionamentos importados. 

[[voltar ao topo]](#top)

## 
Aba Membros da Fila

As filas são usuários que não serão utilizados por nenhum funcionário específico da empresa. E elas existem para que o processo de Ordens de Serviço funcione de maneira mais organizada. 

Em um setor onde tem várias pessoas, é criado uma fila com o nome do setor e os usuários são vinculados a essa fila; dessa forma, ao ser aberta, a OS irá diretamente para a Fila e o primeiro membro da fila que puder executar a Ordem de Serviço, pode retirar a OS da fila e transferir para seu executante. Além disso, o executante de fila é utilizado no cadastro da equipe da [FAP - Ficha de Acompanhamento de Projeto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604394), pois ao adicionar uma fila como membro da equipe, automaticamente todos os seus membros estarão disponíveis no momento da abertura de algum item de OS da FAP.

[[voltar ao topo]](#top)

## 
Aba Gerentes

Gerentes são os usuários que estão acima do usuário que foi selecionado, eles terão, por exemplo, permissão para reabrir Ordens de Serviço já fechadas, ou até mesmo alterar os itens dos subordinados. Os gerentes também serão considerados na [Agenda de Recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604574). 

![gerentes.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/1500011746801)

Assim, nessa aba temos a marcação **"Líder imediato"**, em que, ao marcá-la, o sistema permitirá que cada usuário possua somente um líder imediato. Essa marcação também permitirá que os executantes visualizem a agenda de seus pares. Para um melhor entendimento, observe o esquema abaixo:

![hierarquia.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/19383556741143)

[[voltar ao topo]](#top)

## 
Aba Subordinados

Por meio dessa você irá cadastrar os colaboradores subordinados, por exemplo:

Se a usuária Adriana estiver selecionado e o usuário Andrey for cadastrado nessa aba, o Andrey será subordinado à Adriana. Esse registro é equivalente a selecionar o usuário Andrey e, cadastrar a usuária Adriana na aba Gerentes.

![subordinados.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/1500011479642)

[[voltar ao topo]](#top)

## 
Botão Outras Opções...

No botão Outras Opções..., temos a opção **"Importar Relacionamentos" **que, ao selecioná-la, possibilita a realização da importação dos relacionamentos de um usuário para outro. Ao ser acionada, o sistema abrirá um pop-up com o mesmo nome da opção:

![importa_relacionamento.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/1500011480882)

Quando você selecionar a marcação **"Manter relacionamento atual"**, os relacionamentos que o usuário possui serão mantidos. Caso a importação seja feita com esse campo desmarcado, será apresentada a seguinte mensagem na confirmação do procedimento:

***"Os relacionamentos atuais serão removidos antes de fazer a importação. Deseja continuar?"***

Ao clicar em **"Sim"** o procedimento será finalizado.

Além disso, na importação de relacionamentos o sistema terá o comportamento abaixo:

O usuário recebedor do relacionamento irá herdar para si o gerente do usuário e seus subordinados, que foram importados.

Ou seja, ao selecionar um determinado **"Usuário A"** sem relacionamento e importar para ele os relacionamentos do **"Usuário B"**, uma vez que este possui relacionamento com o **"Usuário Gerente"** e seus subordinados **"Usuário Subordinado 1"** e **"Usuário Subordinado 2"**, o Usuário A também se tornará o gerente do Usuário Subordinado 1 e Usuário Subordinado 2, e além de se tornar o subordinado do Usuário Gerente.

O Usuário Gerente, por sua vez, será o gerente do Usuário A e Usuário B.

Dado o exposto, considere a representação abaixo:

![organograma.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/19383528286999)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [FAP - Ficha de Acompanhamento de Projeto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604394)
- [Agenda de Recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604574)