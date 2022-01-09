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

# Replace Missing values - Where blank values replace with unknown
athletes['birth_country'] = athletes['birth_country'].replace(np.nan, 'Unknown')
medals['athlete_sex'] = medals['athlete_sex'].replace(np.nan, 'Unknown')

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

# Example custom function
def multiplythreenums (a,b,c) :
    return a * b * c
print (multiplythreenums(3,3,3))
print (multiplythreenums(9900,8800,7700))

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



# 1 - Gender breakdown of competing athletes
gender_breakdown = athletes.gender.value_counts()
plt.figure(figsize=(12,8))
plt.title('Gender breakdown of the athletes')
plt.pie(gender_breakdown, labels=gender_breakdown.index,autopct='%1.1f%%',startangle=90)
#plt.show()

# 2 - Top 5 countries with the most athletes
country_rep = athletes.country.value_counts().sort_values(ascending=False).head(5)
plt.figure(figsize=(10,6))
plt.title('Countries with most competing athletes (Top 5)')
sns.barplot(x=country_rep.index,y=country_rep, palette = 'Set3')
plt.xlabel('Countries')
plt.ylabel('Number of Athletes')
#plt.show()

# 3 - Age Breakdown across the athletes
plt.figure(figsize=(12,8))
plt.title('Age breakdown of the athletes')
plt.xlabel('Age')
plt.ylabel('Number of athletes')
plt.hist(athletes.Age, bins = np.arange(12,70,2),color='pink',edgecolor ='black')
# plt.show()

# 4 - Top 10 countries with most medal wins
event_medals = medals.country.value_counts().sort_values(ascending=False).head(8)
plt.figure(figsize=(14,10))
plt.title('Countries with the most medals (Top 10)')
sns.barplot(x=event_medals,y=event_medals.index, palette = 'Set2')
plt.xlabel('Number of medals')
#plt.show()

# 5 - Seaborn Scatter Plot showing Age by Olympic Discipline
plt.figure(figsize=(16,12))
sns.set_style("whitegrid")
axis = sns.scatterplot (x="Age", y="discipline", data=athletes, hue='gender')
plt.title ('Age by Olympic Discipline')
#plt.show()


