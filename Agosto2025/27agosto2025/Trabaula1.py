def apresentar():
    print(f"Sua idade é {idade} anos")
    return

def conferir(X):
    if X >= 18:
        print("Você é beeeeeeeeeem velho!")
        print(".")
        print(".")
        print(".")
        print("Só isso mesmo")
        print("você é velho.")
    else:
        print("Você é menor de idade, vai comer terra.")
        print("OU ver alguma coisa tipo. . .")
        print("Peppa Pig," \
        " Galinha Pintadinha," \
        "Mundo Bita," \
        "Super Fofos," \
        "Bubble Guppies," \
        "Doki," \
        "Jelly Jam," \
        "Mecanimais.")
        return
    
idade = int(input("Quantos aons você tem? "))

apresentar()
conferir(idade)