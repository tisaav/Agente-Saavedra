# Erro no cálculo de dissídio (RRA) - Evento DSR ausente

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39364807896471-Erro-no-c%C3%A1lculo-de-diss%C3%ADdio-RRA-Evento-DSR-ausente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39364807896471-Erro-no-c%C3%A1lculo-de-diss%C3%ADdio-RRA-Evento-DSR-ausente)  
> **ID:** `39364807896471` | **Última Atualização:** 2026-07-29T13:23:08Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39364799218839)

 **MENSAGEM**

O evento de DSR (Descanso Semanal Remunerado) não está sendo considerado no cálculo de dissídio (RRA), gerando diferenças nos valores  de RRA, mesmo que o DSR exista na folha de pagamento do mês de referência.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39364807893527)

 **SITUAÇÃO**

Ao calcular a folha de dissídio com eventos de RRA configurados, o sistema não demonstra os valores de DSR correspondentes aos eventos de hora extra, mesmo com os eventos de RRA criados e vinculados corretamente. O DSR aparece calculado na folha mensal normal, mas não é considerado no cálculo do dissídio.

 

 

Os **eventos de RRA (Rendimentos Recebidos Acumuladamente)** são eventos especiais utilizados para registrar valores pagos ao trabalhador que se referem a **anos anteriores ao ano do pagamento**. Esses valores têm um **tratamento tributário diferenciado**, sendo calculados separadamente da folha mensal para evitar tributação indevida.

## Quando Utilizar Eventos de RRA

Os eventos de RRA são aplicados em situações como:

- 
**Dissídio coletivo** com efeito retroativo em meses anteriores

- 
**Diferenças salariais** de períodos passados

- **Verbas reconhecidas judicialmente**

- 
**Ajustes de remuneração** pagos fora da competência original

- 
**Pagamentos retroativos** cujo pagamento ocorre em um ano calendário posterior ao da competência original

 

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39364799219095)

 **SOLUÇÃO**

Para corrigir o problema, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39364807894039)

 Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento de hora extra que está sendo utilizado no cálculo da folha do funcionário.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39364807894167)

 Verifique se existe um evento personalizado ativo que possui a mesma característica do evento padrão de hora extra.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39364799219735)

 Caso exista um evento personalizado ativo, desative-o temporariamente.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39364799219991)

 Reative o evento padrão de hora extra que estava desativado.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39364799220119)

 Acesse a tela **"Cálculo de Folha"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e recalcule a folha do funcionário.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39364807894935)

 Verifique se os valores de **"DSR"** passaram a ser demonstrados corretamente no cálculo do dissídio.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39364807895319)

 Confira se o evento de RRA correspondente ao **"DSR"** está criado e vinculado ao evento de DSR na aba **"Avançado"** do cadastro de eventos, no campo **"Evento de Diferença - RRA"**.
 

Artigo :

[https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA)

 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39364799221143)

 **CAUSA**

O problema ocorre porque o cálculo de DSR reconhece a característica do evento, e não apenas o evento efetivamente utilizado na folha. Quando um evento padrão de hora extra está desativado e sua característica foi vinculada a um evento personalizado, o sistema continua considerando o evento original (não utilizado no cálculo atual do funcionário) para o cálculo do DSR, o que impacta incorretamente os valores no dissídio.

Além disso, se o evento de DSR estiver desativado ou se não houver um **"Evento de Diferença - RRA"** vinculado ao evento de DSR, o sistema não conseguirá calcular corretamente as diferenças no dissídio.


---

### 🔗 Links e Referências Internas:

- [https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA)