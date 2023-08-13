# This is a module for computing calculations given reading
import math


class DataCalculator:
    @staticmethod
    def calculate_weather_by_year(data, year):
        # Data structure to hold calculations result
        calculations = {
            "highest_temps": {
                "day": None,
                "temp": -float("inf"),
            },
            "lowest_temps": {
                "day": None,
                "temp": float("inf"),
            },
            "max_humidity": {
                "day": None,
                "humidity": -float("inf"),
            },
        }
        for day, day_data in data.items():
            if day.startswith(str(year)):
                if day_data["max_temp"] > calculations["highest_temps"]["temp"]:
                    calculations["highest_temps"]["temp"] = day_data["max_temp"]
                    calculations["highest_temps"]["day"] = day
                if day_data["min_temp"] < calculations["lowest_temps"]["temp"]:
                    calculations["lowest_temps"]["temp"] = day_data["min_temp"]
                    calculations["lowest_temps"]["day"] = day
                if day_data["mean_humidity"] > calculations["max_humidity"]["humidity"]:
                    calculations["max_humidity"]["humidity"] = day_data["mean_humidity"]
                    calculations["max_humidity"]["day"] = day
        return calculations

    @staticmethod
    def calculate_weather_by_year_and_month(data, year, month):
        # Data structure to hold calculations result
        calculations = {
            "highest_avg": {
                "temp": -float("inf"),
            },
            "lowest_avg": {
                "temp": float("inf"),
            },
            "avg_humidity": {
                "humidity": -float("inf"),
            },
        }
        highest_temps = []
        lowest_temps = []
        mean_humidities = []
        for day, day_data in data.items():
            if day.startswith(str(year) + "-" + str(month)):
                highest_temps.append(day_data["max_temp"])
                lowest_temps.append(day_data["min_temp"])
                mean_humidities.append(day_data["mean_humidity"])
        calculations["highest_avg"]["temp"] = sum(highest_temps) // len(highest_temps)
        calculations["lowest_avg"]["temp"] = sum(lowest_temps) // len(lowest_temps)
        calculations["avg_humidity"]["humidity"] = sum(mean_humidities) // len(
            mean_humidities
        )
        return calculations
