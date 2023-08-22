import pandas as pd

carbon=pd.read_csv("allData/required_data.csv")
electricity=pd.read_csv("allData/PricesElectricity.csv")
psource=pd.read_csv("allData/PowerSource.csv")
ngprice=pd.read_csv("allData/NGPrices.csv")

cnt=input("From which country you belong? (in camel case) \n")

q1=input("How much distances(in Km) do you travel daily (via Bike, Scooter , Car,etc., not bicycle)?\n")
q2=input("Do you travel long distances like within the country or internationally? (y/n)\n")
q3=0
q4=0

if q2.lower()=="y":
	q3=input("How much distances do you cover each year by land vehicles( long distances)? (in km)\n")
	q4=input("How much distances do you cover by air vehicles( long distances)? (in km)\n")

q5=int(input("What is your monthly electricity bill( in $)? \n"))


total=0

# Electricity
ECo2={'Hydropower':20,'Gas':490,'Oil':730,'Coal':820,'Nuclear':40,'Wind':11}
# 1kwh coal=820
# 1kwh ng = 490
# 1kwh oil= 730
# 1kwh nuc=40
# 1kwh hydal=20
# 1kwh wind=11
# 1kwh solar=48 (no one has...as primmary source)



ElectSource=psource[psource['country'] == cnt]['major_power_source'].values[0]
# ElectCo2=ECo2[ElectSource]*
# TO BE UPDATED AND CONTINUED


# Normal vehicles per month co2 emmision
# 100g CO2 per km
# In tonnes
NVehiclePerYear=(int(q1)*100*365)/1000000

# Air vehicle per month co2 emmision
#285 grams per km per passenger
AirVehiclePerYear=(int(q3)*285)/1000000

# Land Vehicle(Trains) per month co2 emmision
LandVehiclePerYear=(int(q4)*50)/1000000
total=NVehiclePerYear+AirVehiclePerYear+LandVehiclePerYear+elec
print(total)
print("The average co2 emmision in your country is : ")

