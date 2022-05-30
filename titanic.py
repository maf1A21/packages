import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import seaborn as sns
from locale import normalize

data = pd.read_csv("titanic.csv")
data['Relatives'] = data['SibSp'] + data['Parch']

print(data.loc[(data['Survived'] == 1) & (data['Sex'] == 'male')])
print(data.isnull().sum())
print(data.loc[440:450:2, ['Sex', 'Age']])

data['Pclass'] = data['Pclass'].replace({1: "Макрочел", 2: "Чел", 3: "Микрочел"})
print(data['Pclass'].value_counts())

data['Fare_bin'] = pd.cut(data.Fare, bins=[-1, 20, 1000], labels=["Нормально", "Много"])
data = data.sort_values('Fare', ascending=False)
print("Возраст богатых женщин: ", data.loc[(data['Pclass'] == "Макрочел") & (data['Sex'] == 'female'), 'Age'].mean(), "\nВозраст богатых мужчин: ", data.loc[(data['Pclass'] == "Макрочел") & (data['Sex'] == 'male'), 'Age'].mean(), "\nВозраст женщин среднячков: ", data.loc[(data['Pclass'] == "Чел") & (data['Sex'] == 'female'), 'Age'].mean(), "\nВозраст мужчин среднячков: ", data.loc[(data['Pclass'] == "Чел") & (data['Sex'] == 'male'), 'Age'].mean(),"\nВозраст женщин работяг: ", data.loc[(data['Pclass'] == "Микрочел") & (data['Sex'] == 'female'), 'Age'].mean(), "\nВозраст мужчин работяг: ", data.loc[(data['Pclass'] == "Микрочел") & (data['Sex'] == 'male'), 'Age'].mean())


deadMen = data.loc[(data['Sex'] == 'male') & (data['Survived'] == 0), 'Age']
deadWomen = data.loc[(data['Sex'] == 'female') & (data['Survived'] == 0), 'Age']
dead = pd.DataFrame(data={'Men': deadMen, 'Women': deadWomen}, index=[i for i in range(max(deadMen.size, deadWomen.size))])
plt.figure()

dff = pd.DataFrame(data=dead, columns=['Men', 'Women'])
bp = sns.boxplot(x="variable", y="value", data=pd.melt(dff), whis=[5, 95])
bp.axes.set_title("Умершие", fontsize=16)
bp.set_xlabel("Пол", fontsize=14)
bp.set_ylabel("Возраст", fontsize=14)
plt.show()

