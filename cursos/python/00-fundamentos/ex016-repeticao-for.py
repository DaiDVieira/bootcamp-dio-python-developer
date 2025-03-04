texto = input("Entre com um texto: ")
VOGAIS = "AEIOU"

# exemplo com iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() # adiciona uma quebra de linha

# exemplo com a função built-in range - tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

print()

# conversao do objeto range em lista
lista = list(range(4))
print(lista)