import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# Amostra Estratificada

# Importando base de dados
iris = pd.read_csv('dados/Iris.csv')
iris['class'].value_counts()

# Criando amostra
x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size = 0.5, stratify = iris.iloc[:, 4])
y.value_counts()


# Importando base de dados
infert = pd.read_csv('dados/Infert.csv')
infert['education'].value_counts()

# Criando amostra
x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size = 0.6, stratify = infert.iloc[:, 1])
y1.value_counts()