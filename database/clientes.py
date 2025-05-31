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

def inserir_equipamento(gesp, cod_modelo, modelo):
    conexao = conectar_banco_dados_clientes()
    cursor = conexao.cursor()

    status = "DISPONÍVEL"

    cursor.execute(
    """
    INSERT INTO TabelaClientes
    (gesp, cod_modelo, modelo, status)
    VALUES (?, ?, ?, ?)
    """, (gesp, cod_modelo, modelo, status)
    )

    conexao.commit()
    conexao.close()



def listar_clientes():
    conexao = conectar_banco_dados_clientes()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT * FROM TabelaClientes
    ORDER BY gesp ASC
    """
    )
    
    clientes = cursor.fetchall()
 
    cursor.close()

    return clientes