import pandas as pd

df=pd.read_csv('co2.csv')

miyangin=0
for i in range (0,500):
    miyangin = miyangin + df['out1'][i]

print(miyangin)
miyangin=miyangin/500

print(miyangin)