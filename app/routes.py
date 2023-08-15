from app import app
from .data_reader import DataReader
from .data_calculator import DataCalculator
from .report_generator import ReportGenerator
import os

data_reader = DataReader()
ALL_DATA = data_reader.all_readings


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/weather-summary/<int:year>")
def weather_summary_by_year(year):
    calculation = DataCalculator.calculate_weather_by_year(ALL_DATA, year)
    report = ReportGenerator.generate_weather_report_by_year(calculation)
    print(report)
    return f"Viewing Note {year}"


@app.route("/weather-summary/<int:year>/<int:month>")
def weather_summary_by_year_and_month(year, month):
    calculation = DataCalculator.calculate_weather_by_year_and_month(
        ALL_DATA, year, month
    )
    report = ReportGenerator.generate_weather_report_by_year_and_month(calculation)
    print(report)
    return f"Viewing Note {year} and {month}"


@app.route("/temperature-charts/<int:year>/<int:month>")
def temperature_charts(year, month):
    print("here")
    calculation = DataCalculator.calculate_temperature_charts(ALL_DATA, year, month)
    print("there")
    report = ReportGenerator.generate_Temperature_chart(calculation)
    print(report)
    return f"Viewing Note {year} and {month}"


@app.route("/combined-temperature-charts/<int:year>/<int:month>")
def combined_temperature_charts(year, month):
    return f"Viewing Note {year} and {month}"
