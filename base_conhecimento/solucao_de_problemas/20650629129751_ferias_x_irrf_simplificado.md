# Férias x IRRF Simplificado

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20650629129751-F%C3%A9rias-x-IRRF-Simplificado](https://ajuda.sankhya.com.br/hc/pt-br/articles/20650629129751-F%C3%A9rias-x-IRRF-Simplificado)  
> **ID:** `20650629129751` | **Última Atualização:** 2026-07-29T13:18:23Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659298455)

 SOLUÇÃO:**

A partir de 2023, foi estabelecido através da MP 1171/23 um novo modelo do cálculo do IRRF retido, passando a admitir uma dedução simplificada mensal caso o valor da mesma seja maior que os valores das deduções legais (INSS Retido, Dependentes e Pensão Alimentícia).

O nosso sistema, levava para a folha mensal, o valor de INSS junto com o já descontado de férias, com o IRRF simplificado, tivemos que separar os dois valores.

Com isso tivemos que alterar alguns eventos e fórmulas para que a apuração do IRRF funcionasse corretamente, no caso de férias no mês.

**Importante:**

Se estiver utilizando o módulo Pessoal+ e os eventos referidos abaixo estiverem como padrão (protegidos), a atualização será feita automaticamente, através do botão 'Atualizar' da tela principal do cadastro de eventos.

![eventos 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659299351)

#### **Configuração de Eventos e Fórmulas**

**Módulo Pessoal+**

Deverão ser feitos manualmente caso os eventos discriminados abaixo não estejam protegidos (sem cadeado no card).

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650629095575)

** Alteração da Configuração de Eventos:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450444998551)

 XXXX - Ressarcimento INSS Férias

Acesse a tela **Eventos** *(Pessoal+ » Cadastros » Eventos) *selecione o evento com a descrição:  RESSARCIMENTO INSS FÉRIAS e faça as alterações listadas abaixo:

- Retire a incidência de IRRF:

 Aba Avançado/ Campo IRRF - selecionar a opção “Não Incide”.

![Ressarcimento 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659303191)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450444998551)

 Retire a identificação do Evento

 Aba Básico>> Campo “Identificação do evento”>> Selecionar a opção “0 - Sem Identificação”.

![Inss ferias 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659303959)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450444998551)

 Altere a incidência IRRF na aba Esocial

 Aba ESOCIAL>> Campo “Incidência p/ IRRF” >> Alterar a incidência de IRRF para “09 - VERBA TRANSITADA PELA FOLHA DE PAGAMENTO DE NATUREZA DIVERSA DE RENDIMENTO OU RETENCAO/ISENCAO/DEDUCAO DE IR”.

![esocial 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659306391)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659307799)

** Alteração da fórmula de INSS:**

**XXXX - INSS**

Acesse a tela **Fórmulas** *(Pessoal+ » Cadastros » Fórmulas), *selecione a fórmula com a descrição: INSS e alterar o texto da fórmula para: 

 IF((fTemNaLista(formatnumeric('00', QueFuncionario.VINCULO), '02,80,90,99') = 'S') OR (QueFuncionario.CODCATEGESOCIAL = 111), 0, IF(&DIASTRA >= 0, TRUNCFOL(IF(@F_RECOMPOSICAOBASEINSS > FTF(1, 3, @F_RECOMPOSICAOBASEINSS, &Refere, QueFuncionario.TIPTAB), FTF(1, 4, @F_RECOMPOSICAOBASEINSS, &Refere, QueFuncionario.TIPTAB) - @F_RECOMPOSICAOINSSRETIDO, (((@F_RECOMPOSICAOBASEINSS * FTF(1, 1, @F_RECOMPOSICAOBASEINSS, &Refere, QueFuncionario.TIPTAB)) / 100) - @F_RECOMPOSICAOINSSRETIDO)), 2), 0)) - IF(@E_RESSARCIMENTOINSSFERIAS > 0, @E_RESSARCIMENTOINSSFERIAS ,0)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659310359)

 Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o INSS da folha mensal.

**Evento**

**XXXX - INSS Descontado nas férias**

**

![ferias 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650629114263)

**

![avançado 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659318295)

**

![descontado 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659319831)

**

**Fórmula**

**

![formula 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650629119127)

**

