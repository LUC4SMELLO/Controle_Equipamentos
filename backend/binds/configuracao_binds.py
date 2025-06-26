from frontend.janela import janela

from frontend.frame_equipamentos import (
    entry_gesp_cadastrar,
    entry_codigo_modelo_cadastrar,
    entry_modelo_cadastrar,
    botao_cadastrar_equipamento,
    cadastrar_equipamento_gui,
    

    entry_gesp_alterar,
    entry_codigo_modelo_alterar,
    botao_buscar_equipamento,
    buscar_equipamento_gui,
    entry_modelo_alterar,
    botao_alterar_equipamento,
    alterar_informacoes_equipamento_gui,

    entry_gesp_excluir,
    entry_codigo_modelo_excluir,
    entry_modelo_excluir,
    botao_excluir_equipamento,
    excluir_equipamento_gui
)
from frontend.frame_responsavel import(
    entry_codigo_cliente_cadastrar,
    entry_nome_cadastrar,
    entry_cpf_cadastrar,
    entry_email_cadastrar,
    botao_cadastrar_responsavel,
    cadastrar_responsavel_gui,

    entry_codigo_cliente_alterar,
    botao_buscar_responsavel,
    buscar_responsavel_gui,
    entry_nome_alterar,
    entry_cpf_alterar,
    entry_email_alterar,
    botao_alterar_responsavel,
    alterar_informacoes_responsavel_gui,

    entry_codigo_cliente_excluir,
    entry_nome_excluir,
    entry_cpf_excluir,
    entry_email_excluir,
    botao_excluir_responsavel,
    excluir_responsavel_gui
)

from frontend.frame_emprestar import (
    entry_codigo_cliente_emprestrar,
    entry_gesp_emprestar,
    entry_contrato_emprestrar,
    botao_emprestrar_equipamento,
    emprestrar_equipamento_gui
)

from frontend.frame_devolver import (
    entry_codigo_cliente_devolver,
    entry_gesp_a_devolver,
    entry_modelo_devolver,
    botao_devolver_equipamento,
    devolver_equipamento_gui
)

from frontend.frame_baixa import (
    entry_gesp_a_dar_baixa,
    botao_dar_baixa,
    dar_baixa_equipamento_gui
)

from frontend.frame_listagem import (
    #EQUIPAMENTOS
    entry_gesp_listagem,
    entry_modelo_listagem,
    botao_listar_equipamentos,
    mostrar_listagem_equipamentos_gui,

    # EQUIPAMENTOS EMPRESTADOS
    frame_listagem_equipamentos_emprestados,
    entry_gesp_equipamentos_emprestados,
    entry_contrato_equipamentos_emprestados,
    entry_codigo_cliente_equipamentos_emprestados,
    entry_nome_equipamentos_emprestados,
    entry_cpf_equipamentos_emprestados,
    entry_email_equipamentos_emprestados,
    botao_listar_equipamentos_emprestados,
    mostrar_listagem_equipamentos_emprestados_gui,

    # EQUIPAMENTOS RESPONSÁVEIS
    entry_codigo_cliente_responsaveis,
    entry_nome_responsaveis,
    entry_cpf_responsaveis,
    entry_email_responsaveis,
    botao_listar_responsaveis,
    mostrar_listagem_responsaveis_gui

)
    

def foco_no_proximo_widget(event, proximo_widget=None, executar_funcao=None):
    if proximo_widget and executar_funcao:
        proximo_widget.focus_set()
        executar_funcao()

    elif proximo_widget:
        proximo_widget.focus_set()

    else:
        executar_funcao()


def binds_equipamentos():
    entry_gesp_cadastrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_codigo_modelo_cadastrar))
    entry_codigo_modelo_cadastrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_modelo_cadastrar))
    entry_modelo_cadastrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_cadastrar_equipamento))
    botao_cadastrar_equipamento.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=cadastrar_equipamento_gui))

    entry_gesp_alterar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_buscar_equipamento))
    botao_buscar_equipamento.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_codigo_modelo_alterar, executar_funcao=buscar_equipamento_gui))
    entry_codigo_modelo_alterar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_modelo_alterar))
    entry_modelo_alterar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_alterar_equipamento))
    botao_alterar_equipamento.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=alterar_informacoes_equipamento_gui))

    entry_gesp_excluir.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_codigo_modelo_excluir))
    entry_codigo_modelo_excluir.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_modelo_excluir))
    entry_modelo_excluir.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_excluir_equipamento))
    botao_excluir_equipamento.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=excluir_equipamento_gui))

