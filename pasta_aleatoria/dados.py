import pandas as pd

dados = pd.read_csv('math.csv', sep=',')
print(dados[['Login ID','Full Name']])