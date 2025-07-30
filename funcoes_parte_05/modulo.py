import math
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def primeiro_grau(a, b):
    if a == 0:
        raise ValueError("A não pode ser zero em uma equação do 1º grau.")
    x = -b / a
    return x

def segundo_grau(a, b, c):
    if a == 0:
        # Quando 'a' é 0, a equação é de 1º grau: bx + c = 0
        return [primeiro_grau(b, c)]
    
    delta = (b ** 2) - (4 * a * c)

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [f"x' = {x1}", f'x" = {x2}']
    elif delta == 0:
        x = -b / (2 * a)
        return [f"x = {x}"]
    else:
        return ["Não há raízes reais."]
