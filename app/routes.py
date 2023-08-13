from app import app
from .data_reader import DataReader
import os

data_reader = DataReader()
ALL_DATA = data_reader.all_readings


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/weather-summary/<int:year>")
def weather_summary_by_year(year):
    return f"Viewing Note {year}"


@app.route("/weather-summary/<int:year>/<int:month>")
def weather_summary_by_year_and_month(year, month):
    return f"Viewing Note {year} and {month}"


@app.route("/temperature-charts/<int:year>/<int:month>")
def temperature_charts(year, month):
    return f"Viewing Note {year} and {month}"


@app.route("/combined-temperature-charts/<int:year>/<int:month>")
def combined_temperature_charts(year, month):
    return f"Viewing Note {year} and {month}"
