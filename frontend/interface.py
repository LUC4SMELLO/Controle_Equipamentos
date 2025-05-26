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
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_cadastrar_equipamento.place(x=10, y=10)

botao_cadastrar_responsavel = tk.Button(
    janela,
    text="Cadastrar Responsável",
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_cadastrar_responsavel.place(x=220, y=10)

botao_emprestar_equipamento = tk.Button(
    janela,
    text="Emprestar Equipamento",
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_emprestar_equipamento.place(x=430, y=10)

botao_devolver_equipamento = tk.Button(
    janela,
    text="Devolver Equipamento",
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_devolver_equipamento.place(x=640, y=10)

botao_dar_baixa_equipamento = tk.Button(
    janela,
    text="Dar Baixa Equipamento",
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_dar_baixa_equipamento.place(x=850, y=10)

botao_dar_baixa_equipamento = tk.Button(
    janela,
    text="Listagem",
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_dar_baixa_equipamento.place(x=1060, y=10)

janela.mainloop()
