print("Digite o número referente ao estado da carta:")
print("1. Flor de cunho")
print("2. Soberba")
print("3. Muito bem conservada")
print("4. Bem conservada")
print("5. Outros estados")
ESTADO = int(input())

match ESTADO:
    case 1:
        print("QUE FODA, TOMA R$ 1.000.000,00!")
    case 2:
        print("Porra, ta otima, te dou R$ 250.000,00!")
    case 3:
        print("Te dou uns R$ 100.00,00")
    case 4:
        print("Até que vai, toparia R$ 30.000,?")
    case 5:
        print("QUE MERDA É ESSA?")
    case _:
        print("Você é burro!? Os numeros são só de 1 a 5 porra.")