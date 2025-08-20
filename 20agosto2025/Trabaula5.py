SERVIÇO = input("VocÊ foi atendido? ")
if SERVIÇO == "sim":
    print("Porfavor de uma nota de 1 a 5:")
    print("1) uma merda!")
    print("2) meio bosta.")
    print("3) mais ou menos.")
    print("4) legal.")
    print("5) muito foda!")
    NOTA = input()
    print("A nota dada foi", NOTA )
    print("Obrigado pela preferencia!")
if SERVIÇO == "não":
    NOTA = 0
    print("A nota dada foi", NOTA)
    input("Porfavor nos diga o porque:")