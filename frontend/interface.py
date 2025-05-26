from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

from frames import frame_cadastro_equipamentos, frame_outros, janela


def mostrar_frame(frame):
    # Oculta todos os frames
    frame_cadastro_equipamentos.place_forget()
    frame_outros.place_forget()
    
    # Mostra apenas o frame desejado
    frame.place(x=10, y=150)


# Criar o botão com imagem e texto
botao_cadastrar_equipamento = tk.Button(
    janela,
    text="Cadastrar Equipamento",
    command= lambda: mostrar_frame(frame_cadastro_equipamentos),
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_cadastrar_equipamento.place(x=10, y=10)

botao_cadastrar_responsavel = tk.Button(
    janela,
    text="Cadastrar Responsável",
    command= lambda: mostrar_frame(frame_outros),
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
