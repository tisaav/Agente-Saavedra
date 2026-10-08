# Operação Bloqueada: A empresa 'X' não consegue emitir esse documento por estar configurada com ambiente produção em uma base de teste

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360052449293-Opera%C3%A7%C3%A3o-Bloqueada-A-empresa-X-n%C3%A3o-consegue-emitir-esse-documento-por-estar-configurada-com-ambiente-produ%C3%A7%C3%A3o-em-uma-base-de-teste](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052449293-Opera%C3%A7%C3%A3o-Bloqueada-A-empresa-X-n%C3%A3o-consegue-emitir-esse-documento-por-estar-configurada-com-ambiente-produ%C3%A7%C3%A3o-em-uma-base-de-teste)  
> **ID:** `360052449293` | **Última Atualização:** 2026-07-22T15:29:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789506379799)

 MENSAGEM**:

[CORE_E05561] Operação Bloqueada: A empresa 1 não consegue emitir esse documento por estar configurada com ambiente produção em uma base de teste. Avise o administrador para que o mesmo ajuste o registro da base na tela de Administração do servidor.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789514843671)

 CAUSA:**

Ao tentar emitir uma notas com ambiente produção , em bases registradas como teste apresenta o erro acima.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789514850839)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789506388759)

 Logado com o usuário SUP, acessar a tela **Administração do Servidor**, aba **Registro de Base de Dados. **

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789506391191)

![adm do servidor 03-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789506391959)

Nessa tela vão ser apresentados todos os tipos de base configuradas para esse banco de dados. Ou seja, base teste, base treina, base produção.*
*

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789514864407)

 Ajuste o campo "Tipo" corretamente, conforme correspondente a base que encontra-se logado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789506397591)

 Em seguida salvar e realizar o processo novamente .

**Importante:**

- Caso o registro da base esteja correto, será necessário reavaliar a configuração inserida para o tipo de ambiente de emissão da NF-e [Tela 'Empresa' (Preferências) >> Aba NFE/NFC-e , campo "Ambiente NF-e/NFC-e]. Emissão em ambiente PRODUÇÃO só será aceito em base do tipo = PRODUÇÃO.

- Persistindo a mensagem de validação, acionar o Service Desk para análises detalhadas.