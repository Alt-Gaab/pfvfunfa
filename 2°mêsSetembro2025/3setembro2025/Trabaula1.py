gabarito = ["B", "C", "A", "E", "D"]
for X in range(len(gabarito)):
    print(f"Digite a sua resposta da questão {X + 1}:")
    resposta = input()
    if resposta == gabarito[X]:
        print("Você acertou a questão!")
    elif resposta != gabarito[X]:
        print("Você errou a questão!")