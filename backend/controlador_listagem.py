from database.equipamentos import *
from database.equipamentos_emprestados import *


def buscar_dados(filtro_modelo=""):
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    if filtro_modelo:
        cursor.execute("""
            SELECT gesp, codigo_modelo, modelo
            FROM TabelaEquipamentos
            WHERE modelo LIKE ?
            """, ('%' + filtro_modelo + '%',)
            )
    else:
        cursor.execute(
        """
        SELECT gesp, codigo_modelo, modelo
        FROM TabelaEquipamentos
        """
        )

    dados = cursor.fetchall()
    conexao.close()

    return dados
