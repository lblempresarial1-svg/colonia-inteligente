
def tomar_decisao(energia, consumo):
    print("\n=== DECISÃO AUTOMÁTICA ===")

    if energia < 50 and consumo > 50:
        print("ALERTA: ativar modo de economia.")
        print("Manter suporte à vida e desligar sistemas não essenciais.")

    elif energia < 50:
        print("ALERTA: nível de energia baixo.")
        print("Reduzir o consumo.")

    elif consumo > energia:
        print("ALERTA: consumo maior que a energia disponível.")

    else:
        print("SISTEMA NORMAL: energia suficiente.")
