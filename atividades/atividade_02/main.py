# TODO - atividade:
# Crie um programa que receba do usuário o nome, o peso em kg e a altura em metros,
# e calcule o valor do IMC (Índice de Massa Corporal).

# O programa deve mostrar o valor do IMC com 2 casas decimais e o diagnóstico com base em:
# < 18.5: abaixo do peso
# 18.5 a < 25: peso ideal
# 25 a < 30: acima do peso
# 30 a < 35: obeso
# 35 a < 40: obesidade nível 2
# >= 40: obesidade mórbida
# O usuário poderá repetir quantas vezes quiser.

while True:
    try:
        # Entrada de dados
        print(f"{'-' * 20} CÁLCULO DE IMC {'-' * 20}")
        nome = input("Informe seu nome: ").title().strip()
        peso = float(input("Informe seu peso (em kg): ").replace(",", "."))
        altura = float(input("Informe sua altura (em metros): ").replace(",", "."))

        # Cálculo do IMC
        imc = peso / altura ** 2
        print(f"O valor do IMC de {nome} é {imc:.2f}.")

        # Diagnóstico com base no IMC
        if imc < 18.5:
            print(f"{nome} está abaixo do peso.")
        elif imc < 25:
            print(f"{nome} está no peso ideal.")
        elif imc < 30:
            print(f"{nome} está acima do peso.")
        elif imc < 35:
            print(f"{nome} está obeso.")
        elif imc < 40:
            print(f"{nome} está com obesidade nível II.")
        else:
            print(f"{nome} está com obesidade mórbida.")

        # Pergunta se deseja continuar
        while True:
            repetir = input("Deseja refazer? (s/n): ").lower().strip()
            if repetir in ("s", "n"):
                break
            else:
                print("Opção inválida. Digite 's' ou 'n'.")

        if repetir == "n":
            print("Programa encerrado.")
            break

    except Exception as e:
        print(f"Não foi possível calcular o IMC. Erro: {e}")
        continue
