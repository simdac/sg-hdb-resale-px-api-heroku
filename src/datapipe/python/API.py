import requests
import json
import pandas as pd




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



class API():
    '''
    The API class provides helpful functions to interact with the https://data.gov.sg/ API

    Attibutes
    -----------
    num: int
        The link number
    qry: str
        The query for the API database

    Methods
    ----------
    limit_fun(num)
        Adding the limit query to the API


    head(num = None)
        Return the url with limit query attached


    get(qry, num)
        Returns url with a query to select particular rows from the database of the API

    '''


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





def get_Json(url):
    file = requests.get(url)
    jsonData = file.json()

    return jsonData





def get_all():
    for i in range(len(links)):
        url = 'https://data.gov.sg/api/action/datastore_search?&resource_id='+links[i]

        jsonData = get_Json(url)
        total = jsonData['result']['total']


        api = API(i)
        uri = api.head(total)
        print(uri)
        jsonData = get_Json(uri)
        data = jsonData['result']['records']

        if i == 0:
            df = pd.DataFrame(data)

        else:
            df2 = pd.DataFrame(data)
            df = df.append(df2, ignore_index=True)

        
    return df
