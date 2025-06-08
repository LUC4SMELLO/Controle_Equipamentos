from tkinter import ttk
import tkinter as tk

from backend.controlador_listagem import mostrar_listagem_equipamentos_emprestados_back

def criar_frame_listagem_equipamentos_emprestados(janela_pai):

    def mostrar_listagem_equipamentos_emprestados_gui():

        gesp = entry_gesp.get().strip()

        resultados = mostrar_listagem_equipamentos_emprestados_back(gesp)

        
        for item in tree_equipamentos_emprestados.get_children():
            tree_equipamentos_emprestados.delete(item)

        for linha in resultados:
            tree_equipamentos_emprestados.insert("", "end", values=linha)

    frame_listagem_equipamentos_emprestados = tk.Frame(janela_pai, width=1300, height=400)
    
    label_equipamentos_emprestados = tk.Label(frame_listagem_equipamentos_emprestados, text="EQUIPAMENTOS EMPRESTADOS", font=("Arial", 20, "bold"))
    label_equipamentos_emprestados.place(x=10, y=10)

    label_gesp = tk.Label(frame_listagem_equipamentos_emprestados, text="GESP:", font=("Arial", 15, "bold"))
    label_gesp.place(x=10, y=70)

    entry_gesp = tk.Entry(frame_listagem_equipamentos_emprestados, font=("Arial", 15), width=12)
    entry_gesp.place(x=80, y=70)

    scrollbar_vertical_equipamentos = ttk.Scrollbar(frame_listagem_equipamentos_emprestados, orient="vertical")
    scrollbar_vertical_equipamentos.place(x=770, y=70, height=270)

    scrollbar_horizontal_equipamentos = ttk.Scrollbar(frame_listagem_equipamentos_emprestados, orient="horizontal")
    scrollbar_horizontal_equipamentos.place(x=250, y=340, width=1200)

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
    tree_equipamentos_emprestados.place(x=250, y=70, width=1000, height=270)

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

    botao_listar_equipamentos = tk.Button(frame_listagem_equipamentos_emprestados, text="Listar", command=mostrar_listagem_equipamentos_emprestados_gui, font=("Arial", 15))
    botao_listar_equipamentos.place(x=10, y=305)

    return frame_listagem_equipamentos_emprestados