import numpy as np
import matplotlib.pyplot as plt

def trimf(x,a,b,c):
    if x<=a:
        return 0
    elif a<x<=b:
        return (x-a)/(b-a)
    elif b<x<c:
        return (c-x)/(c-b)
    else:
        return 0

umidade_universo = np.arange(0,101,1)
temperatura_universo = np.arange(0,41,1)
luminosidade_universo = np.arange(0,101,1)
irrigacao_universo = np.arange(0,101,1)


def umidade_baixa(x):
    return trimf(x,0,0,50)

def umidade_media(x):
    return trimf(x,25,50,75)

def umidade_alta(x):
    return trimf(x,50,100,100)

def temperatura_baixa(x):
    return trimf(x, 0, 0, 20)

def temperatura_media(x):
    return trimf(x, 10, 22, 34)

def temperatura_alta(x):
    return trimf(x, 25, 40, 40)

def luminosidade_baixa(x):
    return trimf(x, 0, 0, 50)

def luminosidade_media(x):
    return trimf(x, 25, 50, 75)

def luminosidade_alta(x):
    return trimf(x, 50, 100, 100)

def irrigacao_baixa(y):
    return trimf(y, 0, 0, 50)

def irrigacao_media(y):
    return trimf(y, 25, 50, 75)

def irrigacao_alta(y):
    return trimf(y, 50, 100, 100)


def fuzzificar(umidade,temperatura,luminosidade):
    graus = {
        "umidade_baixa":umidade_baixa(umidade),
        "umidade_media": umidade_media(umidade),
        "umidade_alta": umidade_alta(umidade),

        "temperatura_baixa": temperatura_baixa(temperatura),
        "temperatura_media": temperatura_media(temperatura),
        "temperatura_alta": temperatura_alta(temperatura),

        "luminosidade_baixa": luminosidade_baixa(luminosidade),
        "luminosidade_media": luminosidade_media(luminosidade),
        "luminosidade_alta": luminosidade_alta(luminosidade)
    }

    print("\n--- FUZZIFICAÇÃO ---")
    for chave, valor in graus.items():
        print(f"{chave}: {valor:.3f}")

    return graus

regras = [
    ("umidade_baixa", "temperatura_alta", "luminosidade_alta", "alta"),
    ("umidade_baixa", "temperatura_alta", "luminosidade_media", "alta"),
    ("umidade_baixa", "temperatura_media", "luminosidade_alta", "alta"),
    ("umidade_baixa", "temperatura_media", "luminosidade_media", "media"),
    ("umidade_baixa", "temperatura_baixa", "luminosidade_baixa", "media"),

    ("umidade_media", "temperatura_alta", "luminosidade_alta", "media"),
    ("umidade_media", "temperatura_media", "luminosidade_media", "media"),
    ("umidade_media", "temperatura_baixa", "luminosidade_baixa", "baixa"),

    ("umidade_alta", "temperatura_alta", "luminosidade_alta", "baixa"),
    ("umidade_alta", "temperatura_media", "luminosidade_media", "baixa"),
    ("umidade_alta", "temperatura_baixa", "luminosidade_baixa", "baixa"),
    ("umidade_alta", "temperatura_alta", "luminosidade_baixa", "baixa")
]

def aplicar_regras(graus):
    ativacoes = []

    for regra in regras:
        entrada1 = regra[0]
        entrada2 = regra[1]
        entrada3 = regra[2]
        saida = regra[3]

        grau_entrada1 = graus[entrada1]
        grau_entrada2 = graus[entrada2]
        grau_entrada3 = graus[entrada3]

        grau_ativacao = min(grau_entrada1, grau_entrada2, grau_entrada3)

        ativacoes.append({
            "regra": regra,
            "grau_ativacao": grau_ativacao,
            "saida": saida
        })

    return ativacoes

def calcular_saida_agregada(ativacoes):
    saida_agregada = []

    for y in irrigacao_universo:
        valores_regras = []

        for ativacao in ativacoes:
            grau = ativacao["grau_ativacao"]
            saida = ativacao["saida"]

            if saida == "baixa":
                pertinencia_saida = irrigacao_baixa(y)
            elif saida == "media":
                pertinencia_saida = irrigacao_media(y)
            elif saida == "alta":
                pertinencia_saida = irrigacao_alta(y)

            saida_regra = min(grau, pertinencia_saida)

            valores_regras.append(saida_regra)

        valor_agregado = max(valores_regras)

        saida_agregada.append(valor_agregado)

    return np.array(saida_agregada)


def defuzzificar(saida_agregada):
    numerador = np.sum(irrigacao_universo * saida_agregada)
    denominador = np.sum(saida_agregada)

    if denominador == 0:
        return 0

    return numerador / denominador

def sistema_fuzzy(umidade, temperatura, luminosidade):
    graus = fuzzificar(umidade, temperatura, luminosidade)

    ativacoes = aplicar_regras(graus)

    saida_agregada = calcular_saida_agregada(ativacoes)

    valor_final = defuzzificar(saida_agregada)

    return graus, ativacoes, saida_agregada, valor_final
