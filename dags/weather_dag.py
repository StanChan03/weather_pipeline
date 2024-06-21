from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import psycopg2
from psycopg2.extras import execute_values

default_args = {
    'owner': 'StanChan',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


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
        dbname='weather_data',
        user='stanleychan',
        password='DerpyTacos@529',
        host='localhost'
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

dag = DAG(
    'weather_dag',
    default_args=default_args,
    description='A simple weather data fetching and storing DAG',
    schedule_interval=timedelta(minutes=10),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

fetch_and_store_task = PythonOperator(
    task_id='fetch_and_store_data',
    python_callable=fetch_and_store_data,
    dag=dag,
)

fetch_and_store_task
