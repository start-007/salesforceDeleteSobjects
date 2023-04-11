import requests
from credentials import Headers


url="https://devrev4-dev-ed.develop.my.salesforce.com/services/data/v57.0/query?q=SELECT+Id+From+Contact+LIMIT+200"
response=requests.get(url,headers=Headers)

url="https://devrev4-dev-ed.develop.my.salesforce.com/services/data/v57.0/sobjects/Contact/"
for i in range(len(response.json()["records"])):
    res=requests.delete(url+response.json()["records"][i]["Id"],headers=Headers)
    print(res)


