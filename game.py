import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly as py
from sys import argv

def dice_roll():
	N=np.random.random_integers(1,6)
	return N


target = open('file1.csv', 'w')
target.truncate()


for i in range(50):
	target.write(str(dice_roll() + dice_roll()))
	target.write("\n")

target.close()

pd.read_csv('file1.csv').hist(bins=[1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5])
plt.title("Roll of the dice")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()