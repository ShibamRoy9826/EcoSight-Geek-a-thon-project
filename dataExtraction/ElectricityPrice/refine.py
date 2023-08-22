import pandas

df=pandas.read_csv("Prices.csv")

df=df[['Country name','Average price of 1KW/h (USD)']]
newNames={'Country name':'country', 'Average price of 1KW/h (USD)':'AvgPrice'}
# print(df.columns)
df.rename(newNames,inplace=True)
df.to_csv("PricesElectricity.csv")
print(df)