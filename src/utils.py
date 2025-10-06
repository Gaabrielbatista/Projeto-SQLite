import os
from tabulate import tabulate

# Funções para main
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")
# Pausa para visualização
def pausar():
    input("\nPressione Enter para continuar...\n ")

# Funções para database
# Valida os dados do carro
def validar_dados_carro(modelo=None, ano=None, cor=None):
    # Verificação str e int
    if modelo is not None:
        if not isinstance(modelo, str):
            raise Exception("Erro: Modelo deve ser do tipo string.")
    if ano is not None:
        if type(ano) is not int:
            raise Exception("Erro: Ano deve ser do tipo int.")
    if cor is not None:
        if not isinstance(cor, str):
            raise Exception("Erro: Cor deve ser do tipo string.")
        
    # Validações
    modelo = (modelo.strip().capitalize() if type(modelo) == str else None)
    cor = (cor.strip().capitalize() if type(cor) == str else None)

    if not modelo:
        raise Exception("Erro: Modelo não pode estar vazio.")
    if 1900 > ano or ano > 2030:
        raise Exception("Erro: O ano precisa estar entre 1900 e 2030.")
    
    return (modelo, ano, cor)
    