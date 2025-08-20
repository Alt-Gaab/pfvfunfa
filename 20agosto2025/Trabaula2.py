print("Digite tres numeros distintos:")
X = input()
Y = input()
Z = input()

if X < Y < Z:
    print("Eles tesão en ordem crescente.")
if X > Y > Z:
    print("Eles estão em ordem decrescente.")
elif not X < Y < Z or X > Y > Z:
    print("Eles estão todos misturados.")