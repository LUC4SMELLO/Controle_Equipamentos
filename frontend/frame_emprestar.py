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

def emprestrar_equipamento_gui():
    codigo_cliente = entry_codigo_cliente_emprestrar.get()
    gesp = entry_gesp_emprestar.get()
    contrato = entry_contrato_emprestrar.get()


    valido, mensagem = validar_formulario_emprestimo(codigo_cliente, gesp, contrato)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None

    valido, mensagem = cliente_existe(codigo_cliente)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    valido, mensagem = responsavel_existe(codigo_cliente)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    valido, mensagem = equipamento_existe(gesp)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    valido, mensagem = equipamento_disponivel(gesp)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None

    messagebox.showinfo("Sucesso", "Equipamento Emprestado!")

    emprestar_equipamento_back(gesp, codigo_cliente, contrato)

    entry_codigo_cliente_emprestrar.delete(0, tk.END)
    entry_gesp_emprestar.delete(0, tk.END)
    entry_contrato_emprestrar.delete(0, tk.END)

# FRAME EMPRESTAR EQUIPAMENTO
frame_emprestar_equipamento = tk.Frame(janela, width=400, height=350)

label_emprestar_equipamento = tk.Label(frame_emprestar_equipamento, text="EMPRESTAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_emprestar_equipamento.place(x=10, y=10)

label_codigo_cliente_emprestrar = tk.Label(frame_emprestar_equipamento, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
label_codigo_cliente_emprestrar.place(x=10, y=70)

entry_codigo_cliente_emprestrar = tk.Entry(frame_emprestar_equipamento, font=("Arial", 15), width=10)
entry_codigo_cliente_emprestrar.place(x=195, y=70)

label_gesp_emprestar = tk.Label(frame_emprestar_equipamento, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_emprestar.place(x=10, y=110)

entry_gesp_emprestar = tk.Entry(frame_emprestar_equipamento, font=("Arial", 15), width=12)
entry_gesp_emprestar.place(x=80, y=110)

label_contrato_emprestrar = tk.Label(frame_emprestar_equipamento, text="CONTRATO:", font=("Arial", 15, "bold"))
label_contrato_emprestrar.place(x=10, y=150)

entry_contrato_emprestrar = tk.Entry(frame_emprestar_equipamento, font=("Arial", 15), width=7)
entry_contrato_emprestrar.place(x=140, y=150)

botao_emprestrar_equipamento_emprestrar = tk.Button(frame_emprestar_equipamento, text="Emprestrar", command=emprestrar_equipamento_gui, font=("Arial", 15))
botao_emprestrar_equipamento_emprestrar.place(x=10, y=210)
