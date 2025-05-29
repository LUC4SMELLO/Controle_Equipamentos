from database.equipamentos import *


def cadastrar_equipamento_back(gesp, codigo_modelo, modelo):
    inserir_equipamento(gesp, codigo_modelo, modelo)


def emprestrar_equipamento_back(codigo_cliente, gesp, contrato):
    pass