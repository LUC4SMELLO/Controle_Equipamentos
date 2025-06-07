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

def devolver_equipamento_gui():
    gesp = entry_gesp_a_devolver.get()
    codigo_cliente = entry_codigo_cliente_devolver.get()
    modelo = entry_modelo_devolver.get()
    
    valido, mensagem = validar_formulario_devolver(codigo_cliente, gesp, modelo)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    valido, mensagem = cliente_existe(codigo_cliente)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        limpar_entrada_devolver_equipamentos()
        return None
    
    valido, mensagem = equipamento_existe(gesp)
    if valido:
        messagebox.showerror("Erro", mensagem)
        limpar_entrada_devolver_equipamentos()
        return None

    valido, mensagem = equipamento_emprestado(gesp, codigo_cliente)    
    if not valido:
        messagebox.showerror("Erro", mensagem)
        limpar_entrada_devolver_equipamentos()
        return None
    
    messagebox.showinfo("Sucesso!", "Equipamento Devolvido!")

    devolver_equipamento_back(gesp, codigo_cliente)

    limpar_entrada_devolver_equipamentos()

    
def limpar_entrada_devolver_equipamentos():
    entry_gesp_a_devolver.delete(0, tk.END)
    entry_codigo_cliente_devolver.delete(0, tk.END)
    entry_modelo_devolver.delete(0, tk.END)

# FRAME DEVOLVER EQUIPAMENTO
frame_devolver_equipamento = tk.Frame(janela, width=400, height=350)

label_devolver_equipamento = tk.Label(frame_devolver_equipamento, text="DEVOLVER EQUIPAMENTO", font=("Arial", 20, "bold"))
label_devolver_equipamento.place(x=10, y=10)

label_codigo_cliente = tk.Label(frame_devolver_equipamento, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
label_codigo_cliente .place(x=10, y=70)

entry_codigo_cliente_devolver = tk.Entry(frame_devolver_equipamento, font=("Arial", 15), width=10)
entry_codigo_cliente_devolver.place(x=195, y=70)

label_gesp_a_devolver = tk.Label(frame_devolver_equipamento, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_a_devolver.place(x=10, y=110)

entry_gesp_a_devolver = tk.Entry(frame_devolver_equipamento, font=("Arial", 15), width=12)
entry_gesp_a_devolver.place(x=80, y=110)

label_modelo_devolver = tk.Label(frame_devolver_equipamento, text="COD MODELO:", font=("Arial", 15, "bold"))
label_modelo_devolver.place(x=10, y=150)

entry_modelo_devolver = tk.Entry(frame_devolver_equipamento, font=("Arial", 15), width=12)
entry_modelo_devolver.place(x=165, y=150)

botao_devolver_equipamento = tk.Button(frame_devolver_equipamento, text="Devolver", command=devolver_equipamento_gui,font=("Arial", 15))
botao_devolver_equipamento.place(x=10, y=210)

botao_cancelar_devolucao_equipamento = tk.Button(frame_devolver_equipamento, text="Cancelar", command=limpar_entrada_devolver_equipamentos, font=("Arial", 15))
botao_cancelar_devolucao_equipamento.place(x=300, y=210)