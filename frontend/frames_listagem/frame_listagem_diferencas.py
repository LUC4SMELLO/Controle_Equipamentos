from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

def criar_frame_listagem_diferencas(janela_pai):

    def mostrar_listagem_diferencas_gui():
        pass

    frame_listagem_diferenças = tk.Frame(janela_pai, width=1300, height=400)

    label_diferencas = tk.Label(frame_listagem_diferenças, text="DIFERENÇAS", font=("Arial", 20, "bold"))
    label_diferencas.place(x=10, y=10)

    botao_listar_equipamentos = tk.Button(frame_listagem_diferenças, text="Listar", command=mostrar_listagem_diferencas_gui, font=("Arial", 15))
    botao_listar_equipamentos.place(x=10, y=305)

    return frame_listagem_diferenças


