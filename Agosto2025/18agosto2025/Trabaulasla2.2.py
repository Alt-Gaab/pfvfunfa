print("Digite suas quatro notas:")
N1 = int(input())
N2 = int(input())
N3 = int(input())
N4 = int(input())
média = N1 + N2 + N3 + N4
somar = média / 4
print(somar)
if somar <= 5:
    print("Burro do caralho! Vai fazer o ano denovo!")
elif somar >= 6.5:
    print("Parabéns, você não é um burro do caralho.")
else:
    somar < 5 or somar > 6.5
    print("Você ainda tem esperança de não ser um burro do caralho.")