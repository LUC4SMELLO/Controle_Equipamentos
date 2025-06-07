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

def mostrar_frame_listagem(frame):
    frame_listagem_equipamentos.place_forget()
    frame_listagem_responsaveis.place_forget()

    frame.place(x=10, y=80)


frame_listagem_inicial = tk.Frame(janela, width=1200, height=800)

label_listagem = tk.Label(frame_listagem_inicial, text="LISTAGEM", font=("Arial", 20, "bold"))
label_listagem.place(x=20, y=10)

botao_listagem_equipamentos = tk.Button(frame_listagem_inicial, text="Equipamentos", command=lambda: mostrar_frame_listagem(frame_listagem_equipamentos), font=("Arial", 15))
botao_listagem_equipamentos.place(x=200, y=10)

botao_listagem_responsaveis = tk.Button(frame_listagem_inicial, text="Responsáveis", command=lambda: mostrar_frame_listagem(frame_listagem_responsaveis), font=("Arial", 15))
botao_listagem_responsaveis.place(x=390, y=10)

botao_listagem_clientes = tk.Button(frame_listagem_inicial, text="Clientes", font=("Arial", 15))
botao_listagem_clientes.place(x=580, y=10)





def mostrar_listagem_equipamentos_gui():

    gesp = entry_gesp_listagem.get().strip()
    modelo = entry_modelo_listagem.get().strip()

    status = []
    if var_emprestado.get():
        status.append("EMPRESTADO")
    if var_disponivel.get():
        status.append("DISPONÍVEL")
    if var_baixado.get():
        status.append("BAIXADO")
    if var_todos.get():
        status = ["TODOS"]  

    resultados = mostrar_listagem_equipamentos_back(modelo, status, gesp)

    
    for item in tree_equipamentos.get_children():
        tree_equipamentos.delete(item)

    for linha in resultados:
        tree_equipamentos.insert("", "end", values=linha)


# FRAME LISTAGEM EQUIPAMENTOS
frame_listagem_equipamentos = tk.Frame(frame_listagem_inicial, width=800, height=350)

label_equipamentos = tk.Label(frame_listagem_equipamentos, text="EQUIPAMENTOS", font=("Arial", 20, "bold"))
label_equipamentos.place(x=10, y=10)

label_gesp = tk.Label(frame_listagem_equipamentos, text="GESP:", font=("Arial", 15, "bold"))
label_gesp.place(x=10, y=70)

entry_gesp_listagem = tk.Entry(frame_listagem_equipamentos, font=("Arial", 15), width=12)
entry_gesp_listagem.place(x=80, y=70)

label_modelo = tk.Label(frame_listagem_equipamentos, text="MODELO:", font=("Arial", 15, "bold"))
label_modelo.place(x=10, y=105)

entry_modelo_listagem = tk.Entry(frame_listagem_equipamentos, font=("Arial", 15), width=9)
entry_modelo_listagem.place(x=115, y=105)

label_listar_apenas = tk.Label(frame_listagem_equipamentos, text="LISTAR APENAS:", font=("Arial", 15, "bold"))
label_listar_apenas.place(x=10, y=145)

var_emprestado = tk.BooleanVar()
var_disponivel = tk.BooleanVar()
var_baixado = tk.BooleanVar()
var_todos = tk.BooleanVar()

# CHECK BUTTONS
check_emprestado = tk.Checkbutton(frame_listagem_equipamentos, text="Emprestado", font=("Arial", 12, "bold"), variable=var_emprestado)
check_emprestado.place(x=10, y=175)

check_disponivel = tk.Checkbutton(frame_listagem_equipamentos, text="Disponível", font=("Arial", 12, "bold"), variable=var_disponivel)
check_disponivel.place(x=10, y=200)

check_baixado = tk.Checkbutton(frame_listagem_equipamentos, text="Baixado", font=("Arial", 12, "bold"), variable=var_baixado)
check_baixado.place(x=10, y=225)

check_todos = tk.Checkbutton(frame_listagem_equipamentos, text="Todos", font=("Arial", 12, "bold"), variable=var_todos)
check_todos.place(x=10, y=250)



# CRIA A BARRA DE SCROLL EQUIPAMENTOS
scrollbar_vertical_equipamentos = ttk.Scrollbar(frame_listagem_equipamentos, orient="vertical")
scrollbar_vertical_equipamentos.place(x=770, y=70, height=270)



# region TREEVIEW EQUIPAMENTOS
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

colunas = ("gesp", "codigo_modelo", "modelo", "status")
tree_equipamentos = ttk.Treeview(
    frame_listagem_equipamentos,
    columns=colunas,
    show="headings",
    height=12,
    yscrollcommand=scrollbar_vertical_equipamentos.set
)
tree_equipamentos.place(x=250, y=70, width=520, height=270)

