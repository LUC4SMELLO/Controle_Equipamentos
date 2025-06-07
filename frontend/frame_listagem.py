from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from frontend.frame_listagem_equipamentos import criar_frame_listagem_equipamentos
from frontend.frame_listagem_responsaveis import criar_frame_listagem_reponsaveis

from frontend.janela import janela


def mostrar_frame_listagem(frame):
    frame_listagem_equipamentos.place_forget()
    frame_listagem_responsaveis.place_forget()

    frame.place(x=10, y=80)


frame_listagem_inicial = tk.Frame(janela, width=1200, height=800)

frame_listagem_equipamentos = criar_frame_listagem_equipamentos(frame_listagem_inicial)
frame_listagem_responsaveis = criar_frame_listagem_reponsaveis(frame_listagem_inicial)


label_listagem = tk.Label(frame_listagem_inicial, text="LISTAGEM", font=("Arial", 20, "bold"))
label_listagem.place(x=20, y=10)

botao_listagem_equipamentos = tk.Button(frame_listagem_inicial, text="Equipamentos", command=lambda: mostrar_frame_listagem(frame_listagem_equipamentos), font=("Arial", 15))
botao_listagem_equipamentos.place(x=200, y=10)

botao_listagem_responsaveis = tk.Button(frame_listagem_inicial, text="Responsáveis", command=lambda: mostrar_frame_listagem(frame_listagem_responsaveis), font=("Arial", 15))
botao_listagem_responsaveis.place(x=390, y=10)

botao_listagem_clientes = tk.Button(frame_listagem_inicial, text="Clientes", font=("Arial", 15))
botao_listagem_clientes.place(x=580, y=10)
