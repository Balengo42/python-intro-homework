import requests
response = requests.get("https://api.agify.io/?name=michael")
data = response.json()
print("Name: ", data["name"])
print("Predicted age:", data["age"])   
print("Birthday:", data.get("birthday", "Not available")) 