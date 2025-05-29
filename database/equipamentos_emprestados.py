import sqlite3

from equipamentos import atualizar_status_equipamento

def conectar_banco_dados_equipamentos_emprestados():
    return sqlite3.connect("TabelaEquipamentosEmprestados.db")


def criar_tabela_equipamentos_emprestados():
    conexao = conectar_banco_dados_equipamentos_emprestados()
    cursor = conexao.cursor()
    
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaEquipamentosEmprestados (
        gesp VARCHAR(10) NOT NULL,
        codigo_cliente VARCHAR(6),
        contrato VARCHAR(10),
        FOREIGN KEY (gesp) REFERENCES TabelaEquipamentos(gesp)
    )
    """
    )

    # CONFIRMA O COMANDO SQL E FECHA A CONEXÃO
    conexao.commit()
    cursor.close()


def emprestar_equipamento(gesp, codigo_cliente, contrato):
    conexao = conectar_banco_dados_equipamentos_emprestados()
    cursor = conexao.cursor()

    status = "Emprestado"

    cursor.execute(
    """
    INSERT into TabelaEquipamentosEmprestados (gesp, codigo_cliente, contrato)
    VALUES (?, ?, ?)
    """,(gesp, codigo_cliente, contrato)
    )

    atualizar_status_equipamento(gesp, status)

    conexao.commit()
    cursor.close()


def listar_equipamentos_emprestados():
    conexao = conectar_banco_dados_equipamentos_emprestados()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT * FROM TabelaEquipamentosEmprestados
    ORDER BY gesp ASC
    """
    )
    
    equipamentos = cursor.fetchall()
 
    cursor.close()

    return equipamentos