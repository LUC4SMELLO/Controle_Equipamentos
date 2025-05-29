from tkinter import *
import tkinter as tk

from database.equipamentos import inserir_equipamento

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



# FRAME CADASTRO DE EQUIPAMENTOS
frame_cadastro_equipamentos = tk.Frame(janela, width=400, height=350)

label_cadastro_equipamentos = Label(frame_cadastro_equipamentos, text="CADASTRAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_cadastro_equipamentos.place(x=10, y=10)

label_gesp_cadastrar = tk.Label(frame_cadastro_equipamentos, text="GESP:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_gesp_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=80, y=70)

label_cod_modelo = tk.Label(frame_cadastro_equipamentos, text="COD MODELO:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_cod_modelo = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=165, y=110)

label_modelo_cadastrar = tk.Label(frame_cadastro_equipamentos, text="MODELO:", font=("Arial", 15, "bold")).place(x=10, y=150)
entry_modelo_cadastrar = tk.Entry(frame_cadastro_equipamentos, font=("Arial", 15), width=12).place(x=110, y=150)

botao_cadastrar_equipamento = tk.Button(frame_cadastro_equipamentos, text="Cadastrar", font=("Arial", 15)).place(x=10, y=210)



# FRAME CADASTRAR RESPONSÁVEL
frame_cadastro_responsavel = tk.Frame(janela, width=400, height=350)

label_cadastrar_responsavel = Label(frame_cadastro_responsavel, text="CADASTRAR RESPONSÁVEL", font=("Arial", 20, "bold"))
label_cadastrar_responsavel.place(x=10, y=10)

label_codigo_cliente = tk.Label(frame_cadastro_responsavel, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_codigo_cliente = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=10).place(x=195, y=70)

label_nome = tk.Label(frame_cadastro_responsavel, text="NOME:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_nome = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=30).place(x=85, y=110)

label_cpf = tk.Label(frame_cadastro_responsavel, text="CPF:", font=("Arial", 15, "bold")).place(x=10, y=150)
entry_cpf = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15)).place(x=70, y=150)

label_email = tk.Label(frame_cadastro_responsavel, text="E-MAIL:", font=("Arial", 15, "bold")).place(x=10, y=190)
entry_email = tk.Entry(frame_cadastro_responsavel, font=("Arial", 15), width=30).place(x=90, y=190)

botao_cadastrar_responsavel = tk.Button(frame_cadastro_responsavel, text="Cadastrar", font=("Arial", 15)).place(x=10, y=250)



# FRAME EMPRESTAR EQUIPAMENTO
frame_emprestar_equipamento = tk.Frame(janela, width=400, height=350)

label_emprestar_equipamento = Label(frame_emprestar_equipamento, text="EMPRESTAR EQUIPAMENTO", font=("Arial", 20, "bold"))
label_emprestar_equipamento.place(x=10, y=10)

label_codigo_cliente = tk.Label(frame_emprestar_equipamento, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_codigo_cliente = tk.Entry(frame_emprestar_equipamento, font=("Arial", 15), width=10).place(x=195, y=70)

label_gesp_a_emprestar = tk.Label(frame_emprestar_equipamento, text="GESP:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_gesp_a_emprestar = tk.Entry(frame_emprestar_equipamento, font=("Arial", 15), width=12).place(x=80, y=110)

label_contrato = tk.Label(frame_emprestar_equipamento, text="CONTRATO:", font=("Arial", 15, "bold")).place(x=10, y=150)
entry_contrato = tk.Entry(frame_emprestar_equipamento, font=("Arial", 15), width=7).place(x=140, y=150)

botao_emprestrar_equipamento = tk.Button(frame_emprestar_equipamento, text="Emprestrar", font=("Arial", 15)).place(x=10, y=210)



# FRAME DEVOLVER EQUIPAMENTO
frame_devolver_equipamento = tk.Frame(janela, width=400, height=350)

label_devolver_equipamento = tk.Label(frame_devolver_equipamento, text="DEVOLVER EQUIPAMENTO", font=("Arial", 20, "bold")).place(x=10, y=10)

label_codigo_cliente = tk.Label(frame_devolver_equipamento, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_codigo_cliente = tk.Entry(frame_devolver_equipamento, font=("Arial", 15), width=10).place(x=195, y=70)

label_gesp_a_emprestar = tk.Label(frame_devolver_equipamento, text="GESP:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_gesp_a_emprestar = tk.Entry(frame_devolver_equipamento, font=("Arial", 15), width=12).place(x=80, y=110)

label_modelo_devolver = tk.Label(frame_devolver_equipamento, text="COD MODELO:", font=("Arial", 15, "bold")).place(x=10, y=150)
entry_modelo_devolver = tk.Entry(frame_devolver_equipamento, font=("Arial", 15), width=12).place(x=165, y=150)

botao_devolver_equipamento = tk.Button(frame_devolver_equipamento, text="Devolver", font=("Arial", 15)).place(x=10, y=210)



# FRAME DAR BAIXA EQUIPAMENTO 
frame_dar_baixa_equipamento = tk.Frame(janela, width=400, height=350)

label_dar_baixa_equipamento = Label(frame_dar_baixa_equipamento, text="DAR BAIXA EQUIPAMENTO", font=("Arial", 20, "bold")).place(x=10, y=10)

label_gesp_a_dar_baixa = tk.Label(frame_dar_baixa_equipamento, text="GESP:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_gesp_a_dar_baixa = tk.Entry(frame_dar_baixa_equipamento, font=("Arial", 15), width=12).place(x=80, y=70)

label_motivo = tk.Label(frame_dar_baixa_equipamento, text="MOTIVO:", font=("Arial", 15, "bold")).place(x=10, y=110)
entry_motivo = tk.Text(frame_dar_baixa_equipamento, font=("Arial", 15), width=15, height=3).place(x=110, y=110)

botao_dar_baixa = tk.Button(frame_dar_baixa_equipamento, text="Dar Baixa", font=("Arial", 15)).place(x=10, y=210)



# FRAME LISTAGEM
frame_listagem = tk.Frame(janela, width=400, height=350)

label_listagem = tk.Label(frame_listagem, text="LISTAGEM", font=("Arial", 20, "bold")).place(x=10, y=10)

label_produto = tk.Label(frame_listagem, text="MODELO:", font=("Arial", 15, "bold")).place(x=10, y=70)
entry_produto = tk.Entry(frame_listagem, font=("Arial", 15, "bold"), width=6).place(x=130, y=70)

label_listar_apenas = tk.Label(frame_listagem, text="LISTAR APENAS:", font=("Arial", 15, "bold")).place(x=10, y=110)

check_emprestado = tk.Checkbutton(frame_listagem, text="Emprestado", font=("Arial", 10, "bold")).place(x=10, y=145)
check_disponivel = tk.Checkbutton(frame_listagem, text="Disponível", font=("Arial", 10, "bold")).place(x=10, y=165)
check_baixado = tk.Checkbutton(frame_listagem, text="Baixado", font=("Arial", 10, "bold")).place(x=10, y=185)
check_reservado = tk.Checkbutton(frame_listagem, text="Reservado", font=("Arial", 10, "bold")).place(x=10, y=185)
check_todos = tk.Checkbutton(frame_listagem, text="Todos", font=("Arial", 10, "bold")).place(x=10, y=205)

botao_listar = tk.Button(frame_listagem, text="Listar", font=("Arial", 15)).place(x=10, y=265)


