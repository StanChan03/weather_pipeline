import requests
import psycopg2
from psycopg2.extras import execute_values

def get_weather_data(city):
    api_key = '83a9559d905d951a9bcc23ff9e3d7a0e'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    weather_data = {
        'city': city,
        'observed_at_seconds': data['dt'],
        'temperature_c': data['main']['temp'],
        'weather_condition': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'humidity': data['main']['humidity']
    }
    return weather_data

def store_data(weather_data):
    conn = psycopg2.connect(
        dbname = 'weather_data',
        user = 'stanleychan',
        password = 'DerpyTacos@529',
        host = 'localhost'
    )
    cursor = conn.cursor()
    query = """
        INSERT INTO weather(city, observed_at_seconds, temperature_c, weather_condition, wind_speed, humidity)
        VALUES %s
        """
    values = [(weather_data['city'], weather_data['observed_at_seconds'], weather_data['temperature_c'], weather_data['weather_condition'],
               weather_data['wind_speed'], weather_data['humidity'])]
    
    execute_values(cursor, query, values)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_and_store_data():
    cities = ['New York', 'Berkeley', 'Los Angeles', 'San Francisco', 'San Diego', 'Ontario', 'Berlin', 'Stockholm']
    for city in cities:
        weather_data = get_weather_data(city)
        store_data(weather_data=weather_data)

fetch_and_store_data()


