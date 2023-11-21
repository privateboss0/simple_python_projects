import requests
import smtplib
from email.mime.text import MIMEText

# Your email address and password
YOUR_EMAIL = "aolaxxxx@gmail.com"
YOUR_PASSWORD = "xxxxx xxxxx xxxxx xxxxx"

# The city and country you want the weather for
CITY = "Ogun"
COUNTRY = "Nigeria"

# Get the weather data from the API
weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid=API KEYS")
weather_data = weather_response.json()

# Get the air quality data from the API
air_quality_response = requests.get(f"https://api.openweathermap.org/data/2.5/air_pollution?city={CITY},{COUNTRY}&appid=API KEYS")
air_quality_data = air_quality_response.json()

# Define the email variable
aolaxxxx = "aolaxxxx@gmail.com"

weather = weather_data["weather"][0]["main"]
windspeed = weather_data["wind"]["speed"]
humidity = weather_data["main"]["humidity"]
temperature = weather_data["main"]["temp"] * 9/5 + 32

# Convert the temperature from Kelvin to Fahrenheit and then to Celsius: KFC :)
temperature_in_fahrenheit = (weather_data["main"]["temp"] - 273.15) * 9/5 + 32
temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5/9

# Check if the air quality data has a "current" key
if "current" in air_quality_data:
    # Get the air quality index
    air_quality_index = air_quality_data["data"]["current"]["aqi"]
else:
    # If the air quality data does not have a "current" key, set the air quality index to None
    air_quality_index = None

# Create the email message
message = MIMEText(f"The weather in {CITY}, {COUNTRY} is {weather}. The windspeed is {windspeed} m/s. The humidity is {humidity}%. The temperature is {temperature_in_celsius} degrees Celsius. The air quality index is {air_quality_index}.")
message["Subject"] = "Weather Report"
message["From"] = aolaxxxx
message["To"] = aolaxxxx

# Send the email
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(YOUR_EMAIL, YOUR_PASSWORD)
smtp_server.sendmail(YOUR_EMAIL, YOUR_EMAIL, message.as_string())
smtp_server.quit()