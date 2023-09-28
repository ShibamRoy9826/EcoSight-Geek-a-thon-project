import pandas
import os

print(os.getcwd())
d=pandas.read_csv("importantData.csv")

# Data vars
ElecCO2={'Hydropower':20,'Gas':490,'Oil':730,'Coal':820,'Nuclear':40,'Wind':11}


# Inputs

def getPercentage(something,total):
	return (something / total) * 100

def CalculateTotal(Country, DailyDist, LongDistLand, LongDistAir, ElecBill , GasBill):

    # Electricity Emmissions
    try:
        SourceElec=d[d['country'] == Country.lower()]['major_power_source'].values[0]
        PriceElec=d[d['country']==Country.lower()]['AvgPrice'].values[0]
        KwHElec=(float(ElecBill)/float(PriceElec))
        ElecMonthly=(ElecCO2[SourceElec]*KwHElec)/1000000


        # Gas Emmissions
        NGKwh=float(GasBill)*0.121
        NGMonthly=(NGKwh*490)/1000000


        # Daily Vehicle emmission
        NVehiclePerYear=(float(DailyDist)*100*365)/1000000

        # Air Vehicle emmission
        AirVehiclePerYear=(float(LongDistAir)*285)/1000000

        # Land Vehicle( Long Distances ) emmission
        LandVehiclePerYear=(float(LongDistLand)*50)/1000000

        total=NVehiclePerYear+AirVehiclePerYear+LandVehiclePerYear+(ElecMonthly*12)+(NGMonthly*12)
        found=True

        return found,total,getPercentage(NVehiclePerYear,total),getPercentage(AirVehiclePerYear,total),getPercentage(LandVehiclePerYear,total),getPercentage(ElecMonthly*12,total),getPercentage(NGMonthly*12,total)

    except:
        SourceElec=d[d['country'] == 'Avg']['major_power_source'].values[0]
        PriceElec=d[d['country']=='Avg']['AvgPrice'].values[0]
        KwHElec=(float(ElecBill)/float(PriceElec))
        ElecMonthly=(ElecCO2[SourceElec]*KwHElec)/1000000


        # Gas Emmissions
        NGKwh=float(GasBill)*0.121
        NGMonthly=(NGKwh*490)/1000000


        # Daily Vehicle emmission
        NVehiclePerYear=(float(DailyDist)*100*365)/1000000

        # Air Vehicle emmission
        AirVehiclePerYear=(float(LongDistAir)*285)/1000000

        # Land Vehicle( Long Distances ) emmission
        LandVehiclePerYear=(float(LongDistLand)*50)/1000000

        total=NVehiclePerYear+AirVehiclePerYear+LandVehiclePerYear+(ElecMonthly*12)+(NGMonthly*12)
        found=False

        return found,total,getPercentage(NVehiclePerYear,total),getPercentage(AirVehiclePerYear,total),getPercentage(LandVehiclePerYear,total),getPercentage(ElecMonthly*12,total),getPercentage(NGMonthly*12,total)
def getPerCapita(Country):
    try:
        return d[d['country']==Country.lower()]['co2_per_capita'].values[0]
    except:
        return d[d['country']=='Avg']['co2_per_capita'].values[0]