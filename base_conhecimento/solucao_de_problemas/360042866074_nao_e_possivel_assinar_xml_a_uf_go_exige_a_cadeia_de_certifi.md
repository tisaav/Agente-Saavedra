# Não é possível assinar xml a uf (GO) exige a cadeia de certificado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042866074-N%C3%A3o-%C3%A9-poss%C3%ADvel-assinar-xml-a-uf-GO-exige-a-cadeia-de-certificado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042866074-N%C3%A3o-%C3%A9-poss%C3%ADvel-assinar-xml-a-uf-GO-exige-a-cadeia-de-certificado)  
> **ID:** `360042866074` | **Última Atualização:** 2026-07-22T16:05:41Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114895716503)

 MENSAGEM:**

Não é possível assinar xml a uf (GO) exige a cadeia de certificado.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114886917911)

 SITUAÇÃO:**

Ao tentar realizar emissão de NF-e é apresentada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114886923031)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

- Desde novembro de 2014 a Receita Estadual de Goiás passou a exigir a cadeia completa no certificado digital.

- No nosso emissor de NFe, o SanNFe, foi feita a validação do certificado, no intuito de identificar que o mesmo não possui a cadeia e apresentar uma mensagem para o usuário.

- Como o envio de uma NF-e é um serviço crítico e pode comprometer o faturamento de uma empresa, tem-se a seguir um passo-a-passo de como exportar o certificado conforme exigido para a Sefaz do Estado de Goiás.

- O **Manual de orientações segue em anexo**, vale ressaltar que não trata-se de um incidente causado pelo sistema Sankhya, que deve ser tratado junto a pessoa/empresa responsável pela emissão do certificado. Nosso intuito disponibilizando esse Manual é uma tentativa de auxiliar o cliente, porém a validação desse não esta sob nossa alçada e responsabilidade.

- Caso a solução acima não o atenda, aconselhamos contactar a **empresa que emitiu o certificado digital** e explicar a necessidade da presença de tais informações no certificado, para que estes lhe auxiliem na instalação do certificado adquirido com a cadeia completa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114895728407)

 CAUSA:**

Ocorre quando os certificados não foram gerados com a Cadeia de certificação das Autoridades que regulamenta a confiança do certificado, através de um criterioso processo de identificação, tornando-o um documento eletrônico confiável.

 

**Artigos relacionados:**

[Certificado não possui cadeia de hierarquia CA.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043005313)

**Anexo**:


---

### 🔗 Links e Referências Internas:

- [Certificado não possui cadeia de hierarquia CA.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043005313)