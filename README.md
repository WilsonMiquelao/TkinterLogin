# Tela de Login com Validação (Tkinter)

Aplicação simples desenvolvida em Python utilizando a biblioteca `tkinter` para criar uma interface gráfica de login com validações básicas de e-mail e senha.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: biblioteca GUI nativa do Python
- **Messagebox**: para exibição de mensagens de erro e sucesso

---

## 📋 Funcionalidades

- ✅ Interface gráfica amigável
- ✅ Campo para digitar e-mail
- ✅ Campo para digitar senha (ocultada)
- ✅ Botão de login com validações:
  - E-mail deve conter `@`
  - Senha deve ter mais de 6 caracteres

---

## 🧠 Lógica de Funcionamento

- A função `verificar_login()` é executada ao clicar no botão **Login**
- Valida se:
  - O e-mail contém o caractere `@`
  - A senha tem mais de 6 caracteres
- Exibe uma `messagebox` com erro ou sucesso

---

## 💡 Exemplo de Uso

1. Usuário digita:  
   - **E-mail**: `usuario@gmail.com`  
   - **Senha**: `1234567`

2. Clica em **Login**

3. Resultado:  
   - Mensagem de sucesso: `Login realizado com sucesso!`

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/tela-login-tkinter.git
   cd tela-login-tkinter
