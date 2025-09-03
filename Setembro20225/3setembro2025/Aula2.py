print("Vou almoçar em um restaurante a quilo!")

original = ["arroz", "feijão", "batata", "alface", "frango"]
print(f"Eis, a minha comida:{original}")
derivada = original
print(f"Meu amige irá comer também:{derivada}")

print("Vou alterar as opções sem ele ver. . .")
original.remove("arroz")
original.remove("feijão")
original.remove("alface")
original.append("picanha")
original.append("linguiça")

print("Amiguinhe, me mostra o que você vai comer?")
print(f"Claro! Dá uma conferida {derivada}")