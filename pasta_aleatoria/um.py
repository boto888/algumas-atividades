contem = ['um',2,'tres',4]
contador = []
for i in contem:
    if isinstance(i, str):
        contador.append(i)
print(len(contador))
