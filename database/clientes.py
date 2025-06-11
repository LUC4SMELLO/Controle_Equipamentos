import sqlite3

def conectar_banco_dados_clientes():
    return sqlite3.connect("TabelaClientes.db")


def criar_tabela_clientes():
    conexao = conectar_banco_dados_clientes()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaClientes (
    codigo_cliente VARCHAR(10) NOT NULL,
    razao_social VARCHAR(10),
    PRIMARY KEY (codigo_cliente)
    )
    """
    )

def inserir_cliente(codigo_cliente, razao_social):
    conexao = conectar_banco_dados_clientes()
    cursor = conexao.cursor()

    cursor.execute(
    """
    INSERT INTO TabelaClientes
    (codigo_cliente, razao_social)
    VALUES (?, ?)
    """, (codigo_cliente, razao_social)
    )

    conexao.commit()
    conexao.close()

def excluir_cliente(codigo_cliente, razao_social):
    try:
        conexao = conectar_banco_dados_clientes()
        cursor = conexao.cursor()

        cursor.execute(
        """
        DELETE FROM TabelaClientes
        WHERE codigo_cliente = ? AND razao_social = ?
        """, (codigo_cliente, razao_social)
        )

        conexao.commit()
        conexao.close()
    except sqlite3.Error as e:
        print("Erro ao atualizar o status:", e)



def listar_clientes():
    conexao = conectar_banco_dados_clientes()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT * FROM TabelaClientes
    ORDER BY codigo_cliente ASC
    """
    )
    
    clientes = cursor.fetchall()
 
    cursor.close()

    return clientes