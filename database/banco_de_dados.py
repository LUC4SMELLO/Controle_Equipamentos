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

from servicos.servico_equipamentos import (
    buscar_e_retornar_equipamento
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



