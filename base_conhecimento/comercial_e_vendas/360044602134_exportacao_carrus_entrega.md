# Exportação Carrus Entrega

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602134-Exporta%C3%A7%C3%A3o-Carrus-Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602134-Exporta%C3%A7%C3%A3o-Carrus-Entrega)  
> **ID:** `360044602134` | **Última Atualização:** 2026-07-29T14:24:07Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311857262999)

 Módulo: **Comercial > Conexão         
```

O Sankhya Om possui uma integração com o Sistema Carrus Entrega; essa integração é apenas de mão única, ou seja, o Sankhya Om apenas envia os dados ao Carrus Entrega e não importará nada deste último.

**Observação:** Os scripts de banco de dados correspondentes à esta integração são específicos, por isso devem ser solicitados diretamente ao suporte da Sankhya.

No Sankhya Om esta funcionalidade não depende do parâmetro **"Utiliza Integração com o módulo Carrus? - UTILINTCARRUS"**.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4417921036311)

Esta tela apresenta no Painel de Filtros, o campo **"Empresa"** que é de preenchimento obrigatório. Além disso, você poderá informar a **"Ordem de Carga"** para obter uma filtragem maior das informações a serem exibidas na grade. 

A opção **"Transmitir"** é utilizada para realizar a integração com Carrus Entrega e as Ordens de Carga. Para proceder com a transmissão, você deve selecionar no mínimo uma ordem de carga; caso esta medida não seja tomada, o sistema emitirá a seguinte mensagem: 

***"Nenhuma ordem de carga selecionada! Deseja enviar todas?"***

**Observação:** Ao acionar a opção Transmitir, serão preenchidos os campos obrigatórios das tabelas TBINTROMANEIO, TBINTPEDIDO, TBINTITEMPEDIDO, TBINTINTEGRACAO, e além disso, as triggers dessas tabelas irão popular a tabela do banco de integração CARRUSINT via DBLINK. Para que a integração funcione, é necessário criar um DBLINK com o nome INTEGRACAO_CARRUS, obrigatoriamente.

**Importante: **É obrigatório que os produtos possuam em seu Cadastro o **"****Código de barras"** informado na aba [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacdigodebarras), ou na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas). 

## Como implantar a Integração

Primeiramente, verifique qual o nome do serviço criado no servidor onde está instalado o módulo Carrus Entrega por meio do arquivo **"****tnsnames.ora"**, que geralmente fica instalado nesta pasta: 

```text
\oracle\product\10.2.0\client_1\NETWORK\ADMIN\tnsnames.ora
```

No exemplo abaixo, o nome é **"XE"**:

```text
XE =

 (DESCRIPTION = 

         (ADDRESS_LIST = 

                 (ADDRESS = (PROTOCOL = TCP)(**HOST = 192.168.0.4**)(PORT = 1521)) 

         ) 

         (CONNECT_DATA = 

                 (SERVICE_NAME = ORCL) 

         )

 ) 
```

No servidor onde está instalado o banco de dados do MGE, você deve adicionar dentro do arquivo tnsnames.ora a seguinte estrutura:

```text
CARRUS =

 (DESCRIPTION = 

         (ADDRESS_LIST = 

                 (ADDRESS = (PROTOCOL = TCP)(**HOST = 192.168.0.4**)(PORT = 1521)) 

         ) 

         (CONNECT_DATA = 

                 (SERVICE_NAME = XE) 

         ) 

 ) 
```

Observe que o **IP** em negrito,** **neste caso é o IP da máquina onde está instalado o banco de dados Carrus. 

Em seguida, através de uma ferramenta de conexão com o banco, por exemplo, o **TOAD**, realize a criação do **DBLINK **da seguinte maneira: 

```text
Create database link INTEGRACAO_CARRUS 

connect to CARRUSINT identified by SQL using 'NOME' 
```

Atente-se a opção Using, pois o nome varia de acordo com a instalação. Observe que o **Using = Carrus **foi o nome do serviço que foi criado no arquivo tnsnames.ora anteriormente; 

Depois de realizadas as configurações, bastará criar Pedidos/Notas, utilizar a [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238734-Forma%C3%A7%C3%A3o-de-Carga) para associar os Pedidos a uma Ordem de Carga, acessar a tela Exportação CarrusEntrega, selecionar as ordens de carga desejadas e transmiti-las. 

**Observação:** Utilize os comandos abaixo para selecionar registros na tabela do banco CarrusInt:

```text
SELECT * FROM TBINTROMANEIO@INTEGRACAO_CARRUS 

SELECT * FROM TBINTPEDIDO@INTEGRACAO_CARRUS 

SELECT * FROM TBINTITEMPEDIDO@INTEGRACAO_CARRUS 

SELECT * FROM TBINTINTEGRACAO@INTEGRACAO_CARRUS 
```


---

### 🔗 Links e Referências Internas:

- [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacdigodebarras)
- [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas)
- [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238734-Forma%C3%A7%C3%A3o-de-Carga)