
def analisar_energia(geracao, consumo, reserva):

    print("\n=== ANÁLISE DE ENERGIA ===")

    saldo = geracao - consumo

    print("Geração:", geracao)
    print("Consumo:", consumo)
    print("Reserva:", reserva)

    if consumo > geracao:
        print("ALERTA: consumo maior que geração.")

    elif geracao > consumo:
        print("SUGESTÃO: armazenar energia excedente.")

    else:
        print("SISTEMA EQUILIBRADO.")

    if reserva < 20:
        print("ATENÇÃO: reserva de energia crítica.")

    print("Saldo energético:", saldo)
