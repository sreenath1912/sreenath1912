import pandas as pd

df = pd.read_csv(r'C:\Users\Awcc\Documents\Data_Python\weather_by_cities_group_by.csv')
print(df.head())
x = df.pivot_table(index='city', values=['temperature', 'windspeed'])
print(x)
df = pd.read_csv(r'C:\Users\Awcc\Downloads\titanic.csv')
print(df.head())
y= df.pivot_table(index='Sex', values='Survived')*100
print(y)

