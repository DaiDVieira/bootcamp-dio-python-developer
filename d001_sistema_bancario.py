def depositar(saldo_atual, valor, extrato, /):
    if valor > 0:
        saldo_atual += valor
        extrato += f"Depósito:\t R$ {valor: .2f}\n"
    else:
        print("Valor de depósito inválido. Tente novamente.")
    return saldo_atual, extrato

def exibir_extrato(saldo_atual, extrato, /):
    print("------------- Extrato ------------")
    if not extrato:
        print("Não foram realizadas movimentações")    
    else:   
        print(extrato)
    print(f"\nSaldo:\t\t R$ {saldo_atual:.2f}")
    print("----------------------------------")

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
            print("Saque")

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigada por utilizar nosso sistema!")
            break

        else:
            print("Operação inválida. Por favor selecione novamente a operação desejada.")


main()