import requests

def get_weather(city):
    api_key = "70e65efa024641dda971032822a037c1"
    base_url = "http://api.weatherstack.com/current"
    params = {"access_key": api_key, "query": city, "units": "m"}
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            temperature = data["current"]["temperature"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_speed"]
            
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Error: Invalid response from API. Please check your API key and city name.")
    else:
        print("Error fetching weather data. Please check your internet connection and try again.")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
