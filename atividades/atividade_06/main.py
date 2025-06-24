import calendar

while True:

    ano = int(input("Informe o ano que deseja ver o calendario: "))
    if ano >= 1990:
        break
    else:
        print("Por favor insira um ano maior de 1990.\n")


print(f"\nCalendário do ano {ano}\n")
print(calendar.calendar(ano))


