def verificarcidade(N, C):
    if C  == "Rio de Janeiro":
        print("Olá", N)
        print("Bem vinde a cidade maravilhosa!")
    else:
        print("Bem vinde a", C)

nome = input ("Digite seu nome: ")
cidade = input("Digite o nome da sua cidade: ")
verificarcidade(nome,cidade)