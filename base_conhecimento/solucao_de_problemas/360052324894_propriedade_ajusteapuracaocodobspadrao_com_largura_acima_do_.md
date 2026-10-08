# Propriedade 'AjusteApuracao.CODOBSPADRAO' com largura acima do limite: (x > 5)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360052324894-Propriedade-AjusteApuracao-CODOBSPADRAO-com-largura-acima-do-limite-x-5](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052324894-Propriedade-AjusteApuracao-CODOBSPADRAO-com-largura-acima-do-limite-x-5)  
> **ID:** `360052324894` | **Última Atualização:** 2026-07-22T15:29:18Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18587059984151)

 MENSAGEM**:

Propriedade 'AjusteApuracao.CODOBSPADRAO' com largura acima do limite: (x > 5).

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18587023651095)

 CAUSA:**

Ocorre quando ao clicar sobre o botão "Gerar Dif.Alíq.ICMS em Outros Déb/Créd*"* na tela **Registro de Apuração do ICMS** *(Livros Fiscais » Relatórios » Registro de Apuração do ICMS)*,* *com o campo "*Dif.ICMS na observação, sem afetar Débito/Crédito*" marcado, e o parâmetro **Código da Observação para Diferença de ICMS- ****CODOBSDIFICMS ** tiver informado um código de observação com mais de 5 dígitos.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18587059994775)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18587023659159)

 Acesse a tela 'Preferências' (Configurações » Avançado » Preferências)
Procure pelo parâmetro: **CODOBSDIFICMS **

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18587060003735)

 Informe no campo "Inteiro" do parâmetro** **o código da observação cadastrada na tela **Observações para Notas (Comercial » Arquivo » Cadastros » Observações para Notas)**, onde este código não pode conter mais do que 5 dígitos.

![codobs.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360086936894)