import requests
import json









authKey = '228205717243423189106x3663'

apiKey = '4227ca92784d4f8292daaa30ab42d521'
#Limit of 2,500 requests per day
#
street = 'ANG+MO+KIO+AVE+3'
block = '323+block'
town = 'ANG MO KIO'
geocode = 'https://api.opencagedata.com/geocode/v1/json?q='+block+'%'+street+'%'+town+'%Singapore&key=4227ca92784d4f8292daaa30ab42d521'





class MapApi():
    def __init__(self):
        self.base_url = 'https://api.opencagedata.com/geocode/v1/json?q='
        self.endKey = '%Singapore&key=4227ca92784d4f8292daaa30ab42d521'

    def getTown(self, town):
        town = self.convertToQuery(town)
        url = self.base_url+town+self.endKey
        return self.getLatLng(url)

    def getLatLng(self, url):
        file = requests.get(url)
        data = file.json()
        lat = data['results'][0]['geometry']['lat']
        lng = data['results'][0]['geometry']['lng']
        cordinates = (lat,lng)
        return cordinates



    def convertToQuery(self, string_query):
        que = string_query.replace(' ','+')
        return que



#api = MapApi()
#print(api.getTown(town))
