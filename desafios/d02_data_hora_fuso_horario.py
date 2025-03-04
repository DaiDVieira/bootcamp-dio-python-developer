def depositar(saldo_atual, valor, extrato, /):
    if valor > 0:
        saldo_atual += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
    else:
        print("Valor de depósito inválido. Tente novamente.")

    return saldo_atual, extrato

def exibir_extrato(saldo_atual, extrato, /):
    print("------------- Extrato ------------")
    if not extrato:
        print("Não foram realizadas movimentações.")    
    else:   
        print(extrato)
    print(f"\nSaldo:\t\t R$ {saldo_atual:.2f}")
    print("----------------------------------")

def sacar(saldo_atual, valor, extrato, numero_saques, limite_valor, /):
    if valor > 0:
        if saldo_atual < valor:
            print("Saldo insuficiente. Não será possível realizar o saque.")
        else:
            if valor >= limite_valor:
                print(f"Não é possível sacar valores maiores que R$ {limite_valor}. Tente novamente.")
            else:
                saldo_atual -= valor
                numero_saques += 1
                extrato += f"Saque:\t\t R$ {valor:.2f}\n"

    else:
        print("Valor de saque inválido. Tente novamente.")

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

    print("----- Usuário criado com sucesso! -----")
    

def criar_conta(usuarios, contas, agencia, numero_conta, /):
    if usuarios != []:
        cpf = input("Digite o CPF do usuário: ")
        usuario = filtar_usuario(cpf, usuarios)
        print(f"teste usuario: {usuario}")
        if usuario != None:
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
            numero_conta += 1
        else:
            print(f"Usuário de CPF {cpf} não está cadastrado. Operação cancelada.")
            return
    else:
        print("Não há usuários cadastrados. Cadastre um usuário antes de criar uma conta.")

    for conta in contas:
        print(conta)

    print(numero_conta)

    print("----- Conta criada com sucesso! -----")

    return numero_conta

def filtar_usuario(cpf, usuarios, /):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            posicao_usuario = usuarios.index(cpf)
            return usuario[posicao_usuario]
        else:
            return None  
    # usuario_filtrado = [usuarios.index(cpf) for usuario in usuarios if usuario["cpf"] == cpf]
    # return usuario_filtrado[usuarios.index(cpf)] if usuario_filtrado else None

def listar_contas(lista_contas):
    pass

def main():
    menu = """
-------------- MENU --------------
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

    print(usuarios)

    while True:
        opcao = input(menu)

        if opcao == "1":
            valor = float(input("\nDigite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":
            if numero_saques == LIMITE_SAQUES:
                print(f"Número máximo de {LIMITE_SAQUES} saques diários atingido. Tente novamente amanhã.")
            else:
                valor = float(input("\nDigite o valor do saque: "))
                saldo, extrato, numero_saques = sacar(saldo, valor, extrato, numero_saques, limite)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            numero_conta = criar_conta(usuarios, contas, AGENCIA, numero_conta)

        elif opcao == "5":
            print("Listar contas")

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            print("Obrigada por utilizar nosso sistema!")
            break

        else:
            print("Operação inválida. Por favor selecione novamente a operação desejada.")


main()