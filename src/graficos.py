import os
import numpy as np
import matplotlib.pyplot as plt

from sistema_fuzzy_mandani import (
    umidade_baixa,
    umidade_media,
    umidade_alta,
    temperatura_baixa,
    temperatura_media,
    temperatura_alta,
    luminosidade_baixa,
    luminosidade_media,
    luminosidade_alta,
    irrigacao_baixa,
    irrigacao_media,
    irrigacao_alta,
    irrigacao_universo
)


def criar_pasta_resultados():
    os.makedirs("resultados/graficos", exist_ok=True)


def plotar_funcoes_pertinencia():
    criar_pasta_resultados()

    umidade_universo = np.arange(0, 101, 1)
    temperatura_universo = np.arange(0, 41, 1)
    luminosidade_universo = np.arange(0, 101, 1)

    plt.figure(figsize=(8, 4))
    plt.plot(umidade_universo, [umidade_baixa(x) for x in umidade_universo], label="Baixa")
    plt.plot(umidade_universo, [umidade_media(x) for x in umidade_universo], label="Média")
    plt.plot(umidade_universo, [umidade_alta(x) for x in umidade_universo], label="Alta")
    plt.title("Funções de pertinência - Umidade do solo")
    plt.xlabel("Umidade (%)")
    plt.ylabel("Grau de pertinência")
    plt.legend()
    plt.grid()
    plt.savefig("resultados/graficos/funcoes_umidade.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(temperatura_universo, [temperatura_baixa(x) for x in temperatura_universo], label="Baixa")
    plt.plot(temperatura_universo, [temperatura_media(x) for x in temperatura_universo], label="Média")
    plt.plot(temperatura_universo, [temperatura_alta(x) for x in temperatura_universo], label="Alta")
    plt.title("Funções de pertinência - Temperatura")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Grau de pertinência")
    plt.legend()
    plt.grid()
    plt.savefig("resultados/graficos/funcoes_temperatura.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(luminosidade_universo, [luminosidade_baixa(x) for x in luminosidade_universo], label="Baixa")
    plt.plot(luminosidade_universo, [luminosidade_media(x) for x in luminosidade_universo], label="Média")
    plt.plot(luminosidade_universo, [luminosidade_alta(x) for x in luminosidade_universo], label="Alta")
    plt.title("Funções de pertinência - Luminosidade")
    plt.xlabel("Luminosidade (%)")
    plt.ylabel("Grau de pertinência")
    plt.legend()
    plt.grid()
    plt.savefig("resultados/graficos/funcoes_luminosidade.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(irrigacao_universo, [irrigacao_baixa(y) for y in irrigacao_universo], label="Baixa")
    plt.plot(irrigacao_universo, [irrigacao_media(y) for y in irrigacao_universo], label="Média")
    plt.plot(irrigacao_universo, [irrigacao_alta(y) for y in irrigacao_universo], label="Alta")
    plt.title("Funções de pertinência - Irrigação")
    plt.xlabel("Intensidade de irrigação (%)")
    plt.ylabel("Grau de pertinência")
    plt.legend()
    plt.grid()
    plt.savefig("resultados/graficos/funcoes_irrigacao.png")
    plt.close()


def plotar_saida_agregada(saida_agregada, nome_arquivo):
    criar_pasta_resultados()

    plt.figure(figsize=(8, 4))
    plt.plot(irrigacao_universo, saida_agregada, label="Saída fuzzy agregada")
    plt.title("Saída agregada")
    plt.xlabel("Intensidade de irrigação (%)")
    plt.ylabel("Grau de pertinência")
    plt.legend()
    plt.grid()
    plt.savefig(nome_arquivo)
    plt.close()