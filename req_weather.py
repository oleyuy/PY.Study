import requests
def get_cordinates(user_city):
    try:
        headers = {
            "User-Agent": "MyWeatherApp/1.0 (olehniki05@gmail.com)"
        }
        response = requests.get(
            f"https://nominatim.openstreetmap.org/search?q={user_city}&format=json&limit=1",
            headers=headers).json()
        
        if not response:
            raise ValueError("City not found")

        data = response[0]
        lat = float(data['lat'])
        lon = float(data['lon'])
        return lat, lon

    except Exception as e:
        raise ValueError('City not found or API error') from e


def get_weather(user_city,latitude, longitude):
    lat = latitude
    lon = longitude

    params = {
    'latitude': lat,
    'longitude': lon,
    'current_weather': True
    }

    responce =requests.get("https://api.open-meteo.com/v1/forecast",params=params).json()
    
    weather = responce['current_weather']
    print(f"temp in {user_city}: {weather['temperature']}°C, wind: {weather['windspeed']}m/s")
    if int(weather['temperature'])>20:
        print('wear sunglasses its hot in',user_city)


user_city = input('input your city:')
latitude, longitude = get_cordinates(user_city)
get_weather(user_city,latitude,longitude)



