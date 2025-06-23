import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from backend.controlador_listagem import mostrar_listagem_responsaveis_back

def criar_frame_listagem_reponsaveis(janela_pai):

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

        if not resultados:
            messagebox.showinfo("Aviso", "Não Há Responsáveis a Serem Listados")
            return None

    # FRAME LISTAGEM RESPONSÁVEIS
    frame_listagem_responsaveis = tk.Frame(janela_pai, width=1200, height=350)

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

    return frame_listagem_responsaveis