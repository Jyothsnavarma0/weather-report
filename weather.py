import requests
import tkinter as tk
from tkinter import messagebox
def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", "Failed to fetch weather data.")
        return None
def display_weather(data):
    if data is None:
        return
    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    weather_description = data["weather"][0]["description"].capitalize()
    root = tk.Tk()
    root.title(f"Weather in {city_name}")
    info_label = tk.Label(root, text=f"Weather in {city_name}: {weather_description}")
    temp_label = tk.Label(root, text=f"Temperature: {temperature}°C")
    humidity_label = tk.Label(root, text=f"Humidity: {humidity}%")
    pressure_label = tk.Label(root, text=f"Pressure: {pressure} hPa")
    wind_label = tk.Label(root, text=f"Wind Speed: {wind_speed} m/s")
    info_label.pack()
    temp_label.pack()
    humidity_label.pack()
    pressure_label.pack()
    wind_label.pack()
    root.mainloop()
if __name__ == "__main__":
    api_key = "58e6c9a66af248f60c5cf00296b7a240"  
    city = input("Enter the city name: ")
    weather_data = get_weather_data(api_key, city)
    if weather_data:
        display_weather(weather_data)
if __name__ == "__main__":
    api_key = "58e6c9a66af248f60c5cf00296b7a240"
    while True:
        city = input("Enter the city name (type 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather_data = get_weather_data(api_key, city)
        if weather_data:
            display_weather(weather_data)
        choice = input("Do you want to search for weather in another city? (y/n): ")
        if choice.lower() not in ['y', 'yes']:
            break
