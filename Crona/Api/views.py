from django.shortcuts import render
from rest_framework import generics
def Home(request):
    url = "https://coronavirus-19-api.herokuapp.com/countries"
    data = requests.get(url)
    serverError = False
    try:
        data = data.json()
    except :
        serverError = True
        serverError = {"serverError" : serverError}
        return render(request,template_name="index.html",context=serverError)
    cases,todayCases,deaths,recovered =0,0,0,0
    error = False
    country = "Global"
    
    if request.method == "POST" and not request.POST["country"]=="":
        for x in data:
            if x.get("country").lower()== request.POST["country"].lower():
                cases += x["cases"]
                todayCases += x["todayCases"] 
                deaths += x["deaths"]
                recovered += x["recovered"]
                country = x["country"]
                error = False
                break
            else:
                error = True
                continue
    else:
        for x in data:
            error = False
            try:
                todayCases += x["todayCases"]
            except:
                todayCases +=0
            try:
                cases += x["cases"]
            except:
                cases +=0
            try:
                deaths += x["deaths"]
            except:
                deaths +=0
            try:
                recovered += x["recovered"]
            except:
                recovered +=0
    if error : 
        data = {"error":error,"cases" : cases,"todayCases":todayCases,"deaths":deaths,"recovered":recovered,"country":country}
    else :
        data = {"cases" : cases,"todayCases":todayCases,"deaths":deaths,"recovered":recovered,"country":country}

    return render(request,template_name="index.html",context=data)




import requests 
from rest_framework.response import Response
class CountryView(generics.ListAPIView):
    def get(self, request,country="India", *args, **kwargs):
        url = "https://coronavirus-19-api.herokuapp.com/countries"
        data = requests.get(url)
        try :
            data = data.json()
        except :
            return Response({"error":"Please Visit after some time"})
        for x in data:
            if x.get("country").lower()==country.lower():
                DataIndia = x
                break
            else :
                DataIndia="null"
                continue
        if DataIndia == "null" :
            return Response({"error":"Please Provide Valid Country Name"})
        data = {"Success" : DataIndia}
        return Response(data)

class GlobalView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        url = "https://coronavirus-19-api.herokuapp.com/countries"
        data = requests.get(url)
        try :
            data = data.json()
        except :
            return Response({"error":"Please Visit after some time"})
        data = {"Success" : data}
        return Response(data)

