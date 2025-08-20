print("O que você vai fazer amanhã de manhã?")
print("dormir / estudar / planejar")
MANHA = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar / treinar / trabalhar")
TARDE = input()

if not MANHA or not TARDE:
    print("Você não vai fazer nada da vida não?")
else:
    if MANHA == "dormir" or TARDE == "jogar":
        print("Mó vagabundo você.")
    elif MANHA == "estudar" or TARDE == "treinar":
        print("Pra que, não vai adiantar de nada.")
    elif MANHA == "planejar" and TARDE == "trabalhar":
        print("De que adianta ajudar a perpetuar esse sistéma capitalista? Apenas para ter um caixão mais bonito no final?")
    else:
        print("Não combinamos estas ações...")

print("Tenha um pessimo dia.")