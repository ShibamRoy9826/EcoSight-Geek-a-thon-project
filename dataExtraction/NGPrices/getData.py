import pandas

df={'country':[],'natural_gas_price':[]}
with open("data.txt","r") as f:
	for line in f.readlines():
		if line!="":
			splt=line.split("\t")
			print(splt)
			df['country'].append(splt[0])
			df['natural_gas_price'].append(splt[1])
df=pandas.DataFrame(df)
df.to_csv("NGPrices.csv")