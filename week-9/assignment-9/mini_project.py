import requests
 
BASE_URL = "https://api.restcountries.com/countries/v5"
API_KEY = "rc_live_09360045b2ed4ce8a2be16d98b782c91"  
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
 
 
def fetch_all_countries():
    countries = []
    offset = 0
    limit = 100 
 
    try:
        while True:
            response = requests.get(
                BASE_URL,
                headers=HEADERS,
                params={
                    "response_fields": "names.common,capitals,region,population",
                    "limit": limit,
                    "offset": offset,
                },
            )
            if response.status_code != 200:
                print(f"Request failed: status {response.status_code}")
                return []
 
            load = response.json()
            page = load["data"]["objects"]
            countries.extend(page)
 
            if not load["data"]["meta"].get("more"):
                break
            offset += limit
 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching countries: {e}")
        return []
 
    return [cleaned_country(c) for c in countries]
 
 
def cleaned_country(raw):
    capitals = raw.get("capitals")
    if capitals:
        capital = capitals[0].get("name", "N/A")
    else:
        capital = "N/A"
 
    return {
        "name": raw["names"]["common"],
        "capital": capital,
        "region": raw.get("region", "N/A"),
        "population": raw.get("population", 0),
    }
 
 
def print_country(country):
    print(
        f"{country['name']} — Capital: {country['capital']} | "
        f"Region: {country['region']} | Population: {country['population']:,}"
    )
 
 
def search_by_name(countries):
    term = input("Search: ").strip().lower()
    matches = [c for c in countries if term in c["name"].lower()]
 
    if not matches:
        print(f"No countries found matching '{term}'.")
        return
 
    for country in matches:
        print_country(country)
 
 
def filter_by_region(countries):
    region = input("Enter a region (e.g. Africa, Asia, Europe): ").strip().lower()
    matches = [c for c in countries if c["region"].lower() == region]
 
    if not matches:
        print(f"No countries found in region '{region}'.")
        return
 
    matches.sort(key=lambda c: c["population"], reverse=True)
    for country in matches:
        print_country(country)
 
 
def main():
    countries = fetch_all_countries()
    if not countries:
        print("Could not load country data. Exiting.")
        return
 
    while True:
        print("\n=== Country Explorer ===")
        print("1. Search by name")
        print("2. Filter by region")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()
 
        if choice == "1":
            search_by_name(countries)
        elif choice == "2":
            filter_by_region(countries)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")
 
 
if __name__ == "__main__":
    main()