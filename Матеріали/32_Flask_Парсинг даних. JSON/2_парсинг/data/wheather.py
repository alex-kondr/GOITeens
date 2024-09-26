import os

from dotenv import load_dotenv
import requests


load_dotenv()


def get_wheater(city: str = "Odesa") -> dict:
    key = os.getenv("WHEATHER_API")
    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key={key}"
    wheater_info = requests.get(url).json()
    wheather = {
        "city": wheater_info.get("location", {}).get("name") + ", " + wheater_info.get("location", {}).get("region"),
        "temp": wheater_info.get("current", {}).get("temp_c")
    }
    return wheather