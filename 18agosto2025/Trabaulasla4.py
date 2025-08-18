input("Digite o nome de uma filmeou série:")
print("Agora de uma nota:")
NOTA = int(input())
match NOTA:
    case 1:
        print("MUITOMERDA!")
    case 2:
        print("Bem Bosta.")
    case 3:
        print("Até que é bom.")
    case 4:
        print("Bem legal.")
    case 5:
        print("Muito Foda!")
if NOTA <= 2:
    input("Mas Porque?")
    print("Que argumento mais merda esse.")