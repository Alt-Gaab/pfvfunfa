#Ver pq ta dandoe errado
P = input("Digite seu peso:")
A = input("Digite sua altura:")
IMC = P / A * 2
if IMC < 18:
    print("Seu desnutrido!")
elif IMC >= 18:
    print("Você é normal.")