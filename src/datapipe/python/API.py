import requests
import json
import pandas as pd



'''       MAKE EASY AND QUICK CONNECTION TO API GOV                             '''

base_url = 'https://data.gov.sg/api/action/'
search = 'datastore_search?'
resource = 'resource_id='
offset = 'offset='
amp = '&'
limit = '&limit={}'
query = '&q={}'

#               Jan 2017 - now,                            Jan 2015 - Dec 2016 ,                Mar 2012 - Dec 2014 ,             2000 - Feb 2012                                1990 - 1999
links = ['42ff9cfe-abe5-4b54-beda-c88f9bb438ee','1b702208-44bf-4829-b620-4615ee19b57c','83b2fc37-ce8c-4df4-968b-370fd818138b','8c00bf08-9124-479e-aeca-7cc411d884c4', 'adbbddd3-30e2-445f-a123-29bee150a6fe']
# only latest 2 have Remaining lease (years)



'''   A simple class to access and query gov api      '''
class API():

    def __init__(self, num):
        self.url = 'https://data.gov.sg/api/action/datastore_search?&resource_id='+links[num]

    def limit_fun(self, num):
        l = limit.format(str(num))
        uri = self.url+l
        return uri


    def head(self, num = None):

        if num is None:
            url = self.limit_fun(5)
            return url
        else:
            url = self.limit_fun(num)
            return url





    def get(self, qry, num):

            q = query.format(qry)
            url = self.limit_fun(num)+ q
            return url

    def get_total(self):
        total = ''









def get_all():
    for i in range(len(links)):
        url = 'https://data.gov.sg/api/action/datastore_search?&resource_id='+links[i]
        print(url)
        file = requests.get(url)
        jsonData = file.json()
        data = jsonData['result']['records']
        total = jsonData['result']['total']
        #api = API(0)

        print(i)
        print(total)
        total=0
        #api =


api = API(0)
url = api.head(56335)
#url = api.get('2 ROOM',5)


print(url)
file = requests.get(url)
jsonData = file.json()

total = jsonData['result']['total']
df = pd.DataFrame(data)
#parse = json.dumps(jsonData, indent=4)

get_all()





print(df.head())
print(df.info())
print(df.shape)
print(df.tail())
