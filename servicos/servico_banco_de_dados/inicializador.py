from database.equipamentos_emprestados import (
    criar_tabela_equipamentos_emprestados
)
from database.equipamentos import (
    criar_tabela_equipamentos
)
from database.responsaveis import (
    criar_tabela_responsaveis
)
from database.clientes import (
    criar_tabela_clientes
)


def inicializador_bancos_dados():
    criar_tabela_equipamentos_emprestados()
    criar_tabela_equipamentos()
    criar_tabela_responsaveis()
    criar_tabela_clientes()