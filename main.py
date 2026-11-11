
from dados import (
    colonia,
    vento_historico,
    energia_historica,
    mostrar_dados
)

from decisoes import tomar_decisao
from previsao import prever_energia
from analise_energia import analisar_energia


def menu():
    while True:
        print("\n================================")
        print("     COLÔNIA INTELIGENTE")
        print(" GERENCIAMENTO DE ENERGIA")
        print("================================")
        print("1 - Visualizar dados da colônia")
        print("2 - Executar decisões automáticas")
        print("3 - Prever geração de energia")
        print("4 - Analisar consumo de energia")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            mostrar_dados()

        elif opcao == "2":
            energia = (
                colonia["energia"]["geracao_solar"] +
                colonia["energia"]["geracao_eolica"]
            )

            consumo = colonia["energia"]["consumo"]

            tomar_decisao(energia, consumo)

        elif opcao == "3":
            vento = float(input("Informe a velocidade do vento: "))

            resultado = prever_energia(
                vento,
                vento_historico,
                energia_historica
            )

            print(
                "Previsão de geração eólica:",
                round(resultado, 2)
            )

        elif opcao == "4":
            geracao = (
                colonia["energia"]["geracao_solar"] +
                colonia["energia"]["geracao_eolica"]
            )

            consumo = colonia["energia"]["consumo"]
            reserva = colonia["energia"]["reserva"]

            analisar_energia(geracao, consumo, reserva)

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
