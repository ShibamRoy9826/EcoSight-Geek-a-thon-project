import pandas

df={"country":[],"major_power_source":[]}

with open("PowerSource.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        if line!="\n":
            splt=line.split(": ")
            df['country'].append(splt[0])
            df['major_power_source'].append(splt[1])

df=pandas.DataFrame(df)

df.to_csv("PowerSource.csv")
