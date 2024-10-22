import requests

response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")

if response.status_code == 200:
    iss_data = response.json()
    lat = iss_data['latitude']
    long = iss_data['longitude']
    
    base_url = "https://api.wheretheiss.at/v1/coordinates"

    response2 = requests.get(f"{base_url}/{lat},{long}")

    if response2.status_code == 200:
        iss_info = response2.json()
        print(f"Country Code : {iss_info['country_code']}")
        print(f"Timezone : {iss_info['timezone_id']}")

    else: 
        print(f"Failed to retrieve data : {response2.status_code}")

else:
    print(f"Failed to retrieve data : {response.status_code}")



