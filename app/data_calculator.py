# This is a module for computing calculations given reading
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
