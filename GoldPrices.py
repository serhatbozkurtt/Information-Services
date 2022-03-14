import base64, requests, sys, json
import requests
import json
import datetime

client_id = "l7xx052c5c1953a141d09d7ceabb221aa757"
client_secret = "f78b4311a28b4a56a901e06383e79634"

# Encode the client ID and client secret
authorization = base64.b64encode(bytes(client_id + ":" + client_secret, "ISO-8859-1")).decode("ascii")


headers = {
    "Authorization": f"Basic {authorization}",
    "Content-Type": "application/x-www-form-urlencoded"
}
body = {
    "grant_type": "client_credentials"
}

response = requests.post("https://apigw.vakifbank.com.tr:8443/auth/oauth/v2/token", data=body, headers=headers)

#print(response.text)

a = json.loads(response.text)
print("a " , a)
print(a['access_token'])

access_token = a['access_token']

getgoldp= "getGoldPrices"

url = "https://apigw.vakifbank.com.tr:8443/"

url = url + getgoldp

bugun = datetime.date.today()
hour = datetime.datetime.now()
hour = hour.hour
minute = datetime.datetime.now()
minute = minute.minute
second = datetime.datetime.now()
second = second.second
tarih = str(bugun) + "T" + str(hour) + ":" + str(minute) + ":" + str(second) + "+03:00"
print(tarih)


payload = json.dumps({
  "PriceDate": tarih
})
headers = {
  'Authorization': "Bearer " + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(json.dumps(response.json(), indent=4, sort_keys=True))


