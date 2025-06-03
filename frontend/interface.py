import sys
import os

from tkinter import *
import tkinter as tk


# Adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.frame_equipamentos import frame_cadastro_equipamentos
from frontend.frame_responsavel import frame_cadastro_responsavel
from frontend.frame_emprestar import frame_emprestar_equipamento
from frontend.frame_devolver import frame_devolver_equipamento
from frontend.frame_baixa import frame_dar_baixa_equipamento
from frontend.frame_listagem import frame_listagem

from frontend.janela import janela
def mostrar_frame(frame):
    frame_cadastro_equipamentos.place_forget()
    frame_cadastro_responsavel.place_forget()
    frame_emprestar_equipamento.place_forget()
    frame_devolver_equipamento.place_forget()
    frame_dar_baixa_equipamento.place_forget()
    frame_listagem.place_forget()
    
    frame.place(x=10, y=150)

def iniciar_interface():
    botao_cadastrar_equipamento = tk.Button(
        janela,
        text="Equipamento",
        command= lambda: mostrar_frame(frame_cadastro_equipamentos),
        font=("Arial", 12, "bold"),
        compound="top",
        height=5,
        width=19,
    )
    botao_cadastrar_equipamento.place(x=10, y=10)


    botao_cadastrar_responsavel = tk.Button(
        janela,
        text="Responsável",
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
