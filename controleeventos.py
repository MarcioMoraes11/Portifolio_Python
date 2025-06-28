# Projeto: Sistema de Gerenciamento de Eventos Universitários - UniFECAF
# Autor: Márcio Moraes
# Data: 27/06/2025

# Descrição: Este programa permite o cadastro, atualização, visualização e inscrição em eventos universitários.

# Importando bibliotecas 
from datetime import datetime
# Essa biblioteca é usada para manipular a data fazendo com que o usuário não consiga cadastrar eventos em datas passadas e ou inexistentes.

eventos = {}

# Função para cadastrar um novo evento
def cadastrar_evento():
    print("\n--- Novo Evento ---")
    nome = input("Nome do evento: ").strip().capitalize()

    if nome in eventos:
        print("Erro: um evento com esse nome já existe.")
        return

    
    try:
        data_inserida = input("Data (dd/mm/aaaa): ")
        data_sub = datetime.strptime(data_inserida, '%d/%m/%Y').date()

        # Compara a data inserida com a data de hoje (sem as horas)
        if data_sub < datetime.now().date():
            print("Erro: Não é possível cadastrar eventos em uma data passada.")
            return

        descricao = input("Descrição: ").strip().capitalize()
        max_participantes = int(input("Total de vagas: "))

        eventos[nome] = {
            "data": data_inserida, 
            "descricao": descricao,
            "max_participantes": max_participantes,
            "inscritos": []
        }
        print("Evento cadastrado!")

    except ValueError:
        # 
        print("Erro: Data em formato inválido ou total de vagas não é um número.")

def atualizar_evento():
    print("\n--- Atualizar Evento ---")
    nome = input("Qual evento você quer atualizar? ").strip().capitalize()

    if nome not in eventos:
        print("Erro: Evento não encontrado.")
        return

    print(f"Atualizando {nome}. Deixe em branco para não alterar.")
    try:
        # 
        nova_data_inserida = input(f"Nova data ({eventos[nome]['data']}): ")
        if nova_data_inserida:
            
            nova_data_sub = datetime.strptime(nova_data_inserida, '%d/%m/%Y').date()
            if nova_data_sub < datetime.now().date():
                print("Erro: A nova data não pode ser no passado.")
            else:
                eventos[nome]['data'] = nova_data_inserida

        nova_descricao = input(f"Nova descrição ({eventos[nome]['descricao']}): ").strip().capitalize()
        if nova_descricao:
            eventos[nome]['descricao'] = nova_descricao

        novo_max_str = input(f"Novo total de vagas ({eventos[nome]['max_participantes']}): ")
        if novo_max_str:
            eventos[nome]['max_participantes'] = int(novo_max_str)

        print("Evento atualizado com sucesso!")

    except ValueError:
        print("Erro: Formato de data ou de vagas inválido.")

# Função para visualizar todos os eventos que as pessoas podem se inscrever
def visualizar_eventos():
    print("\n--- Eventos Disponíveis ---")

    if not eventos:
        print("Não há eventos cadastrados.")
        return

    for nome, detalhes in eventos.items():
        vagas_restantes = detalhes['max_participantes'] - len(detalhes['inscritos'])

        print("--------------------")
        print(f"Evento: {nome}")
        print(f"Data: {detalhes['data']}")
        print(f"Descrição: {detalhes['descricao']}")
        print(f"Vagas restantes: {vagas_restantes}")

# Função para inscrever um aluno em um evento
def inscrever_aluno():
    print("\n--- Inscrição em Evento ---")
    nome_evento = input("Em qual evento você quer se inscrever? ").strip().capitalize()

    if nome_evento not in eventos:
        print("Erro: Este evento não existe.")
        return
    
    if len(eventos[nome_evento]['inscritos']) >= eventos[nome_evento]['max_participantes']:
        print("Que pena! As vagas para este evento estão esgotadas. Tente outro evento.")
        return

    nome_aluno = input("Digite seu nome: ").strip().capitalize()
    if nome_aluno in eventos[nome_evento]['inscritos']:
        print("Você já está inscrito neste evento.")
        return

    eventos[nome_evento]['inscritos'].append(nome_aluno)
    print(f"Inscrição de {nome_aluno} no evento {nome_evento} realizada!")

# Função para visualizar inscritos em um evento específico
def visualizar_inscricoes():
    print("\n--- Ver Inscritos ---")
    nome_evento = input("De qual evento você quer ver a lista de inscritos? ").strip().capitalize()

    if nome_evento not in eventos:
        print("Erro: Evento não encontrado.")
        return

    inscritos = eventos[nome_evento]['inscritos']
    print(f"\nParticipantes de {nome_evento}:")

    if not inscritos:
        print("Ninguém se inscreveu neste evento ainda.")
    else:
        for aluno in inscritos:
            print(f"- {aluno}")

# Função para excluir qualquer evento
def excluir_evento():
    print("\n--- Excluir Evento ---")
    nome = input("Qual evento você quer excluir? ").strip().capitalize()

    if nome in eventos:
        # Confirmação antes de excluir qualquer evento
        confirma = input(f"Tem certeza que quer apagar '{nome}'? (s - Confirma) (n - Cancela): ").lower()
        if confirma == 's':
            del eventos[nome]
            print(f"Evento '{nome}' foi excluído.")
        else:
            print("Evento cancelado.")
    else:
        print("Erro: Evento não encontrado.")


# Loop Principal do Programa
while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Cadastrar Evento")
    print("2. Atualizar Evento")
    print("3. Ver Eventos")
    print("4. Se Inscrever em Evento")
    print("5. Ver Inscritos")
    print("6. Excluir Evento")
    print("7. Sair")

    opcao = input("Digite o número da sua opção: ")

    if opcao == '1':
        cadastrar_evento()
    elif opcao == '2':
        atualizar_evento()
    elif opcao == '3':
        visualizar_eventos()
    elif opcao == '4':
        inscrever_aluno()
    elif opcao == '5':
        visualizar_inscricoes()
    elif opcao == '6':
        excluir_evento()
    elif opcao == '7':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha um número do menu.")
