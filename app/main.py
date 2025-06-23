import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.interface import iniciar_interface
from servicos.servico_banco_de_dados.inicializador import inicializador_bancos_dados
from backend.binds.cofiguracao_binds import configurar_todas_binds


if __name__ == "__main__":
    inicializador_bancos_dados()
    configurar_todas_binds()
    iniciar_interface()
 