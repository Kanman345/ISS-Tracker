import requests

response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")

if response.status_code == 200:
    iss_data = response.json()
    print(f"Latitude : {iss_data['latitude']}")
    print(f"Longitude : {iss_data['longitude']}")

else:
    print(f"Failed to retrieve data: {response.status_code}")


    













    