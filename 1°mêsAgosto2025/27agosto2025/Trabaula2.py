# DEUSEUENTENDI :D
import random

def parimpar(X,Y):
    resultado = (X + Y) % 2
    if resultado == 0:
        print("É par, o ser humano venceu!")
    else:
        print("É impar, o computador venceu!")


n1 = random.randint (0, 10)
n2 = int(input("Ser humano - digite um numero:"))
parimpar(n1,n2)
print("Computador gerou:", n1)
print("Você digitou:", n2)