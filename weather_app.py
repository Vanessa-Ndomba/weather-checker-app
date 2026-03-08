import requests


def get_weather():
    """Get and display weather for a South African city"""

    # Get user input
    city = input("\nEnter a city in South African: ").strip()

    if not city:
        print("❌ Please enter a city name.")
        return

    # Format city name properly
    city = city.title()

    # Add South Africa country code
    location = f"{city},ZA"

    # Your API key - REPLACE THIS WITH YOUR ACTUAL API KEY
    # Get a free API key from: https://openweathermap.org/api
    api_key = "f8f4cef1c0dc7154e899d50d4471792e"  # <-- Replace with your actual API key

    # API endpoint with metric units (Celsius)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        # Make the API request
        response = requests.get(url, timeout=10)
        data = response.json()

        # Check for different error conditions
        if response.status_code == 401:
            print("\n❌ API key error: Invalid or missing API key.")
            print("   Get a free API key from: https://openweathermap.org/api")
            return
        elif response.status_code == 404:
            print(f"\n❌ City '{city}' not found in South Africa.")
            print("   Try: Johannesburg, Cape Town, Durban, Pretoria, Port Elizabeth")
            return
        elif response.status_code != 200:
            print(f"\n❌ Error: {data.get('message', 'Unknown error')}")
            return

        # If API request succeeded (status code 200)
        if data.get("cod") == 200:
            # Extract weather data
            temperature = round(data["main"]["temp"])
            feels_like = round(data["main"]["feels_like"])
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]

            # Determine weather condition
            desc_lower = description.lower()
            if "rain" in desc_lower:
                condition = "🌧️ Rainy"
                icon = "🌧️"
            elif "cloud" in desc_lower:
                condition = "☁️ Cloudy"
                icon = "☁️"
            elif "clear" in desc_lower or "sun" in desc_lower:
                condition = "☀️ Sunny"
                icon = "☀️"
            elif "mist" in desc_lower or "fog" in desc_lower:
                condition = "🌫️ Foggy"
                icon = "🌫️"
            elif "thunder" in desc_lower:
                condition = "⛈️ Thunderstorm"
                icon = "⛈️"
            elif "snow" in desc_lower:
                condition = "❄️ Snowy"
                icon = "❄️"
            else:
                condition = f"{description.capitalize()}"
                icon = "🌡️"

            # Display weather information
            print("\n" + "=" * 45)
            print(f"      WEATHER IN {city.upper()}, SOUTH AFRICA")
            print("=" * 45)
            print(f"{icon}  Condition: {condition}")
            print(f"🌡️  Temperature: {temperature}°C (feels like {feels_like}°C)")
            print(f"💧  Humidity: {humidity}%")
            print(f"💨  Wind Speed: {wind_speed} m/s")
            print(f"📊  Pressure: {pressure} hPa")
            print(f"📝  Details: {description.capitalize()}")
            print("=" * 45)

    except requests.exceptions.ConnectionError:
        print("\n❌ Network error: Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("\n❌ Timeout error: The request took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request error: {e}")
    except KeyError as e:
        print(f"\n❌ Data error: Unexpected response format - {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


def main():
    """Main program loop"""
    print("=" * 45)
    print("     SOUTH AFRICAN WEATHER FORECAST APP")
    print("=" * 45)
    print("\nThis app shows current weather for South African cities")

    while True:
        get_weather()

        # Ask if user wants to check another city
        while True:
            again = input("\n🔍 Check another city? (yes/no): ").strip().lower()
            if again in ['yes', 'y']:
                break
            elif again in ['no', 'n']:
                print("\n👋 Thank you for using the Weather App! Goodbye!")
                return
            else:
                print("❌ Please enter 'yes' or 'no'")


if __name__ == "__main__":
    main()