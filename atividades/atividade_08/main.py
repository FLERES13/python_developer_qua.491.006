import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    notas = []

    while True:
        print("1 – Informar uma nota do aluno (0 a 10)")
        print("2 – Calcular a média e sair")
        opcao = input("Informe a opção desejada: ").strip()
        clear()

        match opcao:
            case "1":
                try:
                    entrada = input("Insira a nova nota: ").replace(",", ".").strip()
                    nova_nota = float(entrada)
                    if 0 <= nova_nota <= 10:
                        notas.append(nova_nota)
                        print("Nota inserida com sucesso!\n")
                    else:
                        print("Nota inválida! Deve ser entre 0 e 10.\n")
                except ValueError:
                    print("Entrada inválida! Digite um número válido.\n")
                continue

            case "2":
                if not notas:
                    print("Nenhuma nota foi informada. Não é possível calcular a média.")
                else:
                    media = sum(notas) / len(notas)
                    print(f"Média: {media:.2f}")
                    if media >= 7:
                        print("Aluno está APROVADO")
                    elif media >= 5:
                        print("Aluno está de RECUPERAÇÃO")
                    else:
                        print("Aluno está REPROVADO")
                break

            case _:
                print("Opção inválida! Tente novamente.\n")
                continue

    print("\nPrograma encerrado.")

if __name__ == "__main__":
    main()






