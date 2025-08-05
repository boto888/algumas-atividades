numero1 = int(input('um:'))
numero2 = int(input('dois:'))
numero3 = int(input('tres:'))

if (numero1 > numero2) and ( numero1 > numero3):
    print(numero1)
elif (numero2 > numero1) and (numero2 > numero3):
    print(numero2)
else:
    print(numero3)