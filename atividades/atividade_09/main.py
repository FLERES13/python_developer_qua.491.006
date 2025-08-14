import os
import random
import datetime
from datetime import date

usuarios = []

while True:
    usuario = {}

    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Alterar dados do usuário")
    print("4 - Sortear usuário")
    print("5 - Excluir usuário")
    print("6 - Sair do programa")
    opcao = input("Escolha uma opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                usuario["nome"] = input("Informe o nome do usuário: ").strip().title()
                usuario["data de nascimento"] = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
                usuario["email"] = input("Informe o email do usuário: ").strip().lower()
                usuario["CPF"] = input("Informe o CPF do usuário: ").strip()
                usuario["telefone"] = input("Informe o telefone do usuário: ").strip()
                usuario["gênero"] = input("Informe o gênero do usuário: ").strip()
                usuario["data de cadastro"] = date.today().strftime("%d/%m/%Y")
                usuario["hora de cadastro"] = datetime.datetime.now().strftime("%H:%M:%S")

                usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Usuário {usuario.get('nome')} cadastrado com sucesso!")

            except Exception as e:
                print(f"Não foi possível cadastrar o usuário: {e}")

        case "2":
            try:
                for i in range(len(usuarios)):
                    print(f"Índice: {i}")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i][chave]}")
                    print('-' * 40)
            except Exception as e:
                print(f"Não foi possível listar usuários: {e}")

        case "3":
            try:
                i = int(input("Informe o índice do usuário que deseja alterar: ").strip())
                os.system("cls" if os.name == "nt" else "clear")
                if i >= 0 and i < len(usuarios):
                    print(f"{'-' * 20} Dados do Usuário {'-' * 20}")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i][chave]}")
                    print("\n")
                    while True:
                        chave_escolhida = input("Informe a chave que deseja alterar: ").strip().lower()
                        if chave_escolhida in usuarios[i]:
                            usuarios[i][chave_escolhida] = input(f"Informe o novo valor para {chave_escolhida}: ").strip()
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Chave alterada com sucesso!")
                        else:
                            print("Chave inexistente.")
                        
                        while True:
                            prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                            if prosseguir in ["s", "n"]:
                                break
                            else:
                                print("Opção inválida.")

                        if prosseguir == "n":
                            break
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar os dados do usuário: {e}")

        case "4":
            try:
                if usuarios:
                    i = random.randint(0, len(usuarios) - 1)
                    print("Usuário sorteado:")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                else:
                    print("Nenhum usuário cadastrado para sortear.")
            except Exception as e:
                print(f"Não foi possível sortear o usuário: {e}")

        case "5":
            try:
                i = int(input("Informe o índice do usuário que deseja excluir: ").strip())
                if i >= 0 and i < len(usuarios):
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    while True:
                        excluir = input("Deseja excluir este usuário? (s/n): ").strip().lower()
                        if excluir in ["s", "n"]:
                            break
                        else:
                            print("Opção inválida.")

                    match excluir:
                        case "s":
                            del usuarios[i]
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário excluído com sucesso!")
                        case "n":
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário não excluído.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível excluir o usuário: {e}")

        case "6":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")
