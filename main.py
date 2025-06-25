#Limpeza de dados com os dado do Titanic

# Importando o pandas
import pandas as pd
# Importando a base do titanic
titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# Visualizando a base
print(titanic.head())
# Seu formato
print(titanic.info())