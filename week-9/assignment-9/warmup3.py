import requests 
params = {"region": "Europe"}

response = requests.get(
  'https://api.restcountries.com/countries/v5',
  headers={'Authorization': 'Bearer rc_live_09360045b2ed4ce8a2be16d98b782c91'}, 
  params = params
)


data = response.json()
countries = data["data"]["objects"]

for country in countries[:10]:
    print(country["names"]["common"])
