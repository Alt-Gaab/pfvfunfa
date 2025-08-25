print("Cada um dos dois jogaores de escolher entre pedra, papel, e tesoura:")
J1 = input("Jogador 1, escolha:")
J2 = input("Jogador 2, escolha:")

"tesoura" > "papel"
"papel" > "pedra"
"pedra" > "tesoura"

if J1 > J2:
    print("Jogador 1 vence!")

if J2 > J1:
    print("Jogador 2 vence!")

if J1 == J2:
    print("Empate!")