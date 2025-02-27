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

def main():
    menu = """
-------------- MENU --------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("\nDigite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            if numero_saques == LIMITE_SAQUES:
                print(f"Número máximo de {LIMITE_SAQUES} saques diários atingido. Tente novamente amanhã.")
            else:
                valor = float(input("\nDigite o valor do saque: "))
                saldo, extrato, numero_saques = sacar(saldo, valor, extrato, numero_saques, limite)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigada por utilizar nosso sistema!")
            break

        else:
            print("Operação inválida. Por favor selecione novamente a operação desejada.")


main()