from tkinter import *
import tkinter as tk

janela = tk.Tk()
janela.title("Controle de Equipamentos")
janela.geometry("1280x650")


# CADASTRO DE EQUIPAMENTOS
frame_cadastro_equipamentos = tk.Frame(janela, width=400, height=350)

label_cadastro_equipamentos = Label(frame_cadastro_equipamentos, text="CADASTRAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_cadastro_equipamentos.place(x=10, y=10)

label_gesp = tk.Label(frame_cadastro_equipamentos, text="GESP:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_gesp = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=80, y=70)

label_cod_modelo = tk.Label(frame_cadastro_equipamentos, text="COD MODELO:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_cod_modelo = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=165, y=110)

label_modelo = tk.Label(frame_cadastro_equipamentos, text="MODELO:", font=("Arial", 15, "bold")).place(x=10, y=150)
entry_modelo = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=110, y=150)

botao_salvar = tk.Button(frame_cadastro_equipamentos, text="Cadastrar", font=("Arial", 15)).place(x=10, y=210)

frame_outros = tk.Frame(janela)
tk.Label(frame_outros, text="Aqui você pode colocar outras opções.").pack()