# exemplo com loop infinito
while True:
    numero = int(input("Informe um numero: "))
    if numero == 10:
        break

    print(numero)

for numero in range(100):
    if numero == 12:
        break

    print(numero, end=" ")

# exibe apenas os numero impares
for numero in range(100):
    if numero % 2 == 0:
        continue

    print(numero, end=" ")