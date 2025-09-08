print("Vou montar a minha marmita com 5 alimentos!")
marmita = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, a nossa marmita:", marmita)

resposta = input("Quer montar uma marmita diferente? (s/n) ")
if resposta == "s":
    for X in range(len(marmita)):
        print(f'Digite o {X + 1}° item do cardapio:')
        marmita[X] = input()
    print("A marmita montada foi:", marmita)
    print("Os três primeiros itens foram:", marmita[0:3])
    print("O último item foi:", marmita[-1])
else:
    print("Ok. Você decide. . .")