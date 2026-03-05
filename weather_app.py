# Weather Checker Program

def check_weather():

    city = input("Enter your city: ")

    weather_data = {
        "Cape Town": {"temp": 21, "condition": "Sunny"},
        "Johannesburg": {"temp": 18, "condition": "Windy"},
        "Durban": {"temp": 25, "condition": "Rainy"}
    }

    if city in weather_data:
        temp = weather_data[city]["temp"]
        condition = weather_data[city]["condition"]

        print("\nWeather in", city)
        print("Temperature:", temp, "°C")
        print("Condition:", condition)

    else:
        print("Weather data not available for this city.")


check_weather()