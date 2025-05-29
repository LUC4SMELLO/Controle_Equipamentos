from database.equipamentos import inserir_equipamento
from database.equipamentos_emprestados import emprestar_equipamento


def cadastrar_equipamento_back(gesp, codigo_modelo, modelo):
    inserir_equipamento(gesp, codigo_modelo, modelo)


def emprestrar_equipamento_back(gesp, codigo_cliente, contrato):
    emprestar_equipamento(gesp, codigo_cliente, contrato)