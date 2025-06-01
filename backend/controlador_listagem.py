from database.equipamentos import conectar_banco_dados_equipamentos

def mostrar_listagem_back(modelo_filtro="", status_selecionados=[], gesp_filtro=""):
    """FAZ UMA CONSULTA SQL COM BASE NOS FILTROS"""

    conn = conectar_banco_dados_equipamentos()
    cursor = conn.cursor()

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
    conn.close()

    return resultado
