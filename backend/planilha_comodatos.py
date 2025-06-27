import pandas as pd

caminho = "O:/FATURAMENTO/Lucas/Controle_Equipamentos/comodato.xlsx"

dados = pd.read_excel(caminho, sheet_name="Comodato", header=2)

colunas_para_excluir = [
    "Território",
    "Distribuidor",
    "CPF",
    "CNPJ",
    "Razão Social",
    "Nome Fantasia",
    "GEC",
    "SubCanal",
    "Cidade",
    "Série",
    "Quant, Portas", 
    "Logomarca",
    "Qtde",
    "Emissão",
    "Vencimento",
    "Vendedor",
    "Rota",
    "NFe",
    "Conservação",
    "COD,CIA", 
    "DESC,CIA",
    "KPI",
    "DESC,KPI",
    2506,
    2505,
    2504
]

colunas_para_renomear = {
    "Matrícula Cliente": "Código Cliente",
    "Nr Equipamento": "Equipamento",
    "Código": "Código Modelo",
    "Produto": "Modelo"
    }

dados.drop(colunas_para_excluir, axis=1, inplace=True)
dados.rename(columns=colunas_para_renomear, inplace=True)


print(dados)