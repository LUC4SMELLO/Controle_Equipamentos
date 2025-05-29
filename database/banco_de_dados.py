from equipamentos import *
from responsaveis import *

# EQUIPAMENTOS
conectar_banco_dados_equipamentos()
criar_tabela_equipamentos()

# inserir_equipamento("GESP101013", "38", "220L")
# inserir_equipamento("GESP101012", "38", "220L")
# inserir_equipamento("GESP101015", "38", "220L")
# inserir_equipamento("GESP101014", "38", "220L")
# inserir_equipamento("GESP101052", "38", "220L")


##RESPONSAVEIS
conectar_banco_dados_responsaveis()
criar_tabela_responsaveis()

# inserir_responsavel("12125", "Lucas", "11111111100", "emaiteste@gmail.com")
# inserir_responsavel("12126", "Tiago", "11111111100", "emaiteste@gmail.com")
# inserir_responsavel("12127", "Lápis", "11111111100", "emaiteste@gmail.com")
# inserir_responsavel("12128", "Macarrao", "11111111100", "emaiteste@gmail.com")
# inserir_responsavel("12129", "Garrafa", "11111111100", "emaiteste@gmail.com")

print("EQUIPAMENTOS:")
for equipamento in listar_equipamentos():
    print(equipamento)

print("")

print("RESPONSÁVEIS:")
for responsavel in listar_responsaveis():
    print(responsavel)


