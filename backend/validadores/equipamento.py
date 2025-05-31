def validar_cadastro_equipamentos(gesp, codigo_modelo, modelo):
    if not gesp or not codigo_modelo or not modelo:
        return False, "Todos os Campos Devem Estar Preenchidos."
    if len(gesp.strip()) < 10:
        return False, "O GESP Deve Ter no Minímo 10 Caracteres."
    
    return True, "Cadastro Válido."


def validar_formulario_emprestimo(codigo_cliente, gesp, contrato):
    if not codigo_cliente or not gesp or not contrato:
        return False, "Todos os Campos Devem Estar Preenchidos."
    if len(gesp.strip()) < 10:
        return False, "O GESP Deve Ter no Minímo 10 Caracteres."
    
    if not codigo_cliente.isdigit():
        return False, "O Código do Cliente Dever Ser Númerico."
    if not contrato.isdigit():
        return False, "O Contrato Dever Ser Númerico."


    return True, "Empréstimo Válido."
    
def validar_formulario_devolver(codigo_cliente, gesp, modelo):
    if not codigo_cliente or not gesp or not modelo:
        return False, "Todos os Campos Devem Estar Preenchidos."
    if len(gesp.strip()) < 10:
        return False, "O GESP Deve Ter no Minímo 10 Caracteres."
    
    if not codigo_cliente.isdigit():
        return False, "O Código do Cliente Dever Ser Númerico."


    return True, "Devolução Válida."


def validar_dar_baixa(gesp):
    if not gesp:
        return False, "Preencha o Campo GESP."
    if len(gesp.strip()) < 10:
        return False, "O GESP Deve Ter no Minímo 10 Caracteres."
    
    return True, "Baixa Válida."