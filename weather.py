

import requests 
import json 
import time

# Take temp in kalvin and return farenheit
def convertToF(temp):
  temp_f = round( (temp - 273.15) * (9/5) + 32, 2 )
  return temp_f

def displayF(description, wind, temp, temp_min, temp_max, feels_like, city):
  print('\n')
  print("Loading data...")
  time.sleep(1.5)

  print(f"""
---------------------------
Current Weather: {city}
---------------------------
  Description: {description}
  Wind Speed: {wind}
  Temp: {temp}
  Temp min: {temp_min}
  Temp max: {temp_max}
  Feels like: {feels_like}
---------------------------
  """)
  

def weather_data(base_url, api_key):

  running = True

  while running:

    city_name = input("Enter city name: ")

    # Add error handling to make sure a city doesn't numbers/characters that dont belong 

    zip_code = input("Enter zip code: ")

    # Add error handling 
    try:
      # Make request to api
      complete_url = f'{base_url}{city_name},{zip_code}&appid={api_key}'

      response = requests.get(complete_url)

      if response.status_code != 200:
        raise ConnectionError

      w_data = response.json()

      # Variables to extract data from w_data
      description = w_data['weather'][0]['description']
      wind = w_data['wind']['speed']
      temp = convertToF(w_data['main']['temp'])
      temp_min = convertToF(w_data['main']['temp_min'])
      temp_max = convertToF(w_data['main']['temp_max'])
      feels_like = convertToF(w_data['main']['feels_like'])

      # Display data in a clean format
      displayF(description, wind, temp, temp_min, temp_max, feels_like, city_name)

    except KeyError:
      print("Weather data was not found for info entered")
    except ConnectionError:
      print("Connection was not successful")
    
    usesr_input = input("Would you like to check another citys weather? (y/n)").lower() 

    if usesr_input == 'n':
      print("Thanks for using the weather app!")
      running = False




def main():
  base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
  api_key = '55592219da64379c5a1872dccb250590'

  weather_data(base_url, api_key)


if __name__ == "__main__":
  main()



