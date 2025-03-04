saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >=saque)
print(exp)

conta_normal_com_saldo_suficente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficente = conta_especial and saldo >= saque
exp_3 = conta_normal_com_saldo_suficente or conta_especial_com_saldo_suficente
print(exp_3)