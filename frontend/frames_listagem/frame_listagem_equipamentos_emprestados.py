from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from backend.controlador_listagem import mostrar_listagem_equipamentos_emprestados_back

def criar_frame_listagem_equipamentos_emprestados(janela_pai):

    def mostrar_listagem_equipamentos_emprestados_gui():

        gesp = entry_gesp_equipamentos_emprestados.get().strip()
        contrato = entry_contrato_equipamentos_emprestados.get().strip()
        codigo_cliente = entry_codigo_cliente_equipamentos_emprestados.get().strip()
        nome = entry_nome_equipamentos_emprestados.get().strip()
        cpf = entry_cpf_equipamentos_emprestados.get().strip()
        email = entry_email_equipamentos_emprestados.get().strip()

        

        resultados = mostrar_listagem_equipamentos_emprestados_back(
            gesp, contrato, codigo_cliente, nome, cpf, email
            )

        
        for item in tree_equipamentos_emprestados.get_children():
            tree_equipamentos_emprestados.delete(item)

        for linha in resultados:
            tree_equipamentos_emprestados.insert("", "end", values=linha)

        if not resultados:
            messagebox.showinfo("Erro", "Não Há Equipamentos Emprestados a Serem Listados")

    frame_listagem_equipamentos_emprestados = tk.Frame(janela_pai, width=1300, height=400)
    
    label_equipamentos_emprestados = tk.Label(frame_listagem_equipamentos_emprestados, text="EQUIPAMENTOS EMPRESTADOS", font=("Arial", 20, "bold"))
    label_equipamentos_emprestados.place(x=10, y=10)

    label_gesp = tk.Label(frame_listagem_equipamentos_emprestados, text="GESP:", font=("Arial", 15, "bold"))
    label_gesp.place(x=10, y=70)

    entry_gesp_equipamentos_emprestados = tk.Entry(frame_listagem_equipamentos_emprestados, font=("Arial", 15), width=12)
    entry_gesp_equipamentos_emprestados.place(x=80, y=70)

    label_contrato = tk.Label(frame_listagem_equipamentos_emprestados, text="CONTRATO:", font=("Arial", 15, "bold"))
    label_contrato.place(x=10, y=110)

    entry_contrato_equipamentos_emprestados = tk.Entry(frame_listagem_equipamentos_emprestados, font=("Arial", 15))
    entry_contrato_equipamentos_emprestados.place(x=145, y=110)

    label_codigo_cliente = tk.Label(frame_listagem_equipamentos_emprestados, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
    label_codigo_cliente.place(x=10, y=145)

    entry_codigo_cliente_equipamentos_emprestados = tk.Entry(frame_listagem_equipamentos_emprestados, font=("Arial", 15), width=15)
    entry_codigo_cliente_equipamentos_emprestados.place(x=200, y=145)

    label_nome = tk.Label(frame_listagem_equipamentos_emprestados, text="NOME:", font=("Arial", 15, "bold"))
    label_nome.place(x=10, y=185)

    entry_nome_equipamentos_emprestados = tk.Entry(frame_listagem_equipamentos_emprestados, font=("Arial", 15), width=25)
    entry_nome_equipamentos_emprestados.place(x=90, y=185)

    label_cpf_listagem = tk.Label(frame_listagem_equipamentos_emprestados, text="CPF:", font=("Arial", 15, "bold"))
    label_cpf_listagem.place(x=10, y=225)

    entry_cpf_equipamentos_emprestados = tk.Entry(frame_listagem_equipamentos_emprestados, font=("Arial", 15), width=25)
    entry_cpf_equipamentos_emprestados.place(x=90, y=225)

    label_email_listagem = tk.Label(frame_listagem_equipamentos_emprestados, text="E-MAIL:", font=("Arial", 15, "bold"))
    label_email_listagem.place(x=10, y=265)

    entry_email_equipamentos_emprestados = tk.Entry(frame_listagem_equipamentos_emprestados, font=("Arial", 15), width=25)
    entry_email_equipamentos_emprestados.place(x=90, y=265)

    scrollbar_vertical_equipamentos = ttk.Scrollbar(frame_listagem_equipamentos_emprestados, orient="vertical")
    scrollbar_vertical_equipamentos.place(x=1150, y=70, height=270)

    scrollbar_horizontal_equipamentos = ttk.Scrollbar(frame_listagem_equipamentos_emprestados, orient="horizontal")
    scrollbar_horizontal_equipamentos.place(x=400, y=340, width=750)

    # region TREEVIEW EQUIPAMENTOS
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

    colunas = ("gesp", "codigo_cliente", "contrato", "nome", "cpf", "email")
    tree_equipamentos_emprestados = ttk.Treeview(
        frame_listagem_equipamentos_emprestados,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical_equipamentos.set,
        xscrollcommand=scrollbar_horizontal_equipamentos.set
    )
    tree_equipamentos_emprestados.place(x=400, y=70, width=750, height=270)

    scrollbar_vertical_equipamentos.config(command=tree_equipamentos_emprestados.yview)
    scrollbar_horizontal_equipamentos.config(command=tree_equipamentos_emprestados.xview)

    tree_equipamentos_emprestados.heading("gesp", text="GESP", anchor="center")
    tree_equipamentos_emprestados.heading("codigo_cliente", text="CÓDIGO CLIENTE", anchor="center")
    tree_equipamentos_emprestados.heading("contrato", text="CONTRATO", anchor="center")
    tree_equipamentos_emprestados.heading("nome", text="NOME", anchor="center")
    tree_equipamentos_emprestados.heading("cpf", text="CPF", anchor="center")
    tree_equipamentos_emprestados.heading("email", text="E-MAIL", anchor="center")

    tree_equipamentos_emprestados.column("gesp", width=150, anchor="center")
    tree_equipamentos_emprestados.column("codigo_cliente", width=200, anchor="center")
    tree_equipamentos_emprestados.column("contrato", width=130, anchor="center")
    tree_equipamentos_emprestados.column("nome", width=250, anchor="center")
    tree_equipamentos_emprestados.column("cpf", width=250, anchor="center")
    tree_equipamentos_emprestados.column("email", width=400, anchor="center")
    # endregion

    botao_listar_equipamentos_emprestados = tk.Button(frame_listagem_equipamentos_emprestados, text="Listar", command=mostrar_listagem_equipamentos_emprestados_gui, font=("Arial", 15))
    botao_listar_equipamentos_emprestados.place(x=10, y=305)

    return (
        frame_listagem_equipamentos_emprestados,
        entry_gesp_equipamentos_emprestados,
        entry_contrato_equipamentos_emprestados,
        entry_codigo_cliente_equipamentos_emprestados,
        entry_nome_equipamentos_emprestados,
        entry_cpf_equipamentos_emprestados,
        entry_email_equipamentos_emprestados,
        botao_listar_equipamentos_emprestados,
        mostrar_listagem_equipamentos_emprestados_gui
    )