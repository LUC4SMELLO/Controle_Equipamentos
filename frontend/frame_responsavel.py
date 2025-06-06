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

def cadastrar_responsavel_gui():
    codigo_cliente = entry_codigo_cliente_cadastrar.get()
    nome = entry_nome_cadastrar.get()
    cpf = entry_cpf_cadastrar.get()
    email = entry_email_cadastrar.get()


    valido, mensagem = validar_formulario_cadastro_responsavel(codigo_cliente, nome, cpf, email)
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

# FRAME RESPONSÁVEL
frame_cadastro_responsavel = tk.Frame(janela, width=1200, height=350)

#CADASTRAR RESPONSÁVEL
label_cadastrar_responsavel = tk.Label(frame_cadastro_responsavel, text="CADASTRAR RESPONSÁVEL", font=("Arial", 20, "bold"))
label_cadastrar_responsavel.place(x=5, y=10)

label_codigo_cliente_cadastrar = tk.Label(frame_cadastro_responsavel, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
label_codigo_cliente_cadastrar.place(x=5, y=70)

entry_codigo_cliente_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=10)
entry_codigo_cliente_cadastrar.place(x=190, y=70)

label_nome_cadastrar = tk.Label(frame_cadastro_responsavel, text="NOME:", font=("Arial", 15, "bold"))
label_nome_cadastrar.place(x=5, y=110)

entry_nome_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=25)
entry_nome_cadastrar.place(x=85, y=110)

label_cpf_cadastrar = tk.Label(frame_cadastro_responsavel, text="CPF:", font=("Arial", 15, "bold"))
label_cpf_cadastrar.place(x=5, y=150)

entry_cpf_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15))
entry_cpf_cadastrar.place(x=60, y=150)

label_email_cadastrar = tk.Label(frame_cadastro_responsavel, text="E-MAIL:", font=("Arial", 15, "bold"))
label_email_cadastrar.place(x=5, y=190)

entry_email_cadastrar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=25)
entry_email_cadastrar.place(x=85, y=190)

botao_cadastrar_responsavel_cadastrar = tk.Button(frame_cadastro_responsavel, text="Cadastrar", command=cadastrar_responsavel_gui, font=("Arial", 15))
botao_cadastrar_responsavel_cadastrar.place(x=5, y=250)

def buscar_responsavel_gui():

    codigo_cliente = entry_codigo_cliente_alterar.get()

    if not codigo_cliente:
        messagebox.showerror("Erro", "Preencha o Código do Cliente.")
        return None

    valido, mensagem = cliente_existe(codigo_cliente)
    if not valido:
        messagebox.showerror(valido, mensagem)
        return None

    entry_codigo_cliente_alterar.delete(0, tk.END)
    entry_nome_alterar.delete(0, tk.END)
    entry_cpf_alterar.delete(0, tk.END)
    entry_email_alterar.delete(0, tk.END)


    dados_equipamentos = buscar_e_retornar_responsavel(codigo_cliente)

    if not dados_equipamentos:
        messagebox.showerror("Erro", "Nenhum Cliente Encontrado.")
        return None

    codigo_cliente = dados_equipamentos[0][0]
    nome = dados_equipamentos[0][1]
    cpf = dados_equipamentos[0][2]
    email = dados_equipamentos[0][3]

    entry_codigo_cliente_alterar.insert(0, codigo_cliente)
    entry_nome_alterar.insert(0, nome)
    entry_cpf_alterar.insert(0, cpf)
    entry_email_alterar.insert(0, email)


def alterar_informacoes_responsavel_gui():
    codigo_cliente = entry_codigo_cliente_alterar.get()
    nome = entry_nome_alterar.get()
    cpf = entry_cpf_alterar.get()
    email = entry_email_alterar.get()

    valido, mensagem = validar_formulario_excluir_responsavel(codigo_cliente, nome, cpf, email)
    if not valido:
       messagebox.showerror("Erro", mensagem)
       return None

    messagebox.showinfo("Sucesso", "Informações Alteradas!")

    alterar_informacoes_responsavel_back(codigo_cliente, nome, cpf, email)

    entry_codigo_cliente_alterar.delete(0, tk.END)
    entry_nome_alterar.delete(0, tk.END)
    entry_cpf_alterar.delete(0, tk.END)
    entry_email_alterar.delete(0, tk.END)


# ALTERAR RESPONSÁVEL
label_alterar_responsavel = tk.Label(frame_cadastro_responsavel, text="ALTERAR RESPONSÁVEL", font=("Arial", 20, "bold"))
label_alterar_responsavel.place(x=445, y=10)

