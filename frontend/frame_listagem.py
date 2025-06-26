from tkinter import *
import tkinter as tk


from frontend.frames_listagem.frame_listagem_equipamentos import criar_frame_listagem_equipamentos
from frontend.frames_listagem.frame_listagem_equipamentos_emprestados import criar_frame_listagem_equipamentos_emprestados
from frontend.frames_listagem.frame_listagem_responsaveis import criar_frame_listagem_reponsaveis
from frontend.frames_listagem.frame_listagem_clientes import criar_frame_listagem_clientes

from frontend.janela import janela


def mostrar_frame_listagem(frame):
    frame_listagem_equipamentos.place_forget()
    frame_listagem_equipamentos_emprestados.place_forget()
    frame_listagem_responsaveis.place_forget()
    frame_listagem_clientes.place_forget()

    frame.place(x=10, y=80)


frame_listagem_inicial = tk.Frame(janela, width=1200, height=800)


( 
    frame_listagem_equipamentos,
    entry_gesp_listagem,
    entry_modelo_listagem,
    botao_listar_equipamentos,
    mostrar_listagem_equipamentos_gui,
) = criar_frame_listagem_equipamentos(frame_listagem_inicial)

(
    frame_listagem_equipamentos_emprestados,
    entry_gesp_equipamentos_emprestados,
    entry_contrato_equipamentos_emprestados,
    entry_codigo_cliente_equipamentos_emprestados,
    entry_nome_equipamentos_emprestados,
    entry_cpf_equipamentos_emprestados,
    entry_email_equipamentos_emprestados,
    botao_listar_equipamentos_emprestados,
    mostrar_listagem_equipamentos_emprestados_gui
) = criar_frame_listagem_equipamentos_emprestados(frame_listagem_inicial)

frame_listagem_responsaveis = criar_frame_listagem_reponsaveis(frame_listagem_inicial)
frame_listagem_clientes = criar_frame_listagem_clientes(frame_listagem_inicial)


label_listagem = tk.Label(frame_listagem_inicial, text="LISTAGEM", font=("Arial", 20, "bold"))
label_listagem.place(x=20, y=10)

botao_listagem_equipamentos = tk.Button(frame_listagem_inicial, text="Equipamentos", command=lambda: mostrar_frame_listagem(frame_listagem_equipamentos), font=("Arial", 15))
botao_listagem_equipamentos.place(x=200, y=10)

botao_listagem_equipamentos_emprestados = tk.Button(frame_listagem_inicial, text="Equipamentos Emprestados", command=lambda: mostrar_frame_listagem(frame_listagem_equipamentos_emprestados), font=("Arial", 15))
botao_listagem_equipamentos_emprestados.place(x=360, y=10)

botao_listagem_responsaveis = tk.Button(frame_listagem_inicial, text="Responsáveis", command=lambda: mostrar_frame_listagem(frame_listagem_responsaveis), font=("Arial", 15))
botao_listagem_responsaveis.place(x=645, y=10)

botao_listagem_clientes = tk.Button(frame_listagem_inicial, text="Clientes", command=lambda: mostrar_frame_listagem(frame_listagem_clientes), font=("Arial", 15))
botao_listagem_clientes.place(x=805, y=10)
