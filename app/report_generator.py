# This is a report generator for creating the reports given the computation results
from datetime import datetime


class ReportGenerator:
    def convert_date(input_date):
        date_obj = datetime.strptime(input_date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d")
        return formatted_date

    @staticmethod
    def generate_weather_report_by_year(calculations):
        report = [
            f"Highest: {calculations['highest_temps']['temp']}C on {ReportGenerator.convert_date(calculations['highest_temps']['day'])}",
            f"Lowest: {calculations['lowest_temps']['temp']}C on {ReportGenerator.convert_date(calculations['lowest_temps']['day'])}",
            f"Humidity: {calculations['max_humidity']['humidity']}% on {ReportGenerator.convert_date(calculations['max_humidity']['day'])}",
        ]
        return report