divisor = tk.LabelFrame(frame_cadastro_responsavel, border=False, background="silver", width=5, height=300)
divisor.place(x=413, y=10)

botao_buscar_responsavel = tk.Button(frame_cadastro_responsavel, text="Buscar", command=buscar_responsavel_gui, font=("Arial", 10, "bold"))
botao_buscar_responsavel.place(x=765, y=68)

label_codigo_cliente_alterar = tk.Label(frame_cadastro_responsavel, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
label_codigo_cliente_alterar.place(x=450, y=70)

entry_codigo_cliente_alterar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=10)
entry_codigo_cliente_alterar.place(x=635, y=70)

label_nome_alterar = tk.Label(frame_cadastro_responsavel, text="NOME:", font=("Arial", 15, "bold"))
label_nome_alterar.place(x=450, y=110)

entry_nome_alterar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=25)
entry_nome_alterar.place(x=530, y=110)

label_cpf_alterar = tk.Label(frame_cadastro_responsavel, text="CPF:", font=("Arial", 15, "bold"))
label_cpf_alterar.place(x=450, y=150)

entry_cpf_alterar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15))
entry_cpf_alterar.place(x=505, y=150)

label_email_alterar = tk.Label(frame_cadastro_responsavel, text="E-MAIL:", font=("Arial", 15, "bold"))
label_email_alterar.place(x=450, y=190)

entry_email_alterar = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=25)
entry_email_alterar.place(x=530, y=190)

botao_alterar_responsavel = tk.Button(frame_cadastro_responsavel, text="Alterar", command=alterar_informacoes_responsavel_gui, font=("Arial", 15))
botao_alterar_responsavel.place(x=450, y=250)

def excluir_responsavel_gui():
    codigo_cliente = entry_codigo_cliente_excluir.get()
    nome = entry_nome_excluir.get()
    cpf = entry_cpf_excluir.get()
    email = entry_email_excluir.get()

    valido, mensagem = validar_formulario_excluir_responsavel(codigo_cliente, nome, cpf, email)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None

    valido, mensagem = responsavel_existe(codigo_cliente)
    if not valido:
        messagebox.showerror("Erro", mensagem)
        return None

    messagebox.showinfo("Sucesso", "Reponsável Excluído com Sucesso!")

    excluir_responsavel_back(codigo_cliente, nome, cpf, email)

    entry_codigo_cliente_excluir.delete(0, tk.END)
    entry_nome_excluir.delete(0, tk.END)
    entry_cpf_excluir.delete(0, tk.END)
    entry_email_excluir.delete(0, tk.END)



# EXCLUIR RESPONSÁVEL
label_excluir_responsavel = tk.Label(frame_cadastro_responsavel, text="EXCLUIR RESPONSÁVEL", font=("Arial", 20, "bold"))
label_excluir_responsavel.place(x=865, y=10)

divisor = tk.LabelFrame(frame_cadastro_responsavel, border=False, background="silver", width=5, height=300)
divisor.place(x=413, y=10)

label_codigo_cliente_excluir = tk.Label(frame_cadastro_responsavel, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
label_codigo_cliente_excluir.place(x=870, y=70)

entry_codigo_cliente_excluir = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=10)
entry_codigo_cliente_excluir.place(x=1055, y=70)

label_nome_excluir = tk.Label(frame_cadastro_responsavel, text="NOME:", font=("Arial", 15, "bold"))
label_nome_excluir.place(x=870, y=110)

entry_nome_excluir = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=25)
entry_nome_excluir.place(x=950, y=110)

label_cpf_excluir = tk.Label(frame_cadastro_responsavel, text="CPF:", font=("Arial", 15, "bold"))
label_cpf_excluir.place(x=870, y=150)

entry_cpf_excluir = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15))
entry_cpf_excluir.place(x=925, y=150)

label_email_excluir = tk.Label(frame_cadastro_responsavel, text="E-MAIL:", font=("Arial", 15, "bold"))
label_email_excluir.place(x=870, y=190)

entry_email_excluir = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=25)
entry_email_excluir.place(x=950, y=190)

botao_excluir_responsavel = tk.Button(frame_cadastro_responsavel, text="Excluir", command=excluir_responsavel_gui, font=("Arial", 15))
botao_excluir_responsavel.place(x=870, y=250)



divisor = tk.LabelFrame(frame_cadastro_responsavel, border=False, background="silver", width=5, height=300)
divisor.place(x=833, y=10)