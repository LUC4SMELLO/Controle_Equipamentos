import sqlite3

def conectar_banco_dados_equipamentos():
    return sqlite3.connect("TabelaEquipamentos.db")


def criar_tabela_equipamentos():
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaEquipamentos (
        gesp VARCHAR(10),
        cod_modelo VARCHAR(10),
        modelo VARCHAR(10),
        status VARCHAR(10)
        )
    """
    )

    # CONFIRMA O COMANDO SQL E FECHA A CONEXÃO
    conexao.commit()
    cursor.close()


def inserir_equipamento(gesp, cod_modelo, modelo):
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    INSERT INTO TabelaEquipamentos
    (gesp, cod_modelo, modelo)
    VALUES (?, ?, ?)
    """, (gesp, cod_modelo, modelo)
    )

    conexao.commit()
    conexao.close()


def listar_equipamentos():
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT * FROM TabelaEquipamentos
    ORDER BY gesp ASC
    """
    )
    
    equipamentos = cursor.fetchall()
 
    cursor.close()

    return equipamentos
