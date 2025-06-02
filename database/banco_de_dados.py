import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clientes import (
    conectar_banco_dados_clientes,
    criar_tabela_clientes,
    inserir_cliente,
    listar_clientes
)

from equipamentos import (
    conectar_banco_dados_equipamentos, 
    criar_tabela_equipamentos, 
    inserir_equipamento, 
    atualizar_status_equipamento,
    listar_equipamentos 
)

from responsaveis import (
    conectar_banco_dados_responsaveis, 
    criar_tabela_responsaveis, 
    inserir_responsavel, 
    listar_responsaveis
)

from equipamentos_emprestados import (
    conectar_banco_dados_equipamentos_emprestados,
    criar_tabela_equipamentos_emprestados,
    emprestar_equipamento,
    listar_equipamentos_emprestados,
    devolver_equipamento
)

## CLIENTES
conectar_banco_dados_clientes()
criar_tabela_clientes()

# inserir_cliente(1, "Lucas Mello")
# inserir_cliente(2, "João")
# inserir_cliente(550, "Marcos")

## EQUIPAMENTOS
conectar_banco_dados_equipamentos()
criar_tabela_equipamentos()

# inserir_equipamento("GESP876543", "1234", "56L")
# inserir_equipamento("GESP234567", "9876", "123L")
# inserir_equipamento("GESP543210", "4321", "78L")
# inserir_equipamento("GESP901234", "5678", "901L")
# inserir_equipamento("GESP112233", "9988", "45L")
# inserir_equipamento("GESP445566", "1122", "678L")
# inserir_equipamento("GESP778899", "3344", "90L")
# inserir_equipamento("GESP001122", "5566", "234L")
# inserir_equipamento("GESP334455", "7788", "56L")
# inserir_equipamento("GESP667788", "9900", "789L")
# inserir_equipamento("GESP990011", "1212", "12L")
# inserir_equipamento("GESP223344", "3434", "345L")
# inserir_equipamento("GESP556677", "5656", "67L")
# inserir_equipamento("GESP889900", "7878", "890L")
# inserir_equipamento("GESP100100", "0101", "10L")
# inserir_equipamento("GESP202020", "2323", "234L")
# inserir_equipamento("GESP303030", "4545", "56L")
# inserir_equipamento("GESP404040", "6767", "789L")
# inserir_equipamento("GESP505050", "8989", "90L")
# inserir_equipamento("GESP606060", "0011", "123L")
# inserir_equipamento("GESP707070", "2233", "45L")
# inserir_equipamento("GESP808080", "4455", "678L")
# inserir_equipamento("GESP909090", "6677", "90L")
# inserir_equipamento("GESP010101", "8899", "234L")
# inserir_equipamento("GESP121212", "1010", "56L")
# inserir_equipamento("GESP343434", "3232", "789L")
# inserir_equipamento("GESP565656", "5454", "12L")
# inserir_equipamento("GESP787878", "7676", "345L")
# inserir_equipamento("GESP135790", "1357", "890L")
# inserir_equipamento("GESP246802", "2468", "10L")
# inserir_equipamento("GESP975310", "9753", "234L")
# inserir_equipamento("GESP864201", "8642", "56L")
# inserir_equipamento("GESP753198", "7531", "789L")
# inserir_equipamento("GESP642087", "6420", "90L")
# inserir_equipamento("GESP531976", "5319", "123L")
# inserir_equipamento("GESP420865", "4208", "45L")
# inserir_equipamento("GESP319754", "3197", "678L")
# inserir_equipamento("GESP208643", "2086", "90L")
# inserir_equipamento("GESP197532", "1975", "234L")
# inserir_equipamento("GESP086421", "0864", "56L")
# inserir_equipamento("GESP369147", "3691", "789L")
# inserir_equipamento("GESP258036", "2580", "12L")
# inserir_equipamento("GESP147925", "1479", "345L")
# inserir_equipamento("GESP036814", "0368", "67L")
# inserir_equipamento("GESP925703", "9257", "890L")
# inserir_equipamento("GESP814692", "8146", "10L")
# inserir_equipamento("GESP703581", "7035", "234L")
# inserir_equipamento("GESP692470", "6924", "56L")
# inserir_equipamento("GESP581369", "5813", "789L")


## RESPONSAVEIS
conectar_banco_dados_responsaveis()
criar_tabela_responsaveis()

#inserir_responsavel("1", "Lucas", "11111111100", "emaiteste@gmail.com")


## EQUIPAMENTOS EMPRESTADOS
conectar_banco_dados_equipamentos_emprestados()
criar_tabela_equipamentos_emprestados()

print("CLIENTES:")
for cliente in listar_clientes():
    print(cliente)

print("")

print("EQUIPAMENTOS:")
for equipamento in listar_equipamentos():
    print(equipamento)

print("")

print("RESPONSÁVEIS:")
for responsavel in listar_responsaveis():
    print(responsavel)

print("")

print("EQUIPAMENTOS EMPRESTADOS:")
for equipamentos in listar_equipamentos_emprestados():
    print(equipamentos)



