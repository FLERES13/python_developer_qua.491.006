import os

# funções

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def velocidade_media(vi, vf):
    vm = vf - vi  # conforme sua lógica
    return vm

def tempo_medio(tf, ti):
    tm = tf - ti
    return tm 

def aceleracao_media(vm, tm):
    if tm != 0:
        am = vm / tm
        return am
    else:
        return "Erro: tempo médio não pode ser zero."

def mru(si, v, t):
    s = si + v * t
    return s
