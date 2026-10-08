# E0178 Rejeição: Regime especial de tributação não permitido para o prestador do serviço com código de tributação na data de competência, informados na DPS, conforme parametrização do município de incidência do ISSQN.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222573510295-E0178-Rejei%C3%A7%C3%A3o-Regime-especial-de-tributa%C3%A7%C3%A3o-n%C3%A3o-permitido-para-o-prestador-do-servi%C3%A7o-com-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-na-data-de-compet%C3%AAncia-informados-na-DPS-conforme-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222573510295-E0178-Rejei%C3%A7%C3%A3o-Regime-especial-de-tributa%C3%A7%C3%A3o-n%C3%A3o-permitido-para-o-prestador-do-servi%C3%A7o-com-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-na-data-de-compet%C3%AAncia-informados-na-DPS-conforme-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN)  
> **ID:** `37222573510295` | **Última Atualização:** 2026-07-22T14:17:41Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222539682071)

 **MENSAGEM**

E0178 Rejeição: Regime especial de tributação não permitido para o prestador do serviço com código de tributação na data de competência, informados na DPS, conforme parametrização do município de incidência do ISSQN.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222539682327)

 **SITUAÇÃO**

Ao emitir uma NFS-e, a nota é rejeitada pela Sefaz com a mensagem de erro E0178, indicando que o **regime especial de tributação do ISS** configurado para a empresa **não é permitido pelo município** de incidência do ISSQN, considerando o código de tributação e a data de competência informados.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222554872343)

 **SOLUÇÃO**

Para corrigir a rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222554872855)

 Acesse a tela **''Empresa"** (Configurações » Cadastros » Empresas » Preferências da Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222554874263)

 Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba **"Geral"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222539685015)

 Localize o campo **"Regime esp. tributação ISS (NFS-e)"** e verifique qual regime especial de tributação está configurado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222539685911)

 Consulte o **manual da Prefeitura do município** de incidência do ISSQN para identificar quais regimes especiais de tributação são permitidos para o serviço prestado. Os códigos variam conforme o município, podendo incluir opções como:

- 

**''Tributável''**

- 

**''Simples Nacional''**

- 

**''Microempresa Municipal''**

- 

**''Estimativa''**

- 

**''Sociedade de Profissionais''**

- 

**''Cooperativa''**

- 

**''Microempresário Individual (MEI)''**

- 

**''Isento''**

- 

**''Imune''**

- 

**''Não Incidência no Município''**

- 

**''Exigibilidade Suspensa''**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222554877975)

 Ajuste o campo **"Regime esp. trib. ISS (NFS-e)"** com o código correto permitido pelo município de incidência do ISSQN, conforme identificado na documentação da Prefeitura.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222554878615)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222589690391)

 Na aba **“NFS-e”**, verifique o campo **“Cód. Natureza Oper. ISS (NFS-e)”** e confirme se ele está configurado corretamente de acordo com o tipo de operação realizada e as regras do município de incidência do ISSQN.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37810236186263)

 Acesse a tela ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37810213590935)

 Na aba **''Cabeçalho''**, no campo **''Cidade de Prestação de Serviço''**, verifique se o município de incidência do ISSQN está informado corretamente.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37810213592855)

 Emita novamente a NFS-e e verifique se a rejeição foi solucionada.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222554879255)

 **CAUSA**

A rejeição ocorre quando o **regime especial de tributação do ISS** configurado no cadastro da empresa **não é aceito pelo município** de incidência do ISSQN para o tipo de serviço prestado, considerando o código de tributação e a data de competência informados na Declaração de Prestação de Serviços (DPS). Cada município possui **parametrizações específicas** que definem quais regimes são permitidos, e a divergência entre a configuração do sistema e as regras municipais gera a rejeição.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)