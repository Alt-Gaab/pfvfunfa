P = float(input("Digite seu peso:"))
A = float(input("Digite sua altura:"))
IMC = P / A * 2
print(IMC)
if IMC < 18:
    print("Seu desnutrido!")
elif IMC >= 18:
    print("Você é normal.")