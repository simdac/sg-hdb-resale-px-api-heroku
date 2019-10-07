import requests
import sqlite3
import enum
import pandas as pd
import json

#API Variables
base_url = 'https://data.gov.sg/api/action/'
search = 'datastore_search?'
resource = 'resource_id='
offset = 'offset='
amp = '&'
columns=[]
colType=[]
mainData = []
flag=0
DataCount = 0
num = 0
#               Jan 2017 - now,                            Jan 2015 - Dec 2016 ,                Mar 2012 - Dec 2014 ,             2000 - Feb 2012                                1990 - 1999
links = ['42ff9cfe-abe5-4b54-beda-c88f9bb438ee','1b702208-44bf-4829-b620-4615ee19b57c','83b2fc37-ce8c-4df4-968b-370fd818138b','8c00bf08-9124-479e-aeca-7cc411d884c4', 'adbbddd3-30e2-445f-a123-29bee150a6fe']
# only latest 2 have Remaining lease (years)

#DB
sqlFile = 'resalePricesDB.sqlite'
df = pd.DataFrame()
Filenum = 0


class SQL(enum.Enum):
    '''

    A ENUM class having basic, widely used SQL statements


    '''

    Create = "CREATE TABLE"
    Alter  = "ALTER TABLE"
    Insert = "INSERT INTO"
    Delete = "DELETE FROM"
    Select = "SELECT"

    



class SQLite():


    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self.tableName = 'resale_flat_prices'


    def create_table(self, tableN, column, type):
        self.tableName = tableN
        self.cursor.execute(SQL.Create.value + " {tn} ".format(tn=self.tableName) + " ({} {})".format(column[0], type[0]))

    def add_columns(self, name, type):
        self.cursor.execute(SQL.Alter.value + " {} ".format(self.tableName)+"ADD COLUMN '{}' {} ".format(name, type))

    def add_multiple_columns(self, column, type):
        length  = len(column)
        for i in range(1, length):
            self.cursor.execute(SQL.Alter.value + " {} ".format(self.tableName) + "ADD COLUMN '{}' {} ".format(column[i], type[i]))


    def add_values(self,column,records):
        length  = len(column)
        if length ==11:
            length = length+1
        question = "? "
        for i in range(1, length):
            question = question+ ", ? "

        self.cursor.execute(SQL.Insert.value + " {} ".format(self.tableName) + " VALUES (" + question + ")", records)
        self.conn.commit()


    def close(self):
        self.conn.commit()
        self.conn.close()


#Gets the header for the Columns and thir data types
def getColumns(data):
    global columns, colType
    columns = []
    colType = []

    for i in range(0,len(data['result']['fields'])):
        id   = data['result']['fields'][i]['id']
        type = data['result']['fields'][i]['type']
        if type == 'numeric' or type =='int4':
            type = 'INTEGER'
        else:
            type = type.upper()
        columns.append(id)
        colType.append(type)



def reorderList(list):
    myOrder = [10,6,0,1,11,4,9,3,2,8,7,5]
    list = [list[i] for i in myOrder]

    if Filenum != 0:
        #lastDataId = 54424 + list[0]
        #lastDataId = 109230 + list[0]
        #lastDataId = 160433 + list[0]
        lastDataId =  898485 + list[0]

        list[0] = lastDataId

    return list


# Get the Values forch each column
def getData(data):
    for colmn in data['result']['records']:
        records = []
        for col in colmn:

            rec = colmn[col]
            records.append(rec)

        if Filenum == 2 or Filenum ==3 or Filenum==4:
            b = records[:]
            b[7:7] = [None]

        list = reorderList(b)
        print(list)

        #lite.add_values(columns, list)
        mainData.append(list)



# Get all data from that file
def getJson(n, offnum=0):
    global num, flag, mainData, df

    limit = num + 1//100
    offnum = 0
    print(limit)
    numb = 92300
    for i in range(0 , limit):

        url = base_url + search + offset + str(offnum) + amp + resource + links[n]
        file = requests.get(url)
        data = file.json()

        if flag==0:
            getColumns(data)
            df.assign(columns = columns)
            flag=1

        getData(data)
        print(offnum)
        offnum = offnum + 100
        #parsed =  json.dumps(data, indent=4)
        #print(parsed)
        mainData = []



def getFile(Filenum):
    global num

    print("File Number: {num}".format(num=Filenum + 1))

    url = base_url + search + resource + links[Filenum]
    file = requests.get(url).json()

    # Total no. of records in the file
    num = file['result']['total']
    print("Total Number of Entries: {n}".format(n=num))

    return file


def run():
    global num, Filenum


    #for Filenum in range(0,len(links)):
        #getJson(Filenum)
    getJson(Filenum)

Filenum = 4

getColumns(getFile(Filenum))

print(columns)
print(len(columns))

lite = SQLite(sqlFile)
#lite.create_table('resale_flat_prices_1',columns,colType)
#lite.add_multiple_columns(columns,colType)
run()


lite.close()
