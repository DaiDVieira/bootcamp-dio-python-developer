from datetime import datetime

def depositar(saldo_atual, valor, extrato, data, /):
    if valor > 0:
        saldo_atual += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\t {data}\n"
    else:
        print("Valor de depósito inválido. Tente novamente.")
    print("------------------------------------------------")

    return saldo_atual, extrato

def exibir_extrato(saldo_atual, extrato, data, /):
    print("-------------------- Extrato -------------------")
    if not extrato:
        print("Não foram realizadas movimentações.")    
    else:   
        print(extrato)
    print(f"\nSaldo:\t\t R$ {saldo_atual:.2f}\t {data}")
    print("------------------------------------------------")

def sacar(saldo_atual, valor, extrato, numero_saques, limite_valor, data, /):
    if valor > 0:
        if saldo_atual < valor:
            print("Saldo insuficiente. Não será possível realizar o saque.")
        else:
            if valor >= limite_valor:
                print(f"Não é possível sacar valores maiores que R$ {limite_valor}. Tente novamente.")
            else:
                saldo_atual -= valor
                numero_saques += 1
                extrato += f"Saque:\t\t R$ {valor:.2f}\t {data}\n"

    else:
        print("Valor de saque inválido. Tente novamente.")

    print("------------------------------------------------")

    return saldo_atual, extrato, numero_saques

def criar_usuario(usuarios, /):
    cpf = input("Digite o CPF (somente números): ")

    usuario = filtar_usuario(cpf, usuarios)
    if usuario != None:
        print(f"Usuário com CPF {cpf} já está cadastrado.")
        return

    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (somente números): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})

    print("--------- Usuário criado com sucesso! ---------")
    

def criar_conta(usuarios, agencia, numero_conta, /):
    if usuarios != []:
        cpf = input("Digite o CPF do usuário: ")
        usuario = filtar_usuario(cpf, usuarios)
        print(f"teste usuario: {usuario}")
        if usuario:
            print("--------- Conta criada com sucesso! ---------")
            return ({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        else:
            print(f"Usuário de CPF {cpf} não está cadastrado. Operação cancelada.")
            return
    else:
        print("Não há usuários cadastrados. Cadastre um usuário antes de criar uma conta.")

def filtar_usuario(cpf, usuarios, /):  
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def listar_contas(contas, /):
    print("------------- Contas cadastradas -------------")
    for conta in contas:
        texto = f"""\
Agência:\t\t{conta['agencia']}
Conta Corrente:\t\t{conta['numero_conta']}
Titular:\t\t{conta['usuario']['nome']}
        """
        print(texto)

def main():
    menu = """
-------------------- MENU --------------------
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Contas
[6] Novo Usuário
[0] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    usuarios = []
    contas = []
    numero_conta = 1
    AGENCIA = "0001"

    while True:
        data = datetime.now()
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        opcao = input(menu)
        data_hora_atual = datetime.now()

        if opcao == "1":
            valor = float(input("\nDigite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato, data)  
            print(f"{data_hora_atual} - DEPÓSITO")
            
        elif opcao == "2":
            if numero_saques == LIMITE_SAQUES:
                print(f"Número máximo de {LIMITE_SAQUES} saques diários atingido. Tente novamente amanhã.")
            else:
                valor = float(input("\nDigite o valor do saque: "))
                saldo, extrato, numero_saques = sacar(saldo, valor, extrato, numero_saques, limite, data)
            print(f"{data_hora_atual} - SAQUE")

        elif opcao == "3":
            exibir_extrato(saldo, extrato, data)
            print(f"{data_hora_atual} - EXTRATO")

        elif opcao == "4":
            conta = criar_conta(usuarios, AGENCIA, numero_conta)
            numero_conta += 1
            contas.append(conta)
            print(f"{data_hora_atual} - CRIAR_CONTA")

        elif opcao == "5":
            listar_contas(contas)
            print(f"{data_hora_atual} - LISTAR_CONTAS")

        elif opcao == "6":
            criar_usuario(usuarios)
            print(f"{data_hora_atual} - CRIAR_USUARIO")

        elif opcao == "0":
            print("Obrigada por utilizar nosso sistema!")
            break

        else:
            print("Operação inválida. Por favor selecione novamente a operação desejada.")


main()