print("Digite o tamanho de 3 lados de um triangulo:")
A = input("1° lado:")
B = input("2° lado:")
C = input("3° lado:")

if A == B == C:
    print("É um triângulo equilátero.")
if A == B !=C or A == C != B or B == C != A:
    print("É um triângulo isósceles.")
if A != B and B != C and A != C:
    print("É um triângulo escaleno.")