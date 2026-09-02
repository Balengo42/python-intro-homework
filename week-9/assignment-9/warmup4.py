import requests

try:
    response = requests.get("https://some-bad-url.example.com")
    if response.status_code != 200:
        print(f"Status code: {response.status_code}")
    else:
        data = response.json()
        print(data)

except requests.exceptions.RequestException:
    print("Error: Could not reach the server. Check your connection and try again.")