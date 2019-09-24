import requests
from requests.models import PreparedRequest
import pandas as pd

req = PreparedRequest()




class MYSQL():
    def __init__(self):
        self.table = "resale_flat_prices"

    def head(self, num=None):
        if num is not None:
            sql = "SELECT * FROM {} ".format(self.table)+"LIMIT {}".format(num)
            return sql

        else:
            sql = "SELECT * FROM {} ".format(self.table)+"LIMIT 5"
            return sql


    def describe(self):
        sql = "DESCRIBE {}".format(self.table)
        return sql


    def tail(self, id, num = None):

        if num is not None:
            sql = "SELECT * FROM {} ".format(self.table)+"ORDER BY {} ".format(id)+" DESC LIMIT {} ".format(num)
            return sql
        else:
            sql = "SELECT * FROM {} ".format(self.table)+"ORDER BY {} ".format(id)+" DESC LIMIT 5"
            return sql



def get_headers(txt):
    headers= []
    for i in range(len(txt)):
        if txt[i] =="<th>":
            headers.append(txt[i+1])
    return headers


def get_data(txt):
    fullData = []

    for i in range(len(txt)):
        row = i
        rowData = []
        data = []
        if txt[i]=="<tr>" and txt[i+1]!="<th>":


            while (txt[row]!="</tr>"):
                td = row + 1

                if txt[row]=="<td>":

                    while (txt[td]!="</td>"):
                        data.append(txt[td])
                        td = td +1

                    tdata = ' '.join(data)
                    rowData.append(tdata)
                    data=[]

                row = row +1

            fullData.append(rowData)
            rowData=[]

    return fullData
