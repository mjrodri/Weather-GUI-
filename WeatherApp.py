import requests
import tkinter as tk
from tkinter import ttk

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        result_text.set(
            f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Description: {weather_data['weather'][0]['description']}"
        )
    else:
        result_text.set("Error fetching weather data. Please check your input.")

def get_weather_for_city():
    city = city_entry.get()
    weather_data = get_weather(api_key_entry.get(), city)
    display_weather(weather_data)

# Create the main application window
app = tk.Tk()
app.title("Weather App")

# Create and place widgets in the window
api_key_label = ttk.Label(app, text="API Key:")
api_key_label.grid(row=0, column=0, padx=5, pady=5)
api_key_entry = ttk.Entry(app)
api_key_entry.grid(row=0, column=1, padx=5, pady=5)

city_label = ttk.Label(app, text="City:")
city_label.grid(row=1, column=0, padx=5, pady=5)
city_entry = ttk.Entry(app)
city_entry.grid(row=1, column=1, padx=5, pady=5)

get_weather_button = ttk.Button(app, text="Get Weather", command=get_weather_for_city)
get_weather_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(app, textvariable=result_text, wraplength=400)
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the application
app.mainloop()