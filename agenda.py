agenda = []  # lista criada para armazenar os compromissos/informações
# -------------------------------------------------------
# FUNÇÕES

def incluir_compromisso(data, hora, duracao, descricao):
    compromisso = {"data": data, "hora": hora,  # dicionário para cada categoria
                   "duracao": duracao, "descricao": descricao}
    # adiciona as informações que serão descritas para a agenda
    agenda.append(compromisso)
    print("Compromisso adicionado com sucesso!")

def consultar_compromisso(data, hora=None):
    compromissos = []  # *essa lista funciona somente nessa função*
    for c in agenda:  # percorre a agenda e armazena cada compromisso em "c"
        # verifica se a data especificada é igual a "c"..
        if c["data"] == data and (hora is None or c["hora"] == hora):
            # ..caso for true = "c" é adicionada em compromissos
            compromissos.append(c)
    if not compromissos:  # se "c" não for encontrado, exibe a mensagem abaixo
        print("Agenda vazia")
        return
    else:
        for c in compromissos:  # se a lista compromissos não estiver vazia, então tem todos os compromissos que satisfazem a busca
            # é chamado "c" junto a "data" visto que foi criado um dicionário para designar os campos da lista
            print("Data:", c["data"])
            print("Hora:", c["hora"])
            print("Duração:", c["duracao"])
            print("Descrição:", c["descricao"])
            sair = input("\nDigite 0 para voltar ao menu: ")
            if sair == '0':  # volta para o menu
                return
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
    elif opcao == "2":
        data = input("Digite a data (dd/mm/aaaa): ")
        hora = input("Digite a hora (hh:mm) (opcional): ")
        if hora:
            consultar_compromisso(data, hora)
        else:
            consultar_compromisso(data)
    # elif opcao == "3":
    # elif opcao == "4":
    # elif opcao == "5":
    elif opcao == "6":
        break
    else:
        print("Opção inválida")
