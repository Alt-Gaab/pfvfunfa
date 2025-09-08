#Tem alguma coisa errada
print("Cada um dos dois jogaores de escolher entre pedra, papel, e tesoura:")
J1 = str(input("Jogador 1, escolha:"))
J2 = str(input("Jogador 2, escolha:"))
if J1 and J2 != "pedra" or "tesoura" or "papel":
    print("Isso é pedra, papel e tesoura imbecil.")

"tesoura" > "papel"
"papel" > "pedra"
"pedra" > "tesoura"

if J1 < J2:
    print("Jogador 1 vence!")

if J2 < J1:
    print("Jogador 2 vence!")

if J1 == J2:
    print("Empate!")