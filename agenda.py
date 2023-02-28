import os  # utilizado para "limpar" o terminal, deixar a agenda mais limpa
import time  # utilizado para timer das mensagens, deixar a agenda mais limpa

agenda = []  # lista criada para armazenar os compromissos/informações

# FUNÇÕES


def incluir_compromisso(data, hora, duracao, descricao):
    compromisso = {"data": data, "hora": hora,  # dicionário para cada categoria
                   "duracao": duracao, "descricao": descricao}
    # adiciona as informações que serão descritas para a agenda
    agenda.append(compromisso)
    print("Compromisso adicionado com sucesso!")
    time.sleep(3)
    print("", end='')  # volta para o menu depois de 3 segundos


# recebe a data e hora como argumentos e retorna a lista com as informações descritas
def consultar_compromisso(data, hora=None):
    compromissos = []  # *essa lista funciona somente nessa função*
    for c in agenda:  # percorre a agenda e armazena cada compromisso em "c"
        # verifica se a data especificada é igual a "c"..
        if c["data"] == data and (hora is None or c["hora"] == hora):
            # ..caso for true = "c" é adicionada em compromissos
            compromissos.append(c)
    if not compromissos:  # se "c" não for encontrado, exibe a mensagem abaixo
        print("Agenda vazia")
        time.sleep(3)
        print("", end='')  # volta para o menu depois de 3 segundos
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

# data e hora são obrigatórios - duração e descrição são opcionais


def alterar_compromisso(data, hora, duracao=None, descricao=None):
    for c in agenda:  # percorre a agenda e armazena cada compromisso em "c"
        # verifica se a data/hora da agenda correspondem aos que serão informados
        if c["data"] == data and c["hora"] == hora:
            if duracao is not None:
                # se a duração for informada, atualiza a duração do compromisso
                c["duracao"] = duracao
            if descricao is not None:
                # se a descrição for informada, atualiza com a informação que foi digitada
                c["descricao"] = descricao
            print("Compromisso alterado com sucesso!")
            time.sleep(3)
            print("", end='')  # volta para o menu depois de 3 segundos
            return  # encerra a função

    # se a função chegar até aqui, significa que não foi encontrado nenhuma informação com o que foi descrito
    print("Compromisso não encontrado")
    time.sleep(3)
    print("", end='')


def excluir_compromisso(data, hora):
    # utiliza a função enumerate para cada item "c" da lista para obter o "i" e o "c"
    for i, c in enumerate(agenda):
        # verifica se as informações descritas pelo usuário estão em "c"
        if c["data"] == data and c["hora"] == hora:
            del agenda[i]  # caso True, exclui as informações da lista
            print("Compromisso excluído com sucesso!")
            time.sleep(3)
            # apaga a linha anterior onde a mensagem foi exibida
            print("", end='')
            return  # encerra a função
    # caso a função não entrar no if, exibe essa mensagem na tela
    print("Compromisso não encontrado")
    time.sleep(3)
    print("", end='')  # volta para o menu depois de 3 segundos


def listar_todos_compromissos():
    if not agenda:  # se não tiver nenhuma informação na lista, exibe a mensagem
        print("Agenda vazia")
        time.sleep(3)
        print("", end='')  # volta para o menu depois de 3 segundos
    else:
        for c in agenda:  # percorre "c" na lista exibindo a data, hora, duração e descrição
            print("Data:", c["data"])
            print("Hora:", c["hora"])
            print("Duração:", c["duracao"])
            print("Descrição:", c["descricao"])
        sair = input("\nDigite 0 para voltar ao menu: ")
        if sair == '0':
            return


# -------------------------------------------------------
# PROGRAMA
while True:
    os.system('cls')  # limpa o que está descrito anteriormente
    print("------------------\n AGENDA \n------------------ ")
    print("1. Incluir compromisso")
    print("2. Consultar compromisso")
    print("3. Alterar compromisso")
    print("4. Excluir compromisso")
    print("5. Listar todos os compromissos")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")
    # "limpa" o terminal para realizar uma das opções escolhidas
    os.system('cls')

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
    elif opcao == "3":
        data = input("Digite a data (dd/mm/aaaa): ")
        hora = input("Digite a hora (hh:mm): ")
        duracao = input("Digite a nova duração (em horas) (opcional): ")
        descricao = input("Digite a nova descrição (opcional): ")
        alterar_compromisso(data, hora, duracao, descricao)
    elif opcao == "4":
        data = input("Digite a data (dd/mm/aaaa): ")
        hora = input("Digite a hora (hh:mm): ")
        excluir_compromisso(data, hora)
    elif opcao == "5":
        listar_todos_compromissos()
    elif opcao == "6":
        break
    else:
        print("Opção inválida")
