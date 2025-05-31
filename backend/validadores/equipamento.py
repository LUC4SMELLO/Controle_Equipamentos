from frontend.frames import *

def validar_cadastro_equipamentos(gesp, codigo_modelo, modelo):
    if not gesp or not codigo_modelo or not modelo:
        return False, "Todos os Campos Devem Estar Preenchidos."
    if len(gesp.strip()) < 10:
        return False, "O GESP Deve Ter no Minímo 10 Caracteres."
    
    return True, "Cadastro Válido."