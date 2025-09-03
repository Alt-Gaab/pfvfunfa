print("Aqui estão as tarefas do dia:")
tarefas = ["Arrumar a casa", "Lavar a roupa", "Fazer o almoço", "Estudar", "Ir ao mercado"]
print(tarefas)

resposta = input("Já terminou alguma tarefa? (s/n):")
if resposta == "s":
    feita = input("Qual tarefa você já feiz?")
    if feita in tarefas:
        tarefas.remove(feita)
        print(f"Parabéns! Você já fez: {feita}")
        outra = input("Gostaria de adicionar uma outra tarefa? (s/n)?")
        if outra == "s":
            nova = input("Qual tarefa gostaria de adicionar?")
            tarefas.append(nova)
            print("Tarefa adicionada!")
        elif outra == "n":
            print("Beleza, preguissoso!")
        print("Ainda faltam estas tarefas:", tarefas)
    else:
        print("Tarefa não encontrada na lista.")
elif resposta == "n":
    print("Então vai fazer logo!")