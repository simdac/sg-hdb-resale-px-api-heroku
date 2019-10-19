
import  pandas as pd



df = pd.read_csv('resale_flat_prices.csv')
print(df.head())
d = df.loc[df.town =='YISHUN']
print(df.shape)
print(d['flat_type'].unique())



''
