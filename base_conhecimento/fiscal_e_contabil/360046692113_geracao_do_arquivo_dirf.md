# Geração do Arquivo DIRF

> **Módulo:** Fiscal e Contábil | **Subseção:** Declarações federais  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360046692113-Gera%C3%A7%C3%A3o-do-Arquivo-DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046692113-Gera%C3%A7%C3%A3o-do-Arquivo-DIRF)  
> **ID:** `360046692113` | **Última Atualização:** 2026-09-15T17:35:36Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313133575447)

******

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313133576727)

****
```

| Módulo: Livros Fiscais > Conexão         Versão disponível: A partir da 4.2 |
| --- |

Por meio desta tela, você realizará a geração da DIRF e irá cadastrar as informações dos registros RESPO e DECPJ. Além disso, você poderá efetuar a geração dos rendimentos, bem como, impostos e contribuições retidas na fonte.

#### ****

[Configurações Iniciais](#configura%C3%A7%C3%B5esiniciais)[Aba Geral](#abageral)

[Aba RESPO](#abarespo)[Aba DECPJ](#abadecpj)

| Funcionalidades da tela |  |
| --- | --- |
|  |  |
|  |  |

 

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416262178967)

### 
**Configurações Iniciais **

Primeiramente, na tela de [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba **"Informações para DIRF"**, preencha as informações a serem enviadas ao registro **"DECPJ – Declarante Pessoa Jurídica"**.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416253812631)

```text

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/42313133578391)

 Se a marcação** "Situação Especial" **for selecionada, o campo** "Data do Evento" **será
          habilitado e torna-se obrigatório o preenchimento.
```

Nesta mesma tela, aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abapropriedades) o campo **"Empresa Matriz (EFD)"** possuirá a função de vincular a empresa matriz no cadastro das filiais. 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416253917335)

Com as configurações acima realizadas, acesse a tela Geração do Arquivo DIRF, e preencha no Painel Principal, os campos **"Empresa"**, **"Dt. Inicial"** e **"Dt. Final" **para a geração do registro DIRF.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416262132503)

Após preencher estes campos, acione o botão **"Processar"** que fará com que as informações inseridas nesta tela sejam apresentadas para conferência.

Com a verificação e validação das informações inseridas para a geração do arquivo, você pode acionar o botão **"Gerar Arquivo"** para que seja gerado um arquivo que posteriormente, será enviado para a Receita.

[[voltar ao topo]](#top)

### 
**Aba Geral**

Nesta aba, temos o campo **"Identificador de estrutura do leiaute"** onde você pode optar entre os leiautes **"AT65HD8"**, **"VR4QLM8"**,**"XJFSFHB"**, **"ARNZRXP" **ou **"R6GP3ZA"** (**a última opção só estará disponível a partir da versão 5.7.3 do Livro Fiscal**).

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416262495511)

[[voltar ao topo]](#top)

### 
**Aba RESPO**

Insira nesta aba as informações do responsável pelo DIRF gerado.

![mceclip9.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416268790807)

[[voltar ao topo]](#top)

### 
**Aba DECPJ**

Por meio desta aba, cadastre as especificações da empresa responsável pelo DIRF deste registro.

![mceclip10.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416268839575)

 

#### **Sub-aba IDREC**

![mceclip11.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416255178007)

Na aba DECPJ, temos ainda a sub-aba **"IDREC"** que comporta as especificações sobre o Declarante Pessoa Jurídica. Referente ao registro, este informará o código da receita utilizado do DARF para recolhimento do imposto incidente sobre o rendimento. As informações do IDREC IRRF, COFINS e CSLL terão origem na tela de [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos) (IMN e IMF) e [Central de Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) (CAB e DIN). Tem-se a seguir os códigos da receita:

- 
**3208 para IRRF:** Aluguéis e Royalties pagos a pessoa física;

- 
**0588 para IRFF:** Rendimento do trabalho sem vínculo empregatício;

- 
**1708 para IRRF:** Remuneração serviços prestados por pessoa jurídica;

- 
**5952 para CSLL/COFINS/PIS:** Retenção Contrib. pagto de PJ a PJ dir privado;

- 
**5987 para CSLL:** Retenção pagamentos de PJ a PJ direito privado;

- 
**5960 para COFINS:** Retenção pagamentos de PJ a PJ direito privado;

- 
**5979 para PIS:** Retenção pagamentos de PJ a PJ direito privado.

#### **Sub-aba BPJDEC**

Na sub-aba IDREC, tem-se a sub-aba BPJDEC em que, o sistema irá exibir as informações da aba que mostrará quais os beneficiários da Pessoa Física do ano calendário declarado que serão apresentados da DIRF. Este registro irá apresentar as informações sobre o beneficiário do rendimento quando tratar-se de pessoa jurídica.

O fator gerador da informação do IRRF será o mesmo da retenção, ou seja, na data do lançamento da nota fiscal ou fatura emitida pela contratada e aceita pela contratante, para PIS/COFINS e CSLL será o pagamento da nota ou parcela.

#### **Sub-aba BPFDEC**

Nessa sub-aba, você inclui informações para geração do grupo de Beneficiários Pessoa Física do Declarante e seus registros filhos, com dados de retenções provenientes de movimentação de parceiros Pessoas Físicas. 

#### **Sub-abas RTRT, RTIRF, RTPO e Documentos**

Nas sub-abas BPJDEC e BPFDEC temos as abas** "RTRT"**, **"RTIRF"** e **"Documentos"**.

Nas abas RTRT E RTIRF preencha os valores correspondentes às retenções de impostos mensais.

Destaca-se que o registro RTRT informará o valor do rendimento tributável mensal, ou seja, a base de cálculo para a retenção na fonte para os registros BPFDEC e BPJDEC. E o registro RTIRF informará o valor do imposto retido na fonte sobre os rendimentos declarados para os registros BPFDEC e BPJDEC.

Temos a sub-aba **"RTPO"** disponível apenas na sub-aba BPFDEC. O registro RTPO refere-se ao INSS e será gerado como somatório de INSS dos IRF que foram gerados no registros RTRT.

Na sub-aba Documentos serão listados todos os lançamentos que fazem parte dos totalizadores apresentados nas abas RTRT e RTIRF. 

[[voltar ao topo]](#top)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16312030528535)

 Acesse também:

[Configurações da DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046065494)


---

### 🔗 Links e Referências Internas:

- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa)
- [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abapropriedades)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)
- [Central de Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas)
- [Configurações da DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046065494)