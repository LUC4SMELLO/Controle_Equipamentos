from tkinter import *
import sys
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

import sys
import os

# Adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from frames import (
    janela,
    mostrar_frame, 
    frame_cadastro_equipamentos,
    frame_cadastro_responsavel,
    frame_emprestar_equipamento,
    frame_devolver_equipamento,
    frame_dar_baixa_equipamento,
    frame_listagem
    )


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
    command= lambda: mostrar_frame(frame_cadastro_responsavel),
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_cadastrar_responsavel.place(x=220, y=10)


botao_emprestar_equipamento = tk.Button(
    janela,
    text="Emprestar Equipamento",
    command= lambda: mostrar_frame(frame_emprestar_equipamento),
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_emprestar_equipamento.place(x=430, y=10)


botao_devolver_equipamento = tk.Button(
    janela,
    text="Devolver Equipamento",
    command= lambda: mostrar_frame(frame_devolver_equipamento),
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_devolver_equipamento.place(x=640, y=10)


botao_dar_baixa_equipamento = tk.Button(
    janela,
    text="Dar Baixa Equipamento",
    command= lambda: mostrar_frame(frame_dar_baixa_equipamento),
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_dar_baixa_equipamento.place(x=850, y=10)


botao_listagem = tk.Button(
    janela,
    text="Listagem",
    command= lambda: mostrar_frame(frame_listagem),
    font=("Arial", 12, "bold"),
    compound="top",
    height=5,
    width=19,
)
botao_listagem.place(x=1060, y=10)


janela.mainloop()
