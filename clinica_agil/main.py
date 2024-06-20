# Sistema de Clínica de Consultas
import datetime
# Listas para armazenar pacientes e agendamentos
pacientes = []
agendamentos = []

def cadastrar_pacientes():
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente: ")

    #Verificar duplicidade do paciente
    for paciente in pacientes:
        if paciente['telefone'] == telefone:
            print("Paciente já cadastrado!\n")
            return

    pacientes.append({"nome": nome, "telefone": telefone})
    print("Paciente cadastrado com sucesso.\n")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return False
    print("\nPacientes cadastrados:")
    for x, paciente in enumerate(pacientes, start=1):
        print(f"{x}, {paciente['nome']} - {paciente['telefone']}")
    return True

def marcar_consulta():
    if not listar_pacientes():
        return
    escolha = int(input("\nEscolha o número do paciente para agendar uma consulta: "))
    if escolha < 1 or escolha > len(pacientes):
        print("Escolha inválida.\n")
        return
    
    dia = input("Digite o dia da consulta (DD/MM/AAAA): ")
    hora = input("Digite a hora da consulta (HH:MM): ")
    especialidade = input("Digite a especialidade desejada: ")

    #Verificar datas retroativas
    data_consulta = datetime.datetime.strptime(dia,'%d/%m/%Y')
    if data_consulta < datetime.datetime.now():
        print("Não é possivel realizar uma consulta para o passado ;)\n")
        return

    # Verificar disponibilidade de agendamento
    for agendamento in agendamentos:
        if agendamento['dia'] == dia and agendamento['hora'] == hora:
            print("Já existe uma consulta agendada para esse dia e horário.\n")
            return

    agendamento = {"paciente": pacientes[escolha-1], "dia": dia, "hora": hora, "especialidade": especialidade}
    agendamentos.append(agendamento)
    print("Consulta agendada com sucesso.\n")

def listar_agendamentos():
     if len(agendamentos) == 0:
        print("Nenhum agendamento encontrado.\n")
        return False
     print("\nAgendamentos:")
     for x, agendamento in enumerate(agendamentos, start=1):
        paciente = agendamento["paciente"]
        print(f"{x}. {paciente['nome']} - {agendamento['dia']} às {agendamento['hora']} - Especialidade: {agendamento['especialidade']}")
     return True
    
def cancelar_consulta():
    if not listar_agendamentos():
        return
    escolha = int(input("Escolha o número do agendamento que deseja cancelar: "))
    if escolha < 1 or escolha > len(agendamentos):
        print("Escolha inválida.\n")
        return
    agendamento = agendamentos.pop(escolha-1)
    print(f"Consulta de {agendamento['paciente']['nome']} no dia {agendamento['dia']} às {agendamento['hora']} cancelada com sucesso.\n")

def menu():
    while True:
        print("===== Menu: =====")
        print("1. Cadastrar paciente")
        print("2. Marcar consulta")
        print("3. Cancelar consulta")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_pacientes()
        elif opcao == 2:
            marcar_consulta()
        elif opcao == 3:
            cancelar_consulta()
        elif opcao == 4:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o menu
menu()