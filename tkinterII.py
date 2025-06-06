import tkinter as tk
from tkinter import messagebox

def verificar_login():
    email = entry_email.get()
    senha = entry_senha.get()
    
    if len(senha) <= 6:
        messagebox.showerror("Erro de Login", "A senha deve ter mais de 6 dígitos.")
    elif "@" not in email:
        messagebox.showerror("Erro de Login", "O e-mail deve conter o caractere '@'.")
    else:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")


root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x200")


label_email = tk.Label(root, text="E-mail:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)


label_senha = tk.Label(root, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)


button_login = tk.Button(root, text="Login", command=verificar_login)
button_login.pack(pady=20)

root.mainloop()
