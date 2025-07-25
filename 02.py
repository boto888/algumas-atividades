idade = []

while True:
    try:
        pessoas = int(input('idade da pessoas: '))
        if pessoas == 0:
            break
        idade.append(pessoas)
    except ValueError:
        print('entrada invalida')
    
if idade:
    quantidade_de_pessoas = len(idade)
    media_de_pessoas = sum(idade)/quantidade_de_pessoas
    maior_idade = max(idade)
    menor_idade = min(idade)
    print(*idade, sep=', ')
    print('-'*20)
    print(quantidade_de_pessoas)
    print('-'*20)
    print(media_de_pessoas)
    print('-'*20)
    print(maior_idade)
    print('-'*20)
    print(menor_idade)
else:
    print('nada foi colocado')


