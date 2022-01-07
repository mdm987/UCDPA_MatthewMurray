# The Tokyo Summer Olympics 2020 Medal Analysis

# Importing the packages used throughout
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importing Data
medals = pd.read_csv('TokyoMedals2020.csv', index_col=0)
athletes = pd.read_csv('TokyoAthletes2020.csv', index_col="name")

# Convert Data Types
medals = medals.astype({"discipline": str})
athletes = athletes.astype({"discipline": str})
medals['medal_date'] = pd.to_datetime(medals['medal_date'])
athletes['birth_date'] = pd.to_datetime(athletes['birth_date'])

# Sorting Data - By Discipline Ascending
medals.sort_values('discipline', ascending=True)
athletes.sort_values('discipline', ascending=False)

# Indexing - Create new object
athletes_object = athletes['birth_date']
print(athletes_object)

# Replace Missing values - Where blank birth country replace with unknown
athletes['birth_country'] = athletes['birth_country'].replace(np.nan, 'Unknown')

# Slicing - Indexed Medals Above
print(medals[33:39])

# loc - Indexed by Name Above
first = athletes.loc["BARR Thomas"]
second = athletes.loc["HARRINGTON Kellie Anne"]
print(first, "\n\n\n", second)

# Iterrows
#for lab, row in medals.iterrows():
  #  print(lab)
  #  print(row)

# Merge athletes & medal
#olympicmerge = pd.concat(
#    map(pd.read_csv, ['TokyoAthletes2020.csv', 'TokyoMedals2020.csv']), ignore_index=True)
#print(olympicmerge)

# Join the dataframes
#olympicjoin_df = athletes.merge(medals, how = 'left', on = 'name')
#print(olympicjoin_df)


# View header shape datatype
print(medals.head())
print(medals.shape)
print(medals.dtypes)
print(medals)
# View header shape datatype
print(athletes.head())
print(athletes.shape)
print(athletes.dtypes)
print(athletes['birth_country'])


# Grouping - Medals by Discipline
#medals = medals.groupby(['discipline', 'medal_type'])['medal_code'].count().reset_index()
#medals.head()


## Scatter Chart Example
#plt.scatter(medals['event'], medals['country'], s=3)
#plt.xlabel('Event')
#plt.ylabel('Country')
#plt.title('Olympic Medals')
#plt.show()


# Plot the top 5 countries with the most athletes competing in Japan 2020
country_rep = athletes.country.value_counts().sort_values(ascending=False).head(5)
plt.figure(figsize=(10,6))
plt.title('Countries with most competing athletes (Top 5)')
sns.barplot(x=country_rep.index,y=country_rep, palette = 'Set3')
plt.show()
