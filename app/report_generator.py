# This is a report generator for creating the reports given the computation results
from datetime import datetime
import calendar


class ReportGenerator:
    def format_to_two_digits(number):
        if number < 10:
            return f"0{number}"
        else:
            return str(number)

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
        def report_row(index, temp, col):
            if temp is None:
                return None
            else:
                return (
                    ReportGenerator.format_to_two_digits(index + 1)
                    + " "
                    + f"\033[{col}m{'+' * abs(temp)}\033[0m"
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
            report.append(report_row(index, high, "91"))
            report.append(report_row(index, low, "94"))
        report = [row for row in report if row is not None]
        return report

    @staticmethod
    def generate_combined_Temperature_chart(calculations):
        def report_row(index, high_temp, low_temp, red, blue):
            if high_temp is None or low_temp is None:
                return None
            else:
                return (
                    ReportGenerator.format_to_two_digits(index + 1)
                    + " "
                    + f"\033[{blue}m{'+' * abs(low_temp)}\033[0m"
                    + f"\033[{red}m{'+' * abs(high_temp)}\033[0m"
                    + " "
                    + str(low_temp)
                    + "C"
                    + " - "
                    + str(high_temp)
                    + "C"
                )

        report = [
            calendar.month_name[calculations["month"]] + " " + str(calculations["year"])
        ]
        for index, (high, low) in enumerate(
            zip(calculations["high_temps"][1:], calculations["low_temps"][1:])
        ):
            report.append(report_row(index, high, low, "91", "94"))
        report = [row for row in report if row is not None]
        return report
