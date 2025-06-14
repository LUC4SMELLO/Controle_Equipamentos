from database.equipamentos import (
    inserir_equipamento,
    atualizar_status_equipamento,
    alterar_informacoes_equipamento,
    excluir_equipamento
)
from database.equipamentos_emprestados import emprestar_equipamento, devolver_equipamento


def cadastrar_equipamento_back(gesp, codigo_modelo, modelo):
    inserir_equipamento(gesp, codigo_modelo, modelo)


def emprestar_equipamento_back(gesp, codigo_cliente, contrato):
    emprestar_equipamento(gesp, codigo_cliente, contrato)


def devolver_equipamento_back(gesp, codigo_cliente):
    devolver_equipamento(gesp, codigo_cliente)


def dar_baixa_equipamento_back(gesp):
    status = "BAIXADO"
    atualizar_status_equipamento(gesp, status)

def alterar_informacoes_equipamento_back(gesp, codigo_modelo, modelo):
    alterar_informacoes_equipamento(gesp, codigo_modelo, modelo)

def excluir_equipamento_back(gesp, codigo_modelo, modelo):
    excluir_equipamento(gesp, codigo_modelo, modelo)