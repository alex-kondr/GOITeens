import requests
from flask import Flask, redirect, request, render_template, url_for, jsonify

from config import settings


app = Flask(__name__)


def get_temp_by_city(city: str, api_key: str = settings.weather_api) -> dict[str, dict]:
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    return requests.get(api_url).json()


@app.route("/", methods=["GET", "POST"])
def get_temp():
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_temp_by_city(city=city)
        weather = {
            "city": city,
            "temp": round(weather_data.get("main", {}).get("temp", 0) - 273),
            "speed": weather_data.get("wind", {}).get("speed")
        }
        return render_template("index.html", weather=weather)

    return render_template("index.html")


@app.get("/api/<city>/")
def get_temp_api(city: str):
        weather_data = get_temp_by_city(city=city)
        weather = {
            "city": city,
            "temp": round(weather_data.get("main", {}).get("temp", 0) - 273),
            "speed": weather_data.get("wind", {}).get("speed")
        }
        response = jsonify(weather)
        response.status_code = 202
        return response


if __name__ == "__main__":
    app.run(debug=True)
