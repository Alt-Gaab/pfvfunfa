def adicao(X, Y):
    W = X + Y
    return W
def subtracao(X, Y):
    return X - Y

print("Digite dois valores inteiros...")
n1 = int(input("X:  "))
n2 = int(input("Y:  "))
op = input("Qual operação (+ ou -)?")

if op == "+":
    Z = adicao(n1, n2)
    print("Resultado da soma:", Z)
elif op == "-":
    Z = subtracao(n1, n2)
    print("Resultado da subtração:", Z)
else:
    print("Opção digitada inexistente! ")