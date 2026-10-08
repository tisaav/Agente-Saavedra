# Como calcular a folha avulsa?

> **Módulo:** Pessoas+ | **Subseção:** Cálculo da Folha  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa)  
> **ID:** `32874835910295` | **Última Atualização:** 2026-09-27T17:43:08Z

---

** Módulo:** Pessoal+                       **                   **

** Versão mínima: **5.36

** Caminhos de acesso: **

1. Painel de configurações (Pessoal+ > Configurações > Painel de Configurações)

1. Eventos (Pessoal+ > Cadastros > Eventos)

1. Lançamento de movimento (Pessoal+ > Rotinas Folha > Lançamento de Movimento)

1. Cálculos (Pessoal+ > Rotinas Folha > Cálculos)

## **Sumário**

[Descrição e Usabilidade](#h_01JYRSHEA47DN2ARPJMPBAAK5J)

1. [Descrição](#h_01HA7B8E3FQG6AQ73CZ3Z4J3C5)

1. [Pré-requisitos](#h_01JY6MMN9K2XQ17EEG4TAA3E1J)

1. [Diagrama de fluxo](#h_01JY6G2G35EK6T62B0DYM3RCCZ)

1. [Jornada de uso](#h_01JXZD26W5467K5JX25EQ46AT1)

1. [Ponto de atenção](#h_01JY6G3YYX358XHFEX7M9RDGT0)

1. [Dicas de usabilidade](#h_01JXZD26WHDATS0Q60K45PGVJJ)

1. [Casos de uso](#h_01JXZD26WN07MF3X3R7TB6Q3A4)

[Perguntas frequentes (FAQ)](#h_01JXZD26WS16MD2RV6DQZ3KG9X)

[Artigos relacionados](#h_01JY6MFXR43YR051W1QRBKC7VM)

## **Descrição e Usabilidade**

 

### **1. Descrição**

 A **Folha Avulsa** permite lançar e calcular pagamentos específicos para um colaborador em uma competência (mês), **sem impactar a folha mensal padrão**. 

Ela é útil para pagamentos de valores pontuais, como **horas extras, comissões** ou outros pagamentos que precisam ser processados **fora do ciclo mensal regular**. 

Essa funcionalidade facilita o controle financeiro e evita erros de duplicidade, pois os valores lançados na folha avulsa são **automaticamente considerados** na folha mensal do colaborador.

 

### **2. Pré-requisitos**

 

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315193782679)

 Regras da folha avulsa**

Antes de iniciar o cálculo, é fundamental entender as regras de funcionamento da **folha avulsa**:

- 

**Uma única folha avulsa por colaborador por competência**: não é permitido lançar mais de uma folha avulsa para o mesmo colaborador no mesmo mês.

- 

**Incompatível com folha mensal ou rescisão já calculadas**: se já houver cálculo mensal ou rescisório na mesma competência, não será possível gerar a folha avulsa.

- 

**Sem envio ao eSocial nesta versão**: a folha avulsa ainda **não possui tributação própria** e, por isso, **não é enviada ao eSocial**.

- 

**Valores recalculados na folha mensal**: os eventos lançados na folha avulsa serão **recalculados na folha mensal**, e o valor já pago será **descontado automaticamente** para evitar duplicidade.
 

#### 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315193782679)

**** Permissões necessárias**

1. Acesse o **Painel de Configurações **(Pessoal+ > Configurações > Painel de Configurações).

1. Vá até a seção **Configuração de Permissões**.

1. 
Selecione a tela **Cálculos**, em seguida, o grupo de usuários desejado e certifique-se de que a permissão **Realizar cálculos avulsos** esteja habilitada para permitir o uso da funcionalidade da folha avulsa.
 

![permissao-calculos-avulsos.gif](https://ajuda.sankhya.com.br/hc/article_attachments/32938547188631)

####  

#### 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315193782679)

 ****Configurações prévias**
** **

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32875230622103)

 Eventos**

Certifique na tela** Eventos** (Pessoal+ > Cadastros > Eventos) que os eventos que você precisa estão configurados para a folha avulsa.

Os tipos de eventos permitidos, ou seja,** **eventos com **gatilho por lançamento de movimento**, são:

- **horas extras;**

- **comissões;**

- **DSR sobre comissões ou horas extras. **

Caso precise criar um novo evento:

- é possível **copiar eventos existentes** e **duplicar** para uso em folha avulsa;

- o evento deve ser acionado apenas por **lançamento de movimento**;

- **não marque** o evento como parte de regras automáticas de cálculo para outros tipos de pagamento (mensal, férias);

![regras-eventos-calculos.png](https://ajuda.sankhya.com.br/hc/article_attachments/32938744585495)

- verifique se o evento **possui reflexos**, como DSR, e se estes também estão corretamente configurados.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32875235633815)

 Lançamento de movimento**

1. Acesse a rotina de **Lançamento de movimento **(Pessoal+ > Rotinas Folha > Lançamento de Movimento) e crie um lançamento do tipo de folha **Avulsa**.

1. Selecione o funcionário, e na aba Lançamento, escolha o tipo de folha como **Avulso**.

1. Escolha o **evento desejado**.

1. Informe o **valor** ou **índice** conforme o caso.

1. 

Salve o lançamento e confira pela aba Visualização.

![lancamento-avulso.png](https://ajuda.sankhya.com.br/hc/article_attachments/32939312524823)

📚 Para mais detalhes, consulte o artigo: [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32938084629271)

  **Relatório de Holerite da Folha Avulsa**

Caso deseje utilizar um layout específico para o holerite da Folha Avulsa, configure o parâmetro **Holerite Folha Avulsa - FPRECIBOFOLAVU **com o código de um relatório cadastrado na tela **Relatórios Formatados**.

- Quando o parâmetro estiver preenchido, o sistema utilizará o relatório informado para emitir os holerites da Folha Avulsa.

- Quando o parâmetro não estiver preenchido, será utilizado automaticamente o mesmo modelo de holerite configurado para a folha mensal.

 

### **3. Diagrama de fluxo**

![folha-avulsa-fluxo.png](https://ajuda.sankhya.com.br/hc/article_attachments/32895527154199)

### 
**4. Jornada de uso **
 

#### **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32875230622103)

 Calcular Folha avulsa**

1. Após o lançamento dos eventos, acesse a tela de **cálculo** (Pessoal+ > Rotinas Folha > Cálculos).

1. 
Clique no card **Avulsa**.
 

![tipo-de-folha-avulsa.png](https://ajuda.sankhya.com.br/hc/article_attachments/32938929060503)

1. Informe a **referência** e **data de pagamento**.

1. Selecione o(s) funcionário(s) desejado(s).

1. Execute o cálculo (**individual ou coletivo**) e confirme a folha.

![calculo-avulso.png](https://ajuda.sankhya.com.br/hc/article_attachments/32939329114903)

**Observações**

- A folha avulsa **não terá tributação automática**.

- É possível **personalizar fórmulas de provisão**, caso deseje calcular descontos legais como INSS ou IRRF.

#### **

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32875235633815)

 Calcular folha mensal**

Depois, calcule normalmente a folha mensal do colaborador, assim:

- os eventos pagos na folha avulsa serão recalculados para gerar as bases de INSS, FGTS e IRRF;

- o valor líquido já pago na folha avulsa será descontado automaticamente do total da folha mensal.

#### 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32938084629271)

  **Emitir Holerite da Folha Avulsa**

Depois de confirmar o cálculo da Folha Avulsa, é possível emitir o recibo individual ou coletivo.

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41838653493143)

Emissão individual**

Na tela **Cálculos** (Pessoal+ > Rotinas Folha), selecione o colaborador calculado e utilize a opção **Emitir Holerite**.

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41838653493143)

**Emissão coletiva**

Na tela **Gerenciador de Folhas**, marque a opção **Ativa Seleção**, selecione os colaboradores desejados e utilize a opção **Emitir Holerite**.

O sistema:

- gera os recibos em PDF ou envia os holerites por e-mail, seguindo o fluxo padrão do sistema;

- 

gera o recibo utilizando:

  - o relatório configurado no parâmetro **FPRECIBOFOLAVU**, quando informado;

  - ou o modelo padrão utilizado para a folha mensal, caso o parâmetro não esteja configurado.
 

### **5. Pontos de atenção**

- Só é possível gerar **uma folha avulsa por colaborador dentro da mesma competência**.

- A folha avulsa só poderá ser calculada se não houver cálculo mensal ou de rescisão realizado para a referência.

- A folha avulsa **não gera tributação, nem é enviada ao eSocial** nesta versão.

- Os eventos pagos na folha avulsa serão recalculados na folha mensal para tributação e o valor será descontado.

- Após cálculo e integração financeiro e contábil, não será possível editar os cálculos da folha avulsa.

- O parâmetro **FPRECIBOFOLAVU** permite definir um modelo exclusivo de holerite para a Folha Avulsa:

  - quando não estiver configurado, será utilizado automaticamente o mesmo relatório da folha mensal;

  - o relatório informado deve estar previamente cadastrado na tela **Relatórios Formatados**.
 

### **6. Dicas de usabilidade**

- Use filtros para selecionar apenas os funcionários necessários ao calcular a folha avulsa.

- Sempre confirme a referência (competência) antes de lançar e calcular para evitar erros.

- 
Utilize o símbolo identificador na folha mensal para conferir eventos pagos via folha avulsa.
 

### **7. Casos de uso**

- Pagamento de horas extras fora do fechamento mensal.

- Pagamento de comissões pontuais.

- Ajustes isolados em valores específicos para um colaborador.

- 
Regularização de pagamentos que não puderam ser incluídos na folha mensal.
 

## **Perguntas frequentes (FAQ)**

 

**1. ****Posso lançar mais de uma folha avulsa para o mesmo colaborador no mesmo mês?**

Não. Apenas uma folha avulsa por colaborador por competência é permitida.

**2. A folha avulsa gera encargos e contribuições?**

Não, a tributação é feita na folha mensal ou rescisão quando os eventos são recalculados.

**3. Posso editar um lançamento na folha avulsa depois do cálculo?**

Após o cálculo e integração financeira, os lançamentos ficam bloqueados para edição.

**4. O que acontece se eu calcular a folha mensal antes da folha avulsa?**

A folha mensal não reconhecerá os valores pagos na folha avulsa e poderá gerar pagamento duplicado.

**5.** **A folha avulsa é um complemento da folha ou um adiantamento?**

A folha avulsa é um tipo de pagamento flexível que pode ser utilizada tanto como complemento da folha principal quanto como adiantamento salarial em diferentes situações. 

É importante destacar que os proventos pagos por meio da folha avulsa serão incluídos no cálculo da folha mensal regular, e o valor já antecipado será descontado para evitar pagamentos duplicados.

**6.** **Posso pagar só 72,5% do valor como adiantamento e reservar 27,5% para impostos da folha mensal?**

Sim. Basta **cadastrar e configurar um evento** para provisionar os descontos na folha avulsa.

**7.** **Qual letra identifica a folha avulsa em relatórios, arquivo de remessa e lançamento de movimento?**

A letra que representa a folha avulsa em todas as tabelas é **"V"** e o nome do campo que a identifica é **TIPFOLHA**.

**8. ****O cálculo da folha avulsa provisiona valores de desconto de INSS e IRRF?**

Nativamente, não há eventos configurados para descontos na folha avulsa, mas existe a possibilidade de cadastrar e configurar um evento para provisionar descontos.

**9. Como é a integração contábil da folha avulsa? **

Segue o mesmo processo das demais folhas, sem alterações.

**10. A folha avulsa faz desconto de crédito do trabalhador (empréstimos)?**

Nativamente, não há eventos configurados para descontos na folha avulsa, mas existe a possibilidade de cadastrar e configurar um evento para provisionar descontos.

**11. Posso pagar comissões na folha avulsa? O DSR, INSS e IR serão calculados?**

Sim, para comissões. Contudo, nativamente, não há eventos configurados para descontos na folha avulsa, mas existe a possibilidade de cadastrar e configurar um evento para provisionar descontos.

**12. ****A folha avulsa é enviada para o eSocial?**

Não há envio para o eSocial.

**13.** **Posso usar a folha avulsa para pagar um funcionário demitido?**

Não. Para isso, use a rescisão complementar.

**14. ****A folha avulsa tem incidência de impostos?**

Não. A tributação é recalculada na folha mensal.

**15. Posso utilizar um holerite diferente para a Folha Avulsa?**

Sim. Basta configurar o parâmetro **FPRECIBOFOLAVU (Holerite Folha Avulsa)** com o código de um relatório cadastrado em **Relatórios Formatados**.

Caso o parâmetro não seja informado, o sistema utilizará automaticamente o mesmo modelo de holerite da folha mensal.

 

## **Artigos relacionados**

- [Painel de configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559)

- [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767)

- [Lançamento de movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/13968004985495)


---

### 🔗 Links e Referências Internas:

- [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)
- [Painel de configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559)
- [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767)
- [Lançamento de movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/13968004985495)