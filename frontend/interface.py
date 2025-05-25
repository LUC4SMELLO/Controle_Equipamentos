from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk


janela = tk.Tk()
janela.title("Controle de Equipamentos")
janela.geometry("1280x650")



# Criar o botão com imagem e texto
botao_cadastrar_equipamento = tk.Button(
    janela,
    text="Cadastrar Equipamento",
    font=("Arial", 10, "bold"),
    compound="top",
    height=5,
    width=50,
)
botao_cadastrar_equipamento.place(x=10, y=10)


janela.mainloop()
