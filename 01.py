conjunto_de_numeros = []

while True:
    try:
        entrada_dos_numeros = int(input('numeros: '))
        if entrada_dos_numeros == 0:
            break
        conjunto_de_numeros.append(entrada_dos_numeros)
    except ValueError:
        print('entrada invalida')

if conjunto_de_numeros:
    soma = len(conjunto_de_numeros)
    print(soma)