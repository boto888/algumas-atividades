conjunto_de_numeros = []

while True:
    entrada_dos_numeros = int(input('numeros: '))
    if entrada_dos_numeros == 0:
        break
    conjunto_de_numeros.append(entrada_dos_numeros)

if conjunto_de_numeros:
    soma = len(conjunto_de_numeros)
    print(soma)