import os
import sqlite3

# Funções para interface

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Pausa para visualização
def pausar():
    input("\nPressione Enter para continuar...")

# Funções para database

# Valida os dados do carro
def validar_dados_carro(modelo=None, ano=None, cor=None):
    # Verificação str e int

    # modelo
    if modelo is not None:
        if not isinstance(modelo, str):
            raise Exception("Erro: Modelo deve ser do tipo string.")
        
    # ano
    if ano is not None:
        if type(ano) is not int:
            raise Exception("Erro: Ano deve ser do tipo int.")
        if (1900 > ano or ano > 2030):
            raise Exception("Erro: O ano precisa estar entre 1900 e 2030.")
        
    # cor
    if cor is not None:
        if not isinstance(cor, str):
            raise Exception("Erro: Cor deve ser do tipo string.")
        
    # Validações
    modelo = (modelo.strip().capitalize() if type(modelo) == str else None)
    cor = (cor.strip().capitalize() if type(cor) == str else None)
    
    return (modelo, ano, cor)
    
# Verifica o id
def verificar_id_existe(id):
    if type(id) is not int:
        raise Exception("Erro: Id não pode estar vazio")
    
    conn = sqlite3.connect("carros.db")
    cur = conn.cursor()

    cur.execute('''SELECT id_carro FROM Carros WHERE id_carro = ?''', (id,))
    resultado = cur.fetchone()

    conn.close()

    if not resultado:
        raise Exception("Erro: Id não encontrado")
    
