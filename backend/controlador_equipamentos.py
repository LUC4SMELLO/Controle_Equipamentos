from database.equipamentos import inserir_equipamento, atualizar_status_equipamento
from database.equipamentos_emprestados import emprestar_equipamento, devolver_equipamento


def cadastrar_equipamento_back(gesp, codigo_modelo, modelo):
    inserir_equipamento(gesp, codigo_modelo, modelo)


def emprestrar_equipamento_back(gesp, codigo_cliente, contrato):
    emprestar_equipamento(gesp, codigo_cliente, contrato)


def devolver_equipamento_back(gesp, codigo_cliente):
    devolver_equipamento(gesp, codigo_cliente)

def dar_baixa_equipamento_back(gesp):
    status = "BAIXADO"
    atualizar_status_equipamento(gesp, status)

