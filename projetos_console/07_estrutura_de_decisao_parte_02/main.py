nome = input("Infome seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",", "."))

if idade >= 12 and altura >= 1.15:
    print(f"(nome) está autorizado a entrar.")
else:
    print(f"(nome) não foi autorizado a entrar.")
        