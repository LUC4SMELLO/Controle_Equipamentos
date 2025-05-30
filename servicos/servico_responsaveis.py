from database.responsaveis import *

def responsavel_existe(codigo_cliente):
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaResponsaveis
    WHERE codigo_cliente = ?
    """, (codigo_cliente,)
    )

    responsavel = cursor.fetchone()
    conexao.close()

    if responsavel:
        return True, "Responsável Já Existe."
    else:
        return False, "Nenhum Responsável Encontrado."