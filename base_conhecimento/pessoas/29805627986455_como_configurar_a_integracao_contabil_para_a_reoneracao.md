# Como configurar a integração contábil para a reoneração?

> **Módulo:** Pessoas+ | **Subseção:** Configuração das Integrações Contábil e Financeira  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/29805627986455-Como-configurar-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-para-a-reonera%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/29805627986455-Como-configurar-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-para-a-reonera%C3%A7%C3%A3o)  
> **ID:** `29805627986455` | **Última Atualização:** 2026-09-27T20:06:25Z

---

A reoneração da folha de pagamento mudou como algumas empresas calculam a contribuição ao INSS. Segundo a **Lei n.º 14.973/2024**, **empresas desoneradas não pagam a contribuição patronal sobre o 13º salário**, e a alíquota de 20% volta a ser aplicada gradualmente em municípios com baixo índice populacional.

Para garantir que o **Pessoal+** faça corretamente a integração contábil do **INSS parte empresa**, ao calcular o 13º salário (seja em rescisões ou na folha de pagamento), é **necessário** ajustar as [Fórmulas contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/10086051863063) dos eventos usados nesse cálculo.

### **O que muda?**

A fórmula contábil não deve utilizar a variável "V_perinss" (percentual INSS) para empresas desoneradas.

### **Como configurar?**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29805961845655)

 **Fórmula para provisão do INSS 13º salário:**

- 

antes;

```text
(V_totbas + V_Incorpora)* (V_perinss + V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100

```

![formula-utiliza-percentual-inss.png](https://ajuda.sankhya.com.br/hc/article_attachments/29806124932247)

- agora.

```text
(V_totbas + V_Incorpora)* (V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100
```

![nova-formula-perinss.png](https://ajuda.sankhya.com.br/hc/article_attachments/29806259852439)

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29805961845655)

 Fórmula para o INSS da folha normal do 13º salário:**

- antes;

```text
(V_totbas )* (V_perinss + V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100
```

![formula-perinss-folha-normal.png](https://ajuda.sankhya.com.br/hc/article_attachments/29806418211223)

- agora.

```text
(V_totbas )* (V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100
```

![nova-formula-perinss-folha-normal.png](https://ajuda.sankhya.com.br/hc/article_attachments/29806518131479)

Essas fórmulas devem ser aplicadas **aos eventos de base de cálculo de 13º salário** utilizados na configuração contábil dos [Registros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214) de empresas **optantes** pela desoneração da folha de pagamento.


---

### 🔗 Links e Referências Internas:

- [Fórmulas contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/10086051863063)
- [Registros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214)