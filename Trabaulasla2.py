print("Digite suas quatro notas:")
N1 = int(input())
N2 = int(input())
N3 = int(input())
N4 = int(input())
média = N1 + N2 + N3 + N4
somar = média / 4
print(somar)
if somar >= 6:
    print("Meus parabens!")
elif somar < 6:
    print("Se fudeu!")