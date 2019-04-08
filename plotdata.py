import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from createdataset import *

#Create dataset
filename = str(input("Please enter the filename of your fb chat, it must be a HTML file\n"))
write_to_csv(filename)
count_messages_bydate()

#Plot data
data = pd.read_csv('sorted.csv')
data.shape
date = data['date'].values
count = data['0'].values
plt.plot(date, count)
plt.show()
