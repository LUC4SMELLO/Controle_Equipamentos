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

def cadastrar_equipamento_gui():
    gesp = entry_gesp_cadastrar.get()
    codigo_modelo = entry_codigo_modelo_cadastrar.get()
    modelo = entry_modelo_cadastrar.get()

    valido, mensagem = validar_formulario_cadastro_equipamentos(gesp, codigo_modelo, modelo)

    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    messagebox.showinfo("Sucesso", "Equipamento Cadastrado!")

    cadastrar_equipamento_back(gesp, codigo_modelo, modelo)    

    limpar_entradas_cadastro_equipamento()


def limpar_entradas_cadastro_equipamento():
    entry_gesp_cadastrar.delete(0, tk.END)
    entry_codigo_modelo_cadastrar.delete(0, tk.END)
    entry_modelo_cadastrar.delete(0, tk.END)

# FRAME EQUIPAMENTOS
frame_cadastro_equipamentos = tk.Frame(janela, width=1300, height=350)

# CADASTRO DE EQUIPAMENTOS
label_alterar_equipamentos = tk.Label(frame_cadastro_equipamentos, text="CADASTRAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_alterar_equipamentos.place(x=5, y=10)

label_gesp_cadastrar = tk.Label(frame_cadastro_equipamentos, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_cadastrar.place(x=5, y=70)

entry_gesp_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_gesp_cadastrar.place(x=75, y=70)

label_codigo_modelo_cadastrar = tk.Label(frame_cadastro_equipamentos, text="COD MODELO:", font=("Arial", 15, "bold"))
label_codigo_modelo_cadastrar.place(x=5, y=110)

entry_codigo_modelo_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_codigo_modelo_cadastrar.place(x=160, y=110)

label_modelo_cadastrar = tk.Label(frame_cadastro_equipamentos, text="MODELO:", font=("Arial", 15, "bold"))
label_modelo_cadastrar.place(x=5, y=150)

entry_modelo_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_modelo_cadastrar.place(x=110, y=150)

botao_cadastrar_equipamento = tk.Button(frame_cadastro_equipamentos, text="Cadastrar", command=cadastrar_equipamento_gui, font=("Arial", 15))
botao_cadastrar_equipamento.place(x=5, y=210)

botao_cancelar_cadastro = tk.Button(frame_cadastro_equipamentos, text="Cancelar", command=limpar_entradas_cadastro_equipamento, font=("Arial", 15))
botao_cancelar_cadastro.place(x=270, y=210)

gesp = tk.StringVar()
codigo_modelo = tk.StringVar()
modelo = tk.StringVar()


def buscar_equipamento_gui():

    gesp = entry_gesp_alterar.get()
    codigo_modelo = entry_codigo_modelo_alterar.get()
    modelo = entry_modelo_alterar.get()

    if not gesp:
        messagebox.showerror("Erro", "Preencha o GESP.")
        return None

    valido, mensagem = equipamento_existe_emprestrar(gesp)
    if not valido:
        messagebox.showerror(valido, mensagem)
        return None

    entry_codigo_modelo_alterar.delete(0, tk.END)
    entry_modelo_alterar.delete(0, tk.END)

    dados_equipamentos = buscar_e_retornar_equipamento(gesp)

    gesp = dados_equipamentos[0][0]
    codigo_modelo = dados_equipamentos[0][1]
    modelo = dados_equipamentos[0][2]

    entry_codigo_modelo_alterar.insert(0, codigo_modelo)
    entry_modelo_alterar.insert(0, modelo)
    

def alterar_informacoes_equipamento_gui():
    gesp = entry_gesp_alterar.get()
    codigo_modelo = entry_codigo_modelo_alterar.get()
    modelo = entry_modelo_alterar.get()

    valido, mensagem = validar_formulario_alterar_equipamento(gesp, codigo_modelo, modelo)
    if not valido:
       messagebox.showerror("Erro", mensagem)
       return None

    messagebox.showinfo("Sucesso", "Informações Alteradas!")

    alterar_informacoes_equipamento_back(gesp, codigo_modelo, modelo)

    limpar_entradas_alterar_equipamento()

def limpar_entradas_alterar_equipamento():
    entry_gesp_alterar.delete(0, tk.END)
    entry_codigo_modelo_alterar.delete(0, tk.END)
    entry_modelo_alterar.delete(0, tk.END)
    

# ALTERAR EQUIPAMENTO
label_alterar_equipamentos = tk.Label(frame_cadastro_equipamentos, text="ALTERAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_alterar_equipamentos.place(x=445, y=10)

divisor = tk.LabelFrame(frame_cadastro_equipamentos, border=False, background="silver", width=5, height=300)
divisor.place(x=413, y=10)

botao_buscar_equipamento = tk.Button(frame_cadastro_equipamentos, text="Buscar", command=buscar_equipamento_gui, font=("Arial", 10, "bold"))
botao_buscar_equipamento.place(x=670, y=68)

label_gesp_alterar = tk.Label(frame_cadastro_equipamentos, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_alterar.place(x=450, y=70)

entry_gesp_alterar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_gesp_alterar.place(x=520, y=70)

label_codigo_modelo_alterar = tk.Label(frame_cadastro_equipamentos, text="COD MODELO:", font=("Arial", 15, "bold"))
label_codigo_modelo_alterar.place(x=450, y=110)

entry_codigo_modelo_alterar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_codigo_modelo_alterar.place(x=605, y=110)

label_modelo_alterar = tk.Label(frame_cadastro_equipamentos, text="MODELO:", font=("Arial", 15, "bold"))
label_modelo_alterar.place(x=450, y=150)

entry_modelo_alterar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_modelo_alterar.place(x=555, y=150)

botao_alterar_equipamento = tk.Button(frame_cadastro_equipamentos, text="Alterar", command=alterar_informacoes_equipamento_gui, font=("Arial", 15))
botao_alterar_equipamento.place(x=450, y=210)

botao_cancelar_alteracoes_equipamento = tk.Button(frame_cadastro_equipamentos, text="Cancelar", command=limpar_entradas_alterar_equipamento, font=("Arial", 15))
botao_cancelar_alteracoes_equipamento.place(x=715, y=210)

def excluir_equipamento_gui():
    gesp = entry_gesp_excluir.get()
    codigo_modelo = entry_codigo_modelo_excluir.get()
    modelo = entry_modelo_excluir.get()

    valido, mensagem = validar_formulario_excluir_equipamentos(gesp, modelo, modelo)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    valido, mensagem = equipamento_existe_excluir(gesp, codigo_modelo, modelo)
    if not valido:
        limpar_entradas_excluir_equipamento()
        messagebox.showerror("Erro", mensagem)
        return None

    messagebox.showinfo("Sucesso", "Equipamento Excluído")

    excluir_equipamento_back(gesp, codigo_modelo, modelo)

    limpar_entradas_excluir_equipamento()

    
def limpar_entradas_excluir_equipamento():
    entry_gesp_excluir.delete(0, tk.END)
    entry_codigo_modelo_excluir.delete(0, tk.END)
    entry_modelo_excluir.delete(0, tk.END)

    

# EXCLUIR EQUIPAMENTO
label_excluir_equipamento = tk.Label(frame_cadastro_equipamentos, text="EXCLUIR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_excluir_equipamento.place(x=865, y=10)

divisor = tk.LabelFrame(frame_cadastro_equipamentos, border=False, background="silver", width=5, height=300)
divisor.place(x=833, y=10)

label_gesp_excluir = tk.Label(frame_cadastro_equipamentos, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_excluir.place(x=870, y=70)

entry_gesp_excluir = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_gesp_excluir.place(x=940, y=70)

label_codigo_modelo_excluir = tk.Label(frame_cadastro_equipamentos, text="COD MODELO:", font=("Arial", 15, "bold"))
label_codigo_modelo_excluir.place(x=870, y=110)

entry_codigo_modelo_excluir = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_codigo_modelo_excluir.place(x=1025, y=110)

label_modelo_excluir = tk.Label(frame_cadastro_equipamentos, text="MODELO:", font=("Arial", 15, "bold"))
label_modelo_excluir.place(x=870, y=150)

entry_modelo_excluir = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_modelo_excluir.place(x=975, y=150)

botao_excluir_equipamento = tk.Button(frame_cadastro_equipamentos, text="Excluir", command=excluir_equipamento_gui, font=("Arial", 15))
botao_excluir_equipamento.place(x=870, y=210)

botao_cancelar_exclusao_equipamento = tk.Button(frame_cadastro_equipamentos, text="Cancelar", command=limpar_entradas_excluir_equipamento, font=("Arial", 15))
botao_cancelar_exclusao_equipamento.place(x=1135, y=210)
