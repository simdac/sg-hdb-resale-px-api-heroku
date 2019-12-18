import requests
import json



access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMzNTAsInVzZXJfaWQiOjMzNTAsImVtYWlsIjoiYWRpdHlhYmhhZGthbWthcjk5QGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU3MDUzNjAwNywiZXhwIjoxNTcwOTY4MDA3LCJuYmYiOjE1NzA1MzYwMDcsImp0aSI6IjZlNGIyMjhjMDMxNGFjNDZhN2I2NzJmYmVhOTJkNmI3In0.-bi2XjC6yJRJMIGJuoe55Z5G1dmmsBfclqNzexMToio'



class MapAPI():

    def __init__(self):
        self.base =  'https://developers.onemap.sg/'
        self.api_ext  =  '/commonapi/search?'
        self.token    =  '&token={}'.format(access_token)
        self.base_url = self.base+ self.api_ext+ self.token

    def searchCord(self,query, geom='Y', addr='Y', page=1):
        #print('***',query)
        query = self.convertQuery(query)
        self.search  = '&searchVal={}'.format(query)
        self.geom    = '&returnGeom={}'.format(geom)
        self.address = '&getAddrDetails={}'.format(addr)
        self.pageNum = '&pageNum={}'.format(page)
        url = self.base_url+ self.search+ self.geom+ self.address+ self.pageNum
        #print(url)
        return self.getLatLng(url)


    def getLatLng(self, url):
        file = requests.get(url)
        data = file.json()
        j = json.dumps(data, indent=4)
        #print(j)
        lat = data['results'][0]['LATITUDE']
        lng = data['results'][0]['LONGITUDE']
        cordinates = (lat,lng)
        #print(cordinates)
        return cordinates

    def convertQuery(self, string_query):
        que = string_query.replace(' ','+')
        return que

#data = MapAPI().search('323 Ang Mo Kio')

#print(data)
