# PIS sobre a folha de pagamento

> **Módulo:** Pessoas+ | **Subseção:** Regras de IRRF e Incidências  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/28240000315543-PIS-sobre-a-folha-de-pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/28240000315543-PIS-sobre-a-folha-de-pagamento)  
> **ID:** `28240000315543` | **Última Atualização:** 2026-09-26T00:35:08Z

---

#### ****

[Legislações vigentes](#Legisla%C3%A7%C3%B5esvigentes)

- [Empresas que são enquadradas na regra](#Empresasques%C3%A3oenquadradasnaregra)
- [Alíquota](#Al%C3%ADquota)
- [Base de cálculo](#Basedec%C3%A1lculo)
- [Prazo de pagamento](#Prazodepagamento)
- [Fato gerador](#Fatorgerador)

[Parametrizações do sistema](#Parametriza%C3%A7%C3%B5esdosistema)

- [Tela Registro Fiscal](#TelaRegistroFiscal)
- [Tela de Eventos](#TeladeEventos)
- [Tela de Processos](#TeladeProcessos)
- [Tela de Cálculos](#TeladeC%C3%A1lculos)
- [Resumo da Folha](#ResumodaFolha)
- [Integração com o Financeiro por Evento](#Integra%C3%A7%C3%A3ocomoFinanceiroporEvento)

| O que é necessário saber? |  |
| --- | --- |
|  |  |

## 
**Legislações vigentes**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/28240000306967)

 [MP nº 2158-35/2001 art. 13](https://www.planalto.gov.br/ccivil_03/mpv/2158-35.htm)

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/28240000306967)

 [IN nº 2121/2022 arts. 300 a 305](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=104314)

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/28240000306967)

 Lei nº 9.715/1998

### 
**Empresas que são enquadradas na regra**

I - Templos de qualquer culto;

II - Partidos políticos;

III - Instituições de educação e de assistência social a que se refere o art. 12 da Lei no 9.532, de 10 de dezembro de 1997;

IV - Instituições de caráter filantrópico, recreativo, cultural, científico e as associações, a que se refere o art. 15 da Lei no 9.532, de 1997;

V - Sindicatos, federações e confederações;

VI - Serviços sociais autônomos, criados ou autorizados por lei;

VII - Conselhos de fiscalização de profissões regulamentadas;

VIII - Fundações de direito privado e fundações públicas instituídas ou mantidas pelo Poder Público;

IX - Condomínios de proprietários de imóveis residenciais ou comerciais; e

X - A Organização das Cooperativas Brasileiras - OCB e as Organizações Estaduais de Cooperativas previstas no art. 105 e seu § 1o da Lei no 5.764, de 16 de dezembro de 1971;

XI- Sociedades cooperativas na forma descrita na IN RFB 2121/2022.

[[voltar ao topo]](#top)

### 
**Alíquota**

1% sobre a folha de pagamento.

[[voltar ao topo]](#top)

### 
**Base de cálculo**

De acordo com o art. 303 da IN RFB 2121/2022: *"a base de cálculo da Contribuição para o PIS/Pasep incidente sobre a folha de salários mensal das entidades relacionadas no art. 301 corresponde ao total das remunerações pagas ou creditadas a empregados nos termos do inciso I do art. 22 da Lei nº 8.212, de 1991"*.

**Não integram a base de cálculo:** excluem-se os valores de que trata o § 9º do art. 28 da lei 8.212/91 (Medida Provisória nº 2.158-35, de 2001, art. 13, caput; Decreto nº 4.524, de 17 de dezembro de 2002, art. 50). Dentre eles:

- 

Salário família;

- 

Ticket alimentação;

- 

Vale transporte;

- 

Férias e licenças-prêmio indenizadas;

- 

Aviso prévio indenizado;

- 

Incentivo pago em decorrência de adesão ao PDV- Plano de Demissão Voluntária;

- 

FGTS pago diretamente ao empregado na rescisão;

- 

Indenizações pagas na rescisão sem justa causa.

[[voltar ao topo]](#top)

### 
**Prazo de pagamento** 

Até 25º dia do mês onde houve o pagamento do salário.

[[voltar ao topo]](#top)

### 
**Fato gerador**

Pagamento dos salários.

[[voltar ao topo]](#top)

## 
**Parametrizações do sistema**

```text
 Estas funcionalidades das telas estarão disponíveis a partir das versões:
           Pessoal+ 5.21 
           sanEsocial 3.8
```

### 
**Tela Registro Fiscal**

Na tela [Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214-Registro-Fiscal#abageral), seção **"PIS sobre a folha de pagamento"**, deverá preencher os seguintes campos:

![registro-fiscal-pis.png](https://ajuda.sankhya.com.br/hc/article_attachments/28240837698199)

**Empresa contribuinte:** habilite esta marcação se a empresa for contribuinte do PIS sobre a folha de pagamento.

**Alíquota:** preencha o valor 1,0% (art. 278, IN RFB 1911/2019).

**Código da Receita:** informe o valor 8301-02, conforme consta no site do [eSocial](https://www.gov.br/esocial/pt-br/noticias/calculo-do-pis-pasep-sobre-a-folha-de-salarios-e-implementado-no-esocial-e-na-dctfweb):

![codigo-pis-2024.png](https://ajuda.sankhya.com.br/hc/article_attachments/28241057947415)

#### **Evento S-1000**

A versão S-1.3 do eSocial trouxe a alteração da descrição da tag DE (indTribFolhaPisCofins) PARA (indTribFolhaPisPasep). Para envio dessa tag como 'S', basta ativar a marcação Empresa contribuinte na seção citada acima vinculado a matriz.

![tag-pis-sobre-folha.png](https://ajuda.sankhya.com.br/hc/article_attachments/28244819426711)

[[voltar ao topo]](#top)

### 
**Tela de Eventos**

Com a versão S-1.3 do eSocial, foi criado o campo **"Código de incidência da rubrica para o PIS/PASEP sobre a folha de salários"** (codIncPisPasep>>dadosRubrica) no evento S-1010. Para atender essa exigência, foi adicionado os campos:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28245809335447)

 No **Pessoal+**, o campo** "Incidência p/ PIS"** na aba [eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#AbaeSocial) da tela [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) e automatizadas as parametrizações dos eventos e fórmulas no momento da atualização do módulo Pessoal+.

![campo-pis-aba-esocial-eventos.png](https://ajuda.sankhya.com.br/hc/article_attachments/28757224470167)

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28245809335447)

 No **MGE**, tela **"Eventos"**, aba **"Incidência"**, o campo **"Incidência p/ PIS PASEP"** com as opções **"00- Não é base de cálculo"**, **"11-Base Mensal"** e **"12-Base 13º salário"**.

![campo-incidenciapis-mge.png](https://ajuda.sankhya.com.br/hc/article_attachments/28757168003735)

A informação desses campos será obrigatória para o eSocial quando o empregador enviar no evento S-1000 a tag **"Indicador de tributação sobre a folha de pagamento - PIS e PASEP"** (indTribFolhaPisPasep) marcada como 'S', conforme o leiaute.

**Importante:** esses campos só serão exibidos nas respectivas telas quando houver ao menos uma empresa matriz cadastrada no sistema como contribuinte do PIS sobre a folha (marcação Empresa contribuinte ativada na tela [Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214)), assim como as informações inseridas, impactando a rotina da folha e o eSocial. Empresas não contribuintes ou casos em que não há empresas contribuintes cadastradas no sistema não serão afetados pelas alterações da versão S-1.3 relacionados ao PIS PASEP e o campo não será exibido.

#### **Eventos Padrão Sankhya**

Os eventos padrões/padrão Sankhya, ou seja, eventos que a Sankhya tem a responsabilidade de parametrizá-los e/ou atualizá-los serão atualizados automaticamente com as devidas parametrizações para o PIS PASEP.

#### **Bases de Cálculo**
As bases de cálculo do PIS sobre a folha de pagamento serão padrão, conforme exemplos abaixo, por isso os eventos que estiverem como personalizados deverão ser inativados para que não haja duplicidade de eventos. Serão duas bases de cálculo para o PIS PASEP:

- 

**BASE PIS PASEP MENSAL** com identificação igual a **"20- Base PIS PASEP"**;

![base-pis-pasep.png](https://ajuda.sankhya.com.br/hc/article_attachments/28245459394199)

- 

**BASE PIS 13º SALÁRIO** com identificação igual a **"33-Base PIS PASEP 13º"**.

![base-pis-pasep-33.png](https://ajuda.sankhya.com.br/hc/article_attachments/28245459396887)

As bases de cálculo serão vinculadas em seus respectivos eventos de acordo com o DE/PARA abaixo:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28245809335447)

 INCIDÊNCIA P/ PIS: 00-NÃO É BASE DE CÁLCULO

- 

Aba [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#AbaAvan%C3%A7ado) > campo **"Outros" **> marcações: **"PIS PASEP"** e **"PIS PASEP 13º SALÁRIO"** desativadas.

- 

Aba [Bases de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#ababasesdecalculo) sem vinculação de base.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28245809335447)

 INCIDÊNCIA P/ PIS: 11-MENSAL

- 

Aba Avançado > campo Outros > marcações: PIS PASEP habilitada, e PIS PASEP 13º SALÁRIO desativada.

- 

Aba Bases de Cálculo com vinculação de BASE PIS MENSAL.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28245809335447)

 INCIDÊNCIA P/ PIS: 12- 13º SALÁRIO

- 

Aba Avançado > campo Outros > marcações: PIS PASEP desabilitada, e PIS PASEP 13º SALÁRIO ativada.

- 

Aba Bases de Cálculo com vinculação de BASE PIS 13º SALÁRIO.

Exemplo: evento 2ª PARCELA 13º SALÁRIO

![ex-segunda-parcela-13.png](https://ajuda.sankhya.com.br/hc/article_attachments/28265692771095)

#### **Evento PIS PASEP**

Terão dois eventos PIS PASEP (mensal e 13º salário) que retornará o valor a pagar da contribuição no Cálculo e no Resumo da Folha. Os eventos serão padrão e por isso os eventos que estiverem como personalizados deverão ser inativados para que não haja duplicidade.

Os dois eventos serão de **"Desconto"**, com **"Base Líquida"** igual a **"Não"**, regra de cálculo em todas folhas onde há pagamento dos valores mencionados no art. 277, da IN RFB 1911/2019 com a devida separação entre mensal e 13º salário e com **"Identificação do evento"** igual a **"114- Evento PIS PASEP"** e **"211- Evento PIS PASEP 13º"**, conforme exemplo abaixo:

![evento-padrao-pis.png](https://ajuda.sankhya.com.br/hc/article_attachments/28246153046295)

#### **Eventos que compõem a Base de Cálculo do PIS PASEP**

Os eventos padrão Sankhya serão atualizados, embora seja responsabilidade da empresa a geração e o envio dos eventos atualizados no evento S-1010, conforme fluxograma abaixo e exemplo:

![fluxo-eventos-incidencia.png](https://ajuda.sankhya.com.br/hc/article_attachments/28383674264983)

Exemplo: evento Salário Base

![exemplo-salario-base-pis.png](https://ajuda.sankhya.com.br/hc/article_attachments/28265804242199)

#### **Fórmulas PIS PASEP**

As fórmulas do evento PIS PASEP Mensal e 13º salário também serão padrão Sankhya, por isso o usuário deverá mantê-las atualizadas inativando as fórmulas personalizadas criadas para esse fim.

#### **Eventos Personalizados**

As empresas contribuintes do PIS PASEP sobre a folha de pagamento deverão atualizar seus eventos personalizados. Ao atualizar qualquer evento personalizado, o sistema automaticamente fará a parametrização abaixo, porém caso a empresa não concorde com a parametrização feita, a mesma poderá ser editada.

![atualizar-eventos-incidencias.png](https://ajuda.sankhya.com.br/hc/article_attachments/28384614201239)

#### **Geração e Envio para o evento S-1010**

Todos os eventos devem ser reenviados ao eSocial por meio do evento S-1010, garantindo a correta comunicação e apuração da contribuição. Para isso, o sistema irá gerar todos os eventos cadastrados e parametrizados com as incidências do PIS/PASEP para envio.

É importante ressaltar que o sistema gerará tanto eventos padrão quanto personalizados. Por esse motivo, na [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175), menu [Eventos Pendentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175-Central-do-eSocial#eventospendentes), a marcação **"Utilizar data de início padrão do sistema"** deve estar desabilitada, permitindo que o usuário defina manualmente a data de início da alteração, conforme o exemplo abaixo:

![envio-eventos-esocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/28246861162391)

![data-envio-alteracao.png](https://ajuda.sankhya.com.br/hc/article_attachments/28246861167895)

Trecho retirado do Manual de Orientação do eSocial versão S-1.3

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/28246916186647)

Trecho retirado do Leiaute do eSocial > Evento S-1010 > tag (codIncPisPasep)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/28246916189335)

![evento-pis-mge.gif](https://ajuda.sankhya.com.br/hc/article_attachments/28917522767895)

Exemplo de envio do evento com o novo campo de incidência:

![xml-evento.png](https://ajuda.sankhya.com.br/hc/article_attachments/28247011747991)

[[voltar ao topo]](#top)

### 
**Tela de Processos**

Na tela [Processos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655), devem ser cadastradas as informações do processo que tenha medida judicial indicando a suspensão da incidência da contribuição do PIS/PASEP, vinculando à empresa contribuinte e os eventos envolvidos. Após o envio do evento S-1070, a empresa deverá realizar a geração e o envio novamente dos eventos vinculados ao processo no S-1010 sem a necessidade de entrar na tela de Eventos e alterar os código de incidência do PIS, que serão mantidos. A conversão dos códigos de incidência seguirá a regra abaixo:

- 

Código de incidência 11- Mensal para Código de incidência 91-Incidência suspensa em decorrência de decisão judicial - PIS/PASEP mensal;

- 

Código de incidência 12-13º salário para Código de incidência 92-Incidência suspensa em decorrência de decisão judicial - PIS/PASEP 13º salário.

Abaixo segue um exemplo de Processo cadastrado que suspende a incidência de PIS PASEP:

![identificacao-processo.png](https://ajuda.sankhya.com.br/hc/article_attachments/28266721883287)

Quando o Processo discutir apenas sobre a suspensão de incidência para o PIS, deverá selecionar no campo **"Identificação do Processo" **da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655-Processos#AbaPropriedades) a opção **"PIS/PASEP (1- Exclusivamente tributária)"** e, assim a marcação **"PIS/PASEP"** da seção **"Não incidência na folha de pagamento"** será ativada automaticamente, conforme abaixo:

![aba-propriedades-processos.png](https://ajuda.sankhya.com.br/hc/article_attachments/28247698634135)

**MGE**

**

![processo-pis-mge.gif](https://ajuda.sankhya.com.br/hc/article_attachments/28741015991575)

**

Caso a empresa contribuinte esteja discutindo em único Processo, além da suspensão da incidência do PIS, outras contribuições previdenciárias, poderá escolher as outras opções no campo Identificação do Processo, mas deverá ativar a marcação PIS/PASEP.

**Observação:** para Processos relacionados à suspensão de incidência do PIS, o eSocial exige que a Matéria do Processo seja marcada como **"1 - Exclusivamente tributária ou tributária e FGTS"**. Por isso, o sistema define essa opção automaticamente no campo **"Matéria do Processo ou Alvará Judicial (eSocial)"** quando a marcação PIS/PASEP estiver ativada. Caso tente salvar com outra opção, será exibida uma mensagem de erro indicando a validação exigida pelo eSocial:

***"O campo "Matéria do Processo ou Alvará Judicial (eSocial)" para este tipo de processo deve ser igual a "1 - Exclusivamente tributária ou tributária e FGTS"."***

Na aba [Empresas Participantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655-Processos#AbaEmpresasParticipantes), deverá vincular a empresa contribuinte do PIS que discute a suspensão da incidência. Ao salvar o cadastro, o sistema verificará se a empresa é contribuinte do PIS quando a marcação PIS/PASEP (seção Não incidência na folha de pagamento, aba Propriedades) estiver ativada. Caso não seja contribuinte, será exibida a seguinte mensagem de erro:

***"A empresa vinculada ao processo não é contribuinte do PIS/Pasep, portanto, não é possível aplicar a suspensão de exigibilidade para eventos relacionados à incidência do PIS."***

Na aba [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655-Processos#AbaEventos) serão vinculados todos os eventos que estão sendo discutidos no Processo. Ao incluir os eventos nessa aba, o sistema automaticamente irá gerar o evento S-1010 para envio dos novos códigos de incidência do PIS suspendendo a incidência, além disso enviará no mesmo evento as informações do processo, conforme exemplo abaixo:

**Pessoal+**

![cadastro-processos.png](https://ajuda.sankhya.com.br/hc/article_attachments/28266721895959)

![eventos-envios-1010-1070.png](https://ajuda.sankhya.com.br/hc/article_attachments/28266839829911)

![xml-1010.png](https://ajuda.sankhya.com.br/hc/article_attachments/28266854517911)

**MGE**

![processo-incidencia-pis-mge.gif](https://ajuda.sankhya.com.br/hc/article_attachments/28741668461463)

![calculo-incidencia-pis-mge.gif](https://ajuda.sankhya.com.br/hc/article_attachments/28741668462743)

![xml-pis-sobre-folha-mge.png](https://ajuda.sankhya.com.br/hc/article_attachments/28741713455639)

É importante destacar que o cadastro do Processo envolvendo a incidência de PIS PASEP será refletido no Cálculo, Resumo da Folha, além do eSocial.

[[voltar ao topo]](#top)

### 
**Tela de Cálculos**

A tela [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031) pode ser acessada diretamente ou pelo [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599).

Ao realizar a [conferência Individual](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031-C%C3%A1lculos#AbaFolha), seção **"eSocial"**, é possível comparar a base de cálculo do PIS calculada pelo sistema com a enviada ao eSocial. Esse comparativo facilita a identificação de diferenças entre a base vinculada ao evento e as configurações de incidência do eSocial.
Se houver divergências, deve-se verificar as configurações do evento nas abas [eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#AbaeSocial) e [Bases de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#ababasesdecalculo) da tela [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767), além da tela [Processos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655), onde podem existir eventos vinculados a processos que suspendem a incidência do PIS/PASEP.

![incidencia-pis.png](https://ajuda.sankhya.com.br/hc/article_attachments/28268213081239)

Para auxiliar na conferência, o pop-up **"Eventos que compõem a base"** agora inclui os eventos excluídos da base por estarem vinculados a processos que suspendem a incidência, indicando que sua ausência se deve a uma medida judicial.

![eventos-suspensao-exigibilidade.png](https://ajuda.sankhya.com.br/hc/article_attachments/28248953619607)

No **MGE**, ao calcular a folha, quando houver vinculação do Evento a um Processo, a marcação **"PIS PASEP"** na seção **"Não incide na folha de pagamento"** estiver habilitada e o Evento S-1070 relacionado a esse Processo estiver sido finalizado com sucesso, o sistema não irá considerar na base de cálculo do PIS PASEP os seguintes eventos:

- 

Evento **"20- BASE PIS PASEP"** quando a incidência for igual a **"11/91"**;

- 

Evento **"BASE PIS PASEP 13º"** quando a incidência for igual a **"12/92"**.

![calculo-pis-mge.gif](https://ajuda.sankhya.com.br/hc/article_attachments/28736224946071)

[[voltar ao topo]](#top)

### 
**Resumo da Folha**

O Resumo da folha é gerado através da tela [Gerenciador de Folhas,](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599-Gerenciador-de-Folhas#Bot%C3%B5esdaTela) por meio do botão **"Resumo da folha"**. 

![resumo-da-folha-gerenciador.png](https://ajuda.sankhya.com.br/hc/article_attachments/28266938568983)

Aqui, foi ajustada a visualização das informações relacionadas ao PIS PASEP e incluídas as informações de base de cálculo e valor a pagar do PIS 13º salário, conforme exemplo abaixo:

Exemplo: Base de cálculo mensal e 13º salário dentro da referência.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/28249284659991)

**MGE**

Exemplo: mensal 13º com alíquota 1%

**

![resumo-da-folha-mge1.png](https://ajuda.sankhya.com.br/hc/article_attachments/28742993741463)

**

[[voltar ao topo]](#top)

### 
**Integração com o financeiro por evento**

Os eventos de desconto do PIS PASEP sobre a folha de pagamento calculados na referência deverão ser integrados com o financeiro.

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/28240000306967)

 **Pessoal+:** através da rotina **"Integração com financeiro por evento"**, conforme exemplo abaixo:

![integracao-financeira-eventos.gif](https://ajuda.sankhya.com.br/hc/article_attachments/28249381111191)

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/28240000306967)

 **MGE:** por meio da rotina **"Integração com o Financeiro"**, conforme ilustrado abaixo:

![integracao-financeiro-pis-mge.gif](https://ajuda.sankhya.com.br/hc/article_attachments/28919391389847)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214-Registro-Fiscal#abageral)
- [eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#AbaeSocial)
- [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767)
- [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#AbaAvan%C3%A7ado)
- [Bases de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#ababasesdecalculo)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
- [Eventos Pendentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175-Central-do-eSocial#eventospendentes)
- [Processos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655)
- [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655-Processos#AbaPropriedades)
- [Empresas Participantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655-Processos#AbaEmpresasParticipantes)
- [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405166245655-Processos#AbaEventos)
- [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)
- [conferência Individual](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031-C%C3%A1lculos#AbaFolha)
- [Gerenciador de Folhas,](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599-Gerenciador-de-Folhas#Bot%C3%B5esdaTela)