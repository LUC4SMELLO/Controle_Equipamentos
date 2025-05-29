from database.responsaveis import *


def cadastrar_responsavel_back(codigo_cliente, nome, cpf, email):
    inserir_responsavel(codigo_cliente, nome, cpf, email)
