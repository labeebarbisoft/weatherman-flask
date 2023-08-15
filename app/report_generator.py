# This is a report generator for creating the reports given the computation results
from datetime import datetime
import calendar


class ReportGenerator:
    @staticmethod
    def generate_weather_report_by_year(calculations):
        def convert_day_month_year(input_date):
            date_obj = datetime.strptime(input_date, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%B %d")
            return formatted_date

        report = [
            f"Highest: {calculations['highest_temps']['temp']}C on {convert_day_month_year(calculations['highest_temps']['day'])}",
            f"Lowest: {calculations['lowest_temps']['temp']}C on {convert_day_month_year(calculations['lowest_temps']['day'])}",
            f"Humidity: {calculations['max_humidity']['humidity']}% on {convert_day_month_year(calculations['max_humidity']['day'])}",
        ]
        return report

    @staticmethod
    def generate_weather_report_by_year_and_month(calculations):
        report = [
            f"Highest Average: {calculations['highest_avg']['temp']}C",
            f"Lowest Average: {calculations['lowest_avg']['temp']}C",
            f"Average Mean Humidity: {calculations['avg_humidity']['humidity']}%",
        ]
        return report

    @staticmethod
    def generate_Temperature_chart(calculations):
        def format_to_two_digits(number):
            if number < 10:
                return f"0{number}"
            else:
                return str(number)

        def report_row(index, temp):
            if temp is None:
                return "Data not available"
            elif temp <= 0:
                return "Below zero"
            else:
                return (
                    format_to_two_digits(index + 1)
                    + " "
                    + "+" * temp
                    + " "
                    + str(temp)
                    + "C"
                )

        report = [
            calendar.month_name[calculations["month"]] + " " + str(calculations["year"])
        ]
        for index, (high, low) in enumerate(
            zip(calculations["high_temps"][1:], calculations["low_temps"][1:])
        ):
            report.append(report_row(index, high))
            report.append(report_row(index, low))
        return report
