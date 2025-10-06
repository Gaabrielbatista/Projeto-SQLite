from database import *
from main import exibir_dados
from os import system

system("cls")

# Mostra tabela
exibir_dados()

# Pausa para visualização
def pausar():
    input("\nPressione Enter para continuar...\n ")

if __name__ == "__main__":
    # Cria tabela
    criar_tabela()

    inserir_carro("carro_teste", 2024, "")

    exibir_dados()
    pausar()

    atualizar_carro(1, modelo="outro aí")