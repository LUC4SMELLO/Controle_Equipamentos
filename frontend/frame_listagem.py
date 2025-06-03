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

def mostrar_listagem_gui():

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

    resultados = mostrar_listagem_back(modelo, status, gesp)

    
    for item in tree.get_children():
        tree.delete(item)

    for linha in resultados:
        tree.insert("", "end", values=linha)


# FRAME LISTAGEM
frame_listagem = tk.Frame(janela, width=800, height=350)

label_listagem = tk.Label(frame_listagem, text="LISTAGEM", font=("Arial", 20, "bold"))
label_listagem.place(x=10, y=10)

label_gesp = tk.Label(frame_listagem, text="GESP:", font=("Arial", 15, "bold"))
label_gesp.place(x=10, y=70)

entry_gesp_listagem = tk.Entry(frame_listagem, font=("Arial", 15), width=12)
entry_gesp_listagem.place(x=80, y=70)

label_modelo = tk.Label(frame_listagem, text="MODELO:", font=("Arial", 15, "bold"))
label_modelo.place(x=10, y=105)

entry_modelo_listagem = tk.Entry(frame_listagem, font=("Arial", 15), width=9)
entry_modelo_listagem.place(x=115, y=105)

label_listar_apenas = tk.Label(frame_listagem, text="LISTAR APENAS:", font=("Arial", 15, "bold"))
label_listar_apenas.place(x=10, y=145)

var_emprestado = tk.BooleanVar()
var_disponivel = tk.BooleanVar()
var_baixado = tk.BooleanVar()
var_todos = tk.BooleanVar()

# CHECK BUTTONS
check_emprestado = tk.Checkbutton(frame_listagem, text="Emprestado", font=("Arial", 12, "bold"), variable=var_emprestado)
check_emprestado.place(x=10, y=175)

check_disponivel = tk.Checkbutton(frame_listagem, text="Disponível", font=("Arial", 12, "bold"), variable=var_disponivel)
check_disponivel.place(x=10, y=200)

check_baixado = tk.Checkbutton(frame_listagem, text="Baixado", font=("Arial", 12, "bold"), variable=var_baixado)
check_baixado.place(x=10, y=225)

check_todos = tk.Checkbutton(frame_listagem, text="Todos", font=("Arial", 12, "bold"), variable=var_todos)
check_todos.place(x=10, y=250)



# CRIA A BARRA DE SCROLL
scrollbar_vertical = ttk.Scrollbar(frame_listagem, orient="vertical")
scrollbar_vertical.place(x=770, y=70, height=270)



# region TREEVIEW
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

colunas = ("gesp", "codigo_modelo", "modelo", "status")
tree = ttk.Treeview(
    frame_listagem,
    columns=colunas,
    show="headings",
    height=12,
    yscrollcommand=scrollbar_vertical.set
)
tree.place(x=250, y=70, width=520, height=270)

scrollbar_vertical.config(command=tree.yview)

tree.heading("gesp", text="GESP", anchor="center")
tree.heading("codigo_modelo", text="CÓDIGO MODELO", anchor="center")
tree.heading("modelo", text="MODELO", anchor="center")
tree.heading("status", text="STATUS", anchor="center")

tree.column("gesp", width=120, anchor="center")
tree.column("codigo_modelo", width=160, anchor="center")
tree.column("modelo", width=120, anchor="center")
tree.column("status", width=120, anchor="center")
# endregion

botao_listar = tk.Button(frame_listagem, text="Listar", command=mostrar_listagem_gui, font=("Arial", 15))
botao_listar.place(x=10, y=305)
