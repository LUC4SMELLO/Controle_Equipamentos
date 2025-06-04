from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.controlador_equipamentos import *
from backend.controlador_responsaveis import *
from backend.validadores.equipamento import *
from backend.validadores.responsaveis import *
from backend.controlador_listagem import *
from servicos.servico_equipamentos import *
from servicos.servico_responsaveis import *
from servicos.servico_clientes import *

from frontend.janela import janela

def dar_baixa_equipamento_gui():
    gesp = entry_gesp_a_dar_baixa.get()

    validado, mensagem = validar_formulario_dar_baixa(gesp)
    if not validado:
        messagebox.showerror("Erro", mensagem)
        return None
    
    validado, mensagem = equipamento_baixado(gesp)
    if validado:
        messagebox.showerror("Erro", mensagem)
        return None

    validado, mensagem = equipamento_existe(gesp)
    if not validado:
        messagebox.showerror("Erro", mensagem)
        return None

    messagebox.showinfo("Sucesso", "Equipamento Baixado!")

    dar_baixa_equipamento_back(gesp)

    entry_gesp_a_dar_baixa.delete(0, tk.END)

# FRAME DAR BAIXA EQUIPAMENTO 
frame_dar_baixa_equipamento = tk.Frame(janela, width=400, height=350)

label_dar_baixa_equipamento = tk.Label(frame_dar_baixa_equipamento, text="DAR BAIXA EQUIPAMENTO", font=("Arial", 20, "bold"))
label_dar_baixa_equipamento.place(x=10, y=10)

label_gesp_a_dar_baixa = tk.Label(frame_dar_baixa_equipamento, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_a_dar_baixa.place(x=10, y=70)

entry_gesp_a_dar_baixa = tk.Entry(frame_dar_baixa_equipamento, font=("Arial", 15), width=12)
entry_gesp_a_dar_baixa.place(x=80, y=70)

botao_dar_baixa = tk.Button(frame_dar_baixa_equipamento, text="Dar Baixa", command=dar_baixa_equipamento_gui, font=("Arial", 15))
botao_dar_baixa.place(x=10, y=210)