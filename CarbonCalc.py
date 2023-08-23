import pandas as pd

# all data
carbon=pd.read_csv("allData/required_data.csv")
electricity=pd.read_csv("allData/PricesElectricity.csv")
psource=pd.read_csv("allData/PowerSource.csv")
NotFoundCountry=False

# Questions
cnt=input("From which country you belong? (in camel case) \n")
q1=input("How much distances(in Km) do you travel daily (via Bike, Scooter , Car,etc., not bicycle)?\n")
q2=input("Do you travel long distances like within the country or internationally? (y/n)\n")
q3=0
q4=0

if q2.lower()=="y":
	q3=input("How much distances do you cover each year by land vehicles( long distances)? (in km)\n")
	q4=input("How much distances do you cover by air vehicles( long distances)? (in km)\n")

elecBill=float(input("What is your monthly electricity bill( in $)? \n"))

NGBill=float(input("What is your monthly natural gas bill/cost (in $)?"))

total=0

# Electricity

# Added newlines to keys cause the dataset also has them
# Better than removing the newline characters ig
ECo2={'Hydropower\n':20,'Gas\n':490,'Oil\n':730,'Coal\n':820,'Nuclear\n':40,'Wind\n':11}
# 1kwh coal=820
# 1kwh ng = 490
# 1kwh oil= 730
# 1kwh nuc=40
# 1kwh hydal=20
# 1kwh wind=11
# 1kwh solar=48 (no one has...as primmary source)


if cnt not in psource.country:
	ElectSource='Coal'
	NotFoundCountry=True

ElectSource=psource[psource['country'] == cnt]['major_power_source'].values[0]
ElectPrice=electricity[electricity['country']==cnt]['AvgPrice'].values[0]
ElectKwH=(elecBill/float(ElectPrice.replace("$","")))
# Electricity Co2 emission in Tonnes
ElectMonthly=(ECo2[ElectSource]*ElectKwH)/1000000


# Natural gas co2 emission in tonnes
# avg price of NG over the world is 0.121
NGKwh=NGBill*0.121
NGMonthly=(NGKwh*490)/1000000

# Normal vehicles per month co2 emmision
# 100g CO2 per km
# In tonnes
NVehiclePerYear=(float(q1)*100*365)/1000000

# Air vehicle per month co2 emmision
#285 grams per km per passenger
AirVehiclePerYear=(float(q3)*285)/1000000

# Land Vehicle(Trains) per month co2 emmision
LandVehiclePerYear=(float(q4)*50)/1000000

# Total calculation
total=NVehiclePerYear+AirVehiclePerYear+LandVehiclePerYear+(ElectMonthly*12)+(NGMonthly*12)

print("\n\nAir Vehicles:- ",AirVehiclePerYear)
print("Land Vehicles(long distances):- ", LandVehiclePerYear)
print("Daily Vehicles:- ",NVehiclePerYear)
print("NG yearly:-",NGMonthly*12)
print("electricity yearly:- ",ElectMonthly*12)



print("\n\nYour total annual CO2 emmision is : ",total)
print("The average co2 emmision in your country is : ",carbon[carbon['country']==cnt]['co2_per_capita'].values[0])

