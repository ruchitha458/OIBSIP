import requests
import json

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None

def main():
    api_key = "72d217a137d58992bdcacab92cb8d82f"
    location = input("Enter city name or ZIP code: ")
    
    weather_info = get_weather(api_key, location)
    if weather_info:
        print("\nCurrent Weather:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to fetch weather data. Please check your input.")

if __name__ == "__main__":
    main()