**Fórmula do valor:**

 IF((@F_DIASDEFERIASNAREFERENCIA <= 0), 0, IF((MemSetVar('ProvINSSComp', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '@C_PROVISAODEDESCONTOINSS')) / IF(MemSetVar('IndProvINSSComp', IF(MemSetVar('Ind4410', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '@C_FERIAS, @C_LICENCAREMUNERADA')) > 0, MemGetVar('Ind4410'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '@C_MEDIADEFERIAS'))) > 0, MemGetVar('IndProvINSSComp'), 1)) * @F_DIASDEFERIASNAREFERENCIA) > 0), MemGetVar('ProvINSSComp'), IF((MemSetVar('ProvINSSProx', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '@C_PROVISAODEDESCONTOINSS')) / IF(MemSetVar('IndProvINSSProx', IF(MemSetVar('Ind4410Prox', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '@C_FERIAS, @C_LICENCAREMUNERADA')) > 0, MemGetVar('Ind4410Prox'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '@C_MEDIADEFERIAS'))) > 0, MemGetVar('IndProvINSSProx'), 1)) * @F_DIASDEFERIASNAREFERENCIA) > 0), MemGetVar('ProvINSSProx'), IF((MemSetVar('ProvINSSProx1', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '@C_PROVISAODEDESCONTOINSS')) / IF(MemSetVar('IndProvINSSProx1', IF(MemSetVar('Ind4410Prox1', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '@C_FERIAS, @C_LICENCAREMUNERADA')) > 0, MemGetVar('Ind4410Prox1'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '@C_MEDIADEFERIAS'))) > 0, MemGetVar('IndProvINSSProx1'), 1)) * @F_DIASDEFERIASNAREFERENCIA) > 0) AND (&MESATU = 3), MemGetVar('ProvINSSProx1'), 0))))  

 

**MGE/ Módulo MGE Pessoal**

**Configuração de Eventos e Fórmulas**

Deverão ser feitos manualmente caso os eventos discriminados  abaixo não estejam protegidos (campo “Protegido” desmarcado).

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650629095575)

**Alteração da Configuração de Eventos**
**XXXX - RESSARCIMENTO INSS FERIAS**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450444998551)

 Acesse o menu “Eventos” Selecione o evento com a descrição: RESSARCIMENTO INSS FERIAS e fazer as alterações listadas abaixo: 

**XXXX - RESSARCIMENTO INSS FERIAS**

Retire a incidência de IRRF: Aba Base de Cálculo / Campo IRRF - selecionar a opção “Não Incide”.

![incide 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650629120535)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450444998551)

 Retire a identificação do Evento: Aba Propriedades>> Campo “Identificação do Evento”>> Selecionar a opção “0 - Sem Identificação”.

![sem natureza 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659324311)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450444998551)

 Altere a incidência IRRF na aba Esocial

 Aba Incidência >> Campo “Incidência p/ IRRF” >> Alterar a incidência de IRRF para “09 - VERBA TRANSITADA PELA FOLHA DE PAGAMENTO DE NATUREZA DIVERSA DE RENDIMENTO OU RETENCAO/ISENCAO/DEDUCAO DE IR”.

![Descrição 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659325335)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659307799)

** Alteração da fórmula de INSS:**

**XXXX - INSS**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450444998551)

 Acesse a tela Fórmulas, selecione a fórmula com a descrição: INSS e altere o texto da fórmula para: 

 IF((fTemNaLista(formatnumeric('00', QueFuncionario.VINCULO), '02,80,90,99') = 'S') OR (QueFuncionario.CODCATEGESOCIAL = 111),0,IF(&DIASTRA >= 0,TRUNCFOL(IF(&INSSMESAMES = 'S',0, IF(&F5080 > FTF(1,3,&F5080,&Refere,QueFuncionario.TIPTAB), FTF(1,4,&F5080,&Refere,QueFuncionario.TIPTAB) - &F5090,(((&F5080 * FTF(1,1,&F5080,&Refere,QueFuncionario.TIPTAB)) / 100) - &F5090))),2),0)) - IF(&E9340>0, &E9340,0) 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659310359)

 Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o INSS da folha mensal.
Evento:  XXXX - INSS DESCONTADO NAS FERIAS

![desconto 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650629123863)

![liquido 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659327255)

![nao incide 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20650659328535)

**Fórmula:**

**XXXX - INSS Férias**

 IF((&F4432 <= 0), 0, IF((MemSetVar('ProvINSSComp', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '9330')) / IF(MemSetVar('IndProvINSSComp', IF(MemSetVar('Ind4410', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '4410')) > 0, MemGetVar('Ind4410'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '4430'))) > 0, MemGetVar('IndProvINSSComp'), 1)) * &F4432) > 0), MemGetVar('ProvINSSComp'), IF((MemSetVar('ProvINSSProx', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '9330')) / IF(MemSetVar('IndProvINSSProx', IF(MemSetVar('Ind4410Prox', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '4410')) > 0,MemGetVar('Ind4410Prox'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '4430'))) > 0, MemGetVar('IndProvINSSProx'), 1)) * &F4432) > 0), MemGetVar('ProvINSSProx'), 0)))