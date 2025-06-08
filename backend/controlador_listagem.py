from database.equipamentos import conectar_banco_dados_equipamentos
from database.equipamentos_emprestados import conectar_banco_dados_equipamentos_emprestados
from database.responsaveis import conectar_banco_dados_responsaveis
from database.clientes import conectar_banco_dados_clientes

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

def mostrar_listagem_equipamentos_emprestados_back(
        gesp_filtro="", contrato_filtro="", codigo_cliente_filtro="",
        nome_filtro="", cpf_filtro="", email_filtro="",
        ):
    
    """FAZ UMA CONSULTA SQL COM BASE NOS FILTROS"""

    conexao = conectar_banco_dados_equipamentos_emprestados()
    cursor = conexao.cursor()

    cursor.execute("ATTACH DATABASE 'TabelaResponsaveis.db' AS resp")

    consulta_sql = """
    SELECT ee.gesp, ee.codigo_cliente, ee.contrato, r.nome, r.cpf, r.email
    from TabelaEquipamentosEmprestados as ee
    JOIN resp.TabelaResponsaveis as r
    on r.codigo_cliente = ee.codigo_cliente
    """

    parametros = []

    if gesp_filtro:
        consulta_sql += " AND ee.gesp LIKE ?"
        parametros.append('%' + gesp_filtro + '%')

    if contrato_filtro:
        consulta_sql += " AND ee.contrato LIKE ?"
        parametros.append('%' + contrato_filtro + '%')

    if codigo_cliente_filtro:
        consulta_sql += " AND ee.codigo_cliente LIKE ?"
        parametros.append('%' + codigo_cliente_filtro + '%')

    if nome_filtro:
        consulta_sql += " AND r.nome LIKE ?"
        parametros.append('%' + nome_filtro + '%')

    if cpf_filtro:
        consulta_sql += " AND r.cpf LIKE ?"
        parametros.append('%' + cpf_filtro + '%')

    if email_filtro:
        consulta_sql += " AND r.email LIKE ?"
        parametros.append('%' + email_filtro + '%')

    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado


def mostrar_listagem_responsaveis_back(codigo_cliente_filtro="", nome_filtro="", cpf_filtro="", email_filtro=""):
    """FAZ UMA CONSULTA SQL COM BASE NOS FILTROS"""

    conexao = conectar_banco_dados_responsaveis()
    cursor = conexao.cursor()

    consulta_sql = "SELECT codigo_cliente, nome, cpf, email FROM TabelaResponsaveis WHERE 1=1"
    parametros = []

    if codigo_cliente_filtro:
        consulta_sql += " AND codigo_cliente LIKE ?"
        parametros.append('%' + codigo_cliente_filtro + '%')

    if nome_filtro:
        consulta_sql += " AND nome LIKE ?"
        parametros.append('%' + nome_filtro + '%')

    if cpf_filtro:
        consulta_sql += " AND cpf LIKE ?"
        parametros.append('%' + cpf_filtro + '%')

    if email_filtro:
        consulta_sql += " AND email LIKE ?"
        parametros.append('%' + email_filtro + '%')

    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado


def mostrar_listagem_clientes_back(codigo_cliente_filtro="", razao_social=""):
    """FAZ UMA CONSULTA SQL COM BASE NOS FILTROS"""

    conexao = conectar_banco_dados_clientes()
    cursor = conexao.cursor()

    consulta_sql = "SELECT codigo_cliente, razao_social FROM TabelaClientes WHERE 1=1"
    parametros = []

    if codigo_cliente_filtro:
        consulta_sql += " AND codigo_cliente LIKE ?"
        parametros.append('%' + codigo_cliente_filtro + '%')

    if razao_social:
        consulta_sql += " AND razao_social LIKE ?"
        parametros.append('%' + razao_social + '%')

    cursor.execute(consulta_sql, parametros)
    resultado = cursor.fetchall()
    conexao.close()

    return resultado