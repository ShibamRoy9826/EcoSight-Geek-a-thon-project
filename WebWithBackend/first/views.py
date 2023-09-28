from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import AUC
from tensorflow.keras.preprocessing import image
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from first import carbonFootprint
import numpy

# Create your views here.
model=load_model('test.h5',compile=False)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[AUC(name='auc')])
def index(request):
    return render(request,'index.html')
    # return HttpResponse(os.getcwd())

def Amazon(request):
    return render(request,'Amazon/amazon.html')

def Carbon(request):

    return render(request,'carbon_calc/carbon_calc.html')

def AirPol(request):
    return render(request,'AirPollution/airQuality.html')
def SatelliteResults(request):
    try:
        uploaded_file = request.FILES.get('image')
        file_name = uploaded_file.name
        path = default_storage.save(file_name, ContentFile(uploaded_file.read()))
        data={}

        # Loading image

        img = image.load_img('EcoSight/media/'+path, target_size=(224,224))
        x = image.img_to_array(img)
        x = numpy.expand_dims(x, axis=0)
        x = x / 255.0

        # Making a prediction
        preds = model.predict(x)
        # preds=x


        # Making a prediction
        # preds = model.predict(image)
        data['agriculture']=round(preds[0][0],2)
        data['mine']=round(preds[0][1],2)
        data['empty']=round(preds[0][2],2)
        data['bloom']=round(preds[0][3],2)
        data['blowing']=round(preds[0][4],2)
        data['clear']=round(preds[0][5],2)
        data['cloudy']=round(preds[0][6],2)
        data['convolutionaryMine']=round(preds[0][7],2)
        data['cultivation']=round(preds[0][8],2)
        data['deforestation']=round(preds[0][9],2)
        data['haze']=round(preds[0][10],2)
        data['partlyCloudy']=round(preds[0][11],2)
        data['primary']=round(preds[0][12],2)
        data['road']=round(preds[0][13],2)
        data['logging']=round(preds[0][14],2)
        data['pollution']=round(preds[0][15],2)
        data['water']=round(preds[0][16],2)
        return render(request,'results/resultsSatellite.html',data)
    except Exception as e:
        return HttpResponse(e)

def CarbonResults(request):
    try:
        # Arguments to be passed to it
        country=request.GET['Country']
        daildist=request.GET['DailyDist']
        airdist=request.GET['AirDist']
        landdist=request.GET['LandDist']
        elecbill=request.GET['ElecBill']
        gasbill=request.GET['GasBill']

        found,ans,dailyV,airV,landV,elec,gas=carbonFootprint.CalculateTotal(country,daildist,airdist,landdist,elecbill,gasbill)


        ans=round(ans, 2)
        dailyV=round(dailyV,2)
        airV=round(airV,2)
        landV=round(landV,2)
        elec=round(elec,2)
        gas=round(gas,2)
        rec=[]
        d={'electricity bills':elec,'gas bills':gas,'daily rides':dailyV,'air travels':airV,'long land travels':landV}
        g=False


        if ans<2.5:
            rec.append("You are all good to go! try to maintain this!")
        else:

            max_key = max(d, key=d.get)

            a="Your carbon emmissions are quite high, try reducing your "+max_key+"!"
            rec.append(a)
        per_Cap=carbonFootprint.getPerCapita(country)

        if ans>per_Cap:
            rec.append("Your carbon emmisions are higher than the country average!")
        else:
            rec.append("Your carbon emmision are lower than the country average:)")
        data={'carbon':ans,'dailyV':dailyV,'airV':airV,'landV':landV,'elec':elec,'gas':gas,'recommendations':rec,'found':found}
        return render(request,'results/results.html',data)
    except Exception as e:
        return HttpResponse(e)