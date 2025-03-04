def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")
    
    print("Fim do saque")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(100)