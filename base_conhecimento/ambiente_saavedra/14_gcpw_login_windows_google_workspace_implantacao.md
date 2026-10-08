# 📋 Guia de Implantação de TI: Login Unificado no Windows com Google Workspace (GCPW)

> **Público:** Diretoria, Todos os Colaboradores e Suporte de TI  
> **Tecnologia:** Google Credential Provider for Windows (GCPW) e Chrome Enterprise  
> **Status:** Homologado e Operacional nos Notebooks Dell e Computadores da Empresa  

---

## 📌 1. O Problema (O que o usuário viu)

Anteriormente na Saavedra, cada colaborador precisava gerenciar múltiplos acessos e senhas diferentes para trabalhar:
1. Uma senha para ligar o computador ou notebook Dell (conta local do Windows);
2. Uma senha para acessar os arquivos do servidor de rede;
3. Outra senha para o e-mail corporativo no Google Workspace (`@saavedra.com.br`).

### Os Transtornos do Modelo Antigo:
* **Esquecimento Frequente de Senhas:** Colaboradores esqueciam a senha do Windows após férias ou finais de semana, exigindo intervenção presencial da TI para destravar a máquina.
* **Falta de Segurança e 2FA no Computador:** Se alguém descobrisse a senha do Windows da máquina, tinha acesso total aos arquivos, sem a proteção em duas etapas (2FA) que já existia no Google.
* **Dificuldade na Preparação de Novos Computadores:** Ao entregar um novo notebook Dell Inspiron 14 para um vendedor ou diretor, era necessário criar contas manuais, sem backup e sem gerenciamento centralizado pela nuvem.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

1. **O Desafio do Trabalho Híbrido e Móvel:**  
   Os computadores de mesa tradicionais ficavam presos dentro do escritório e usavam um servidor antigo local (Samba / CentOS) para validar senhas. Quando os diretores e representantes comerciais passaram a usar notebooks fora da empresa, esse servidor local não conseguia mais alcançar os computadores na rua ou no hospital.

2. **A Solução do Google (GCPW):**  
   O **GCPW (Google Credential Provider for Windows)** é uma tecnologia oficial do Google que conecta a tela de bloqueio do Windows 10/11 diretamente com o e-mail corporativo do Google Workspace. Em vez de inventar uma senha para o computador, o usuário passa a usar seu próprio e-mail e senha da Saavedra.

---

## ✅ 3. O que fizemos para implantar?

### Passo 1: Instalação do Google Chrome Enterprise
Para que o Windows consiga abrir a janela de autenticação segura do Google na tela de ligar a máquina, instalamos a versão corporativa do navegador:
* Pacote: `GoogleChromeEnterpriseBundle64.msi`.
* O navegador foi padronizado em todas as estações de trabalho e notebooks.

### Passo 2: Instalação do Provedor de Credenciais (GCPW)
Instalamos o componente do Google no Windows e registramos os módulos de segurança:
* Execução do instalador corporativo `gcpwsetup.exe`.
* Registro das bibliotecas do Windows via comando de sistema (`regsvr32 "C:\Program Files\Google\GCPW\Gaia1_0.dll"`).

### Passo 3: Configuração das Travas de Segurança no Registro do Windows
Para garantir que **apenas contas da empresa** possam acessar os computadores e bloquear qualquer uso indevido:
* **Domínios Autorizados (`domains_allowed_to_login`):** Travado estritamente para **`saavedra.com.br`**.  
  *(Isso impede terminantemente que qualquer pessoa faça login na máquina usando um e-mail pessoal `@gmail.com` ou de terceiros).*
* **Token de Gerenciamento (`CloudManagementEnrollmentToken`):** Inserção da chave criptográfica que vincula o notebook Dell ao painel do Google Admin da Saavedra.
* **Caminho do Navegador (`chrome_path`):** Apontamento fixo para o executável do Chrome Enterprise.

---

## 👤 4. Como o usuário utiliza no dia a dia?

### Ao Ligar o Computador ou Notebook:
1. Na tela de bloqueio do Windows, clique na opção **"Adicionar Conta de Trabalho"** ou **"Entrar com o Google"**.
2. Digite seu e-mail corporativo completo: `seu.nome@saavedra.com.br`.
3. Digite sua senha do Google Workspace.
4. **Verificação em Duas Etapas (2FA):** O seu celular receberá a notificação de segurança (confirmação de toque ou código de segurança do Google Authenticator).
5. O Windows carregará sua área de trabalho imediatamente.

### Se Você Trocar a Senha do E-mail:
* A senha do computador é atualizada **automaticamente**. Não é preciso pedir ajuda para a TI recriar usuário local.

### Para a TI e Diretoria:
* Se um notebook for perdido ou furtado, a TI consegue bloquear o computador ou apagar os dados remotamente com um único clique dentro do painel do Google Admin.

---

## 🔧 5. Detalhes Técnicos (Para TI e Suporte)

* **Caminho das Chaves de Registro (Windows Registry):**
  `HKEY_LOCAL_MACHINE\Software\Google\GCPW`
* **Parâmetros Configurados via PowerShell / Regedit:**
  | Chave (Valor) | Tipo | Dado Configurado | Função |
  | :--- | :--- | :--- | :--- |
  | `domains_allowed_to_login` | `REG_SZ` | `saavedra.com.br` | Restringe login a contas da organização |
  | `enable_dm_enrollment` | `REG_DWORD` | `0x00000001` (1) | Ativa o gerenciamento remoto do dispositivo |
  | `CloudManagementEnrollmentToken`| `REG_SZ` | `[Token Corporativo]` | Conecta o PC ao Google Admin Console |
  | `chrome_path` | `REG_SZ` | `C:\Program Files\Google\Chrome\Application\chrome.exe` | Caminho do navegador autenticador |

* **Script de Registro e Correção de DLLs (PowerShell como Admin):**
  ```powershell
  # Registro da DLL de autenticacao Gaia
  $dllPath = "C:\Program Files\Google\GCPW\Gaia1_0.dll"
  if (Test-Path $dllPath) {
      regsvr32.exe /s "$dllPath"
      Write-Host "DLL Gaia1_0 registrada com sucesso no Windows." -ForegroundColor Green
  }

  # Validacao das chaves do registro
  New-Item -Path "HKLM:\Software\Google" -Name "GCPW" -Force | Out-Null
  Set-ItemProperty -Path "HKLM:\Software\Google\GCPW" -Name "domains_allowed_to_login" -Value "saavedra.com.br"
  Set-ItemProperty -Path "HKLM:\Software\Google\GCPW" -Name "enable_dm_enrollment" -Value 1 -Type DWord
  ```
* **Resultado:** Padronização definitiva de segurança nos notebooks corporativos, autenticação de duplo fator no login da máquina e conformidade com as melhores práticas de LGPD e segurança da informação.
