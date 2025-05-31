from database.clientes import *

def cliente_existe(codigo_cliente):
    conexao = conectar_banco_dados_clientes()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaClientes
    WHERE codigo_cliente = ?
    """, (codigo_cliente,)
    )

    cliente = cursor.fetchone()
    conexao.close()

    if cliente:
        return True, "Cliente Encontrado."
    else:
        return False, "Cliente Não Encontrado."