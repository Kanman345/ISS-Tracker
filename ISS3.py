import requests
from datetime import datetime

date_input = input("Enter the date (DD/MM/YYYY) : ")
time_input = input("Enter the time (HH:MM:SS) : ")

date_time_str = f"{date_input} {time_input}"

try:
    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')

except ValueError:
        print("Invalid date or time format. Please use DD/MM/YYYY and HH:MM:SS.")

else:       
    unix_time = int(date_time_obj.timestamp())

    url = f"https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={unix_time}&units=kilometers"
    
    response = requests.get(url)
    if response.status_code == 200:
        
        iss_data = response.json()
        lat = iss_data[0]['latitude']
        long = iss_data[0]['longitude']

        print(f"The location of the iss on {date_input} at {time_input} was: Latitude = {lat} and Longitude = {long}")       
    else:
        print(f"Failed to retrieve data: {response.status_code}")




