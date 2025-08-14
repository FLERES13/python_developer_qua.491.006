nome = input("informe seu nome: ")
idade = int (input("informe sua idade: "))
altura = float(input("informe a sua altura em metros: ").replace(",", "."))

print(f"Seja bem vindo ao curso de Python, {nome}!")
print(f"Idade do Usuario: {idade}.")
print(f"Altura do usuario: {altura} ")


print(f"{nome}: {type(nome)}.")
print(f"{idade}: {type(idade)}.")
print(f"{altura}: {type(altura)}. ")
