
perguntas = ['telefonou para a vitima?', 'esteve no local do crime?','mora perto da vitima?']
score = 0
for pergunta in perguntas:
    print(pergunta)
    escolha = input('sim ou não: ').lower()
    if escolha == 'sim':
        score += 1
        print('mais um')
print(f'sua pontuação {score}')