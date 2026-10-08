# Foi detectado um conteúdo inválido começando com o elemento 'parteAtingida'

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10759158341143-Foi-detectado-um-conte%C3%BAdo-inv%C3%A1lido-come%C3%A7ando-com-o-elemento-parteAtingida](https://ajuda.sankhya.com.br/hc/pt-br/articles/10759158341143-Foi-detectado-um-conte%C3%BAdo-inv%C3%A1lido-come%C3%A7ando-com-o-elemento-parteAtingida)  
> **ID:** `10759158341143` | **Última Atualização:** 2026-07-29T13:16:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19066995533975)

 MENSAGEM:**

cvc-complex-type.2.4.a: Foi detectado um conteúdo inválido começando com o elemento 'parte Atingida'.

Era esperado um dos'{"http://www.esocial.gov.br/schema/evt/evtCAT/v_S_01_00_00":agenteCausador}'.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19066995538839)

 SITUAÇÃO:**

Ao enviar registro CAT no e-Social  S-2210 a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19066995542039)

 CAUSA:**

Ocorre quando o campo 'Partes do corpo Atingidas' tem mais de uma parte lançada no cadastro da CAT.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19066995550487)

 SOLUÇÃO:**

No campo 'Partes do corpo Atingidas', preencha o grupo {parteAtingida} utilizando apenas um código da tabela **“Tabela 13 - Parte do corpo atingida. **Haja vista que há a previsão de códigos específicos para as situações em que mais de uma parte do corpo é atingida no acidente.

Deve ser especificado o lado atingido (direito ou esquerdo), quando se tratar de parte do corpo
que seja bilateral ou, se atingido ambos os lados, indicar como bilateral. Se o órgão atingido é único
(como, por exemplo, a cabeça), assinalar este campo como não aplicável.

Essa orientação está em conformidade com o manual e layout do e-social.