scrollbar_vertical_equipamentos.config(command=tree_equipamentos.yview)

tree_equipamentos.heading("gesp", text="GESP", anchor="center")
tree_equipamentos.heading("codigo_modelo", text="CÓDIGO MODELO", anchor="center")
tree_equipamentos.heading("modelo", text="MODELO", anchor="center")
tree_equipamentos.heading("status", text="STATUS", anchor="center")

tree_equipamentos.column("gesp", width=120, anchor="center")
tree_equipamentos.column("codigo_modelo", width=160, anchor="center")
tree_equipamentos.column("modelo", width=110, anchor="center")
tree_equipamentos.column("status", width=120, anchor="center")
# endregion

botao_listar_equipamentos = tk.Button(frame_listagem_equipamentos, text="Listar", command=mostrar_listagem_equipamentos_gui, font=("Arial", 15))
botao_listar_equipamentos.place(x=10, y=305)






def mostrar_listagem_responsaveis_gui():

    codigo_cliente = entry_codigo_cliente_listagem.get().strip()
    nome = entry_nome_listagem.get().strip()
    cpf = entry_cpf_listagem.get().strip()
    email = entry_email_listagem.get().strip()

    resultados = mostrar_listagem_responsaveis_back(
        codigo_cliente, nome, cpf, email
        )

    
    for item in tree_responsaveis.get_children():
        tree_responsaveis.delete(item)

    for linha in resultados:
        tree_responsaveis.insert("", "end", values=linha)


# FRAME LISTAGEM RESPONSÁVEIS
frame_listagem_responsaveis = tk.Frame(frame_listagem_inicial, width=1200, height=350)

label_responsaveis = tk.Label(frame_listagem_responsaveis, text="RESPONSÁVEIS", font=("Arial", 20, "bold"))
label_responsaveis.place(x=10, y=10)

label_codigo_cliente = tk.Label(frame_listagem_responsaveis, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
label_codigo_cliente.place(x=10, y=70)

entry_codigo_cliente_listagem = tk.Entry(frame_listagem_responsaveis, font=("Arial", 15), width=15)
entry_codigo_cliente_listagem.place(x=200, y=70)

label_nome = tk.Label(frame_listagem_responsaveis, text="NOME:", font=("Arial", 15, "bold"))
label_nome.place(x=10, y=110)

entry_nome_listagem = tk.Entry(frame_listagem_responsaveis, font=("Arial", 15), width=25)
entry_nome_listagem.place(x=90, y=110)

label_cpf_listagem = tk.Label(frame_listagem_responsaveis, text="CPF:", font=("Arial", 15, "bold"))
label_cpf_listagem.place(x=10, y=150)

entry_cpf_listagem = tk.Entry(frame_listagem_responsaveis, font=("Arial", 15), width=25)
entry_cpf_listagem.place(x=90, y=150)

label_email_listagem = tk.Label(frame_listagem_responsaveis, text="E-MAIL:", font=("Arial", 15, "bold"))
label_email_listagem.place(x=10, y=190)

entry_email_listagem = tk.Entry(frame_listagem_responsaveis, font=("Arial", 15), width=25)
entry_email_listagem.place(x=90, y=190)

# CRIA A BARRA DE SCROLL RESPONSÁVEIS
scrollbar_vertical_responsaveis = ttk.Scrollbar(frame_listagem_responsaveis, orient="vertical")
scrollbar_vertical_responsaveis.place(x=1150, y=70, height=270)

style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

colunas = ("codigo_cliente", "nome", "cpf", "email")
tree_responsaveis = ttk.Treeview(
    frame_listagem_responsaveis,
    columns=colunas,
    show="headings",
    height=12,
    yscrollcommand=scrollbar_vertical_responsaveis.set
)
tree_responsaveis.place(x=400, y=70, width=750, height=270)

scrollbar_vertical_responsaveis.config(command=tree_responsaveis.yview)

tree_responsaveis.heading("codigo_cliente", text="CÓDIGO CLIENTE", anchor="center")
tree_responsaveis.heading("nome", text="NOME", anchor="center")
tree_responsaveis.heading("cpf", text="CPF", anchor="center")
tree_responsaveis.heading("email", text="E-MAIL", anchor="center")

tree_responsaveis.column("codigo_cliente", width=140, anchor="center")
tree_responsaveis.column("nome", width=200, anchor="center")
tree_responsaveis.column("cpf", width=100, anchor="center")
tree_responsaveis.column("email", width=200, anchor="center")


botao_listar_responsaveis = tk.Button(frame_listagem_responsaveis, text="Listar", command=mostrar_listagem_responsaveis_gui, font=("Arial", 15))
botao_listar_responsaveis.place(x=10, y=305)