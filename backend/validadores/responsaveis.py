import re

from validate_docbr import CPF

def validar_escrita_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if re.fullmatch(padrao, cpf):
        return True, "Escrita do CPF válida."
    else:
        return False, "Escrita do CPF inválida."

def validar_cpf(documento_cpf):
    cpf = CPF()

    cpf_validado = cpf.validate(documento_cpf)

    if cpf_validado:
        return True, "CPF Válido."
    else:
        return False, "CPF Inválido."
    
def validar_cadastro_responsavel(codigo_cliente, nome, cpf, email):
    if not codigo_cliente or not nome or not cpf or not email:
        return False, "Todos os Campos Devem Estar Preenchidos."

    valido, mensagem = validar_escrita_cpf(cpf)
    if not valido:
        return False, mensagem
    
    valido, mensagem = validar_cpf(cpf)
    if not valido:
        return False, mensagem

    if "@" not in email:
        return False, "Informe um E-mail Válido."
    
    if not codigo_cliente.isdigit():
        return False, "O Código do Cliente Dever Ser Númerico."
    
    return True, "Cadastro Válido."
