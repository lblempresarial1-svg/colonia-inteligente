
def prever_energia(vento, dados_vento, dados_energia):

    n = len(dados_vento)

    media_x = sum(dados_vento) / n
    media_y = sum(dados_energia) / n

    numerador = 0
    denominador = 0

    for i in range(n):
        numerador += (
            (dados_vento[i] - media_x) *
            (dados_energia[i] - media_y)
        )

        denominador += (dados_vento[i] - media_x) ** 2

    a = numerador / denominador
    b = media_y - (a * media_x)

    previsao = a * vento + b

    return previsao
