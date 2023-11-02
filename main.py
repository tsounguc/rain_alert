import requests
MY_LAT = 38.907192  # Your latitude
MY_LONG = -77.036873  # Your longitude
api_key = 'ac6d28d37e9150d517b296cb947da78d'

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast/hourly", params=parameters)
print(response.status_code)
response.raise_for_status()
data = response.json()

print(data)

