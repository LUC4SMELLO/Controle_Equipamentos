from database.equipamentos import *
from database.equipamentos_emprestados import *


def conectar():
    return sqlite3.connect("TabelaEquipamentos.db")

def buscar_filtrado(modelo_filtro="", status_selecionados=[]):
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT gesp, codigo_modelo, modelo, status FROM TabelaEquipamentos WHERE 1=1"
    parametros = []

    if modelo_filtro:
        sql += " AND modelo LIKE ?"
        parametros.append('%' + modelo_filtro + '%')

    if status_selecionados and "TODOS" not in status_selecionados:
        marcadores = ",".join("?" * len(status_selecionados))
        sql += f" AND status IN ({marcadores})"
        parametros.extend(status_selecionados)

    cursor.execute(sql, parametros)
    resultado = cursor.fetchall()
    conn.close()
    return resultado
