# Execução de Tarefas Impressas WMS

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107513-Execu%C3%A7%C3%A3o-de-Tarefas-Impressas-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107513-Execu%C3%A7%C3%A3o-de-Tarefas-Impressas-WMS)  
> **ID:** `360045107513` | **Última Atualização:** 2026-07-29T14:15:16Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311578944279)

 Módulo: **WMS > Rotinas
```

Esta tela possibilitará a impressão de mapas para execução de tarefas de forma manual, sem o uso de coletores.

Você poderá realizar através desta rotina a execução das seguintes tarefas:

- Armazenamento;

- Expedição;

- Expedição Balcão;

- Transferência;

- Reabastecimento;

- Retorno da expedição, ou;

- Todas conjuntamente.

**Nota:** o processo de conferência será realizado no formato padrão, através de emuladores.

Trataremos abaixo sobre os seguintes tópicos:

[Botões da tela](#bot%C3%B5esdatela)                                                    [Parâmetros que influenciam nesta rotina](#par%C3%A2metrosqueinfluenciamnestarotina)

## 
Botões da tela

A tela de Execução de Tarefas Impressas WMS é composta por botões que executam diversas funções dentro desta rotina, são eles:

![botao-anterior-e-proxima-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16845129040279)

 - **Anterior e Próximo:** Temos aqui, os botões de navegação entre as tarefas já executadas.

![botão Atualizar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16845129045271)

 - **Atualizar:** Ao acionar este botão, será recarregado toda a tela de Execução de Tarefas Impressas WMS.

![Botão Imprime os cheques marcados FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16845129052183)

 - **Gerar Mapa: **Através deste botão, será registrado o **"Nro. Mapa"** para o item da tarefa, bem como será gerado o modelo de mapa da tarefa.

**Observação:** caso a tarefa em questão possua dependência em outra tarefa, não será gerado o mapa; desta forma, você deve primeiramente resolver a dependência para, posteriormente, realizar a geração do mesmo.

![Botão Cancelar Mapa FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16845177069719)

 - **Cancelar Mapa:** Em relação a este botão, quando for acionado, ele cancelará o registro que foi gerado o mapa, porém, que ainda não foi iniciado/finalizado o mapa para a tarefa.

![Botão Início Mapa FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16845173642903)

 - **Início Mapa:** Ao clicar neste botão, será registrado o início do mapa da tarefa.

**Nota:** selecionando o botão acima, será exibido um pop-up solicitando o Nro. Mapa e o **"Executante"**.

![Botão Cancela Execução do Mapa FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16919945978519)

 - **Cancela Execução do Mapa:** este botão retornara o mapa para **"Aberto"** quando o mesmo estiver com a situação **"Em Execução"**.

![Botão Finaliza Mapa FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16919980089623)

 - Será realizado o registro da finalização da execução do mapa da tarefa ao acionar o botão **"Finaliza Mapa"**.

**Observação:** ao acionar o botão acima mencionado, será aberto um pop-up para se informar o Executante, bem como o **"Endereço de Checkout"**, sendo que este último tem seu preenchimento obrigatório apenas quando a tarefa for de **"Expedição"**.

![Botão Modelos de Impressões FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16920044150935)

 - Temos ainda o botão **"Modelos de Impressões"**, onde você poderá encontrar os modelos de relatórios de impressão (**.jrxml*) das tarefas para serem baixadas.

**Importante:** para todos os Tipos de Tarefas, os procedimentos de Gerar, Cancelar, Iniciar e Finalizar o mapa serão os mesmos.

**Observação:** ainda será possível selecionar as tarefas e realizar a geração de mapas em grupo para cada tarefa, sendo que estas terão o mesmo Nro. Mapa.

[[voltar ao topo]](#top)

## 
Parâmetros que influenciam nesta rotina 

**Exige início mapa WMS? - EXIGEINIMAPA: **este parâmetro está vinculado ao botão Início Mapa. Desta forma, quando o parâmetro estiver desabilitado, tem-se que o botão informado não será exibido na tela Execução de Tarefas Impressas WMS.

Para que seja possível realizar a geração/impressão dos mapas de Armazenamento, Transferência, Reabastecimento e Expedição, é necessário que os parâmetros abaixo estejam devidamente configurados de acordo com os [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados):

- **Relatório p/ mapa de recebimento manual - RELMAPRECMAN;**

- **Relatório p/ mapa de transferência manual - RELMAPTRAMAN;**

- **Relatório p/ mapa de reabastecimento manual - RELMAPREAMAN;**

- 
**Relatório p/ mapa de separação manual - RELMAPSEPMAN****.**

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados)