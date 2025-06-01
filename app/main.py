import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.interface import iniciar_interface
from servicos.servico_banco_de_dados.inicializador import inicializador_bancos_dados


inicializador_bancos_dados()


if __name__ == "__main__":
    iniciar_interface()
 