from tkinter import ttk
import tkinter as tk

from backend.controlador_listagem import mostrar_listagem_clientes_back


def criar_frame_listagem_clientes(janela_pai):
    
    def mostrar_listagem_clientes_gui():

        codigo_cliente = entry_codigo_cliente.get().strip()
        razao_social = entry_razao_social.get().strip()

        resultados = mostrar_listagem_clientes_back(
            codigo_cliente, razao_social
            )
        
        for item in tree_clientes.get_children():
            tree_clientes.delete(item)

        for linha in resultados:
            tree_clientes.insert("", "end", values=linha)


    frame_listagem_clientes = tk.Frame(janela_pai, width=1200, height=650)
    

    label_clientes = tk.Label(frame_listagem_clientes, text="CLIENTES", font=("Arial", 20, "bold"))
    label_clientes.place(x=10, y=10)

    label_codigo_cliente = tk.Label(frame_listagem_clientes, text="CÓDIGO CLIENTE:", font=("Arial", 15, "bold"))
    label_codigo_cliente.place(x=10, y=70)

    entry_codigo_cliente = tk.Entry(frame_listagem_clientes, font=("Arial", 15), width=15)
    entry_codigo_cliente.place(x=200, y=70)

    label_razao_social = tk.Label(frame_listagem_clientes, text="RAZÃO SOCIAL:", font=("Arial", 15, "bold"))
    label_razao_social.place(x=10, y=110)

    entry_razao_social = tk.Entry(frame_listagem_clientes, font=("Arial", 15), width=17)
    entry_razao_social.place(x=178, y=110)




    # CRIA A BARRA DE SCROLL CLIENTES
    scrollbar_vertical_clientes = ttk.Scrollbar(frame_listagem_clientes, orient="vertical")
    scrollbar_vertical_clientes.place(x=1150, y=70, height=270)

    scrollbar_horizontal_clientes = ttk.Scrollbar(frame_listagem_clientes, orient="horizontal")
    scrollbar_horizontal_clientes.place(x=400, y=340, width=750)


    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

    colunas = ("codigo_cliente", "razao_social")
    tree_clientes = ttk.Treeview(
        frame_listagem_clientes,
        columns=colunas,
        show="headings",
        height=12,
        yscrollcommand=scrollbar_vertical_clientes.set,
        xscrollcommand=scrollbar_horizontal_clientes.set
    )
    tree_clientes.place(x=400, y=70, width=750, height=270)

    scrollbar_vertical_clientes.config(command=tree_clientes.yview)
    scrollbar_horizontal_clientes.config(command=tree_clientes.xview)

    tree_clientes.heading("codigo_cliente", text="CÓDIGO CLIENTE", anchor="center")
    tree_clientes.heading("razao_social", text="RAZÃO SOCIAL", anchor="center")

    tree_clientes.column("codigo_cliente", width=140, anchor="center")
    tree_clientes.column("razao_social", width=200, anchor="center")


    botao_listar_clientes = tk.Button(frame_listagem_clientes, text="Listar", command=mostrar_listagem_clientes_gui, font=("Arial", 15))
    botao_listar_clientes.place(x=10, y=305)

    return frame_listagem_clientes