import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.interface import iniciar_interface


if __name__ == "__main__":
    iniciar_interface()
 