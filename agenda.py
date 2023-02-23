agenda = []  # lista criada para armazenar os compromissos/informações
# -------------------------------------------------------
# FUNÇÕES

def incluir_compromisso(data, hora, duracao, descricao):
    compromisso = {"data": data, "hora": hora,  # dicionário para cada categoria
                   "duracao": duracao, "descricao": descricao}
    # adiciona as informações que serão descritas para a agenda
    agenda.append(compromisso)
    print("Compromisso adicionado com sucesso!")
# -------------------------------------------------------
# PROGRAMA

while True:
    print("1. Incluir compromisso")
    print("2. Consultar compromisso")
    print("3. Alterar compromisso")
    print("4. Excluir compromisso")
    print("5. Listar todos os compromissos")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        data = input("Digite a data (dd/mm/aaaa): ")
        hora = input("Digite a hora (hh:mm): ")
        duracao = input("Digite a duração (em horas): ")
        descricao = input("Digite a descrição: ")
        incluir_compromisso(data, hora, duracao, descricao)
    # elif opcao == "2":
    # elif opcao == "3":
    # elif opcao == "4":
    # elif opcao == "5":
    elif opcao == "6":
        break
    else:
        print("Opção inválida")