def binds_responsavel():
    entry_codigo_cliente_cadastrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_nome_cadastrar))
    entry_nome_cadastrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_cpf_cadastrar))
    entry_cpf_cadastrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_email_cadastrar))
    entry_email_cadastrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_cadastrar_responsavel))
    botao_cadastrar_responsavel.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=cadastrar_responsavel_gui))

    entry_codigo_cliente_alterar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_buscar_responsavel))
    botao_buscar_responsavel.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_nome_alterar, executar_funcao=buscar_responsavel_gui))
    entry_nome_alterar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_cpf_alterar))
    entry_cpf_alterar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_email_alterar))
    entry_email_alterar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_alterar_responsavel))
    botao_alterar_responsavel.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=alterar_informacoes_responsavel_gui))
    
    entry_codigo_cliente_excluir.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_nome_excluir))
    entry_nome_excluir.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_cpf_excluir))
    entry_cpf_excluir.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_email_excluir))
    entry_email_excluir.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_excluir_responsavel))
    botao_excluir_responsavel.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=excluir_responsavel_gui))

def binds_emprestar_equipamento():
    entry_codigo_cliente_emprestrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_gesp_emprestar))
    entry_gesp_emprestar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_contrato_emprestrar))
    entry_contrato_emprestrar.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_emprestrar_equipamento))
    botao_emprestrar_equipamento.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=emprestrar_equipamento_gui))

def binds_devolver_equipamentos():
    entry_codigo_cliente_devolver.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_gesp_a_devolver))
    entry_gesp_a_devolver.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_modelo_devolver))
    entry_modelo_devolver.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_devolver_equipamento))
    botao_devolver_equipamento.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=devolver_equipamento_gui))
    
def binds_dar_baixa_equipamento():
    entry_gesp_a_dar_baixa.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_dar_baixa))
    botao_dar_baixa.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=dar_baixa_equipamento_gui))
    
def binds_listagem_equipamentos():
    entry_gesp_listagem.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_modelo_listagem))
    entry_modelo_listagem.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_listar_equipamentos))
    botao_listar_equipamentos.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=mostrar_listagem_equipamentos_gui))

def binds_listagem_equipamentos_emprestados():
    entry_gesp_equipamentos_emprestados.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_contrato_equipamentos_emprestados))
    entry_contrato_equipamentos_emprestados.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_codigo_cliente_equipamentos_emprestados))
    entry_codigo_cliente_equipamentos_emprestados.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_nome_equipamentos_emprestados))
    entry_nome_equipamentos_emprestados.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_cpf_equipamentos_emprestados))
    entry_cpf_equipamentos_emprestados.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_email_equipamentos_emprestados))
    entry_email_equipamentos_emprestados.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_listar_equipamentos_emprestados))
    botao_listar_equipamentos_emprestados.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=mostrar_listagem_equipamentos_emprestados_gui))

def binds_listagem_responsaveis():
    entry_codigo_cliente_responsaveis.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_nome_responsaveis))
    entry_nome_responsaveis.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_cpf_responsaveis))
    entry_cpf_responsaveis.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=entry_email_responsaveis))
    entry_email_responsaveis.bind("<Return>", lambda event: foco_no_proximo_widget(event, proximo_widget=botao_listar_responsaveis))
    botao_listar_responsaveis.bind("<Return>", lambda event: foco_no_proximo_widget(event, executar_funcao=mostrar_listagem_responsaveis_gui))
    

def configurar_todas_binds():

    janela.focus_set()

    binds_equipamentos()
    binds_responsavel()
    binds_emprestar_equipamento()
    binds_devolver_equipamentos()
    binds_dar_baixa_equipamento()
    binds_listagem_equipamentos()
    binds_listagem_equipamentos_emprestados()
    binds_listagem_responsaveis()