import requests
import json
import sqlite3
import mysql


#API
base_url = 'https://data.gov.sg/api/action/'
search = 'datastore_search?'
resource = 'resource_id='
offset = 'offset='
amp = '&'

# RESALE DATABASE QUERY  ID
#               Jan 2017 - now,                            Jan 2015 - Dec 2016 ,                Mar 2012 - Dec 2014 ,             2000 - Feb 2012                             1990 - 1999
res = ['42ff9cfe-abe5-4b54-beda-c88f9bb438ee','1b702208-44bf-4829-b620-4615ee19b57c','83b2fc37-ce8c-4df4-968b-370fd818138b','8c00bf08-9124-479e-aeca-7cc411d884c4', 'adbbddd3-30e2-445f-a123-29bee150a6fe']

#0-4
n=2

url = base_url + search + resource + res[n]
file = requests.get(url).json()

#Get total no of pages in that file
num = file['result']['total'] - 1
print(num)

#Get all data from that file
def getData(n, offnum = 0):
    global num
    for i in range(0, num):

        url = base_url + search + offset+ str(offnum) +amp+ resource + res[n]
        file = requests.get(url)
        data = file.json()
        offnum = offnum+100


        parsed = json.dumps(data, indent=4)
        print(parsed)


getData(n)



#Database
#






