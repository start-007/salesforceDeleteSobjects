import requests
from credentials import Headers
url="https://devrev4-dev-ed.develop.my.salesforce.com/services/data/v57.0/query?q=SELECT+Id+From+FeedItem+LIMIT+200"
response=requests.get(url,headers=Headers)
print(response.json())
url="https://devrev4-dev-ed.develop.my.salesforce.com/services/data/v57.0/sobjects/FeedItem/"
for i in range(len(response.json()["records"])):
    res=requests.delete(url+response.json()["records"][i]["Id"],headers=Headers)
    print(res)


