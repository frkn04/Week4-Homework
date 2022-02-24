
import random 
import requests


result = []

count = 0

while count < 100:

    count += 1

    r = requests.get("https://randomuser.me/api/")
    
    name = (str(r.json()["results"][0]["name"]["first"]).replace(" ", "")).lower()
    l_name = (str(r.json()["results"][0]["name"]["last"]).replace(" ", "")).lower()
    city = (str(r.json()["results"][0]["location"]["city"]).replace(" ", "")).lower()
    country = (str(r.json()["results"][0]["location"]["country"]).replace(" ", "")).lower()

    all = name + l_name + city + country

    all = list(all)

    random.shuffle(all)

    result.append("".join(all))
       

print(max(result, key=len))