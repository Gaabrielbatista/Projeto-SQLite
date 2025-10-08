from utils import limpar_terminal, pausar
from database import *
from tabulate import tabulate

# Mostra tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)


def interface_menu():
    criar_tabela()  #tirar

    while True:
        limpar_terminal()

        print("====== BANCO DE DADOS ======\n")
        print("[1] Inserir novo carro\n[2] Atualizar carro existente")
        print("[3] Deletar carro\n[4] Listar carros\n[5] Sair do programa")

        try:
            escolha = int(input("O que deseja fazer? "))
        except ValueError:
            print("Erro: Digite apenas números, tente novamente.")

            pausar()
            continue
        
        match escolha:
            # === OPÇÃO 1 - INSERIR ===
            case 1:
                print("\n[1] Inserir novo carro\n")

                try:
                    modelo = input("Digite o modelo do carro: ")
                    ano = int(input("\nDigite o ano do carro: "))
                    cor = input("\nDigite a cor do carro (não é obrigatório): ")
                    inserir_carro(modelo, ano, cor)
                    
                    pausar()

                except ValueError:
                    print("Erro: Para o ano digite apenas números, tente novamente.")
                    pausar()
                except Exception as e:
                    print(e)
                    pausar()
                    
            case 2:
                # === OPÇÃO 2 - ATUALIZAR ===
                print("\n[2] Atualizar carro existente\n")
                exibir_dados()

                try:
                    id_carro = int(input("ID do carro a atualizar: ").strip())
                    print("\nAtualizar:")
                    print("[1] Modelo\n[2] Ano\n[3] Cor\n[4] Tudo")

                    opcao_atualizar = int(input("Escolha: ").strip())

                    if opcao_atualizar == 1:
                        novo_modelo = input("Digite o novo modelo: ").strip()
                        atualizar_carro(id_carro, modelo=novo_modelo)

                    elif opcao_atualizar == 2:
                        novo_ano = int(input("Novo ano: ").strip())
                        atualizar_carro(id_carro, ano=novo_ano)

                    elif opcao_atualizar == 3:
                        nova_cor = input("Nova cor: ").strip()
                        atualizar_carro(id_carro, cor=nova_cor)
                        
                    elif opcao_atualizar == 4:
                        entrada = input("Digite tudo neste formato: modelo-ano-cor: ")
                        try:
                            novo_modelo, novo_ano, nova_cor = entrada.split("-")
                            novo_ano = int(novo_ano)
                            atualizar_carro(id_carro, modelo=novo_modelo, ano=novo_ano, cor=nova_cor)
                        except ValueError:
                            print("Formato inválido. Use modelo-ano-cor e ano deve ser números.")
                            pausar()

                            continue

                    else:
                        print("Opção inválida.")
                        pausar()
                        continue

                    pausar()

                except ValueError:
                    print("Erro: Digite apenas números.")
                    pausar()

                except Exception as e:
                    print(e)
                    pausar()
                    
            case 3:
                # === OPÇÃO 3 - DELETAR ===
                print("\n[3] Deletar carro\n")
                exibir_dados()

                try:
                    id_carro = int(input("ID do carro a deletar: ").strip())
                    deletar_carro(id_carro)
                    pausar()

                except ValueError:
                    print("Erro: Digite apenas números, tente novamente.")
                    pausar()
                except Exception as e:
                    print(e)
                    pausar()
                    
            case 4:
                # === OPÇÃO 4 - LISTAR ===
                print("\n[4] Listar carros\n")

                exibir_dados()
                pausar()
                
            case 5:
                # === OPÇÃO 5 - SAIR ===
                print("\n[5] Sair do programa\n")
                print("Programa encerrado.\n")
                break
                
            case _:
                print("Escolha inválida.")
                pausar()



interface_menu()
