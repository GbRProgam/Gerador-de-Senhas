import random
import string
import tkinter as tk
from tkinter import ttk

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_e_mostrar_senha():
    tamanho = int(tamanho_entry.get())
    senha_gerada = gerar_senha(tamanho)
    senha_label.config(text="Senha gerada: " + senha_gerada)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Configuração do frame
frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels
ttk.Label(frame, text="Tamanho da senha:").grid(column=0, row=0, sticky=tk.W)
senha_label = ttk.Label(frame, text="")
senha_label.grid(column=0, row=2, columnspan=2, sticky=tk.W)

# Entrada de texto
tamanho_entry = ttk.Entry(frame, width=10)
tamanho_entry.grid(column=0, row=1, sticky=tk.W)

# Botão
gerar_button = ttk.Button(frame, text="Gerar Senha", command=gerar_e_mostrar_senha)
gerar_button.grid(column=1, row=1, sticky=tk.W)

# Inicia a interface
root.mainloop()  
