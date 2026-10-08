# E0650 Rejeição: Em caso de importação de serviço pelo tomador, o ISSQN deve ser retido pelo tomador.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226586816407-E0650-Rejei%C3%A7%C3%A3o-Em-caso-de-importa%C3%A7%C3%A3o-de-servi%C3%A7o-pelo-tomador-o-ISSQN-deve-ser-retido-pelo-tomador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226586816407-E0650-Rejei%C3%A7%C3%A3o-Em-caso-de-importa%C3%A7%C3%A3o-de-servi%C3%A7o-pelo-tomador-o-ISSQN-deve-ser-retido-pelo-tomador)  
> **ID:** `37226586816407` | **Última Atualização:** 2026-07-22T14:14:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226586807831)

 MENSAGEM**

E0650 Rejeição: Em caso de importação de serviço pelo tomador, o ISSQN deve ser retido pelo tomador.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226620852247)

 SITUAÇÃO**

Ao tentar emitir uma **NFS-e de importação de serviço**, o sistema apresenta a rejeição acima, indicando que o **ISSQN não foi configurado para retenção pelo tomador** do serviço.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226620853015)

 SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226586809111)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a **TOP utilizada na emissão da NFS-e**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226620854295)

  Acesse a aba **"NFS-e"** e verifique o campo **"Local de Tributação"**:

- 

Para **importação de serviço**, selecione a opção **"Exterior"**;

- 

Esta configuração fará com que a tag <Tributacao> no XML seja preenchida com o valor **"E"**, indicando tributação no exterior.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226586811031)

 Ainda na aba **"NFS-e"**, localize o campo **"ISSQN Retido"** e configure-o para **"1 - Com retenção de ISSQN"**, garantindo que o **tomador do serviço retenha o imposto**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226620854807)

 Verifique se o parâmetro **"Cidade do ISS conforme CNAE empresa? - CIDISSCNAEEMP"** está **ativado** no sistema, pois ele é necessário para que as opções de **local de tributação** sejam utilizadas corretamente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226586812183)

 Caso a empresa prestadora esteja no **exterior**, certifique-se de que o **cadastro do parceiro** (Configurações > Cadastros > Parceiros) possua o **CNPJ do exterior** devidamente informado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226586813207)

 Salve as alterações e **reemita a NFS-e** com as configurações corretas de **retenção de ISSQN pelo tomador**. 
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226620856983)

 CAUSA**

A rejeição E0650 ocorre quando a empresa está realizando uma **operação de importação de serviço** e o sistema identifica que o **ISSQN não está configurado para retenção pelo tomador**. Conforme a legislação tributária, **em operações de importação de serviço, o tomador é responsável pela retenção e recolhimento do ISSQN**. Se o campo **"ISSQN Retido"** não estiver marcado como **"1 - Com retenção"** ou se o **"Local de Tributação"** não estiver configurado como **"Exterior"**, a prefeitura rejeitará a NFS-e com esta mensagem, exigindo a **adequação da configuração fiscal** antes da emissão do documento.