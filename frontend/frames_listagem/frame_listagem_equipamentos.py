from tkinter import ttk
import tkinter as tk

from backend.controlador_listagem import mostrar_listagem_equipamentos_back


def criar_frame_listagem_equipamentos(janela_pai):

    def mostrar_listagem_equipamentos_gui():

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

        resultados = mostrar_listagem_equipamentos_back(modelo, status, gesp)

        
        for item in tree_equipamentos.get_children():
            tree_equipamentos.delete(item)

        for linha in resultados:
            tree_equipamentos.insert("", "end", values=linha)


    # FRAME LISTAGEM EQUIPAMENTOS
    frame_listagem_equipamentos = tk.Frame(janela_pai, width=800, height=350)

    label_equipamentos = tk.Label(frame_listagem_equipamentos, text="EQUIPAMENTOS", font=("Arial", 20, "bold"))
    label_equipamentos.place(x=10, y=10)

    label_gesp = tk.Label(frame_listagem_equipamentos, text="GESP:", font=("Arial", 15, "bold"))
    label_gesp.place(x=10, y=70)

    entry_gesp_listagem = tk.Entry(frame_listagem_equipamentos, font=("Arial", 15), width=12)
    entry_gesp_listagem.place(x=80, y=70)

    label_modelo = tk.Label(frame_listagem_equipamentos, text="MODELO:", font=("Arial", 15, "bold"))
    label_modelo.place(x=10, y=110)

    entry_modelo_listagem = tk.Entry(frame_listagem_equipamentos, font=("Arial", 15), width=9)
    entry_modelo_listagem.place(x=115, y=110)

    label_listar_apenas = tk.Label(frame_listagem_equipamentos, text="LISTAR APENAS:", font=("Arial", 15, "bold"))
    label_listar_apenas.place(x=10, y=145)

    var_emprestado = tk.BooleanVar()
    var_disponivel = tk.BooleanVar()
    var_baixado = tk.BooleanVar()
    var_todos = tk.BooleanVar()

    # CHECK BUTTONS
    check_emprestado = tk.Checkbutton(frame_listagem_equipamentos, text="Emprestado", font=("Arial", 12, "bold"), variable=var_emprestado)
    check_emprestado.place(x=10, y=175)

    check_disponivel = tk.Checkbutton(frame_listagem_equipamentos, text="Disponível", font=("Arial", 12, "bold"), variable=var_disponivel)
    check_disponivel.place(x=10, y=200)

    check_baixado = tk.Checkbutton(frame_listagem_equipamentos, text="Baixado", font=("Arial", 12, "bold"), variable=var_baixado)
    check_baixado.place(x=10, y=225)

    check_todos = tk.Checkbutton(frame_listagem_equipamentos, text="Todos", font=("Arial", 12, "bold"), variable=var_todos)
    check_todos.place(x=10, y=250)



    # CRIA A BARRA DE SCROLL EQUIPAMENTOS
    scrollbar_vertical_equipamentos = ttk.Scrollbar(frame_listagem_equipamentos, orient="vertical")
    scrollbar_vertical_equipamentos.place(x=770, y=70, height=270)



    # region TREEVIEW EQUIPAMENTOS
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

    colunas = ("gesp", "codigo_modelo", "modelo", "status")
    tree_equipamentos = ttk.Treeview(
        frame_listagem_equipamentos,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical_equipamentos.set
    )
    tree_equipamentos.place(x=250, y=70, width=520, height=270)

    scrollbar_vertical_equipamentos.config(command=tree_equipamentos.yview)

    tree_equipamentos.heading("gesp", text="GESP", anchor="center")
    tree_equipamentos.heading("codigo_modelo", text="CÓDIGO MODELO", anchor="center")
    tree_equipamentos.heading("modelo", text="MODELO", anchor="center")
    tree_equipamentos.heading("status", text="STATUS", anchor="center")

    tree_equipamentos.column("gesp", width=120, anchor="center")
    tree_equipamentos.column("codigo_modelo", width=160, anchor="center")
    tree_equipamentos.column("modelo", width=110, anchor="center")
    tree_equipamentos.column("status", width=120, anchor="center")
    # endregion

    botao_listar_equipamentos = tk.Button(frame_listagem_equipamentos, text="Listar", command=mostrar_listagem_equipamentos_gui, font=("Arial", 15))
    botao_listar_equipamentos.place(x=10, y=305)

    return frame_listagem_equipamentos