from database.responsaveis import *

def responsavel_existe(codigo_cliente, nome=None, cpf=None, email=None):
    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    consulta = "SELECT 1 FROM TabelaResponsaveis WHERE codigo_cliente = ?"
    parametros = [codigo_cliente]
    
    if nome is not None:
        consulta += "AND nome = ?"
        parametros.append(nome)

    if cpf is not None:
        consulta += "AND cpf = ?"
        parametros.append(cpf)

    if email is not None:
        consulta += "AND email = ?"
        parametros.append(email)

    cursor.execute(consulta, parametros)

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