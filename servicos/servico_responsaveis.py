from database.responsaveis import *

def responsavel_existe(codigo_cliente, nome, cpf, email):
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaResponsaveis
    WHERE codigo_cliente = ? AND nome = ? AND cpf = ? AND email = ?
    """, (codigo_cliente, nome, cpf, email)
    )

    responsavel = cursor.fetchone()
    conexao.close()

    if responsavel:
        return True, "Responsável Já Existe."
    else:
        return False, "Nenhum Responsável Encontrado."
    
def buscar_e_retornar_responsavel(codigo_cliente):
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT codigo_cliente, nome, cpf, email FROM TabelaResponsaveis
    WHERE codigo_cliente = ?
    """, (codigo_cliente,)
    )

    resultado = cursor.fetchall()
    conexao.close()

    if not resultado:
        return None
    else:
        return resultado