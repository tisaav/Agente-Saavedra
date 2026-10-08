# As seguintes TOPs não possuem configuração de contabilização e impediram o processamento de XX registros: XX

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36263765443991-As-seguintes-TOPs-n%C3%A3o-possuem-configura%C3%A7%C3%A3o-de-contabiliza%C3%A7%C3%A3o-e-impediram-o-processamento-de-XX-registros-XX](https://ajuda.sankhya.com.br/hc/pt-br/articles/36263765443991-As-seguintes-TOPs-n%C3%A3o-possuem-configura%C3%A7%C3%A3o-de-contabiliza%C3%A7%C3%A3o-e-impediram-o-processamento-de-XX-registros-XX)  
> **ID:** `36263765443991` | **Última Atualização:** 2026-09-17T13:35:17Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36264131732375)

 **MENSAGEM:**

As seguintes TOPs não possuem configuração de contabilização e impediram o processamento de XX registros: XX

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36264131751959)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36421267424791)

 Verifique na tela ****[''TOP Contabilização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o)' e confirme se as TOPs possuem fórmula de contabilização configuradas.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36421267429271)

 Se não houver nenhuma fórmula vinculada, cadastre ao menos uma regra contábil, pois ela é necessária para que o processamento seja concluído.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36424517639575)

 Em seguida, acesse a tela ****[''Agendamentos''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento)** **(Contabilização » Rotinas » Agendamento), abra a aba **“Filtros”** e revise a seção ****[“Parâmetros de Contabilização”](https://ajuda.sankhya.com.br/hc/pt-br/articles/27390133571991-Par%C3%A2metros-de-Contabiliza%C3%A7%C3%A3o)**.**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36424517648663)

 Caso exista algum filtro configurado que esteja eliminando todas as fórmulas das TOPs, ajuste ou remova.

Filtros restritivos podem fazer com que o sistema não encontre nenhuma fórmula válida, mesmo quando elas existem.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36264101883927)

CAUSA:**

A mensagem ocorre, geralmente, por dois motivos: 

- 

**TOP sem fórmulas de contabilização:**

Durante o processamento da tela ''Agendamento''** (**Contabilização » Rotinas » Agendamento), o sistema identifica documentos aptos a serem contabilizados, mas ao verificar a TOP vinculada, não encontra nenhuma fórmula cadastrada na tela ''TOP Contabilizações''** (**Contabilização » Arquivos » TOP Contabilização).

Nesse caso, o sistema entende que não há regra contábil para executar.

- 

**Filtros que eliminam as fórmulas existentes:**

Na tela ''Agendamento'', aba ''**Filtros''**, a seção ''Parâmetros de Contabilização'' permite aplicar filtros sobre as fórmulas das TOPs.

Se algum filtro criado resultar em **nenhuma fórmula retornada, **mesmo que existam fórmulas configuradas, o sistema interpreta que não existe fórmula válida.

Assim, é necessário revisar ou remover o filtro que está restringindo incorretamente as regras de contabilização.

 

![image (27).png](https://ajuda.sankhya.com.br/hc/article_attachments/36421267437079)


---

### 🔗 Links e Referências Internas:

- [''TOP Contabilização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o)
- [''Agendamentos''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento)
- [“Parâmetros de Contabilização”](https://ajuda.sankhya.com.br/hc/pt-br/articles/27390133571991-Par%C3%A2metros-de-Contabiliza%C3%A7%C3%A3o)