''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    saldo = 0
    print(transacoes)

    # TODO: Itere sobre cada transação na lista:
    for valor in transacoes:
        # TODO: Adicione o valor da transação ao saldo
        saldo += valor
        print(saldo)
        
    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return saldo
    

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]
print(transacoes)

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(f"Saldo: R$ {resultado:.2f}")