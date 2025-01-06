import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv", sep=",")
plt.plot(df["dia"], df["venda"])
plt.xlabel("Dia")
plt.ylabel("Preço")
plt.title("Preço da gasolina")
plt.savefig("gasolina.png")
