import sqlite3

def conectar_banco_dados_responsaveis():
    return sqlite3.connect("TabelaResponsaveis.db")


def criar_tabela_responsaveis():
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaResponsaveis (
        codigo_cliente VARCHAR(6) NOT NULL,
        nome VARCHAR(50),
        cpf VARCHAR(11),
        email VARCHAR(50),
  		PRIMARY KEY (codigo_cliente)
        FOREIGN KEY (codigo_cliente) REFERENCES TabelaClientes(codigo_cliente)
    )
    """
    )

    conexao.commit()
    cursor.close()

def inserir_responsavel(codigo_cliente, nome, cpf, email):
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    cursor.execute(
    """
    INSERT INTO TabelaResponsaveis 
    (codigo_cliente, nome, cpf, email)
    VALUES (?, ?, ?, ?)
    """, (codigo_cliente, nome, cpf, email)
    )

    conexao.commit()
    cursor.close()

def alterar_informacoes_responsavel(codigo_cliente, nome, cpf, email):
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    cursor.execute(
    """
    UPDATE TabelaResponsaveis
    SET nome = ?, cpf = ?, email = ?
    WHERE codigo_cliente = ?
    """, (nome, cpf, email, codigo_cliente)
    )

    conexao.commit()
    conexao.close()
    

def listar_responsaveis():
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT * FROM TabelaResponsaveis
    ORDER BY codigo_cliente
    """
    )

    clientes = cursor.fetchall()

    cursor.close()

    return clientes
