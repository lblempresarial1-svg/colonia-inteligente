
# Dados da Colônia Inteligente

colonia = {
    "energia": {
        "geracao_solar": 25,
        "geracao_eolica": 20,
        "consumo": 60,
        "reserva": 100,
        "subsistemas": {
            "solar": "Painéis solares",
            "eolico": "Turbinas eólicas"
        }
    },
    "clima": {
        "temperatura": 22,
        "vento": 11
    },
    "prioridades": [
        "Suporte à vida",
        "Iluminação",
        "Comunicação",
        "Entretenimento"
    ]
}

vento_historico = [8, 10, 12, 14, 16]
energia_historica = [20, 25, 30, 35, 40]


def mostrar_dados():
    print("\n=== DADOS DA COLÔNIA ===")

    print("Energia:", colonia["energia"])
    print("Clima:", colonia["clima"])
    print("Prioridades:", colonia["prioridades"])
