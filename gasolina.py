 import pandas as pd
import matplotlib.pyplot as plt

%%writefile gasolina.csv
dia,venda
1,5.11
2,4.99
3,5.02
4,5.21
5,5.07
6,5.09
7,5.13
8,5.12
9,4.94
10,5.03

df = pd.read_csv("gasolina.csv", sep=",")
plt.plot(df["dia"], df["venda"])
plt.xlabel("Dia")
plt.ylabel("Preço")
plt.title("Preço da gasolina")
plt.savefig("gasolina.png")
