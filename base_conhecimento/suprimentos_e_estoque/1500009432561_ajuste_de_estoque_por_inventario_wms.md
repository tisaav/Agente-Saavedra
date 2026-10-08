# Ajuste de Estoque por Inventário - WMS

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Ajuste-de-Estoque-por-Invent%C3%A1rio-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Ajuste-de-Estoque-por-Invent%C3%A1rio-WMS)  
> **ID:** `1500009432561` | **Última Atualização:** 2026-07-29T14:12:49Z

---

Através da tela Ajuste de Estoque por Inventário, que pode ser acessada pelo menu **"WMS > Inventário"**, realizamos o ajuste de estoque, a [quarta etapa](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS#ajustedeestoqueporinvent%C3%A1rio) do processo de inventário no WMS.

```text
**

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311482887063)

[Como realizar o processo de inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS)
**
```

| Dica: Acesse a documentação "" para verificar as etapas que antecedem o processo de Ajuste de Estoque por Inventário. |
| --- |

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500014642242)

Inicialmente, no lado esquerdo da tela, você deve informar o número do **"Inventário"** que está sendo trabalhado e poderá configurar alguns filtros.

No filtro de **"Contagens Exibidas"**, determine por meio das marcações **"Contagens com divergência"**, **"Contagens sem divergência"** e **"Todas as contagens"**, quais contagens serão apresentadas. As que estiverem com divergência serão apresentadas na cor **vermelha** e as sem divergência na cor **verde**.

No alto dessa tela, temos alguns botões importantes para o processo de ajuste de estoque por inventário, abaixo trataremos sobre cada um deles:

O botão 

![Botão Histórico de Ajustes FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16951425709975)

 **"Histórico de contagens"** trará todas as contagens do endereço nesse inventário ou em todos os outros:

![ajuste1.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500014981441)

No botão 

![botão-recontar-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16951477584407)

 **"Recontar"** existem duas opções:

- 
**Recontar endereço:** Essa opção irá gerar uma nova tarefa de recontagem para o endereço selecionado.

- 
**Recontar OUTROS endereços:** Selecionando essa opção, será feita a geração de uma tarefa de contagem para todos os endereços configurados para o produto da linha que está selecionada na grade.

Além dos botões acima, temos também o botão 

![Botão Gerar ajustes FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16951405072663)

 **"Gerar ajuste"** para os inventários Rotativo e Global e, para o inventário de Implantação, esse botão será alterado para 

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500014981561)

 **"Implantar estoque"**.

**Observação:** no inventário de Implantação, clicando no botão, o sistema irá implantar o estoque direto na tabela de estoque do WMS (TGWEST) e na tabela de contagem do MGEInventário (TGFCTE), registrando o Número do Inventário. Acionando o botão, será aberto o pop-up **"Ajuste de Estoque"**, para você definir os endereços que serão desbloqueados e se o inventário será fechado. Definidos os ajustes, basta clicar no botão **"Gerar Ajuste"**. Observe abaixo como é feito esse processo:

![ajuste2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500014643222)

**Nota:** se o inventário for Rotativo ou Global, nosso sistema fará a atualização do estoque contado na tabela de estoque do WMS. Se a quantidade contada for maior que o estoque, será gerada a diferença para o endereço de sobra definido nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa); por outro lado, se for menor, será gerada a diferença para o endereço de perda, também configurado nas Preferências da Empresa e na tela de [Consulta Estoque com Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias), você realiza a geração das notas de ajuste.

Para o inventário Rotativo, ao acionar o botão 

![Botão Gerar ajustes FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16951405072663)

 **"Gerar ajuste"**, será apresentado o pop-up abaixo:

![ajuste3.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500014662082)

Na seção **"Desbloqueio de endereços"**, quando um endereço estiver bloqueado para o inventário, é possível desbloqueá-lo utilizando as seguintes opções:

- 
**Endereços deste ajuste e endereços sem divergência:** desbloqueia os endereços do ajuste atual e os endereços que não possuem divergência;

- 
**Apenas dos endereços deste ajuste:** desbloqueia os endereços do ajuste atual.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26129370228887)

 O desbloqueio é realizado por meio do endereço fornecido.

A seção **"Tipo de ajuste"** do pop-up **"Contagem de Estoque"** apresentado acima, é influenciada pelo parâmetro **"Tipo de ajuste de estoque por inventário - TIPOAJUSTEEST"** que pode ser configurado de três maneiras:

- 
**Vazio:** Serão apresentadas no pop-up as marcações **"Pela divergência do WMS"** e **"Pela diferença entre MGE e WMS"** na seção Tipo de ajuste;

- 
**Pela divergência do WMS:** Apenas essa marcação será exibida na seção Tipo de ajuste;

- 
**Pela diferença entre MGE e WMS:** Utilizando essa opção, apenas essa marcação será exibida na seção Tipo de ajuste.

**Observação:** na geração do ajuste, no momento da execução da rotina, se for identificado que existe um endereço de divergência com o produto do ajuste, a mensagem abaixo será apresentada:

***"Foi encontrado estoque no endereço especial de divergência para produto(s) do ajuste, deseja:***

***Remover (recomendável)***

***Não remover"***

```text
**

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311482887063)

**
```

| Dica: Para o caso acima, orientamos que seja feita a limpeza do endereço de divergência ao efetuar o ajuste. |
| --- |

Por fim, para o inventário Global, ao acionar o botão 

![Botão Gerar ajustes FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16951405072663)

 **"Gerar ajuste"**, será apresentado o pop-up abaixo:

![ajuste4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500014662342)

A única diferença entre o inventário Rotativo e o Global é que, nesse último, no pop-up Contagem de Estoque são apresentadas as marcações **"Apenas produto com no mínimo X contagens dentro do inventário"** e **"... e com as X últimas contagens iguais"**.

**Importante:** caso o parâmetro **"Permite contagem de estoque com pendências - PERMCONTESTPEND"** esteja habilitado, será possível realizar a contagem e ajuste de estoque de endereços que possuam tarefas de saída pendentes, na realização do processo de inventário Rotativo.

 

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16951279083927)

 Acesse também:

[Histórico de Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120373-Hist%C3%B3rico-de-Ajuste-de-Estoque)

[Como gerar as tarefas de contagem no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Como-gerar-as-tarefas-de-contagem-no-WMS)

[Como realizar o processo de inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS)


---

### 🔗 Links e Referências Internas:

- [quarta etapa](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS#ajustedeestoqueporinvent%C3%A1rio)
- [Como realizar o processo de inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Consulta Estoque com Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias)
- [Histórico de Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120373-Hist%C3%B3rico-de-Ajuste-de-Estoque)
- [Como gerar as tarefas de contagem no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Como-gerar-as-tarefas-de-contagem-no-WMS)