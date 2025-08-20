print("Cada um dos dois jogaores de escolher entre pedra, papel, e tesoura:")
J1 = input("Jogador 1, escolha:")
J2 = input("Jogador 2, escolha:")
if J1 == "tesoura" and J2 == "pedra":
    print("Jogador 2 vence")
if J1 == "tesoura" and J2 == "papel":
    print("Jogador 1 vence")
if J1 == "tesoura" and J2 == "tesoura":
    print("Empate")
if J1 == "papel" and J2 == "tesoura":
    print("Jogador 2 vence")
if J1 == "papel" and J2 == "pedra":
    print("Jogador 1 vence")
if J1 == "papel" and J2 == "papel":
    print("Empate")
if J1 == "pedra" and J2 == "papel":
    print("Jogador 2 vence")
if J1 == "pedra" and J2 == "tesoura":
    print("Jogador 1 vence")
if J1 == "pedra" and J2 == "pedra":
    print("Empate")