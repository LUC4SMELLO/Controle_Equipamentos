import sqlite3

def conectar_banco_dados_equipamentos():
    return sqlite3.connect("TabelaEquipamentos.db")


def criar_tabela_equipamentos():
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaEquipamentos (
        gesp VARCHAR(10) NOT NULL,
        codigo_modelo VARCHAR(10),
        modelo VARCHAR(10),
        status VARCHAR(10),
        PRIMARY KEY (gesp)
    )
    """
    )

    # CONFIRMA O COMANDO SQL E FECHA A CONEXÃO
    conexao.commit()
    cursor.close()


def inserir_equipamento(gesp, codigo_modelo, modelo):
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    status = "DISPONÍVEL"

    cursor.execute(
    """
    INSERT INTO TabelaEquipamentos
    (gesp, codigo_modelo, modelo, status)
    VALUES (?, ?, ?, ?)
    """, (gesp, codigo_modelo, modelo, status)
    )

    conexao.commit()
    conexao.close()


def atualizar_status_equipamento(gesp, novo_status):
    try:
        conexao = conectar_banco_dados_equipamentos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        UPDATE TabelaEquipamentos
        SET status = ?
        WHERE gesp = ?
        """, (novo_status, gesp))

        # Confirmar e fechar
        conexao.commit()
        conexao.close()

    except sqlite3.Error as e:
        print("Erro ao atualizar o status:", e)


def alterar_informacoes_equipamento(gesp, codigo_modelo, modelo):
    try:
        conexao = conectar_banco_dados_equipamentos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        UPDATE TabelaEquipamentos
        SET codigo_modelo = ?, modelo = ?
        WHERE gesp = ?
        """, (codigo_modelo, modelo, gesp)
        )
        
        conexao.commit()
        conexao.close()
    except sqlite3.Error as e:
        print("Erro ao atualizar o status:", e)

def excluir_equipamento(gesp, codigo_modelo, modelo):
    try:
        conexao = conectar_banco_dados_equipamentos()
        cursor = conexao.cursor()

        cursor.execute(
        """
        DELETE FROM TabelaEquipamentos
        WHERE gesp = ? AND codigo_modelo = ? AND modelo = ?
        """, (gesp, codigo_modelo, modelo)
        )
        
        conexao.commit()
        conexao.close()

    except sqlite3.Error as e:
        print("Erro ao atualizar o status:", e)

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
