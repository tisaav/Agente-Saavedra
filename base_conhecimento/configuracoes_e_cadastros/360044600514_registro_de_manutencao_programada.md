# Registro de Manutenção Programada

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600514-Registro-de-Manuten%C3%A7%C3%A3o-Programada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600514-Registro-de-Manuten%C3%A7%C3%A3o-Programada)  
> **ID:** `360044600514` | **Última Atualização:** 2026-07-29T13:50:10Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310763348247)

 **Módulo:** Configurações > Avançado
```

Nessa tela, será possível configurar a Data/Hora da parada do servidor para a manutenção do sistema.

![tela-registro-de-manuten__o-programada.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/13310079066647)

Apenas uma manutenção poderá ser cadastrada por vez e esta permanecerá ativa até seu cancelamento pela tela de registro por meio do botão 

![cancelar FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16705594978967)

 **"Cancelar"**, ou até a reinicialização do servidor; e será possível ainda, realizar alterações em uma manutenção que já foi registrada.

A data/hora da manutenção precisará possuir o tempo mínimo de 10 minutos a mais em relação à hora atual. Caso este período não seja respeitado, o sistema exibirá a mensagem:

***"'Data/Hora da Manutenção' deve possuir ao menos 10 minutos em relação a hora atual"***

A inclusão e alteração das manutenções poderão levar até oito minutos para serem realizadas no sistema, portanto a aparição/remoção do ícone e disparo dos avisos serão exibidos o sistema da seguinte forma: 

Enquanto houver um registro de manutenção ativo, o ícone 

![icone-manutencao-programada.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/13309677679127)

 **"Chave de Manutenção"** será exibido na barra de tarefas, sendo que este estará localizado entre o ícone 

![icone-central-de-ajuda.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/13309984237591)

 **"Central de Ajuda"** do sistema e a pesquisa de telas.

![gif-manutencao-programada.gif](https://ajuda.sankhya.com.br/hc/article_attachments/13309978803351)

![](https://sankhyasd.zendesk.com/hc/article_attachments/360055955214/embim298.gif)

Quando o horário da manutenção estiver próximo, pode-se observar a mensagem com a informação da manutenção e ao clicar em **"Ver Detalhes"** terá os detalhes da manutenção como registrada nessa tela:

![tela-manutencao-programada.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/13310080052375)

![](https://sankhyasd.zendesk.com/hc/article_attachments/360056827793/embim300.gif)

Momentos antes do horário programado para o horário programado, o sistema emitirá um novo alerta informando ao usuário que a manutenção programada poderá ocorrer a qualquer instante.

O disparo das mensagens de aviso da manutenção surgirão no sistema com a característica que, quanto mais próximo do horário da manutenção

![](https://sankhyasd.zendesk.com/hc/article_attachments/360055955254/embim301.gif)

, menor o intervalo das mensagens, de forma que:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458065008535)

 O sistema buscará o tempo restante até a parada;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458065008535)

 Esse número será dividido por 10 e logo em seguida será arredondado. Assim, sempre serão utilizados, como base, os números naturais. Dessa forma, observe o exemplo abaixo:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310763349399)

****

|  |  | O valor encontrado no item "b" será somado com 2. Exemplo: |
| --- | --- | --- |

               Para 57min restantes / 10 = 5,7, que arredondando será = 6. Esse valor somado a 2 = 8.

**1ª Situação****:** Resultado da função anterior menor que 5.

|  | Para resultados menores que 5 minutos o aviso será apresentado a cada 1 minuto (fixo, não utilizará a fórmula descrita anteriormente). |
| --- | --- |

Assim, considere:

**2ª Situação****:** Resultado da função maior que 5. Observe a seguir, um exemplo prático:

Para 47 min restantes / 10 = 4,7, que arredondado será = 5. Esse valor somado a 2 = 7. Isso significa, que o aviso será exibido inicialmente a cada 7 minutos e o intervalo diminuirá gradativamente, conforme a fórmula descrita anteriormente, até os 5 últimos minutos, que depois se tornarão fixos a cada 1 minuto.

**Observação:** esses intervalos podem sofrer variações de até 8 minutos para o primeiro aviso, devido à lentidão decorrente das consultas realizadas para avaliar o tempo restante, alterações no registro, entre outros.

Assim que a hora atual estiver a 5 minutos da hora da manutenção, com exceção do SUP, não será possível realizar login. 

Ao tentar logar no sistema com um usuário que não seja um SUP, o mesmo não poderá entrar e o alerta abaixo será apresentado:

***"Se o usuário for o SUP, o acesso ao sistema ocorrerá normalmente."***

Caso a hora atual ultrapasse a hora da manutenção, esta não será cancelada e os avisos continuarão a ser apresentados. O processo continuará até a reinicialização do servidor ou o cancelamento da manutenção.

Além disso, caso a manutenção estiver programada para um período que ainda esteja consideravelmente distante, como, por exemplo, dois dias após a data atual do sistema, este mostrará os avisos 60 minutos antes a hora da parada. Portanto, salve o seu trabalho e realize o logout do sistema para a manutenção ser realizada.

[[Voltar ao topo]](#top)