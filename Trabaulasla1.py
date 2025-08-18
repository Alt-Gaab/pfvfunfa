print("Quanto de dinheiros você tem?")
BANCO = int(input())
print("Quanto custa o que você quer comprar?")
VALOR = int(input())
if VALOR <= BANCO:
    print("Parabéns, você não é tão pobre.")
elif VALOR > BANCO:
    print("POBRE KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK.")