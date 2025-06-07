from database.equipamentos import conectar_banco_dados_equipamentos
from database.responsaveis import conectar_banco_dados_responsaveis

def mostrar_listagem_equipamentos_back(modelo_filtro="", status_selecionados=[], gesp_filtro=""):
    """FAZ UMA CONSULTA SQL COM BASE NOS FILTROS"""

    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    consulta_sql = "SELECT gesp, codigo_modelo, modelo, status FROM TabelaEquipamentos WHERE 1=1"
    parametros = []

    if modelo_filtro:
        consulta_sql += " AND modelo LIKE ?"
        parametros.append('%' + modelo_filtro + '%')

    if status_selecionados and "TODOS" not in status_selecionados:
        marcadores = ",".join("?" * len(status_selecionados))
        consulta_sql += f" AND status IN ({marcadores})"
        parametros.extend(status_selecionados)

    if gesp_filtro:
        consulta_sql += " AND gesp LIKE ?"
        parametros.append('%' + gesp_filtro + '%')

    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado


def mostrar_listagem_responsaveis_back(codigo_cliente_filtro=""):
    """FAZ UMA CONSULTA SQL COM BASE NOS FILTROS"""

    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    consulta_sql = "SELECT codigo_cliente, nome, cpf, email FROM TabelaResponsaveis WHERE 1=1"
    parametros = []

    # if modelo_filtro:
    #     consulta_sql += " AND modelo LIKE ?"
    #     parametros.append('%' + modelo_filtro + '%')

    # if status_selecionados and "TODOS" not in status_selecionados:
    #     marcadores = ",".join("?" * len(status_selecionados))
    #     consulta_sql += f" AND status IN ({marcadores})"
    #     parametros.extend(status_selecionados)

    if codigo_cliente_filtro:
        consulta_sql += " AND codigo_cliente LIKE ?"
        parametros.append('%' + codigo_cliente_filtro + '%')

    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado
