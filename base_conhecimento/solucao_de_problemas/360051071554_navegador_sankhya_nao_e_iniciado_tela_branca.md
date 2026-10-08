# Navegador Sankhya não é iniciado - Tela "branca"

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360051071554-Navegador-Sankhya-n%C3%A3o-%C3%A9-iniciado-Tela-branca](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051071554-Navegador-Sankhya-n%C3%A3o-%C3%A9-iniciado-Tela-branca)  
> **ID:** `360051071554` | **Última Atualização:** 2026-07-22T15:30:15Z

---

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584750122519)

 CAUSA:**

Quando possuir Sistema Operacional Windows 7, ao atualizar o Navegador Sankhya, o mesmo pode apresentar tela em branco. A causa desse erro pode estar relacionado ao hardware (ex:placa gráfica da máquina).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584782550551)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584782557335)

 Executar o Navegador Sankhya através do 'Windows PowerShell', conforme .gif abaixo:

![Gif_3.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360079594014)

Verificar se foi apresentado erro, conforme imagem abaixo:

![300.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/360079594054)

Nesse caso, uma forma de corrigir o problema será:

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584750147991)

 Localizar o atalho do Navegador Sankhya e com o botão direito, localizar a opção 'Propriedades >> **Destino', ** adicionar a informação abaixo:

** --disable-gpu**

** Exemplo: "C:\SANKHYA\Navegador Sankhya\NavegadorSankhya.exe" --disable-gpu **

Veja em detalhes:

![Gif_4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360079594234)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584750153111)

 Feito isso, tente abrir o navegador novamente.