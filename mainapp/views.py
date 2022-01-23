from wsgiref.util import request_uri
from django.shortcuts import render

import requests #for sending request

# Create your views here.


def index(request):

    # Using Weather Api - https://www.weatherapi.com/
    API_KEY = 'f40f2ff7675a4db5921142853222301'
    BASE_URL ='http://api.weatherapi.com/v1'

    if request.method=='POST':
        city=request.POST.get('city')
        print(city)

        if(city== ''):
            print('No value')
            return render(request,'index.html',{'checker':'Please enter valid info...!'})

        else:
            # abc=input("Enter City : ")
            #request_url = f"{BASE_URL}?appid={API_KEY}&q{abc}"  #checking city with API
            request_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=no"  #checking city with API (Using Weather Api)

            # print(request_url)
            # print('http://api.weatherapi.com/v1/current.json?key=f40f2ff7675a4db5921142853222301&q=kerala&aqi=no')

            response = requests.get(request_url)

            if response.status_code == 200:
                data = response.json()
                # print(data)

                location=data['location']
                weather = data['current']
                # print(weather)
                print(location['tz_id'])
                print(weather['temp_c'])

                return render(request,'index.html',{'location':location['tz_id'],'weather':weather['temp_c'],'static_city':city})

            else:
                print("An error occurred")
                return render(request,'index.html',{'static_city':city,'checker':'An error occurred'})




    return render(request,'index.html',{})