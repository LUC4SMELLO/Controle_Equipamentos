from frontend.frames import *
import re

def validar_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if re.fullmatch(padrao, cpf):
        return True, "CPF válido"
    else:
        return False, "CPF inválido"
    
def validar_cadastro_responsavel(codigo_cliente, nome, cpf, email):
    if not codigo_cliente or not nome or not cpf or not email:
        return False, "Todos os Campos Devem Estar Preenchidos."

    valido, mensagem = validar_cpf(cpf)
    if not valido:
        return False, mensagem

    if "@" not in email:
        return False, "Informe um E-mail Válido."
    
    return True, "Cadastro Válido."
