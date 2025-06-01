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

janela = tk.Tk()
janela.title("Controle de Equipamentos")
janela.geometry("1280x650")


def mostrar_frame(frame):
    frame_cadastro_equipamentos.place_forget()
    frame_cadastro_responsavel.place_forget()
    frame_emprestar_equipamento.place_forget()
    frame_devolver_equipamento.place_forget()
    frame_dar_baixa_equipamento.place_forget()
    frame_listagem.place_forget()
    
    frame.place(x=10, y=150)

def cadastrar_equipamento_gui():
    gesp = entry_gesp_cadastrar.get()
    codigo_modelo = entry_codigo_modelo_cadastrar.get()
    modelo = entry_modelo_cadastrar.get()

    valido, mensagem = validar_cadastro_equipamentos(gesp, codigo_modelo, modelo)

    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    messagebox.showinfo("Sucesso", "Equipamento Cadastrado!")

    cadastrar_equipamento_back(gesp, codigo_modelo, modelo)    

    entry_gesp_cadastrar.delete(0, tk.END)
    entry_codigo_modelo_cadastrar.delete(0, tk.END)
    entry_modelo_cadastrar.delete(0, tk.END)


# FRAME CADASTRO DE EQUIPAMENTOS
frame_cadastro_equipamentos = tk.Frame(janela, width=400, height=350)

label_cadastro_equipamentos = Label(frame_cadastro_equipamentos, text="CADASTRAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_cadastro_equipamentos.place(x=10, y=10)

label_gesp_cadastrar = tk.Label(frame_cadastro_equipamentos, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_cadastrar.place(x=10, y=70)

entry_gesp_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_gesp_cadastrar.place(x=80, y=70)

label_codigo_modelo_cadastrar = tk.Label(frame_cadastro_equipamentos, text="COD MODELO:", font=("Arial", 15, "bold"))
label_codigo_modelo_cadastrar.place(x=10, y=110)

entry_codigo_modelo_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_codigo_modelo_cadastrar.place(x=165, y=110)

label_modelo_cadastrar = tk.Label(frame_cadastro_equipamentos, text="MODELO:", font=("Arial", 15, "bold"))
label_modelo_cadastrar.place(x=10, y=150)

entry_modelo_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12)
entry_modelo_cadastrar.place(x=110, y=150)

botao_cadastrar_equipamento = tk.Button(frame_cadastro_equipamentos, text="Cadastrar", command=cadastrar_equipamento_gui, font=("Arial", 15))
botao_cadastrar_equipamento.place(x=10, y=210)

def cadastrar_responsavel_gui():
    codigo_cliente = entry_codigo_cliente_cadastrar.get()
    nome = entry_nome_cadastrar.get()
    cpf = entry_cpf_cadastrar.get()
    email = entry_email_cadastrar.get()


    valido, mensagem  = validar_cadastro_responsavel(codigo_cliente, nome, cpf, email)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    valido, mensagem = cliente_existe(codigo_cliente)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    valido, mensagem = responsavel_existe(codigo_cliente)
    if valido:
        messagebox.showerror("Erro", mensagem)
        return None

    
    messagebox.showinfo("Sucesso", "Responsável Cadastrado!")

    cadastrar_responsavel_back(codigo_cliente, nome, cpf, email)

    entry_codigo_cliente_cadastrar.delete(0, tk.END)
    entry_nome_cadastrar.delete(0, tk.END)
    entry_cpf_cadastrar.delete(0, tk.END)
    entry_email_cadastrar.delete(0, tk.END)

# FRAME CADASTRAR RESPONSÁVEL
frame_cadastro_responsavel = tk.Frame(janela, width=400, height=350)

label_cadastrar_responsavel = Label(frame_cadastro_responsavel, text="CADASTRAR RESPONSÁVEL", font=("Arial", 20, "bold"))
label_cadastrar_responsavel.place(x=10, y=10)

label_codigo_cliente_cadastrar = tk.Label(frame_cadastro_responsavel, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
label_codigo_cliente_cadastrar.place(x=10, y=70)

entry_codigo_cliente_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=10)
entry_codigo_cliente_cadastrar.place(x=195, y=70)

label_nome_cadastrar = tk.Label(frame_cadastro_responsavel, text="NOME:", font=("Arial", 15, "bold"))
label_nome_cadastrar.place(x=10, y=110)

entry_nome_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=30)
entry_nome_cadastrar.place(x=85, y=110)

label_cpf_cadastrar = tk.Label(frame_cadastro_responsavel, text="CPF:", font=("Arial", 15, "bold"))
label_cpf_cadastrar.place(x=10, y=150)

entry_cpf_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15))
entry_cpf_cadastrar.place(x=70, y=150)

label_email_cadastrar = tk.Label(frame_cadastro_responsavel, text="E-MAIL:", font=("Arial", 15, "bold"))
label_email_cadastrar.place(x=10, y=190)

entry_email_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=30)
entry_email_cadastrar.place(x=90, y=190)

botao_cadastrar_responsavel_cadastrar = tk.Button(frame_cadastro_responsavel, text="Cadastrar", command=cadastrar_responsavel_gui, font=("Arial", 15))
botao_cadastrar_responsavel_cadastrar.place(x=10, y=250)


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

    emprestrar_equipamento_back(gesp, codigo_cliente, contrato)

    entry_codigo_cliente_emprestrar.delete(0, tk.END)
    entry_gesp_emprestar.delete(0, tk.END)
    entry_contrato_emprestrar.delete(0, tk.END)

# FRAME EMPRESTAR EQUIPAMENTO
frame_emprestar_equipamento = tk.Frame(janela, width=400, height=350)

label_emprestar_equipamento = Label(frame_emprestar_equipamento, text="EMPRESTAR EQUIPAMENTO", font=("Arial", 20, "bold"))
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
        return None
    
    valido, mensagem = equipamento_existe(gesp)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None

    valido, mensagem = equipamento_emprestado(gesp, codigo_cliente)    
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None
    
    messagebox.showinfo("Sucesso!", "Equipamento Devolvido!")

    devolver_equipamento_back(gesp, codigo_cliente)

    entry_gesp_a_devolver.delete(0, tk.END)
    entry_codigo_cliente_devolver.delete(0, tk.END)

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

botao_devolver_equipamento = tk.Button(frame_devolver_equipamento, command=devolver_equipamento_gui,text="Devolver", font=("Arial", 15))
botao_devolver_equipamento.place(x=10, y=210)

def dar_baixa_equipamento_gui():
    gesp = entry_gesp_a_dar_baixa.get()

    validado, mensagem = validar_dar_baixa(gesp)
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

label_dar_baixa_equipamento = Label(frame_dar_baixa_equipamento, text="DAR BAIXA EQUIPAMENTO", font=("Arial", 20, "bold"))
label_dar_baixa_equipamento.place(x=10, y=10)

label_gesp_a_dar_baixa = tk.Label(frame_dar_baixa_equipamento, text="GESP:", font=("Arial", 15, "bold"))
label_gesp_a_dar_baixa.place(x=10, y=70)

entry_gesp_a_dar_baixa = tk.Entry(frame_dar_baixa_equipamento, font=("Arial", 15), width=12)
entry_gesp_a_dar_baixa.place(x=80, y=70)

botao_dar_baixa = tk.Button(frame_dar_baixa_equipamento, text="Dar Baixa", command=dar_baixa_equipamento_gui, font=("Arial", 15))
botao_dar_baixa.place(x=10, y=210)


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
scrollbar_vertical.place(x=730, y=70, height=260)



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
tree.place(x=250, y=70)

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
botao_listar.place(x=10, y=295)
