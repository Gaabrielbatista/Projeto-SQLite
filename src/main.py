from database import *
from tabulate import tabulate
from os import system

system("cls")

# Mostra tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)

# Pausa para visualização
def pausar():
    input("\nPressione Enter para continuar...\n ")

# Cria tabela
criar_tabela()

# Adiciona 10 Carros
inserir_carro('Fiat Uno', 2010, 'Prata'),
inserir_carro('Chevrolet Onix', 2022, 'Preto'),
inserir_carro('Volkswagen Gol', 2015, 'Branco'),
inserir_carro('Hyundai HB20', 2020, 'Branco'),
inserir_carro('Toyota Corolla', 2021, 'Cinza'),
inserir_carro('Ford Ka', 2017, 'Vermelho'),
inserir_carro('Renault Sandero', 2019, 'Verde'),
inserir_carro('Jeep Compass', 2023, 'Preto'),
inserir_carro('Honda Civic', 2018, 'Azul'),
inserir_carro('Nissan March', 2014, 'Amarelo');
exibir_dados()

pausar()

# Atualiza 4 carros
atualizar_carro(1, modelo="Toyota Corolla")
atualizar_carro(2, ano=2023)
atualizar_carro(3, cor="Azul")
atualizar_carro(4, cor="Prata", ano=2020, modelo="Honda Civic")
exibir_dados()

pausar()

# Deleta 4 carros
deletar_carro(10)
deletar_carro(9)
deletar_carro(8)
deletar_carro(7)

exibir_dados()
