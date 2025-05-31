from database.equipamentos import *
from database.equipamentos_emprestados import *

def equipamento_existe(gesp):
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaEquipamentos
    WHERE gesp = ?
    """, (gesp,)
    )

    existe = cursor.fetchone()
    conexao.close()

    if existe:
        return True, "Equipamento Existe."
    else:
        return False, "Equipamento Não Encontrado."

def equipamento_disponivel(gesp):
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaEquipamentos
    WHERE gesp = ? AND status = "DISPONÍVEL"
    """, (gesp,)
    )

    disponivel = cursor.fetchone()
    conexao.close()

    if disponivel:
        return True, "Equipamento Disponível."
    else:
        return False, "Equipamento Não Disponível."
    
def equipamento_emprestado(gesp, codigo_cliente):
    conexao = conectar_banco_dados_equipamentos_emprestados()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaEquipamentosEmprestados
    WHERE gesp = ? and codigo_cliente = ?
    """, (gesp, codigo_cliente)
    )

    emprestado = cursor.fetchone()
    conexao.close()

    if emprestado:
        return True, "Equipamento Já Está Emprestado."
    else:
        return False, "Equipamento Não Está Emprestado."
    
def equipamento_baixado(gesp):
    conexao = conectar_banco_dados_equipamentos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    SELECT 1 FROM TabelaEquipamentos
    WHERE gesp = ? AND status = "BAIXADO"
    """, (gesp,)
    )

    emprestado = cursor.fetchone()
    conexao.close()

    if emprestado:
        return True, "Equipamento Já Está Baixado."
    else:
        return False, "Equipamento Não Está Baixado."
