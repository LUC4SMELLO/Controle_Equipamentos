from tkinter import *
import tkinter as tk

janela = tk.Tk()
janela.title("Controle de Equipamentos")
janela.geometry("1280x650")


def mostrar_frame(frame):
    frame_cadastro_equipamentos.place_forget()
    frame_cadastro_responsavel.place_forget()
    
    frame.place(x=10, y=150)

# FRAME CADASTRO DE EQUIPAMENTOS
frame_cadastro_equipamentos = tk.Frame(janela, width=400, height=350)

label_cadastro_equipamentos = Label(frame_cadastro_equipamentos, text="CADASTRAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_cadastro_equipamentos.place(x=10, y=10)

label_gesp = tk.Label(frame_cadastro_equipamentos, text="GESP:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_gesp = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=80, y=70)

label_cod_modelo = tk.Label(frame_cadastro_equipamentos, text="COD MODELO:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_cod_modelo = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=165, y=110)

label_modelo = tk.Label(frame_cadastro_equipamentos, text="MODELO:", font=("Arial", 15, "bold")).place(x=10, y=150)
entry_modelo = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=110, y=150)

botao_cadastrar_equipamento = tk.Button(frame_cadastro_equipamentos, text="Cadastrar", font=("Arial", 15)).place(x=10, y=210)



# FRAME CADASTRAR RESPONSÁVEL
frame_cadastro_responsavel = tk.Frame(janela, width=400, height=350)

label_cadastrar_responsavel = Label(frame_cadastro_responsavel, text="CADASTRAR RESPONSÁVEL", font=("Arial", 20, "bold"))
label_cadastrar_responsavel.place(x=10, y=10)

label_nome = tk.Label(frame_cadastro_responsavel, text="NOME:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_nome = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=30).place(x=85, y=70)

label_cpf = tk.Label(frame_cadastro_responsavel, text="CPF:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_cpf = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15)).place(x=70, y=110)

label_email = tk.Label(frame_cadastro_responsavel, text="E-Mail:", font=("Arial", 15, "bold")).place(x=10, y=150)
entry_email = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=30).place(x=85, y=150)

botao_cadastrar_responsavel = tk.Button(frame_cadastro_responsavel, text="Cadastrar", font=("Arial", 15)).place(x=10, y=210)