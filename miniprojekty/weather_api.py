import requests

API_KEY = "12694b64812c5aaa10eca48dc024a88d"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data["main"]["temp"], data["weather"][0]["description"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None, None

def main():
    city = input("Enter city: ")
    temp, desc = get_weather(city)
    if temp is None:
        print(f"Failed to get weather for {city}")
    else:
        print(f"Temperature in {city} is {temp}°C, {desc}")

main()

