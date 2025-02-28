import sqlite3
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

def get_temperature():
    url = "https://sinoptik.ua/ru/pohoda/vinnytsia"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        temp = soup.find("p", class_="today-temp").text.strip().replace("°", "")
        return float(temp)
    return None

def create_db():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_data(temperature):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (timestamp, temperature) VALUES (?, ?)", (datetime.now(), temperature))
    conn.commit()
    conn.close()

def update_weather():
    while True:
        temperature = get_temperature()
        if temperature is not None:
            insert_data(temperature)
        time.sleep(1800)

create_db()
update_weather()
