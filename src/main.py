from sistema_fuzzy_mandani import fuzzificar, aplicar_regras, calcular_saida_agregada, defuzzificar
from graficos import plotar_funcoes_pertinencia, plotar_saida_agregada


def main():


    plotar_funcoes_pertinencia()
    
    testes = [
        (20, 35, 90),
        (55, 22, 50),
        (90, 15, 20)
    ]

    for i, (umidade, temperatura, luminosidade) in enumerate(testes, start=1):

        graus = fuzzificar(umidade, temperatura, luminosidade)

        ativacoes = aplicar_regras(graus)

        saida_agregada = calcular_saida_agregada(ativacoes)

        plotar_saida_agregada(
            saida_agregada,
            nome_arquivo=f"resultados/graficos/saida_agregada_teste_{i}.png"
        )

        valor_final = defuzzificar(saida_agregada)
        print(f"\n========== TESTE {i} ==========")
        print(f"Umidade: {umidade}")
        print(f"Temperatura: {temperatura}")
        print(f"Luminosidade: {luminosidade}")
        print(f"Saída defuzzificada: {valor_final:.2f}%")


if __name__ == "__main__":
    main()