import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sorted.csv')
data.shape
date = data['date'].values
count = data['0'].values
plt.plot(date, count)
plt.show()
