from database.responsaveis import *


def cadastrar_responsavel_back(codigo_cliente, nome, cpf, email):
    inserir_responsavel(codigo_cliente, nome, cpf, email)

def alterar_informacoes_responsavel_back(codigo_cliente, nome, cpf, email):
    alterar_informacoes_responsavel(codigo_cliente, nome, cpf, email)

def excluir_responsavel_back(codigo_cliente, nome, cpf, email):
    excluir_responsavel(codigo_cliente, nome, cpf, email)