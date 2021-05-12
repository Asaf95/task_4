# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:22:21 2021

@author: Asaf
"""
import requests
import smtplib
import json
dic_dis ={}
def get_lat_lng(address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), api_key))
    response = requests.get(url)
    resp_json_payload = response.json()
    lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    return lat, lng
#Please use your API code
api_file = open("api-key.txt","r")
api_key = api_file.read()
api_file.close()
i = 0 
home = "תל%אביב"
#word = open("dests","utf-8")
dests = open('dests.txt',encoding="utf8")
dests = dests.readlines()
size = len(dests)
list_of_all =list()
for line in dests:
    if i >5 :
        break
    work = dests[i]
    i += 1
# URL JSON
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"
    u = (url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 
# get response
    r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)    
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
    distance = distance.replace(" ","")
    distance =distance.replace("km","")
    city = {work: (distance, time,get_lat_lng(work)[0],get_lat_lng(work)[1])} 
    list_of_all.append(city)
    dic_dis[work] =distance
    
print(list_of_all)
sort_orders = sorted(dic_dis.items(), key=lambda x: x[1])
f = 0
for i in sort_orders:
    print(i[0], i[1])
    f = f + 1
    if f > 2:
        break