# The Tokyo Summer Olympics 2020 Medal Analysis

# Importing the packages used throughout
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create required datasets
medals = pd.read_csv('TokyoMedals2020.csv')
athletes = pd.read_csv('TokyoAthletes2020.csv')

# View header shape datatype
print(medals.head())
print(medals.shape)
print(medals.dtypes)
print(athletes.head())
print(athletes.shape)
print(athletes.dtypes)

## Scatter Chart Example
#plt.scatter(medals['event'], medals['country'], s=3)
#plt.xlabel('Event')
#plt.ylabel('Country')
#plt.title('Olympic Medals')
#plt.show()