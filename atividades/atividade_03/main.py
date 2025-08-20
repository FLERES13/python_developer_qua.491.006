# TODO criar um menu 
import math

while True:
    raio = float(input("Informe o tamanho do círculo: "))

    area = math.pi * raio ** 2
    circunferencia = 2 * math.pi * raio

    print(f"A área do círculo é: {area:.2f}")
    print(f"A circunferência do círculo é: {circunferencia:.2f}")

    sair = input("Deseja sair do programa? (s/n): ").lower().strip()

    if sair == "s":
        print("Programa encerrado.")
        break
    elif sair == "n":
        continue
    else:
        print("Opção inválida. Encerrando por segurança.")
        break
