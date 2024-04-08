from datetime import datetime, timedelta


class Dates:
    def __init__(self):
        self.data_current = datetime.now()
        self.day_current = self.data_current.weekday()
        self.last_day_ago_week = self.data_current - \
            timedelta(days=1)
        self.first_day_ago_week = self.last_day_ago_week - \
            timedelta(days=6)

        self.month_map = {
            "JAN": 1,
            "FEV": 2,
            "MAR": 3,
            "ABR": 4,
            "MAI": 5,
            "JUN": 6,
            "JUL": 7,
            "AGO": 8,
            "SET": 9,
            "OUT": 10,
            "NOV": 11,
            "DEZ": 12
        }

        self.data_filter = ("JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV",
                            "DEZ", "Hoje", "Ontem", "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

        self.data_strucutre_date_relative = {
            "Hoje": self.data_current.strftime('%Y/%m/%d'),
            "Ontem": self.last_day_ago_week.strftime('%Y/%m/%d'),
            "Domingo": None,
            "Segunda": None,
            "Terça": None,
            "Quarta": None,
            "Quinta": None,
            "Sexta": None,
            "Sábado": None
        }

        self.translate_day_week = {
            "Sunday": "Domingo",
            "Monday": "Segunda",
            "Tuesday": "Terça",
            "Wednesday": "Quarta",
            "Thursday": "Quinta",
            "Friday": "Sexta",
            "Saturday": "Sábado"
        }

        for i in range(7):
            data_dia = self.first_day_ago_week + timedelta(days=i)
            self.data_strucutre_date_relative[self.translate_day_week[data_dia.strftime(
                '%A')]] = data_dia.strftime('%Y/%m/%d')

    def month_map(self):
        return self.month_map

    def data_filter(self):
        return self.data_filter

    def date_relative_ago_week(self, day_week):
        return (self.data_strucutre_date_relative.get(day_week))

    def date_current_relative_today(self, value, value_two):
        return (datetime(self.data_current.year, self.month_map.get(
            value), value_two).strftime('%Y/%m/%d'))

    def format_date(self, date, i):
        year = date.split('/')[2]
        month = int(date.split('/')[1])
        day = date.split('/')[0]

        return f"{month+i}/{day}/{year}"
